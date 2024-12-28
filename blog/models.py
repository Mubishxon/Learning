from django.db import models
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courses/')
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("coursesDetailView", args=[self.slug])

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.name