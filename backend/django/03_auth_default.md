# Django Authentication 

## Introduction

Django's authentication system handles user authentication and authorization. It provides robust functionality for managing users, groups, permissions, and sessions.

## Setup
Ensure the `django.contrib.auth` application is included in your installed apps.
```python
# settings.py
INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
]
```

## User Model
### Default User Model
- Django provides a default User model with fields like:
`username`
`password`
`email`
`first_name`
`last_name`
`is_staff`
`is_active`
`is_superuser`

### Create User 
```python
from django.contrib.auth.models import User
user = User.objects.create_user(username='john', password='secret')
```
For using Django's default authentication system, you don’t need to create a custom app or model specifically for 
authentication because Django already provides the necessary functionality out of the box. The default authentication 
system includes the User model, views, and forms, all of which are ready to use.

### 1. **Set Up Your Project**
-   Ensure your Django project is set up and running. You can create a new project if needed:

```python
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

### 2. **Configure the Settings**

-   Add `django.contrib.auth` and `django.contrib.contenttypes` to the `INSTALLED_APPS` in your `settings.py` file (these are included by default in a new Django project).
-   Add `django.contrib.sessions.middleware.SessionMiddleware` and `django.contrib.auth.middleware.AuthenticationMiddleware` to the `MIDDLEWARE` list (also included by default).

### 3. **Create and Apply Migrations**

-   Run migrations to set up the database tables for the authentication system:
```python
python manage.py migrate
```

### 4. **Use Django’s Built-in Views for Auth**

Django provides built-in views to handle common authentication tasks.

-   **Login View**: Use Django’s `LoginView` to display a login form and authenticate users.
-   **Logout View**: Use `LogoutView` to log out users.
-   **Password Change and Reset Views**: Use `PasswordChangeView`, `PasswordResetView`, and others for password management.

In `urls.py` of your app or project:

```python
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
```

### 5. **Templates**

-   Django’s authentication views use templates with specific names in a `registration` directory. You can create these templates and customize them:
    -   `registration/login.html`
    -   `registration/logged_out.html`
    -   `registration/password_change_form.html`
    -   `registration/password_change_done.html`
    -   `registration/password_reset_form.html`
    -   `registration/password_reset_done.html`
    -   `registration/password_reset_confirm.html`
    -   `registration/password_reset_complete.html`

Example `login.html`:

```html
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```

### 6. **Testing**

-   Run your development server:
```python
python manage.py runserver

```
Visit the `/login/` URL to see the login form. You can create a superuser to test login functionality:

[Documentation](https://docs.djangoproject.com/en/5.1/topics/auth/)

