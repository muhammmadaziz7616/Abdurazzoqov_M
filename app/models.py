from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, DateTimeField
from django_resized import ResizedImageField


class User(AbstractUser):
    image = ResizedImageField(size=[90, 90], crop=['middle', 'center'], upload_to='user/images',
                              default='user/default.jpg')


class Person(Model):
    image = models.ImageField(upload_to='user/images', default='user/images/default.jpg')
    title = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
