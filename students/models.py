from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


"""
Basic Models for the applications
"""
class Thought(models.Model):
    date = models.DateField(unique=True)
    text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.text

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    is_anonymous = models.BooleanField(default=True)
    # publish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.post


class Rewards(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.BigIntegerField()



"""
dynamic Forms like google forms
"""

class Form(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    QUESTION_TYPE_CHOICES = [
        ('text', 'Text'),
        ('radio', 'Radio'),
    ]
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    class Meta:
        unique_together = ('response', 'question') # for every question there should be one and only one answer per response

"""
Basic community model to display details about  a community and its description
"""

class Community(models.Model):
    pass