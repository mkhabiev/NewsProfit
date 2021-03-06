from django.db import models
from news_profit.models import User

class Publication(models.Model):
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True, max_length=150)

    def __str__(self):
        return self.title


class FavoritePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)