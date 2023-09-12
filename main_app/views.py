from django.shortcuts import render

# in order to use the model, we have to import
from .models import Cat

# These are the old cats, now we use models.
# cats = [
#     {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#     {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Create your views here.

# define the home view
def home(request):
    # unlike EJS templating, we need the html file extension
    return render(request, 'home.html')

# define the about view
def about(request):
    return render(request, 'about.html')

# Index View for all cats
def cats_index(request):
    # we can pass data to templates, JUST like we did in express.
    # return render(request, 'cats/index.html', {'cats': cats })
    # we need to retrieve our list of cats
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })

# Detail view for a single cat
def cats_detail(request, cat_id):
    # find the cat
    cat = Cat.objects.get(id=cat_id)
    # to check this view function before we have html, use a print!
    # print('this is the cat django found')
    # print(cat)
    return render(request, 'cats/detail.html', { 'cat': cat })