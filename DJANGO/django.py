#  VIRTUAL ENVIRONMENT
"""
- python3.10 -m venv .env  // create a python environment in the folder (.env is the name of your venv)
- source .env/bin/activate  // activate the environment
- deactivate // deactivate it
- rm -rf .env // delete the environment

    organize your work and guarantee the portability of your projects.
    A virtual environment isolates your project dependencies,
    meaning you can have different versions of packages for different projects without conflicts.

    When you move your project folder to a server or other location, the virtual environment 
    you created (if it is included in your project folder) does not automatically move with it. 
    Only files and directories present in your project folder will be moved.However, you can easily recreate the virtual environment on the new system with the requirement file
"""

# DJANGO INSTALLATION
"""
- pip install --upgrade pip // upgrade pip before install django
- pip install django=3.1.6  / - python -m django --version // install and check django version

- pip freeze > requirements.text  // write all dependencies on requirement file
- pip install -r requirements.txt // reinstall django and all dependencies  / - cat requirements.txt // read the file

- django-admin startproject project name // Initialise a new project with django structure
- django admin --help
- python manage.py runserver // run the server

#Dependency isolation  #Python versioning  #Ease of distribution => requirements.text
#System cleanliness and conflicts
"""

# DJANGO OPERATING DIAGRAM
"""
The Django operating diagram, which is based on the MTV (Model-Template-View) architecture,
involves clear communication between URLs, views, models, templates and other components.
"""

# URLs
"""
In Django, URLs are associated with views or view classes that will be executed 
to process the request associated with this URL.

You define URL schemes in an urls.py file for each Django application
which maps URLs to corresponding views.
"""

# Vue
"""
The View represents the logic for processing requests and responses.
It retrieves the necessary data from the models, processes it if necessary, 
then renders them in the templates to generate the HTTP response. (take an HTTP request and return an HTTP response)
"""

#Modèles
"""
Django models represent the data structure of your application.
They are defined in models.py files and generally correspond to tables in a relational database.

    ORM (Object-Relational Mapping) :
    Django provides a powerful ORM that allows you to manipulate database data using Python objects,
    without having to write SQL queries directly.
"""

# Templates
"""
The Template represents the data presentation and the user interface.
"""

# START WITH DJANGO: BASICS MANIPULATIONS
#1
"""
1. Create a URL (urls.py), return a view (create views.py) and in the view, use a function helloworld and 
return Hello world in a html tag with HttpResponse.

2.Create a Templates directory (Default django directory for UI templates), and create a index.html file inside 
and in your view file, return this html file with render.

In your view with render(), you can return files, and others python modules data to a templates files 
#return render(request, 'index.html', context={'date': date})


-by default django looks for Templates and Statics (name known by Django)folder only in applications. 
if you don't create an application, You can manually create and add the path of a directory to the setting.py 
file so that it can be found by Django

STATICFILES_DIRS[
    os.path.join(BASE_DIR, 'directory/static')  => django will search and in application frst 
    (attention with name conflict)
]

TEMPLATES[
    'DIRS': [os.path.join(BASE_DIR, 'docblog/templates')], # for templates
    #'DIRS':['absolute_path_of_the_directory'] 
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'myapp',  #Alwas add the App you create here, 
]

Conflicts
    Templates/appname/index.file appname_file
"""

"""
href="{%static 'css/style.css' %} "  path towards static => important for migration | {% load static %} 
in the begging of the page to be able to call {% %} 
# be careful with name conflict when we use many static folder in different application => rename css file or use
sub folder
"""

# ORM
"""
Django models allow us to link with our application's database. For this we use an ORM (Object Relational Mapping) 
which will allow us, with Python code, to represent our database and to create, update and delete entries 
in our database.

To create a model, we use object-oriented programming by creating a class that inherits from the Model class of the 
django.db.models module.

1. Create table for the application
lass BlogPosts(models.Model): #APP DB TABLE
    title = models.CharField(max_length=255) # DB FIELDS OR COLUMN 
    status = models.BooleanField(default=False) # DEFAULT VALUE 
    date = models.DateField(blank=True) # ALLOW BLANK ENTRY 

2. Make migration 
file that allows you to write to the database. contains history in the database and also allows 
to recreate the database structure

# python manage.py makemigrations appname => make migrations
# python manage.py migrate appname => apply migrations in your database 
# python manage.py sqlmigrate appname migrationname => apply migrations in your database and show sql code 
python manage.py shell => use interactive shell (not python interpreter)

3. create object
# TERMINAL 1 
>> from blog.models import BlogPost
>> post = BlogPost
>> post.save()
>> 
>> 
"""

# ORM (SHELL)
"""
    - model_name.objects.create(attr = 'value') / create automatically the object (don't need to use save() methode )
    - class_name.objects.get.all() / get all objects
    - class_name.objects.get.last()
    - object = class_name.objects.get(pk=1) / get by an attr
    - object.attr "New value" / Insert or Update
    - class_name.objects.get().all().delete() or 
    - var = class_name.objects.all() => Var[0:3].delete() // Delete Object
    # delete() does not work with more than two elements in a list => use for loop
"""

