from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(AbstractBaseUser):
    phone = models.CharField(max_length=100)

class ConfirmationCode(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    valid_until = models.DateTimeField()

    def __str__(self):
        return self.code