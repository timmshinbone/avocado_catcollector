from django.shortcuts import render
# we need to import our class based views
from django.views.generic.edit import CreateView
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

# Now we can inherit from the CreateView to make our cats create view
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # fields = ['name', 'breed', 'description', 'age']
    # special string pattern for a successful create
    # success_url = '/cats/{cat_id}'