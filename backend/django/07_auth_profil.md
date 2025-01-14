## Profile Model
```python
# In models.py of your Django application

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link Profile to User model
    bio = models.TextField(blank=True)  # Optional biography field
    location = models.CharField(max_length=100, blank=True)  # Optional location field
    birth_date = models.DateField(null=True, blank=True)  # Optional birth date field
    # Add other custom fields as needed

    def __str__(self):
        return f'Profile of {self.user.username}'
```

### Signals for Automatic Profile Creation and Update
```python
# In signals.py of your Django application
# File: users_profiles/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # Create profile if user is created
    instance.profile.save()  # Save profile when user is saved
```

**Explanation of Signals:**
- `post_save`: This signal is triggered after a model's `save()` method is called.
- `@receiver`: A decorator that connects the function to the signal.
- `create_or_update_user_profile`: This function creates or updates the profile automatically whenever a User instance is saved.
- `instance.profile.save()`: Ensures the profile is updated after the user is modified.

### Profile Form
```python
# In forms.py of your Django application

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Specify the model to use
        fields = ['bio', 'location', 'birth_date']  # Specify fields to include in the form
        # Add other fields as per your Profile model
```

### Views for Viewing and Editing Profile
```python
# In views.py of your Django application

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def profile_view(request):
    profile = request.user.profile  # Get the profile of the logged-in user
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)  # Render the profile view template

@login_required
def profile_edit(request):
    profile = request.user.profile  # Get the profile of the logged-in user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)  # Bind form to the profile instance
        if form.is_valid():
            form.save()  # Save the form and update the profile
            return redirect('profile_view')  # Redirect to profile view
    else:
        form = ProfileForm(instance=profile)  # Populate form with existing profile data
    context = {
        'form': form
    }
    return render(request, 'profile_edit.html', context)  # Render the profile edit template
```

### Templates for Displaying and Editing Profile
```html
<!-- In templates/profile.html -->

<h2>{{ profile.user.username }}</h2>  <!-- Display username -->
<p>{{ profile.bio }}</p>  <!-- Display biography -->
<p>{{ profile.location }}</p>  <!-- Display location -->
<p>{{ profile.birth_date }}</p>  <!-- Display birth date -->
<!-- Add other fields as per your Profile model -->
```

```html
<!-- In templates/profile_edit.html -->

<form method="POST">  <!-- Form for editing profile -->
    {% csrf_token %}  <!-- CSRF token for security -->
    {{ form.as_p }}  <!-- Render form fields as paragraphs -->
    <button type="submit">Save</button>  <!-- Submit button -->
</form>
```

### Choosing a Profile for a User
- **During User Registration**: Create a profile when a new user registers.
- **User Profile Settings Page**: Allow users to update their profiles through a dedicated settings page.
- **Role-based Profiles**: Customize profiles based on user roles (e.g., admin, editor, reader).

## Example
```python
#models.py

from django.conf import settings
from django.db import models


class KuilaUserProfile(models.Model):
    # One-to-One relationship with the user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    # Field for user's avatar image, allowing null and blank values
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # Field for user's first name, allowing blank values
    first_name = models.CharField(max_length=30, blank=True)
    # Field for user's last name, allowing blank values
    last_name = models.CharField(max_length=30, blank=True)
    # Field for user's phone number, allowing blank values
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        # Return a string representation of the user's full name
        return f'{self.first_name} {self.last_name}'

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import KuilaUserProfile


# Signal receiver to create or update a user profile when a user is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a KuilaUserProfile instance for the newly created user
        KuilaUserProfile.objects.create(user=instance)
    # Update the user's profile (this is redundant with the second signal handler)
    instance.profile.save()


# Signal receiver to save the user profile when a user is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    # Save the user's profile (this assumes the profile is already created)
    instance.profile.save()

    
# views.py
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from users_profiles.models import KuilaUserProfile
from kuila.mixins import KuilaLoginRequiredMixin

# View to display user profile details
class UserProfile(KuilaLoginRequiredMixin, DetailView):
    model = KuilaUserProfile  # The model to use for this view (use the class instead of an instance)
    template_name = 'profile/index.html'  # Template to render
    context_object_name = 'user_profile'  # Name of the context variable to use in the template

    def get_object(self, queryset=None):
        # Get the profile for the currently logged-in user
        user = self.request.user.id
        user_profile = KuilaUserProfile.objects.get(user_id=user)  # Retrieve the profile based on user ID
        return user_profile

# View to update user profile details
class UserProfileUpdate(KuilaLoginRequiredMixin, UpdateView):
    model = KuilaUserProfile  # The model to use for this view
    fields = ['avatar', 'first_name', 'last_name', 'phone_number']  # Fields to include in the form
    template_name = 'profile/update.html'  # Template to render for the form
    success_url = reverse_lazy('profile')  # URL to redirect to upon successful form submission

    def get_object(self, queryset=None):
        # Get the profile for the currently logged-in user
        return KuilaUserProfile.objects.get(user=self.request.user)  # Retrieve the profile based on the logged-in user

    def form_valid(self, form):
        # Ensure that the profile being updated belongs to the current user
        if form.instance.user != self.request.user:
            return redirect('profile')  # Redirect if the profile does not belong to the current user
        return super().form_valid(form)  # Proceed with the form submission if the user is valid
```