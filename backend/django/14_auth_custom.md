
# Custom User Model
To create a custom user model:
- Define your custom user model inheriting from AbstractBaseUser and PermissionsMixin.
- Specify the custom user model in settings.py


## 1. **Create the Custom User Model**
in your app’s `models.py`:

```python
# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom User Manager class that inherits from BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        # Ensure that the email is provided
        if not email:
            raise ValueError("The Email field must be set")
        # Normalize the email to ensure it's in a standard format (lowercase)
        email = self.normalize_email(email)
        # Create a new user instance with the provided email and additional fields
        user = self.model(email=email, **extra_fields)
        # Hash the password using the set_password method
        user.set_password(password)
        # Save the user object in the database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        # Set default values for staff and superuser status
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Use the create_user method to create the superuser
        return self.create_user(email, password, **extra_fields)


# Custom User model class that inherits from AbstractBaseUser and PermissionsMixin
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Define fields for the custom user model
    email = models.EmailField(unique=True)  # Email field, must be unique for each user
    first_name = models.CharField(max_length=30)  # First name of the user, with a max length of 30 characters
    last_name = models.CharField(max_length=30)  # Last name of the user, with a max length of 30 characters
    date_of_birth = models.DateField(null=True, blank=True)  # Date of birth, optional field (can be null or blank)
    is_active = models.BooleanField(default=True)  # Flag indicating whether the account is active (default: True)
    is_staff = models.BooleanField(default=False)  # Flag indicating if the user is a staff member (default: False)
    is_superuser = models.BooleanField(default=False)  # Flag indicating if the user is a superuser (default: False)

    # Attach the CustomUserManager to the CustomUser model for managing users
    objects = CustomUserManager()

    # The USERNAME_FIELD tells Django to use the email as the unique identifier for login
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS specifies the additional fields required when creating a user (besides the USERNAME_FIELD)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # String representation of the user object, returning the email
    def __str__(self):
        return self.email
```

### Key Parts of the Custom User Model:
  
- **CustomUserManager**: This manager is responsible for creating users and superusers. It’s important to define this manager to handle user creation logic (especially for password hashing and setting required fields).

- **CustomUser**: This is the actual custom user model. It inherits from `AbstractBaseUser` for authentication functionality and `PermissionsMixin` for handling permissions and groups.

- We can  apply **personal logic** or **validation** to a field, like `email` or `first_name`, we should handle those fields **explicitly** before passing them to the model. This gives you the opportunity to modify or validate them as needed. for example here,  we want to normalize the email. **`email=email`**: This part is passing the `email` argument to the model when creating a new instance.

- Thee `password=None` means that the `password` argument is **optional** when calling `create_user`. If the caller doesn't provide a password, the method will default to `None`.  This flexibility allows you to handle different scenarios, such as when you might want to create a user without immediately setting a password (e.g., if you're doing something like sending a confirmation email or handling password reset functionality).

- The AbstractBaseUser class includes a `password` field by default, even though we don't explicitly define it in your CustomUser model.
- By adding `PermissionsMixin` to your `TechnoUser` model, you benefit from Django's permissions and groups management features without having to code them yourself.

## 2. **Set the Custom User Model in `settings.py` and make Migrations**

After defining your custom user model, you need to tell Django to use it in the `settings.py` file.

In `settings.py`, add the following line:
```python
AUTH_USER_MODEL = 'yourapp.CustomUser'  # Replace 'yourapp' with the actual app name
```
This tells Django to use your custom `user` model instead of the default User model.

- **Make migrations**
```python
python manage.py makemigrations
python manage.py migrate
```

## 3. **Update the Admin**

If you want to manage the custom user model through Django’s admin interface, you need to update the admin to handle the custom fields.

