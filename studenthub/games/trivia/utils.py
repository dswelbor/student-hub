import json
from .constants import BOOLEAN, MULTIPLE_CHOICE
from .models import Question, Category, Difficulty, TrueFalse, MultipleChoice, Score



def get_question_json(question):
    """
    Takes a Question object and returns question text, type, and answer choices as json
    """
    # Get question type and choices
    # Assume question type is multiple choice
    question_type = MULTIPLE_CHOICE
    try:
        choices = MultipleChoice.custom.get_questions_options(question=question)

    # Question was true/false
    except MultipleChoice.DoesNotExist:
        question_type = BOOLEAN

        try:
            choices = TrueFalse.custom.get_questions_options(question=question)

            # Question had neither T/F not MC answer choices
        except TrueFalse.DoesNotExist:
            choices = []

    # Build question object
    question = {
        'question': question.question,
        'question_type': question_type,
        'choices': choices
    }
    # Return obj json
    return json.dumps(question)


def get_questions_json(questions):
    """
    Takes a QuerySet of Questions and returns a list of json-formatted questions,
     including question text, question type, and answer choices
    """
    question_list = []
    # Iterate through all Questions in QuerySet
    for question in questions:
        # Append each json-formatted Question list
        question_list.append(get_question_json(question))
    return question_list


def get_leaderboard(qty):
    """
    Returns a passed number of json-formatted games in a list. Orders by score, in
    descending order
    """
    scores = Score.custom.get_best_games(qty)

    # Declare and initialize list of best games with headers
    best_games = [json.dumps({
            'user': 'User',
            'correct': 'Correct',
            'total': 'Out Of',
            'score': 'Score',
            'elapsed': 'Time Elapsed'
        })]

    # Iteratively add best games to leaderboard
    for score in scores:
        game = {
            'user': score.username.get_public_name(),
            'correct': score.questions_correct,
            'total': score.total_questions,
            'score': score.weighted_score,
            'elapsed': int(score.elapsed.total_seconds())
        }
        # Add game to list as json
        game_json = json.dumps(game)
        best_games.append(game_json)

    # Return a list of json-formatted games
    return best_games

# TODO: Implement a get_rank() function



