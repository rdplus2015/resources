
# **Django Class-Based Views (CBVs)**

## **Overview**

Class-Based Views (CBVs) in Django offer a structured way to handle HTTP requests by organizing related views into classes, promoting reuse and modularity. CBVs come in various types, each designed for common web application needs.

## **Base Views**

### **Base View: `View`**

The `View` class is the base class for all CBVs. It provides a way to define methods that handle different HTTP methods like GET, POST, etc.

#### **Example**
```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request, *args, **kwargs):
        # Logic to handle a GET request
        category = self.request.GET.get('category')
        # Retrieve posts based on the specified category
        # and pass them to the template for display
        return HttpResponse('Displaying data...')

    def post(self, request, *args, **kwargs):
        # Logic to handle a POST request
        title = self.request.POST.get('title')
        content = self.request.POST.get('content')
        # Process the data (e.g., create a new object in the database)
        return HttpResponse('Data submitted successfully!')
```

#### **Key Methods**
- `dispatch(self, request, *args, **kwargs)`: Determines the HTTP method (GET, POST, etc.) and calls the appropriate method (`get()`, `post()`, etc.).
- `http_method_names`: List of HTTP methods that the view will accept.

## **Class-Based Generic Views**

Django's class-based generic views provide abstract classes implementing common web development tasks.

### **Template View: `TemplateView`**

#### **Example**
```python
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About Us'
        context['description'] = 'Welcome to our about page.'
        return context
```

#### **Key Methods**
- `get_context_data(self, **kwargs)`: Add context to the template rendering.
#### Dynamic pages 
```python
# Import des modules nécessaires
from django.views.generic import TemplateView
from .models import Page  # Assurez-vous d'importer le modèle Page depuis votre application

# Définition de la classe DynamicTemplateView
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

# urls.py 

from django.urls import path
from .views import DynamicTemplateView

urlpatterns = [
    path('pages/<str:page_name>/', DynamicTemplateView.as_view(), name='dynamic_page'),
]
```


### **List View: `ListView`**

#### **Example**
```python
from django.views.generic import ListView
from .models import YourModel

class YourListView(ListView):
    model = YourModel
    template_name = 'yourapp/yourmodel_list.html'  # Specify your template
```

#### **Key Attributes**
- `model`: The model to query.
- `paginate_by`: Number of objects per page.

#### **Key Methods**
- `get_queryset(self)`: Return the list of items for this view.
- `get_context_data(**kwargs)`: Adds additional data to the template context.
- `paginate_queryset(queryset, page_size)`: Handles pagination of the queryset.


### **Detail View: `DetailView`**

#### **Example**
```python
from django.views.generic import DetailView
from .models import YourModel

class YourDetailView(DetailView):
    model = YourModel
    template_name = 'yourapp/yourmodel_detail.html'  # Specify your template
```

#### **Key Attributes**
- `model`: The model to query.
- `pk_url_kwarg`, `slug_url_kwarg`: URL keyword arguments for looking up the object.

#### **Key Methods**
- `get_object(self, queryset=None)`: Retrieves the object.
- `get_context_data(**kwargs)` : Adds additional data to the template context.

### **Form View: `FormView`**

#### **Example**
```python
from django.views.generic import FormView
from .forms import MyForm

class MyFormView(FormView):
    form_class = MyForm
    template_name = 'my_form.html'
    success_url = '/success/'

    def form_valid(self, form):
        # Do something with the form data
        return super().form_valid(form)
```

#### **Key Attributes**
- `form_class`: The form to use.
- `success_url`: URL to redirect upon successful form submission.

#### **Key Methods**
- `form_valid(self, form)`: Called when the form is valid.
- `form_invalid(self, form)`: Called when the form is invalid.

### **Create View: `CreateView`**

#### **Example**
```python
from django.views.generic.edit import CreateView
from .models import YourModel

class YourCreateView(CreateView):
    model = YourModel
    template_name = 'yourapp/yourmodel_form.html'  # Specify your template
    fields = '__all__'  # Or specify fields explicitly
```