In your app’s `admin.py`:
```python
# Importing the necessary modules from Django.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Defining a custom admin class for the CustomUser model.
class CustomUserAdmin(UserAdmin):
    # Specifies the model to use with this admin class.
    model = CustomUser
    
    # Determines the fields displayed in the user list in the admin interface.
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    
    # Specifies the filters available in the user list.
    list_filter = ['is_active', 'is_staff']
    
    # Allows searching for users by email in the admin interface.
    search_fields = ['email']
    
    # Defines the default ordering of users in the admin interface.
    ordering = ['email']

    # Defines the fields displayed when viewing or editing an existing user.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # Default group with email and password.
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),  # Personal information.
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Permissions and groups.
        ('Important dates', {'fields': ('last_login',)}),  # Important dates like last login.
    )

    # Specifies the fields used when adding a new user in the admin interface.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Adds a CSS class for a wider layout.
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff')}  # Fields to display when adding a user.
        ),
    )

# Registers the CustomUser model with the custom admin class.
admin.site.register(CustomUser, CustomUserAdmin)
```

## 6. **Update Forms and Authentication Views**
Django forms act as a powerful intermediary between the template and the database. They handle:

-   **Validation** of user input.
-   **Security** (e.g., protection against SQL injection and XSS).
-   **User feedback** (error handling and displaying messages).
-   **Cleaner and more maintainable code** by separating the concerns of form handling, business logic, and presentation.

Using Django forms allows for a **scalable, secure, and maintainable** approach to handling user authentication and other forms in web applications.


### **User Registration (Sign-Up)**

```python
# forms.py
# Importing necessary modules from Django.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Defining a custom sign-up form that extends UserCreationForm.
class SignUpForm(UserCreationForm):
    
    # Adding fields explicitly here for validations
    # Adding an email field to the form, making it required.
    """
    This explicitly defines the email field in the form, making it clear that the field is required and should be of type EmailField. 
    This allows you to specify additional attributes or behaviors for the email field, such as making it required, adding validation rules, or setting default values.
    """
    email = forms.EmailField(required=True)
    
    
    # Defining metadata for the form.
    class Meta:
        # Specifying the model to use with this form, using Django's `get_user_model` to get the custom user model.
        model = get_user_model()
        # Defining the fields to be included in the form: username, email, and both password fields.
        fields = ('username', 'email', 'password1', 'password2')

    # Overriding the save method to customize how the user instance is saved.
    def save(self, commit=True):
        # Calling the parent class's save method with commit=False to get a user instance without saving it to the database yet.
        user = super().save(commit=False)
        # Setting the email field of the user instance to the cleaned data from the form.
        user.email = self.cleaned_data['email']
        # If commit is True, save the user instance to the database.
        if commit:
            user.save()
        # Returning the user instance.
        return user
        
        """
        Form validation handles user input errors at the user interface level, with error messages returned and displayed to the user. Model validation ensures that validation rules are applied centrally, 
        even when the instance is created or modified without a form (e.g., via scripts or APIs), thereby ensuring data integrity.
        """

# Form for updating user information
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('email', )  # Fields to include in the form for updating

"""
This form is typically used in views like UserUpdate, where logged-in users can update their information (in this case, 
just their email address). By restricting the fields to just the email, the form limits the scope of what can be updated, 
enhancing security and preventing unintended changes to other fields.
"""

```
### Key Points:

-   **`SignUpForm`**: A custom form for user registration that inherits from `UserCreationForm`, adding an email field to the form.
-   **`Meta` class**: Specifies the model (`CustomUser` or the currently active user model) and the fields to be included in the form.
-   **`save` method**: Overridden to ensure that the email is saved correctly to the user instance before saving to the database.
- if we are using the default `LoginView`, `LogoutView` and `DeleteView`, we don’t need to create custom forms for these actions.

