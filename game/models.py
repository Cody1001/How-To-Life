from django.db import models

class Question(models.Model):
    question_name = models.CharField(max_length=25)
    question_text = models.TextField()

    def __str__(self):
        return self.question_name

    def get_answers(self):
        return Answer.objects.filter(question=self)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.TextField()
    karma = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text