#### **Key Attributes**
- `model`: The model to create.
- `fields`: Fields to display in the form.
- 
#### **Key Methods**
- `get_form_class()` : Returns the form class used by the view.
- `get_form(self, form_class=None)`: Returns the form use by the class 
- `get_form_kwargs()` : Returns additional arguments to pass to the form.
- `form_valid(form)` : Handles the case where the form is valid.
- `get_success_url()` : Returns the URL to redirect to after a successful form submission.


### **Update View: `UpdateView`**

#### **Example**
```python
from django.views.generic.edit import UpdateView
from .models import YourModel

class YourUpdateView(UpdateView):
    model = YourModel
    template_name = 'yourapp/yourmodel_form.html'  # Specify your template
    fields = '__all__'  # Or specify fields explicitly
```

#### **Key Attributes**
- `model`: The model to update.
- `fields`: Fields to display in the form.

#### **Key Methods**
- `get_form_class()` : Returns the form class used by the view.
- `get_form(self, form_class=None)`:Creates an instance of the form using the form class returned by get_form_class()
- `get_form_kwargs()` : Returns additional arguments to pass to the form.
- `form_valid(form)` : Handles the case where the form is valid.
- `get_success_url()` : Returns the URL to redirect to after a successful form submission.
- `get_object()`: Returns the object to be updated.

### **Delete View: `DeleteView`**

#### **Example**
```python
from django.views.generic.edit import DeleteView
from .models import YourModel

class YourDeleteView(DeleteView):
    model = YourModel
    template_name = 'yourapp/yourmodel_confirm_delete.html'  # Specify your template
    success_url = '/success-url/'  # Specify the URL to redirect to after delete
```

#### **Key Attributes**
- `model`: The model to delete.
- `success_url`: URL to redirect upon successful deletion.

- `get_object()` : Returns the object to be deleted.
- `get_success_url()`: Returns the URL to redirect to after a successful deletion.

## **Mixins**

Mixins add specific behaviors to views. You can combine them to create custom behavior.

#### **Examples**
- `LoginRequiredMixin`: Requires the user to be logged in.
- `PermissionRequiredMixin`: Requires the user to have specific permissions.

#### **Example Usage**
```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyProtectedView(LoginRequiredMixin, TemplateView):
    template_name = "protected.html"
```

## **Setting Up URLs**

#### **Example**
```python
from django.urls import path
from .views import AboutPageView, YourListView, YourDetailView, YourCreateView, YourUpdateView, YourDeleteView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('yourmodel/', YourListView.as_view(), name='yourmodel-list'),
    path('yourmodel/<int:pk>/', YourDetailView.as_view(), name='yourmodel-detail'),
    path('yourmodel/create/', YourCreateView.as_view(), name='yourmodel-create'),
    path('yourmodel/update/<int:pk>/', YourUpdateView.as_view(), name='yourmodel-update'),
    path('yourmodel/delete/<int:pk>/', YourDeleteView.as_view(), name='yourmodel-delete'),
]
```

## **Customization Tips**

1. **Override `get_context_data`** to add custom context to the template.
2. **Override `get_queryset`** to filter or modify the data returned.
3. **Override `dispatch`** for request-level customization.
4. **Use Mixins** to extend functionality like authentication and authorization.


## **Common Methods in CBVs**

- `get(self, request, *args, **kwargs)`: Handle GET requests.
- `post(self, request, *args, **kwargs)`: Handle POST requests.
- `get_context_data(self, **kwargs)`: Provide context for rendering templates.
- `get_success_url(self)`: Define the URL to redirect to after successful form handling.

## **Best Practices**

- Use CBVs for reusable and maintainable code.
- Combine multiple mixins and methods to achieve complex functionality.
- Keep your views clean by offloading logic to forms or serializers when possible.
- Test your views thoroughly, especially when using mixins and custom logic.

## **Useful Links**

- [Official Django Documentation: Class-Based Views](https://docs.djangoproject.com/en/stable/ref/class-based-views/)
- [Classy Class-Based Views (CCBV)](https://ccbv.co.uk/)