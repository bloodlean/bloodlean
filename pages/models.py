from django.db import models
from account.models import *

class Post(models.Model):

    title = models.CharField(max_length=30)
    description = TextField(blank=True, null=True)
    image = ImageField(upload_to='posts-images')
    author = ForeignKey(CustomUser, on_delete=CASCADE)

    def __str__(self):
        return f'{self.title}'
    