# FILTER
"""
class_name.objects.filter()
class_name.objects.filter()[0:5]
class_name.objects.filter(date__year='2020')[0:5].filter(published=True)
class_name.objects.filter(date__year='2020', title='abcde').exclude(published=True)
"""

# Add a property to the class and class overload
"""
    - Adding properties (methods and attributes) to our classes allows us to not always be
      create fields to display messages or personalized elements.
      added property work with the instance => (self)
      
        @property #use methode like attr 
        def publish_string(self):
            if self.published:
                return "the article was published"
            return "Article not found"
            
        >> object.published_string 
        >> the article was published or Article not found
        
        
        # Overload an Existing method  => OOP 
        
        def save(self, *args, **margs):
            if not self.slug:
                self.slug = slugify(self.title)
            super().save(*args, **margs)
"""

# ORM - RELATIONSHIP
"""
# Create Superuser
    - python manage.py createsuperuser
# Many to One 
    - class BlogPosts(models.Model):
            author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
            # on_delete = models.CASCADE # SET_DEFAULT, default = 1 # models.PROTECT
    
    >>> from blog.models import BlogPosts as bp
    >>> from django.contrib.auth.models import User as u
    >>> user = u.objects.get(pk=1)
    >>> post = bp.objects.get(pk=1)
    >>> post.author = user
    >>> post.save()
    
# Many to Many
     - class BlogPosts(models.Model):
            author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
            # on_delete = models.CASCADE # SET_DEFAULT, default = 1 # models.PROTECT
            category = models.ManyToManyField(Category) # add category  
            # Category class must be defined before BlogPosts class 
            
    >>> from blog.models import BlogPosts, Category
    >>> bp = BlogPosts.objects.all()
    >>> cat = Category.objects.all()
    >>> bp[0].category.set([cat[0], cat[1]]) 
    >>> bp[0].category.clear() # delete all manytomany relations
    
    #set() methode overwrite older value, use add() for adding
    # we can use variable for do the same operations
    >>> post = BlogPosts.objects.get(pk=1)
    >>> post.category.add(cat[0])
    post.category.remove(cat[0]) # remove one ManyMany relation 

# Reverse operations
    # one to many or Many to Many
    - instance.classnameinmin_set.a()  # can use author filter methods
    >>> cat = Category.objects.get(pk=1)
    >>> cat.blogposts_set.all()
    <QuerySet [<BlogPosts: BlogPosts object (1)>, <BlogPosts: BlogPosts object (2)>]>
"""

#VIEW
#HTTPRESPONSE
"""
httpResponse => is the basis of everything we return in our views; text, html pages, Json or 404 by 
modifying its attributes => content, status code, content-type

def Blog_posts(request):
    r = HttpResponse()
    r.content = "Bonjour tout le monde"
    r.status_code = 404
    r[content-type] = 'application/json'
    
# 404
def blogp(request):
    try:
        bp = class-name.objects.get(pk3)
    except class-name.DoesNOtExists:
        raise Http404("not found")
    return HttpResponse(blogp.content)

"""

#SHORTCUT
"""
no need to go through httpresponse for 404 and json and others. these elements have their own purpose
inheriting from the httpresponse class.
use the render shortcut function


#JsonRespinse 
def blogpost(request):
    jr = JsonResponse({"1": "premier article})
    jr.status_code = 202
    return jr 
   
    
#redirect
def blogp(request):
    return redirect("url link or ")

#404
def blog_post(request):
    blog_p = get_object_or_404(BlogPosts, pk=1)


#restriction connected user
#above of a view
@login_required
def blog_post(request):
    blog_p = get_object_or_404(BlogPosts, pk=1)


#restriction with condition 
@user_passes_test(lambda u: u.username =='test')
def blog_post(request):
    blog_p = get_object_or_404(BlogPosts, pk=1)
    # we can use a function with def syntax => lambda is better and readable 
"""

#GABARITS

#var
"""
context={'a': data-from-db} # send data from db to html template 
{{dict-key.object-attr}} # call the content of the variable  
# _ or () are not accepted before variable and methods
"""

#condiotion
"""
{% if var %}
    #HTML TAG  => indentation is not required 
{% elif or else var %}
{% endif var %}
"""

# for loop
"""
{% for post in blog_posts %}
    <h1>{{ post.title }}</h1>
{% endfor %}
"""

#url
"""
<a href="{% url 'index' %}">home</a> 
<a href="{% url 'post' slug='about-us' or slug=post.title %}">services or article</a>
"""

#Alias
"""
{% with a = post.tile  %}
    # html code here, use the alias instead of a long query 
{ % endwith  %}

"""

#filter
"""
django gabarit has filter such as lower() or upper() 
but it preferable to use python methods in the view instead
{{ post.title|lower}} | we can use it inside of python such as slugify filter
{{post.content|truncatwords:300|safe}}
"""

