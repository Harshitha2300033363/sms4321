from django.contrib.auth.models import User
from django.db import models

# model is a predefined,and inheriting a predefined to userdefined so it os a single level inheritance

# Create your models here

#need to explain models.py


from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20,unique=True)
    Name = models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Register_Number


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='example@example.com')  # Add default value
    phone = models.CharField(max_length=15)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name