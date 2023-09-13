from django.db import models
# need the reverse method from django urls for redirects
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    # this is used for redirects from class based views
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})