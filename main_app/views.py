from django.shortcuts import render, redirect
# we need to import our class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# in order to use the model, we have to import
from .models import Cat
from .forms import FeedingForm

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
    # instantiate a feeding form to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form': feeding_form })

# View for adding a feeding to a cat
def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # we need to make sure the form data is valid
    if form.is_valid():
        # then we need to add/save the feeding
        # we dont want to save the feeding until the cat is associated
        new_feeding = form.save(commit=False)
        # associate the feeding with a cat
        new_feeding.cat_id = cat_id
        # save the feeding 
        new_feeding.save()
    # finally, redirect back to the detail page(which refreshes the info)
    return redirect('detail', cat_id=cat_id)

# Now we can inherit from the CreateView to make our cats create view
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # fields = ['name', 'breed', 'description', 'age']
    # special string pattern for a successful create
    # success_url = '/cats/{cat_id}'

# UpdateView, very similar to CreateView, needs model and fields
class CatUpdate(UpdateView):
    model = Cat
    # let's make it so you cant rename a cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    # instead of fields or using the absolure_url, we just use a success_url
    success_url = '/cats'