from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length = 100, blank = False)
    description = models.TextField(max_length = 2000, blank = False)
    image = models.ImageField(upload_to='about/', blank=False)
    point_one = models.TextField(default= "point_1")
    point_two = models.TextField(default= "point_2")
    point_three = models.TextField(default= "point_3")

    def __str__(self):
        return self.title

    # when we add data in database images are uploded to about folder (about/)

class Slider(models.Model):
    title = models.CharField(max_length = 100, blank = False)
    description = models.TextField(max_length = 2000, blank = False)
    image = models.ImageField(upload_to='Slider/', blank=False)

    def __str__(self):
        return self.title
    
class Client(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    link = models.CharField(max_length = 100, blank = False)
    image = models.ImageField(upload_to='client/', blank=False)

    def __str__(self):
        return self.name