### Sign-Up View
```python
# views.py

# views.py

# Importing necessary modules.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.contrib.auth import login
from .forms import SignUpForm

# Defining a class-based view for user sign-up.
class SignUp(View):
    # Specifies the template to be used for rendering the sign-up page.
    template_name = 'registration/signup.html'

    # Handles GET requests to display the sign-up form.
    def get(self, request):
        # If the user is already authenticated, redirect them to the redirect URL.
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        # If not authenticated, initialize an empty sign-up form and render the template with the form.
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    # Handles POST requests to process the sign-up form submission.
    def post(self, request):
        # If the user is already authenticated, redirect them to the redirect URL.
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        # Initialize the form with POST data.
        form = SignUpForm(request.POST)
        # Check if the form is valid.
        if form.is_valid():
            # Save the user and log them in.
            user = form.save()
            login(request, user)
            # Redirect to the success URL.
            return redirect(self.get_success_url())
        # If the form is not valid, render the template with the form (showing errors).
        return render(request, self.template_name, {'form': form})

    # Determines the success URL to redirect to after a successful sign-up.
    def get_success_url(self):
        # Get the 'next' parameter from the URL query string.
        next_url = self.request.GET.get('next')
        # Check if 'next' is a safe URL.
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        # If 'next' is not provided or not safe, default to the dashboard page.
        return reverse('dashboard')

    # Determines the redirect URL for authenticated users.
    def get_redirect_url(self):
        return reverse('dashboard')
```
-   `form.is_valid()` is the overarching check that triggers both field-level and form-level validations.
-   Field-level (`clean_<fieldname>`) validation handles specific rules for individual fields.
-   Form-level (`clean`) validation handles rules that involve multiple fields or the form as a whole.
- **Field-Level Validation**: Check that an `email` field contains a valid email address.
- **Form-Level Validation**: Ensure that the `password1` and `password2` fields match.
This combination ensures that all aspects of the form's data integrity are checked before processing it further.


# Authentication Views
## Generic Views

```python
# urls 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # Custom Views
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    # Default Views 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'), # Displays a form for the user to enter their email address.
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'), # Appears after submitting the password reset form and Informs the user that the email has been sent
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'), # This view is called when the user clicks on the reset link received by email. It displays a form allowing the user to define a new password.
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), # Displayed after the user successfully sets a new password. Informs that the password has been reset and provides instructions for logging in.
    
    path('settings/security/update/password/', auth_views.PasswordChangeView.as_view(template_name='profile/security/update_kuila_user_password.html'), name='update_kuila_user_password'), # Displays a form to allow the user to change their current password.
    path('settings/security/update/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='profile/security/password_change_done.html'), name='password_change_done'), # This view is displayed after the user has successfully changed their password.
    
    # Custo Views (Update users informations)
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
- ### Html template for the forms
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

## Custom View

```python
from django.contrib.auth.views import LoginView, LogoutView  # Importing built-in views for login and logout
from django.urls import reverse_lazy  # For lazily reversing URLs
from django.http import HttpResponseNotAllowed  # For returning a response indicating a method is not allowed
from django.utils.http import is_safe_url  # To check if a URL is safe

# Custom login view inheriting from Django's LoginView
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specifies the template for the login page
    redirect_authenticated_user = True  # Redirects authenticated users to a different page to prevent re-login
    next_page = reverse_lazy('profile')  # Default page to redirect to after a successful login

    # Adds additional data to the context for rendering the template
    def get_context_data(self, **kwargs):
        """Adds data to the template context."""
        context = super().get_context_data(**kwargs)  # Inherit context data from parent class
        context['next'] = self.request.GET.get('next', '')  # Adds the 'next' URL to the context
        return context

    # Determines the URL to redirect to after a successful login
    def get_success_url(self):
        """Determines the redirection URL after login."""
        next_url = self.request.GET.get('next')  # Get 'next' parameter from the request
        if next_url and is_safe_url(url=next_url, allowed_hosts={self.request.get_host()}):
            return next_url  # Redirect to 'next' URL if it is safe
        return self.next_page  # Redirect to default page if 'next' is not safe

    # Handles the case when the form submission is valid
    def form_valid(self, form):
        """Handles valid form submissions."""
        return super().form_valid(form)  # Calls the parent method to handle the form

    # Handles the case when the form submission is invalid
    def form_invalid(self, form):
        """Handles invalid form submissions."""
        return super().form_invalid(form)  # Calls the parent method to handle the invalid form

# Custom logout view inheriting from Django's LogoutView
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Default URL to redirect to after logout

    # Handles POST requests for logging out
    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')  # Get 'next' URL from the POST request
        if next_url and is_safe_url(url=next_url, allowed_hosts={request.get_host()}):
            self.next_page = next_url  # Set next_page to the safe 'next' URL
        return super().post(request, *args, **kwargs)  # Calls the parent method to handle the logout

    # Prevents logout via a GET request, allowing only POST requests for security reasons
    def get(self, request, *args, **kwargs):
        """Prevents logout via GET request."""
        return HttpResponseNotAllowed(['POST'])  # Returns a '405 Method Not Allowed' response
