# Form 
## Basic Setup
- ### Import Forms:
```python
from django import forms
```
- ### Create a Standard Form:
```python
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0)
```

- ### Create a ModelForm:
```python
from .models import ExampleModel

class ExampleModelForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ['name', 'email', 'age']
    labels = {'name': 'yourlabel'}
    widgets = {"date": forms.SelectDateWidget(year=range(2000-2050)}
```

## Widgets
```python
class CustomForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email-input'}))
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2024)))
```

## Validation 

- ### Automatic Validation:
```python
class SimpleForm(forms.Form):
    email = forms.EmailField()
```

- ### Custom Validation:
```python
class SimpleForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email must be from example.com domain')
        return email
```

- ### Global Validation:
```python
class SimpleForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
```

## Rendering Forms in Templates
- ### view
```python
from blog.forms import SignupForm

form = SignupForm()

def signup(request):
    form = SignupForm()
    return render(request, "signup.html", context={"form": form})
```

- ### Basic Form rendering 
```html 
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

- ### Custom form rendering
```html
<form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    <div>
        {{ form.name.label_tag }}
        {{ form.name }}
        {{ form.name.errors }}
    </div>
    <div>
        {{ form.email.label_tag }}
        {{ form.email }}
        {{ form.email.errors }}
    </div>
    <button type="submit">Submit</button>
</form>
```

## Handling Form Data

- ### Basic View to Handle Form:
```python
from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid data
            # form.save()
        # return HttpResponseRedirect(request.path)
            pass 
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values=["author"] = request.user
        init_values=["date"] = datetime.today()
        form = ExampleForm(initial=init_values)
    return render(request, 'example_template.html', {'form': form})
```
## Using ModelForm
- ### ModelForm for Create and Update:

```python
from django.shortcuts import render, get_object_or_404
from .models import ExampleModel
from .forms import ExampleModelForm

def create_or_update_example(request, pk=None):
    if pk:
        instance = get_object_or_404(ExampleModel, pk=pk)
    else:
        instance = None

    if request.method == 'POST':
        form = ExampleModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            # Redirect or further processing
    else:
        form = ExampleModelForm(instance=instance)
    return render(request, 'example_template.html', {'form': form})
```

##  File Uploads
- ### Form with File Field:

```python
class UploadFileForm(forms.Form):
    file = forms.FileField()
```
- ### View to handle the file 
```python
def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            # Further processing
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('destination/path/filename', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
```

## Adding CSS and JavaScript
- ### Customize via Widgets:
```python
class StyledForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-input', 'placeholder': 'Your name'}))
```
- ### Add CSS Classes::
```python
<form method="post" class="custom-form">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
## Error Messages
- ### Display Errors in Templates:
```python
{% for field in form %}
    <div>
        {{ field.label_tag }}
        {{ field }}
        {% for error in field.errors %}
            <div class="error">{{ error }}</div>
        {% endfor %}
    </div>
{% endfor %}
```
# Here’s a practical example using Django 

## Models
- ### First, let’s create a model to use with a ModelForm.
```python
# models.py

from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```
## Forms
- ###  Standard Form
````python
# forms.py

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    attachment = forms.FileField(required=False)

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if 'spam' in subject.lower():
            raise forms.ValidationError("Subject contains forbidden word 'spam'.")
        return subject
````
- ### ModelForm
```python
# forms.py

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'birthdate', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthdate': forms.SelectDateWidget(years=range(1900, 2025), attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the example.com domain.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name and first_name == last_name:
            raise forms.ValidationError("First and last names cannot be the same.")
```
## View
```python
# views.py

from django.shortcuts import render, redirect
from .forms import ContactForm, UserProfileForm
from django.core.files.storage import FileSystemStorage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')
            
            # Handle file upload
            if attachment:
                fs = FileSystemStorage()
                filename = fs.save(attachment.name, attachment)
                uploaded_file_url = fs.url(filename)
            else:
                uploaded_file_url = None

            # Process form data here (e.g., send email)
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = UserProfileForm()
    return render(request, 'profile_form.html', {'form': form})
```
## Template
- ### Contact Form Template

```html
<!-- templates/contact_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Contact Us</h2>
        <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.non_field_errors }}
            <div class="form-group">
                {{ form.subject.label_tag }}
                {{ form.subject }}
                {% for error in form.subject.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.message.label_tag }}
                {{ form.message }}
                {% for error in form.message.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.attachment.label_tag }}
                {{ form.attachment }}
                {% for error in form.attachment.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```
- ### Profile Form Template
```html
<!-- templates/profile_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Create Profile</h2>
        <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.non_field_errors }}
            <div class="form-group">
                {{ form.first_name.label_tag }}
                {{ form.first_name }}
                {% for error in form.first_name.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.last_name.label_tag }}
                {{ form.last_name }}
                {% for error in form.last_name.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.email.label_tag }}
                {{ form.email }}
                {% for error in form.email.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.birthdate.label_tag }}
                {{ form.birthdate }}
                {% for error in form.birthdate.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.profile_picture.label_tag }}
                {{ form.profile_picture }}
                {% for error in form.profile_picture.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <button type="submit" class="btn btn-primary">Save Profile</button>
        </form>
    </div>
</body>
</html>
```
## URL Configuration
```python
# urls.py

from django.urls import path
from .views import contact_view, profile_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('profile/', profile_view, name='profile'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
```
## Success Page Template
```html
<!-- templates/success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Success!</h2>
        <p>Your form has been successfully submitted.</p>
        <a href="{% url 'contact' %}" class="btn btn-primary">Back to Contact Form</a>
        <a href="{% url 'profile' %}" class="btn btn-primary">Back to Profile Form</a>
    </div>
</body>
</html>
```


## Form Fields
### Field Type	Django Class
- Text:`forms.CharField`
- Email:`forms.EmailField`
- Number: `forms.IntegerField`
- Decimal:`forms.DecimalField`
- Date:`forms.DateField`
- URL:`forms.URLField`
- Boolean:`forms.BooleanField`
- Choice:`forms.ChoiceField`
- File:`forms.FileField`
- Image:`forms.ImageField`

## Widgets
### Widget	Django Class
- Input Text: `forms.TextInput`
- Textarea: `forms.Textarea`
- Checkbox: `forms.CheckboxInput`
- RadioButton: `forms.RadioSelect`
- Select: `forms.Select`
- MultiSelect: `forms.CheckboxSelectMultiple`

Opt for Django forms for robust validation, model integration, and security needs, and prefer HTML forms for specific requirements in design, client-side interaction, or simplicity when Django is not involved. 
Use Model Forms when you need to create or update database records.