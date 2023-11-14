from django.db.models import *
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    icon = ImageField('Аватарка', blank=True, null=True)
    about = TextField('Обо мне', blank=True, null=True)

    def __str__(self):
        return f'{self.username}'