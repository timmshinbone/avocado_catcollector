from django.db import models
# need the reverse method from django urls for redirects
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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


# Model for Feedings (Cat -|---< Feeding)
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the choices field option (creates a dropdown)
        choices=MEALS,
        # set a default for our choices
        default=MEALS[0][0]
    )

    # creates cat FK reference
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # this will use a method for obtaining the value of a field.choice
        return f"{self.get_meal_display()} on {self.date}"