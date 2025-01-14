# Permissions and Authorization in Django

Django provides a robust system for managing permissions and authorization, allowing control over user access to different parts of your application.

## 1. Permissions in Django

**Permissions** in Django determine what a user can do. By default, Django creates three permissions for each model: `add`, `change`, and `delete`.

### 1.1. Managing Permissions

Permissions are defined at the model level in Django. Here's how they work:

- **add\_model**: Allows a user to add model instances.
- **change\_model**: Allows a user to modify model instances.
- **delete\_model**: Allows a user to delete model instances.

These permissions are not assigned to users by default. You can also define custom permissions.

### 1.2. Assigning Permissions

- A user will only have these permissions if they are explicitly assigned to them or assigned to a group they belong to.
- **Superusers** automatically have **all permissions** without explicit assignment.

### 1.3. Default Behavior

- If a standard user tries to perform an action requiring a permission they lack, they will be blocked.
- You can manage this via permission checks in your views or the admin interface.

### 1.4. Defining Custom Permissions

- The default permissions (`add`, `change`, `delete`) are added automatically by Django, but you can explicitly define them for clarity.
- To define custom permissions, use the `permissions` option in the `Meta` class of your model:

```python
class Meta:
    permissions = [
        ("add_post", "Can add post"),
        ("change_post", "Can change post"),
        ("delete_post", "Can delete post"),
        ("publish_post", "Can publish post"),  # Custom permission
        ("can_archive", "Can archive posts"),  # Custom permission
    ]
```

### 1.5. Checking Permissions

You can check a user's permissions with the following methods:

- `user.has_perm('app_label.permission_codename')`: Checks if the user has a specific permission.
- `user.has_perms(['app_label.permission_codename1', 'app_label.permission_codename2'])`: Checks if the user has multiple permissions.

```python
user.has_perm('blog.add_post')
```

### 1.6. Assigning Permissions

Permissions can be assigned to users in several ways:

- Via the Django admin interface.
- Using Python commands, such as:

```python
from django.contrib.auth.models import User, Permission

user = User.objects.get(username='john')
permission = Permission.objects.get(codename='add_post')
user.user_permissions.add(permission)
```

Or via groups:

```python
from django.contrib.auth.models import Group

group = Group.objects.get(name='Editors')
group.permissions.add(permission)
user.groups.add(group)
```

### 1.7. Combining Approaches

#### Combined Scenario

- **Initial configuration in code**: Define basic permissions and groups directly in the code for a solid and traceable setup.
- **Dynamic adjustments in the admin**: Use the admin interface for adjustments or exceptions without code changes.

#### Example Workflow

- Define basic groups and permissions in migrations or scripts.
- Use the admin interface for daily user management.

### 1.8. Best Way to Implement

1. **Initialization Script (outside migrations) in a scripts folder**:
   - **Flexibility**: Can be run anytime to reset groups/permissions.
   - **Independence**: Not tied to the migration lifecycle.
   - **Ease of execution**: Can be run manually or integrated into deployment scripts.
2. **Migration**:
   - **Total automation**: Groups and permissions are automatically created when a new database instance is migrated.
   - **History**: Changes are versioned with other database modifications.

### Scenarios

- **Team Development/CI/CD**: Use migrations to ensure consistent environment configuration without manual intervention.
- **Initial Deployment**: An initialization script is ideal for setting up the base configuration before launching migrations, especially if you want to separate this logic from database structure changes.

## 2. Authorization in Django

**Authorization** determines if an authenticated user has the right to perform a specific action. Django uses `PermissionRequiredMixin` and the `permission_required` decorator to manage authorization at the view level.

### 2.1. Using `PermissionRequiredMixin`

`PermissionRequiredMixin` is used with class-based views to restrict access based on permissions.

```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View

class MyView(PermissionRequiredMixin, View):
    permission_required = 'myapp.can_publish'
    login_url = 'myapp:custom_login'
    # ['myapp.can_publish', 'myapp.can_edit'] # multiple permissions
    # raise_exception = True  # Raises an exception if the user lacks permission
    # View code (get and post methods)
```

- `login_url = 'myapp:custom_login'` sets the URL to redirect users without permission.
- This mixin controls view access based on user permissions.
- **`permission_required`** defines the necessary permission to access the view.

### 2.2. Customizing `PermissionRequiredMixin`

You can customize this mixin in the view or ideally in a separate class:

```python
# myapp/mixins.py
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect

class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        return redirect('myapp:custom_login')

    def get_permission_required(self):
        if self.request.user.is_superuser:
            return []  # Superusers do not need permissions
        return super().get_permissions()
```

You can also customize permissions based on user groups or other specific conditions. For example:

In this example, the checked permission changes based on the group the user belongs to.

```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View

class MyView(PermissionRequiredMixin, View):
    def get_permission_required(self):
        if self.request.user.groups.filter(name='Editors').exists():
            return ['myapp.can_edit']
        return ['myapp.can_publish']
```

### 2.3. Using `permission_required` Decorator

`permission_required` is a decorator for function-based views to restrict access.

```python
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('myapp.can_publish', login_url='/login/')
def my_view(request):
    return render(request, 'my_template.html')
```

### 2.4. Overriding `permission_required`

You can redefine `permission_required` with custom logic:

```python
from django.contrib.auth.decorators import permission_required as original_permission_required
from django.contrib import messages
from django.shortcuts import redirect

def permission_required(perm, login_url=None, redirect_field_name='next'):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.has_perm(perm):
                messages.error(request, "You don't have permission to access this page.")
                return redirect(login_url or '/login/')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
```

### Summary

- **Permissions** define what a user *can do*, like adding a post or deleting a comment. They are assigned to users or groups.
- **Authorization** is the decision process that checks if a user is allowed to perform a specific action based on their permissions. Authorization uses permissions to decide if an action can be executed.
- Permissions defined in the `Meta` class do not directly block a user from performing an action but provide a mechanism to control access.

If you don’t customize your authentication or permission system, these are the default permissions and groups. You can manage user access to models, views, and other resources by assigning them to specific groups or directly granting them specific permissions.

- [Documentation](https://docs.djangoproject.com/en/5.0/topics/auth/default/)

## Protect Views Against Unauthorized Users

### `login_required`

Django provides the `@login_required` decorator to restrict view access to authenticated users.

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return HttpResponse('Welcome, authenticated user!')
```

### `LoginRequiredMixin`

`LoginRequiredMixin` is used with class-based views (CBVs) to restrict access to authenticated users.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class MyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome, authenticated user!')
```

- Both tools serve similar purposes, but `@login_required` is used for function-based views, while `LoginRequiredMixin` is for class-based views.
- The `@login_required` decorator and `LoginRequiredMixin` support redirection to a URL defined in `settings.py` with the `LOGIN_URL` variable.
- You can also specify a custom `login_url` directly in each view or class for more granular control.

### Customizing `LoginRequiredMixin`

To customize `LoginRequiredMixin`, you can either extend this mixin or override the `get_login_url` method for custom redirection.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('accounts:login')  # Custom redirect URL

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return super().handle_no_permission()
        else:
            return redirect('accounts:login')
```

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class KuilaLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

    def handle_no_permission(self):
        from django.contrib import messages
        messages.add_message(self.request, messages.INFO, 'You need to be logged in to view this page.')
        return super().handle_no_permission()
```

