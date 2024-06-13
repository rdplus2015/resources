# Function Based View
- A view is simply a Python function that receives an HTTP request as input and returns an HTTP response as output.

```python
from django.http import HttpResponse

def my_view(request):
    # Processing the HTTP request
    if request.method == 'GET':
        # Logic to handle a GET request
        return HttpResponse('This is a response to a GET request')
    elif request.method == 'POST':
        # Logic to handle a POST request
        return HttpResponse('This is a response to a POST request')
```

### POST Method:
- Used to send data to the server for processing, typically employed for actions that modify the state of the server.
```python
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Processing the data (e.g., creating a new object in the database)
    # Rest of the view...
```

### GET Method :
- Used to request data from a specific resource, typically used to retrieve data to display to the user.
```python
def show_posts(request):
    if request.method == "GET":
        category = request.GET.get('category')
        # Retrieve posts based on the specified category
        # and pass them to the template for display
    # Rest of the view...
```

## CRUD OPERATIONS 

###  form.py
```python
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']
```

### Create 
```python
from django.shortcuts import render, redirect
from .forms import MyModelForm

def create_view(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = MyModelForm()
    return render(request, 'create_template.html', {'form': form})
```

### Read 
```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
```
```python
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})
```

### Update
```python
def update_view(request, id):
    obj = MyModel.objects.get(id=id)
    if request.method == "POST":
        form = MyModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = MyModelForm(instance=obj)
    return render(request, 'update_template.html', {'form': form})
```

### Delete 
```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel

def delete_view(request, id):
    obj = get_object_or_404(MyModel, id=id)
    
    if request.method == "POST":
        obj.delete()
        return redirect('success_url')  # Replace 'success_url' with the URL name or path
    
    return render(request, 'delete_template.html', {'object': obj})
```

### Context of use
- `Display of static or dynamic data`: Presentation of content that does not require user input or data manipulation.
- `Simple request handling`: Responding to simple requests such as fetching a list of articles from a database or returning data in JSON format via an API.
- `Simple redirection`: Redirecting users to a specific page, such as a login page, if the user is not authenticated.
- `File download`: Generating and downloading files such as PDF or CSV based on available data.
- `CRUD operations`:  CRUD is also possible without a form but the form helps you validate the data.

### FBV VS CBV 
- Ease of understanding and writing
- Direct manipulation of request and response
- Less structure compared to CBV
- Potential lower reusability
- Potential maintenance difficulty

[Documentation](https://docs.djangoproject.com/en/5.0/topics/http/views/#writing-views)
