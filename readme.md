# Avocado Cat Collector
<sup><sub>**OOP Django Lesson built for SEI-Avocados**</sub></sup>

A Django-based web application for managing a collection of cats, with features for creating, updating, and associating cats with toys and feeding schedules. 

Built as a learning project, this app demonstrates practical use of Object-Oriented Programming (OOP) principles within the Django framework.

## Project Overview
This app lets users:
- Create and manage profiles for their cats.
- Assign toys to cats and track feeding times.
- Leverage Django’s ORM and authentication system for a seamless CRUD experience.

The codebase follows Django’s MTV (Model-Template-View) pattern, with a heavy reliance on OOP to keep logic modular, reusable, and maintainable.

>Side note! 
> Django's MTV is just their version of MVC, the core principles are basically the same, with only slight differences. Over the course of this lesson we'll go over the key differences and why django uses this pattern as opposed to a traditional MVC. The main reason, is that django uses the term 'view' to refer to specific classes that aren't a traditional browser view, those are typically handled by django's built-in templating language!

## OOP Highlights
Here’s how this project showcases the core pillars of Object-Oriented Programming:

#### Encapsulation
- **Models (`main_app/models.py`)**: The `Cat`, `Toy`, and `Feeding` classes encapsulate data and behavior. For example:
```python
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
```
The Cat class bundles attributes (name, breed) with methods like `fed_for_today`, keeping related logic self-contained and protecting data integrity.

#### Inheritance
##### Model Inheritance: 
All models inherit from Django’s `models.Model` base class, gaining database functionality (e.g., save, query) without redundant code.

>Example: Feeding inherits relational capabilities via ForeignKey to Cat, building on the parent class’s structure.

##### View Inheritance (main_app/views.py):
Class-based views like CatCreate extend Django’s `CreateView`:
```python
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
```
This reuses generic CRUD logic while customizing it for the Cat model.

#### Polymorphism
##### Method Overrides: 
The `get_absolute_url` method is implemented differently across models:
```python
def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})
```
Each model (Cat, Toy) provides its own version, adapting the same interface to its context—classic polymorphism in action.

>Why It’s Polymorphic: Both Cat and Toy implement the same method name (`get_absolute_url`), but each provides a unique implementation suited to its context. This allows views or templates to call `object.get_absolute_url()` without knowing the specific class, showcasing polymorphism in practice. For instance, a template can use `{{ cat.get_absolute_url }}` or `{{ toy.get_absolute_url }}` interchangeably, and the correct URL is generated dynamically.

#### Abstraction
##### Django ORM: 
The use of models.Model abstracts away raw SQL, letting me focus on high-level object interactions. For instance, `Cat.objects.all()` hides the database query complexity.

Let's go more in depth with another example:

```python
  # In main_app/views.py or a shell
  # Gets all cats older than 5
  cats = Cat.objects.filter(age__gt=5)
```

**How It Works:** This single line hides the complexity of SQL queries (e.g., `SELECT * FROM main_app_cat WHERE age > 5`). The `models.Model` base class provides this abstraction, letting me work with objects instead of raw database calls. I can call `cat.save()` or `cat.delete()` without writing SQL, focusing on the app’s logic instead.


##### Forms (main_app/forms.py): 
Abstraction also takes place with django's use of forms.
The `FeedingForm` class abstracts form validation and rendering:
```python
class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
```
This simplifies user input handling while keeping the interface clean.

**Benefit:** This abstracts away manual HTML form creation and input validation, reducing repetitive code. The form’s `is_valid()` method encapsulates all checks, making it reusable across views like FeedingCreate.

### Key OOP Features in Action
##### Relationships: 
The Cat and Toy models use a Many-to-Many relationship via `toys = models.ManyToManyField(Toy)`. This encapsulates complex relational logic into a single attribute, showcasing composition.

##### Custom Methods: 
`Cat.fed_for_today()` demonstrates behavior tied to the object, reducing external dependencies and reinforcing encapsulation.

##### Class-Based Views: 
Views like CatUpdate and CatDelete inherit from Django’s `UpdateView` and `DeleteView`, extending functionality with minimal code.

##### Why OOP Matters Here
Using OOP in this project:
- Keeps code modular: Each class (e.g., Cat, Feeding) handles its own domain.
- Makes it scalable: Adding new models or features (e.g., a VetVisit class) is straightforward thanks to inheritance and abstraction.
- Improves readability: Encapsulated logic in classes reduces clutter compared to a procedural approach.
---

Check out `main_app/models.py` and `main_app/views.py` for the core OOP implementations!

---
### Running the Project
##### Clone the repo: 
`git clone https://github.com/timmshinbone/avocado_catcollector.git`
##### Install dependencies: 
`pip install -r requirements.txt`
##### Set up the database: 
`python manage.py migrate`
##### Run the server: 
`python manage.py runserver`

---
## Deployment
This project is fully deployed and accessible live at [https://avogatocollector.onrender.com/](https://avogatocollector.onrender.com/){:target="_blank"}, hosted on Render’s scalable platform. The app leverages a Neon SQL database for persistent storage, ensuring reliable data management for cat profiles, toys, and feeding records.

- **Neon SQL Database**: Integrated as the backend database using PostgreSQL, Neon provides a serverless, cloud-native solution. The Django ORM connects seamlessly via the `DATABASES` setting in `settings.py`, abstracting connection pooling and scaling. This setup supports efficient queries like `Cat.objects.all()` while keeping deployment lightweight.

- **Render Hosting**: Deployed on Render, the app benefits from automatic scaling and a straightforward CI/CD pipeline tied to this GitHub repo. Environment variables (e.g., `DATABASE_URL`, `SECRET_KEY`) are managed securely in Render’s dashboard, aligning with Django’s best practices.

Visit the live site [here](https://avogatocollector.onrender.com/){:target="_blank"} to see the app in action!

Built with Python, Django, and a love for cats 🐱.