#Escape
"""
{{post.content|safe}} 
# the safe filter allows your code to understand and interpret the tags. can be dangerous 
for Js tag when user must send you data.
# we  can use it when with get some data from our db 
{% autoescape off %}
    # html tag -> we can use autoescape if have many place that we need to use safe filter
    # by default is on when the user send data and off when we get data from db 
{ % endautoescape  %}
"""

# Template extension
"""
{% extends 'source/index.html'%} #import the template in your file  
{%bloc bloc-name %} html tag {%bloc endblock %} #insert your data inside. 
that must be place in the template file where the data must be inserted 
"""

# ADMIN DASHBOARD

#Simple
"""
# admin.py
from django.contrib import admin
from blog.models import BlogPost

admin.site.register(BlogPost)

This function allows you to indicate to Django that this model must be present in the administration interface.
"""

#Advaned
"""
To provide a few more options for displaying and editing models, we can create a class that inherits 
from admin.ModelAdmin and use the admin.register decorator

from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
"""

# Admin class managemeent
"""
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display (), list_editable(), list_display_links = (),  search_fields = (), list_filter = (), autocompletfiels()
    empty_value_display = "Unknown"
    list_per_page = 1
    # filter_horizontal 
"""

# custom model
"""
    class Meta: # use it in model 
        verbose_name = 'Article'
    
    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug}) 
        
    @property
    def word_count(self): # call that property in your admin file in list_display 
        return len(self.content.split()) 
"""

# FORM BASED ON FUNCTION
"""
# form.py 
# create amd add fields 

from django import forms
class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=12, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOB, widget=forms.RadioSelect()) # CheckboxSelectMultiple() JOB is a tuple 
    cgu_accept = forms.BooleanField(initial=True)
    
    # verification of one field
    clean_pseudo(self):
        pseudo = self.cleaned_data.get('pseudo)
        if '$' in pseudo:
            raise forms.ValidationError('incorrect value')
        return pseudo 
            
            
# make instance and print 
# views.py
from blog.forms import SignupForm

form = SignupForm()

def signup(request):
    form = SignupForm()
    return render(request, "signup.html", context={"form": form})

    <form method="POST">
        {% csrf_token %}
        {{ form.as_p}}
        <input type="submit" value="S'inscrire">
    </form>
    

# Retrieve data et clean it
# view.py 
from blog.forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST) # form passed to the view, never empty 
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SignupForm() # if there is no data, return empty form 

    return render(request, 'signup.html', context={"form": form})

# Form based on a model
from django import forms
from blog.models import BlogPost

class SignupForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__" # ['author', ...]
        # exclude('status)
    
    # modified label 
    labels = ['title' = 'y title']
    widgets = ("date", forms.SelectDateWidget(year=range(2000-2050))

#Save form
from blog.forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False) #True by default
            model.cgu_accept = True
            model.save()
        return HttpResponseRedirect(request.path) # redirect to the current url 
    else:
        # automatic refill 
        init_values = {}
        if request.user.is_authenticated:
        init_values=["author"] = request.user
    init_values=["date"] = datetime.today()
        form = SignupForm(initial=init_values)

    return render(request, 'signup.html', context={"form": form})

# Initial Value
"""

# VIEW BASED ON CLASS

# View

# TemplateView

# Simple way
"""
#view.py
class HomePageView(TemplateView):
    template_name = 'home.html'

#urls.py
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    ]
"""


# return one template and send dynamic data (medium level)
# the advantage is that you have just one methode to write for change context data
"""
#view.py
class BasePageView(TemplateView):
    template_name = None
    title = None # title can contain data from database and be define here 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class HomePageView(BasePageView):
    template_name = 'home.html'
    title = 'Home' # remove if content is from database 

#urls.py 
urlpatterns = [
    path('example/<str:title>/', HomePageView.as_view(), name='example'),
    path('example/', HomePageView.as_view(title='xxx'), name='example'),
]
"""

# Advanced # dynamic template and one Url
"""
templates/
└── base_templates/
    ├── base.html
    └── partials/
        ├── header.html
        └── footer.html
└── pages/
    ├── page1.html
    └── page2.html

# views.py
from django.views.generic import TemplateView
from .models import Page

class DynamicTemplateView(TemplateView):
    base_template_path = 'base_templates/base.html'
    pages_template_path = 'pages/'

    def get_template_names(self):
        page_name = self.kwargs.get('page_name')
        template_name = f"{self.pages_template_path}{page_name}.html"
        return [template_name, self.base_template_path]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_name = self.kwargs.get('page_name')
        page = Page.objects.get(title=page_name)  # Supposons que le titre correspond au nom de la page
        context['page'] = page
        return context
        
Simplicity in URL management: Having a single URL simplifies the configuration in urls.py, reducing the complexity of
managing URLs in your application.

Flexibility of data model: Using a slug in the URL allows your application to be flexible by enabling easy addition, 
modification, and deletion of pages in the database without needing to modify URLs in your application code.

Code reusability: By using a single view to handle all dynamic pages, you can reuse the same code to render different 
pages, reducing code duplication and simplifying maintenance of your application.

Performance: Ensure that the template lookup based on the slug is efficient to avoid performance issues, especially 
if you have a large number of dynamic pages in your application.
"""

# Create View
