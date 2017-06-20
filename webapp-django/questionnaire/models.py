from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=256)
    hints = models.CharField(max_length=256, blank=True)
    answer = models.CharField(max_length=256)

    def __str__(self):
        return str(self.question)


class SimpleQuestion(Question):
    pass


class MultipleChoiceQuestion(Question):
    choices = models.CharField(choices=[], max_length=256)
    correct = models.IntegerField()

    @classmethod
    def create(cls, question, hints, choices, correct):
        CHOICES = [(index, item) for index, item in enumerate(choices)]
        answer = CHOICES[correct][1]
        mcq = cls(question=question, hints=hints, choices=CHOICES, correct=correct, answer=answer)
        return mcq
