# Django Messages Framework

## Introduction

Django's messaging framework provides a way to store and display one-time notifications to users. It is commonly used to display feedback messages after a user performs an action, such as submitting a form or logging in. These messages can be informational, warning, or error-related.

## 1. Setting Up

To use the messaging framework, you need to include the following in your Django settings:

1. **Add `django.contrib.messages` to `INSTALLED_APPS`:**

    ```python
    INSTALLED_APPS = [
        ...
        'django.contrib.messages',
        ...
    ]
    ```

2. **Add `django.contrib.messages.middleware.MessageMiddleware` to `MIDDLEWARE`:**

    ```python
    MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        ...
    ]
    ```

3. **Add `django.contrib.messages.context_processors.message` to `TEMPLATES`:**

    ```python
    TEMPLATES = [
        {
            ...
            'context_processors': [
                ...
                'django.template.context_processors.messages',
                ...
            ],
        },
    ]
    ```


## 2. Types of Messages

The message levels remain the same:

- `messages.debug`: For debugging messages.
- `messages.info`: For general informational messages.
- `messages.success`: To indicate a successful operation.
- `messages.warning`: For warning messages.
- `messages.error`: To indicate an error.

## 3. Using Messages in Class-Based Views

Here’s how you can use messages in CBVs:

### 3.1. FormView, CreateView, UpdateView, DeleteView

CBVs that handle forms are common places to use messages.

#### Example with `CreateView`:

```python
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import MyModel

class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['field1', 'field2', 'field3']
    template_name = 'myapp/mymodel_form.html'
    success_url = reverse_lazy('mymodel_list')  # Redirect after success

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, 'The object was created successfully.')
        return super().form_valid(form)
```

#### Example with `DeleteView`:
```python
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import MyModel

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'myapp/mymodel_confirm_delete.html'
    success_url = reverse_lazy('mymodel_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'The object was deleted successfully.', extra_tags='alert-success')
        return super().delete(request, *args, **kwargs)
```
## 4. Displaying Messages in Templates

Use the same method to display messages in your templates:

```html
{% if messages %}
  <ul class="messages">
    {% for message in messages %}
      <li class="{% if message.tags %}{{ message.tags }}{% endif %}">
        {{ message }}
      </li>
    {% endfor %}
  </ul>
{% endif %}
```
## 5. Customizing CSS Styles

Add CSS to style your messages according to their level:

```css 
.messages {
    list-style: none;
    padding: 0;
}

.messages li {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
}

.messages .success {
    background-color: #dff0d8;
    color: #3c763d;
}

.messages .error {
    background-color: #f2dede;
    color: #a94442;
}

.messages .warning {
    background-color: #fcf8e3;
    color: #8a6d3b;
}

.messages .info {
    background-color: #d9edf7;
    color: #31708f;
}

.messages .debug {
    background-color: #e7e7e7;
    color: #555555;
}
```

## 6. Available Methods

The available message methods remain the same:

```python
messages.add_message(request, level, message, extra_tags='', fail_silently=False)
messages.debug(request, message, extra_tags='', fail_silently=False)
messages.info(request, message, extra_tags='', fail_silently=False)
messages.success(request, message, extra_tags='', fail_silently=False)
messages.warning(request, message, extra_tags='', fail_silently=False)
messages.error(request, message, extra_tags='', fail_silently=False)
```

## 7. Custom Message Configuration

Custom message configuration options in settings.py:

- `MESSAGE_LEVEL: Sets the minimum level of messages to log.`
- `MESSAGE_TAGS: Allows customizing default CSS tags.`
- `MESSAGE_STORAGE: Specifies the message storage backend.`

```python
from django.contrib.messages import constants as messages

MESSAGE_LEVEL = messages.INFO

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
```

## 8. Available Storage Backends

Available storage backends:

- `django.contrib.messages.storage.session.SessionStorage`
- `django.contrib.messages.storage.cookie.CookieStorage`
- `django.contrib.messages.storage.fallback.FallbackStorage`

### Summary

```text
Level: messages.INFO is typically recommended for production environments to ensure relevant messages are visible while avoiding debug clutter.
Message Tags: Define default tags in settings for consistency and easier global styling management. Use extra tags in message methods for specific cases.
Message Storage: Use SessionStorage for most cases. Consider CookieStorage or FallbackStorage based on your specific needs and privacy considerations.
```