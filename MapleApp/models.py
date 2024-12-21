from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_books')  # New field

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()  # Added email field
    message = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Added first_name field
    last_name = models.CharField(max_length=100)  # Added last_name field
    username = models.CharField(max_length=100, unique=True)  # Added username field
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.username
