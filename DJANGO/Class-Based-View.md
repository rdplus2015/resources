# Class-Based View

- In a class based view, the query is usually accessed as a class attribute:
```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def post(self, request, *args, **kwargs):
        # Logic to handle a POST request
        title = self.request.POST.get('title')
        content = self.request.POST.get('content')
        # Process the data (e.g., create a new object in the database)
        return HttpResponse('Data submitted successfully!')
```
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
```

## Class-based generic views
- Django's class-based generic views provide abstract classes implementing common web development tasks.


```python
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import YourModel

class AboutPageView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About Us'
        context['description'] = 'Welcome to our about page.'
        return context

class YourListView(ListView):
    model = YourModel
    template_name = 'yourapp/yourmodel_list.html'  # Specify your template

class YourDetailView(DetailView):
    model = YourModel
    template_name = 'yourapp/yourmodel_detail.html'  # Specify your template

class YourCreateView(CreateView):
    model = YourModel
    template_name = 'yourapp/yourmodel_form.html'  # Specify your template
    fields = '__all__'  # Or specify fields explicitly

class YourUpdateView(UpdateView):
    model = YourModel
    template_name = 'yourapp/yourmodel_form.html'  # Specify your template
    fields = '__all__'  # Or specify fields explicitly

class YourDeleteView(DeleteView):
    model = YourModel
    template_name = 'yourapp/yourmodel_confirm_delete.html'  # Specify your template
    success_url = '/success-url/'  # Specify the URL to redirect to after delete
```
```python
from django.urls import path
from .views import AboutPageView

urlpatterns = [
    path('urlpath/', MygenericView.as_view(), name='urlname'),
]
```
- Using Class-Based Views (CBV) is often advantageous in projects where modular structure, reusability, and maintainability are essential, and allows the use of mixins.
- In certain situations, you will need to create your own custom views to handle specific use cases, performance requirements, third-party integrations, or complex business logic.

- [Documentation](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/)
- [Documentation](https://ccbv.co.uk/)
