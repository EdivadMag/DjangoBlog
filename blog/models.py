from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Professor(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)
    n_votes = models.IntegerField(default=0)

class Subject(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    semester = models.IntegerField()
    professor = models.ManyToManyField(Professor)

class Student(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)


# Create your models here.
