from django.shortcuts import render

# Create your views here.

# define the home view
def home(request):
    # unlike EJS templating, we need the html file extension
    return render(request, 'home.html')

# define the about view
def about(request):
    return render(request, 'about.html')