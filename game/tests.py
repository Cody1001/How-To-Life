from django.test import TestCase
from .models import Question, Answer

class QuestionModelTests(TestCase):
    def setUp(self):
        question_one = Question.objects.create(
            question_name="Question One",
            question_text="To be or not to be?")

        Answer.objects.create(
            answer_text="To be",
            karma=100,
            votes=0,
            question=question_one
        )

        Answer.objects.create(
            answer_text="Not to be",
            karma=-100,
            votes=0,
            question=question_one
        )

        Answer.objects.create(
            answer_text="I refuse to answer",
            karma=0,
            votes=1,
            question=question_one
        )

        Answer.objects.create(
            answer_text="Boogie boogie",
            karma=50,
            votes=0,
            question=question_one
        )

    def test_answer_set(self):
        """Test the Question get_answers method"""
        question_one = Question.objects.get(question_name="Question One")
        question_one = question_one.get_answers()
        self.assertEqual(question_one.count(), 4)
