# Form 
## Basic Setup
### Import Forms:

```python
from django import forms
```
### Create a Standard Form:
```python
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2024)))
```
### Rendering Forms in Templates
- view 
```python
from blog.forms import SignupForm

form = SignupForm()

def signup(request):
    form = SignupForm()
    return render(request, "signup.html", context={"form": form})
```

- Basic Form rendering 
```html 
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
- Custom form rendering
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

