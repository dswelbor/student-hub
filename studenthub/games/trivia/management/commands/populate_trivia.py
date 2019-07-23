from django.core.management.base import BaseCommand
import http.client
import json
from games.trivia.constants import BOOLEAN, MULTIPLE_CHOICE
from games.trivia.models import Category, Difficulty, Question, MultipleChoice, \
    TrueFalse, Score


class Command(BaseCommand):
    """Adds a custom command to manage.py - populate_trivia"""
    def handle(self, *args, **options):
        # populate_trivia() implements the logic for this manage.py command
        populate_trivia()


def populate_trivia():
    """
    Function that gets questions sets in batches, saves them to db model, and
    terminates when desired qty is reached
    """
    QUESTION_QTY = 325
    batch_size = 50
    test_token = OpenTriviaConsumer()
    test_token.get_result_set(batch_size)
    question_set = test_token.get_questions()
    # Get questions in batches
    total_counter = 0
    while total_counter < QUESTION_QTY and question_set:
        # Save questions and update counter
        total_counter += save_questions(question_set=question_set)

        # Remaining questions < batch size
        if (QUESTION_QTY - total_counter) < batch_size:
            batch_size = QUESTION_QTY - total_counter
        # Get next result batch
        test_token.get_result_set(batch_size)
        question_set = test_token.get_questions()

    print(str(total_counter))


def save_questions(question_set):
    """Saves questions to db model from a question set"""
    counter = 0
    for entry in question_set:
        # New Question not present in db
        if not Question.objects.filter(question=entry['question']):
            # Get category and difficulty
            # get_or_create returns a tuple (obj, was_created)
            cat = Category.objects.get_or_create(category=entry['category'])[0]
            dif = Difficulty.objects.get_or_create(difficulty=entry['difficulty'])[0]

            # Add Question
            new_question = Question(category=cat, difficulty=dif, question=entry['question'])
            new_question.save()  # saves new question in the database

            # True False
            if entry['type'] == BOOLEAN:
                # Add TrueFalse relation
                TrueFalse.objects.create(question=new_question, correct_answer=entry['correct_answer'])

            # Multiple Choice
            elif entry['type'] == MULTIPLE_CHOICE:
                # Add MultipleChoice relation
                # TODO: This assumes a list of at least 3 incorrect answers - implement cleaning/validation for this
                MultipleChoice.objects.create(question=new_question, correct_answer=entry['correct_answer'],
                                              incorrect_b=entry['incorrect_answers'][0],
                                              incorrect_c=entry['incorrect_answers'][1],
                                              incorrect_d=entry['incorrect_answers'][2])

            # New question added - increment counter
            counter += 1

    # Returns the number of questions added to the database
    print("batch complete...{} questions saved".format(counter))

    return counter


class OpenTriviaConsumer:
    """
    Class that consumes questions from OpenTriviaAPI
    """
    # Constants
    HOSTNAME = 'opentdb.com'
    REQ_TOKEN_STR = '/api_token.php?command=request'
    REQ_WITH_TOKEN_PREFIX = '/api.php?amount='
    REQ_WITH_TOKEN_SUFFIX = '&token='

    # TODO: Implement exception handling for functions and methods in this class
    # TODO: Implement constants for OpenTriviaAPI attribute keys

    def __init__(self):
        """Default ctor instantiates object with a token. result_set is initially empty"""
        self.token = OpenTriviaConsumer.get_token()
        self.result_set = None

    @staticmethod
    def get_token():
        """Static method that returns a token for OpenTrivia API"""
        # Connect to OpenTrivia DB
        trivia_db = http.client.HTTPSConnection(OpenTriviaConsumer.HOSTNAME)

        # Get token
        trivia_db.request('GET', OpenTriviaConsumer.REQ_TOKEN_STR)
        token_resp = trivia_db.getresponse()
        token_json = token_resp.read()
        token_json.decode()
        token_content = json.loads(token_json)
        token = token_content["token"]
        trivia_db.close()
        return token

    def get_result_set(self, qty):
        """
        Retrieves a result set of questions based on passed batch size and
        stores it in the object
        """
        # Connect to OpenTrivia DB
        trivia_db = http.client.HTTPSConnection(OpenTriviaConsumer.HOSTNAME)

        trivia_db.request('GET', OpenTriviaConsumer.REQ_WITH_TOKEN_PREFIX + str(qty)
                          + OpenTriviaConsumer.REQ_WITH_TOKEN_SUFFIX + self.token)
        resp = trivia_db.getresponse()

        # Save json from response
        trivia_json = resp.read()
        trivia_json.decode()
        self.result_set = json.loads(trivia_json)

        # Close http connection resource
        trivia_db.close()

        return self.result_set

    def print_questions(self):
        """Simple function to print the results of a query"""
        print('num_of_questions: ' + str(len(self.result_set['results'])))

        i = 0
        for entry in self.result_set['results']:
            print(i)
            print(entry['category'])
            print(entry['question'])
            i += 1

    def get_questions(self):
        """Simple accessor function that returns a list of questions"""
        # Request successful
        if self.result_set['response_code'] == 0:
            return self.result_set['results']
        # Request unsuccessful
        else:
            return []



