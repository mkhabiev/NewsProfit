from django.db import models
from news_profit.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text

    def view_answers(self):
        return Answer.objects.filter(text=self)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='answers')
    text = models.TextField()

    def __str__(self):
        return self.text