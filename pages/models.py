from django.db import models
from account.models import *

class Post(models.Model):

    title = models.CharField('Название',max_length=30)
    description = TextField('Описание',blank=True, null=True)
    image = ImageField('Картинка',upload_to='posts-images')
    author = ForeignKey(CustomUser, on_delete=CASCADE, related_name='Автор')

    def __str__(self):
        return f'{self.title}'
    