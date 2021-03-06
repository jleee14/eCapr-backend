from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255,
                              unique=True)
    username = models.CharField(max_length=100, unique=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    pushes = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['email', 'wins', 'losses', 'pushes']
    USERNAME_FIELD = 'username' 

    def get_username(self):
        return self.username