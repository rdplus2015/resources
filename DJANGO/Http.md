# Http 
HttpRequest and HttpResponse are fundamental objects for handling HTTP requests and constructing HTTP responses.

## HttpRequest
The HttpRequest object represents the HTTP request sent by the client (web browser, mobile application, etc.) 
to the Django server. It contains information about the request and provides methods to access this information.

### request.method :
This indicates the HTTP method used for the request ('GET', 'POST', 'PUT', 'DELETE', etc.).
```python
if request.method == 'POST':
    # Handle a POST request
```

### request.GET :
A dictionary-like object containing all the GET parameters (those passed in the URL).
```python
search_term = request.GET.get('search', '')
```

### request.POST :
A dictionary-like object containing all the POST data.
```python
username = request.POST.get('username')
```

### request.FILES :
A dictionary-like object containing all the uploaded files via a POST request.
```python
uploaded_file = request.FILES['document']
```

### request.user :
The currently authenticated user (if Django’s authentication system is used).
```python
if request.user.is_authenticated:
    # Do something with the user
```

### request.path :
The URL path of the request.
```python
current_path = request.path
```

### request.META :
A dictionary containing all the metadata of the request, such as HTTP headers.
```python
user_agent = request.META['HTTP_USER_AGENT']
```

## HttpResponse Object 
In Django, the HttpResponse object is used to represent the HTTP responses returned by a view.

### Creation :
You can create a response by instantiating HttpResponse directly.
```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world!")
```

### Content:
The first argument to HttpResponse is the content of the response. It can be text, HTML, JSON, etc. 
You can also set the content type with the  `content_type` argument 
```python
response = HttpResponse("<h1>Hello, world!</h1>", content_type="text/html") 
```
### HTTP Headers
You can add HTTP headers to the HttpResponse object.
```python
response = HttpResponse("Hello, world!")
response['Custom-Header'] = 'CustomValue'
```

### HTTP Status
The default HTTP status code is 200 (OK), but you can change it using the status argument.
```python
response = HttpResponse("Not Found", status=404)
```

```python
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def example_view(request):
    if request.method == 'GET':
        # Retrieve data from the GET request
        param = request.GET.get('param', 'default_value')
        return JsonResponse({'param': param})

    elif request.method == 'POST':
        # Process POST data
        data = request.POST.get('data')
        if data:
            return JsonResponse({'status': 'success', 'data': data})
        else:
            return JsonResponse({'status': 'error', 'message': 'No data provided'}, status=400)

    else:
        return HttpResponse(status=405)  # Method not allowed
```

## Shortcut Functions

### render
Used to render a template with a given context.
```python
from django.shortcuts import render

def my_view(request):
    context = {'key': 'value'}
    return render(request, 'my_template.html', context)
```
```python
from django.shortcuts import render

def home_view(request):
    context = {'name': 'John Doe'}
    return render(request, 'home.html', context)
```

### redirect :
Used to redirect to another URL.
```python
from django.shortcuts import redirect

def my_view(request):
    return redirect('/some/url/')
```
```python
from django.shortcuts import redirect

def form_submit_view(request):
    if request.method == 'POST':
        # Handle form submission
        return redirect('/success/')
    return HttpResponse("Invalid method", status=405)
```

### get_object_or_404 :
Retrieves an object or returns a 404 error if the object does not exist.
```python
from django.shortcuts import get_object_or_404
from myapp.models import MyModel

def my_view(request, id):
    obj = get_object_or_404(MyModel, id=id)
    return HttpResponse(f"Object: {obj}")
```
```python
from django.shortcuts import get_object_or_404
from myapp.models import MyModel

def detail_view(request, id):
    obj = get_object_or_404(MyModel, id=id)
    return HttpResponse(f"Details of {obj.name}")
```

### get_list_or_404 :
```python
from django.shortcuts import get_list_or_404
from myapp.models import MyModel

def my_view(request):
    objects = get_list_or_404(MyModel)
    return HttpResponse(f"Objects: {objects}")
```

HTTP requests are simply requests sent by a client (such as a web browser) to a web server (like the one your Django 
site is running on). Use GET when retrieving data from the server in a safe manner without altering the server’s state, 
and use POST when sending data to the server that modifies its state or when sending sensitive or large amounts of data.

[Documentation](https://docs.djangoproject.com/en/5.0/ref/request-response/#httprequest-objects)