```

### Full example 

```python
from django.contrib.auth import login, get_user_model  # Import functions for user login and to get the user model
from django.contrib.auth.decorators import login_required  # Decorator to require login for views
from django.contrib.auth.views import LoginView, LogoutView  # Built-in views for login and logout
from django.http import HttpResponseNotAllowed  # Response for methods not allowed
from django.shortcuts import render, redirect  # Shortcuts for rendering templates and redirecting
from django.urls import reverse_lazy, reverse  # Utilities for reversing URL patterns
from django.utils.decorators import method_decorator  # Decorator utility for class-based views
from django.utils.http import url_has_allowed_host_and_scheme  # Check if a URL is safe for redirection
from django.views import View  # Base class for class-based views
from django.views.generic import DeleteView, UpdateView  # Generic views for delete and update operations

from users_accounts.form import SignUpForm, UserUpdateForm  # Custom forms for sign-up and user update
from users_accounts.models import KuilaUser  # Custom user model

# Sign-up view for handling user registration
class SignUp(View):
    template_name = 'registration/signup.html'  # Template for the sign-up page

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())  # Redirect authenticated users
        form = SignUpForm()  # Initialize a new sign-up form
        return render(request, self.template_name, {'form': form})  # Render the sign-up form

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())  # Redirect authenticated users
        form = SignUpForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the new user
            return redirect(self.get_success_url())  # Redirect to the success URL
        return render(request, self.template_name, {'form': form})  # Re-render the form with errors

    def get_success_url(self):
        """Return the URL to redirect to after successful sign-up."""
        next_url = self.request.GET.get('next')  # Get the 'next' parameter
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url  # Redirect to the 'next' URL if it's safe
        return reverse('dashboard')  # Default redirect to the dashboard

    def get_redirect_url(self):
        """Return the URL to redirect authenticated users."""
        return reverse('dashboard')  # Redirect to the dashboard

# Custom login view that redirects authenticated users to the dashboard
class UserLogin(LoginView):
    template_name = 'registration/login.html'  # Template for the login page
    redirect_authenticated_user = True  # Redirect already logged-in users

    def get_success_url(self):
        """Return the URL to redirect to after successful login."""
        next_url = self.request.GET.get('next')  # Get the 'next' parameter
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url  # Redirect to the 'next' URL if it's safe
        return reverse('dashboard')  # Default redirect to the dashboard

# Custom logout view with login_required to ensure only logged-in users can access
@method_decorator(login_required, name='dispatch')
class UserLogout(LogoutView):
    next_page = reverse_lazy('home')  # Default URL to redirect to after logout

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')  # Get the 'next' URL from the POST request
        if next_url and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
            self.next_page = next_url  # Set next_page to the safe 'next' URL
        return super().post(request, *args, **kwargs)  # Call the parent method

    def get(self, request, *args, **kwargs):
        """Prevents logout via GET request."""
        return HttpResponseNotAllowed(['POST'])  # Only allow POST requests for logout

# View to update user information, restricted to logged-in users
@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = get_user_model()  # Use the custom user model
    form_class = UserUpdateForm  # Form class for updating user information
    template_name = 'profile/security/update_kuila_user_username.html'  # Template for updating user info
    success_url = reverse_lazy('settings')  # Redirect to settings after successful update

    def get_object(self, queryset=None):
        """Return the currently logged-in user."""
        return self.request.user  # Return the user making the request

# View to delete the user account, restricted to logged-in users
@method_decorator(login_required, name='dispatch')
class DeleteUser(DeleteView):
    model = KuilaUser  # Use the custom user model
    template_name = 'profile/security/delete_kuila_user.html'  # Template for confirming user deletion
    success_url = reverse_lazy('home')  # Redirect to the home page after deletion

    def get_object(self, queryset=None):
        """Return the user object to delete."""
        return self.model.objects.get(pk=self.request.user.pk)  # Get the user by primary key
```
[Documentation](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/)

