from django.test import TestCase
from academics.flashcard.models import Course, Flashcard, Module, Subject


class FlashcardTestCase(TestCase):
    def setUp(self):
        # Init subjects, courses, and modules for tests
        math = Subject.objects.create(subject="MATH-TEST")
        eng = Subject.objects.create(subject="ENGINEERING-TEST")
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

        # 3 flashcards in module1_mat266
        Flashcard.objects.create(question="This is a math test q 1abc",
                                 answer="test1abc",
                                 module=module1_mat266)
        Flashcard.objects.create(question="This is a math test q 1def",
                                 answer="test1def",
                                 module=module1_mat266)
        Flashcard.objects.create(question="This is a math test q 1123",
                                 answer="test1123",
                                 module=module1_mat266)

    def test_new_flashcards_unapproved(self):
        """Flashcards are not approved by default"""
        testabc = Flashcard.objects.get(id=1)
        testdef = Flashcard.objects.get(id=2)
        self.assertEqual(testabc.approved, False)
        self.assertEqual(testdef.approved, False)
