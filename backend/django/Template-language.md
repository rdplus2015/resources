# Django Template Language (DTL)

## variables
- Syntax: `{{ variable }}` 
- Example: Display a variable: `{{ user.username }}` or ` {{ object.method() }}`

## Filters
- Syntax: `{{ variable|filter }}`
- Examples: Capitalize: `{{ "hello world"|capfirst }}`
- Examples: Length: `{{ list|length }}`

### Common Filters
- ### Text Manipulation
    - Capitalize: `{{ "hello"|capfirst }}`
    - Uppercase: `{{ "hello"|upper }}`
    - Lowercase: `{{ "HELLO"|lower }}`
    - Title: `{{ "hello world"|title }}`
- ### List Manipulation
  - Length: `{{ list|length }}`
  - Index: `{{ list.0 }}`
- ### Others
    - Date: `{{ date|date:"d-m-Y" }}`
    - Safe for HTML: `{{ unsafe_string|safe }}`
    - the safe filter allows your code to understand and interpret the tags. can be dangerous for Js tag when user must send you data.
    - we  can use it when with get some data from our db 
  
```python
{% autoescape off %}
    - <htmltag> </htmltag> we can use autoescape if have many place that we need to use safe filter
    - by default is on when the user send data and off when we get data from db 
{ % endautoescape  %}
```

## Tags
- Syntax: `{% tag %}`
- Examples:
    - For: `{% for item in list %} ... {% endfor %}`
    - If: `{% if condition %} ... {% endif %}`
```python
{% for item in list %}
    <htmltag> {{ item }}  </htmltag>
{% endfor %}
```
```python
{% if user.is_authenticated %}
    Hello, {{ user.username }}
{% else %}
    Please log in.
{% endif %}
```
## Comment
```python
{% comment %}
    This is a comment (template comment)
{% endcomment %}
```

`<!-- This is a html comment -->`

## Template Inclusion and Inheritance
- ### Inheritance
  - Inherit a parent template:
```python
{% extends "base.html" %}
```

- Define blocks:
```python
{% block content %}
    This is content.
{% endblock %}
```
- ### Inclusion
  - Include a file or  template:
```python
{% include "header.html" %}
```
## URLs and Links
- ### Including Links
    - ### URL by name:
```python
<a href="{% url 'view-name' %}">Link</a>
```

- ### Creating Dynamic Links
  - ### URL with parameters:
```python
<a href="{% url 'view-name' param1 param2 %}">Link</a>
<a href="{% url 'post' slug='about-us' or slug=post.title %}">link</a>
```

## Alias
```python
{% with a = post.tile  %}
    # html code here, use the alias instead of a long query 
{ % endwith  %}
```
## Including Static Files
### Loading Static Files
- Load: 
```python
{% load static %}
```
- Use:
```python
<img src="{% static 'images/logo.png' %}" alt="Logo">
```
- load a libray (Loading Custom Tags)
```python
{% load custom_tags %}
```

## Forms
- Simple form:
```python
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
- Custom form:
```python
<form method="post">
    {% csrf_token %}
    {{ form.field_name.label_tag }} {{ form.field_name }}
    <button type="submit">Submit</button>
</form>
```

```html
<body>
   <h2> Sign Up </h2>
    <form method="post">
        {% csrf_token %}
        {{ form.non_field_errors }}
        <div>
            <label for="id_email">Email:</label>
            {{ form.email }}
            {% if form.email.errors %}
                <div class="error">{{ form.email.errors }}</div>
            {% endif %}
        </div>
        <div>
            <label for="id_password1">Password:</label>
            {{ form.password1 }}
            {% if form.password1.errors %}
                <div class="error">{{ form.password1.errors }}</div>
            {% endif %}
        </div>
        <div>
            <label for="id_password2">Confirm Password:</label>
            {{ form.password2 }}
            {% if form.password2.errors %}
                <div class="error">{{ form.password2.errors }}</div>
            {% endif %}
        </div>
        <button type="submit">Sign Up</button>
    </form>
</body>
```
[Documentation](https://docs.djangoproject.com/en/5.0/topics/templates/)
