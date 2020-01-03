from django.test import TestCase
from academics.flashcard.models import Course, Flashcard, Module, Subject


class FlashcardTestCase(TestCase):
    MATH_SUBJECT = 'MATH-TEST'
    ENG_SUBJECT = 'ENGINEERING-TEST'

    def setUp(self):
        """Setup test db with test flashcard records"""
        # Init subjects, courses, and modules for tests
        math = Subject.objects.create(subject=self.MATH_SUBJECT)
        eng = Subject.objects.create(subject=self.ENG_SUBJECT)
        fse000 = Course.objects.create(course="cat", subject=eng)
        mat266 = Course.objects.create(course="MAT266", subject=math)
        module0_fse000 = Module.objects.create(module="fse000-mod0", course=fse000)
        module1_fse000 = Module.objects.create(module="fse000-mod1", course=fse000)
        module0_mat266 = Module.objects.create(module="mat266-mod0", course=mat266)
        module1_mat266 = Module.objects.create(module="mat266-mod1", course=mat266)

        # Init flashcards classified by subject, course, and module

        # 5 flashcards in module0_fse000
        Flashcard.objects.create(question="This is a test q abc",
                                 answer="testabc",
                                 module=module0_fse000)
        Flashcard.objects.create(question="This is a test q def",
                                 answer="testdef",
                                 module=module0_fse000)
        Flashcard.objects.create(question="This is a test q 123",
                                 answer="test123",
                                 module=module0_fse000)
        Flashcard.objects.create(question="This is a test q 456",
                                 answer="test456",
                                 module=module0_fse000)
        Flashcard.objects.create(question="This is a test q 789",
                                 answer="test789",
                                 module=module0_fse000)

        # 3 flashcards in module1_fse000
        Flashcard.objects.create(question="This is a test q 1abc",
                                 answer="test1abc",
                                 module=module1_fse000)
        Flashcard.objects.create(question="This is a test q 1def",
                                 answer="test1def",
                                 module=module1_fse000)
        Flashcard.objects.create(question="This is a test q 1123",
                                 answer="test1123",
                                 module=module1_fse000)

        # 5 flashcards in module0_mat266
        Flashcard.objects.create(question="This is a math test q abc",
                                 answer="testabc",
                                 module=module0_mat266)
        Flashcard.objects.create(question="This is a math test q def",
                                 answer="testdef",
                                 module=module0_mat266)
        Flashcard.objects.create(question="This is a math test q 123",
                                 answer="test123",
                                 module=module0_mat266)
        Flashcard.objects.create(question="This is a math test q 456",
                                 answer="test456",
                                 module=module0_mat266)
        Flashcard.objects.create(question="This is a math test q 789",
                                 answer="test789",
                                 module=module0_mat266)

        # 2 flashcards in module1_mat266
        Flashcard.objects.create(question="This is a math test q 1abc",
                                 answer="test1abc",
                                 module=module1_mat266)
        Flashcard.objects.create(question="This is a math test q 1def",
                                 answer="test1def",
                                 module=module1_mat266)

    def test_new_flashcards_unapproved(self):
        """Flashcards are not approved by default"""
        testabc = Flashcard.objects.all()[0]
        testdef = Flashcard.objects.all()[1]
        self.assertEqual(testabc.approved, False)
        self.assertEqual(testdef.approved, False)

    def test_custom_get_flashcards(self):
        math = Subject.objects.get(subject=self.MATH_SUBJECT)
        eng = Subject.objects.get(subject=self.ENG_SUBJECT)
        math_flashcards = Flashcard.custom.get_flashcards(10, subject=math)
        math_flashcards_five = Flashcard.custom.get_flashcards(5, subject=math)
        eng_flashcards = Flashcard.custom.get_flashcards(10, subject=eng)
        mat266_mod1 = Module.objects.get(module='mat266-mod1')
        mat266_mod1_flashcards = Flashcard.custom.get_flashcards(5, module=mat266_mod1)

        # expect 7 math flashcards
        self.assertEqual(math_flashcards.count(), 7)
        # expect each card to be a math card
        for card in math_flashcards:
            self.assertEqual(card.module.course.subject.subject, self.MATH_SUBJECT)
        # expect only 5 flashcards
        self.assertEqual(math_flashcards_five.count(), 5)

        # expect 8 engineering flashcards
        self.assertEqual(eng_flashcards.count(), 8)
        # expect each card to be an engineering card
        for card in eng_flashcards:
            self.assertEqual(card.module.course.subject.subject, self.ENG_SUBJECT)

        # expect 2 math->mat266->mod1 cards
        self.assertEqual(mat266_mod1_flashcards.count(), 2)
        # expect each card to be a matt266-mod1 card
        for card in mat266_mod1_flashcards:
            self.assertEqual(card.module.module, 'mat266-mod1')



