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
## Custom User Model
To create a custom user model:
- Define your custom user model inheriting from AbstractBaseUser and PermissionsMixin.
- Specify the custom user model in settings.py

```python
# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

# settings.py
AUTH_USER_MODEL = 'myapp.MyUser'
```

## User Registration (Sign-Up)
### Sign-Up Form
```python
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
```

### Sign-Up View
```python
# views.py

class SignUp(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.get_success_url())
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')

    def get_redirect_url(self):
        return reverse('dashboard')
```
### URL Configuration
```python
# urls.py
from django.urls import path
from .views import sign_up

urlpatterns = [
    path('signup/', sign_up, name='signup'),
]
```

## Profile Model
```python
# In models.py of your Django application

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # Add other custom fields as needed

    def __str__(self):
        return f'Profile of {self.user.username}'
```

### Signals for Automatic Profile Creation and Update
```python
# In models.py or signals.py of your Django application
# users_profiles/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import KuilaUserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        KuilaUserProfile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

```

### Profil form 
```python
# In forms.py of your Django application

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
        # Add other fields as per your Profile model

```

###  Views for Viewing and Editing Profile

```python
@method_decorator(login_required, name='dispatch')
class UserProfile(DetailView):
    model = KuilaUserProfile()
    template_name = 'profile/index.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        user = self.request.user.id
        user_profile = KuilaUserProfile.objects.get(user_id=user)
        return user_profile


class UserProfileUpdate(UpdateView):
    model = KuilaUserProfile
    fields = ['first_name', 'last_name', 'phone_number']
    template_name = 'profile/update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return KuilaUserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            return redirect('profile')
        return super().form_valid(form)
```

````python
# In views.py of your Django application

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def profile_view(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile_edit.html', context)
````


### Templates for Displaying and Editing Profile

```html
<!-- In templates/profile.html -->

<h2>{{ profile.user.username }}</h2>
<p>{{ profile.bio }}</p>
<p>{{ profile.location }}</p>
<p>{{ profile.birth_date }}</p>
<!-- Add other fields as per your Profile model -->
```
```html
<!-- In templates/profile_edit.html -->

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```
Choosing a profile for a user typically depends on your application's design and requirements. 

- `During User Registration`
- `User Profile Settings Page`
- `Role-based Profiles`



## Authentication Views
### Generic Views

```python
# urls 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    path('settings/security/update/password/', auth_views.PasswordChangeView.as_view(template_name='profile/security/update_kuila_user_password.html'), name='update_kuila_user_password'),
    path('settings/security/update/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='profile/security/password_change_done.html'), name='password_change_done'),
    path('settings/security/update/username/', UserUpdate.as_view(), name='update_kuila_user_username'),
    path('settings/security/deletemyaccount/', DeleteUser.as_view(), name='delete_kuila_user'),
]

"""
    it is not mandatory to reference template names in urls.py. 
    If you do not specify template names in URLs, Django will use the default template names, as defined in its generic authentication views.
"""


# Template structure 
"""
- your_project/
    - your_app/
    - your_project/
    - templates/
        - registration/
            - login.html
            - logout.html # Optional if using `LogoutView`
            - password_reset_form.html
            - password_reset_done.html
            - password_reset_confirm.html
            - password_reset_complete.html
    - manage.py
"""

# settings.py
LOGIN_REDIRECT_URL = '/account/profile/'  # URL de redirection après connexion
LOGOUT_REDIRECT_URL = '/login/'  # URL de redirection après déconnexion
``` 
- ### Html template
```html
<!-- templates/registration/ ... -->
<body>
    <h2>Title</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Title</button>
    </form>
</body>
```

```html
<!-- templates/base.html -->
<body>
    <nav>
        {% if user.is_authenticated %}
            <form method="post" action="{% url 'logout' %}">
                {% csrf_token %}
                <button type="submit">Lougout</button>
            </form>
        {% else %}
            <a href="{% url 'login' %}">Login</a>
        {% endif %}
    </nav>
    {% block content %}
    {% endblock %}
</body>
```

### Custom View

```python
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed
from django.utils.http import is_safe_url

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Path to the login template
    redirect_authenticated_user = True  # Redirect authenticated users
    next_page = reverse_lazy('profile')  # URL to redirect after successful login

    def get_context_data(self, **kwargs):
        """Adds data to the template context."""
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        """Determines the redirection URL after login."""
        next_url = self.request.GET.get('next')
        if next_url and is_safe_url(url=next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return self.next_page
    
    def form_valid(self, form):
        """Handles valid form submissions."""
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Handles invalid form submissions."""
        return super().form_invalid(form)
    
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # URL to redirect after logout

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')
        if next_url and is_safe_url(url=next_url, allowed_hosts={request.get_host()}):
            self.next_page = next_url
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Prevents logout via GET request."""
        return HttpResponseNotAllowed(['POST'])
```

### Example 

```python
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.generic import DeleteView, UpdateView

from users_accounts.form import SignUpForm, UserUpdateForm
from users_accounts.models import KuilaUser


class SignUp(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.get_success_url())
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')

    def get_redirect_url(self):
        return reverse('dashboard')


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')


@method_decorator(login_required, name='dispatch')
class UserLogout(LogoutView):
    next_page = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')
        if next_url and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
            self.next_page = next_url
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Prevents logout via GET request."""
        return HttpResponseNotAllowed(['POST'])


@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'profile/security/update_kuila_user_username.html'
    success_url = reverse_lazy('settings')


    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class DeleteUser(DeleteView):
    model = KuilaUser
    template_name = 'profile/security/delete_kuila_user.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Retourne l'objet KuilaUser associé à l'utilisateur connecté
        return self.model.objects.get(pk=self.request.user.pk)

```

#### Update username 
```python
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', )

```
## Securing Access in Django

### User Authentication

- **Using Django's Authentication System:**
  Integrate `django.contrib.auth` to manage user authentication.

- **View Decorators:**
  Use `@login_required` to restrict access to views to logged-in users.

### Permission Management

- **Defining Permissions:**
  Use built-in permissions (`view`, `add`, `change`, `delete`) or create custom permissions.

- **Permission-Based Access Control:**
  Use `user.has_perm()` in your views to check user permissions.

### Advanced Techniques

- **Mixin-Based View Classes:**
  Create custom mixins (`LoginRequiredMixin`, etc.) to reuse authentication logic.

- **Authentication Middleware:**
  Configure `AuthenticationMiddleware` to handle authentication on each request.

- **Flash Messages:**
  Use flash messages to notify users of access errors.

## Concrete Examples

- **Access Restriction:**
  Use `@login_required` on a view to prevent access to a user profile page for non-logged-in users.

- **Permission Check:**
  Check with `user.has_perm('app.add_object')` before allowing a user to add an object in an application.

[Documentation](https://docs.djangoproject.com/en/5.0/topics/auth/default/)