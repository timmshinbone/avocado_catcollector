from django.contrib import admin
# import our cat model
from .models import Cat

# Register your models here.
admin.site.register(Cat)
