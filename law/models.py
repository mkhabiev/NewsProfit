from django.db import models
from news_profit.models import User


class Law(models.Model):
    class Meta:
        verbose_name = 'Закон'
        verbose_name_plural = 'Законы'
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True,
                            max_length=150)

    def __str__(self):
        return self.title

class FavoriteLaw(models.Model):
    law = models.ForeignKey(Law, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)