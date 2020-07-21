from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    pic = models.ImageField(default="default.jpg",null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    CATEGORY =(
    ('available', 'available'),
    ('unavailable','unavailable')
    )
    status = models.CharField(max_length=200, null=True,choices=CATEGORY)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('index')


class Borrow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(Book,null=True,blank=True,on_delete = models.SET_NULL)
    date_posted = models.DateTimeField(default=timezone.now)
    book_return = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
