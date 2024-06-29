# MTV Architecture (Model-Template-View)
The Model-Template-View (MTV) architecture is the fundamental architecture of Django. It comprises the following
components:

- Models: Represent the data structure of the application.
- Templates: Handle the presentation of data and the user interface.
- Views: Process HTTP requests and responses.

In Django, URLs are associated with views or view classes that will be executed  to process the request associated
with this URL.

### Create a Django project
- `django-admin startproject todoapp` 
- `python manage.py runserver` 

### Create a URL path
Django uses the ROOT_URLCONF variable defined in the settings.py file to know which file to use to resolve URL paths.
By default, this variable points to the urls.py file located in the main folder of your Django application.
Inside this file, we can use the path function to associate a URL path with a view:
```python
from django.urls import path
from .views import index

urlpatterns = [
    path("index/", index, name="urlname")
]
```

### Create a view for the URL
```python
from django.http import HttpResponse

def index(request):
     return HttpResponse("Site home page")
```

### Return a template
```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

### Insert data into a template

```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html", context={"value": 5})
```
```html 
<h1>The value associated with the key "value" is {{ value }}</h1>
```
 