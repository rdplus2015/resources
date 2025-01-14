# User, Superuser, and Group Management in Django

## 1. Python Script (Manually Executed via a Script File)

### Example of a Python script to manage users, superusers, and groups in Django:

#### Create a file `manage_users_groups.py` in your Django directory (e.g., in a `core` app).
```python
# core/management/commands/manage_users_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Create, modify or delete users and groups'

    def handle(self, *args, **kwargs):
        # Create a user
        try:
            user = User.objects.create_user('john_doe', 'john@example.com', 'password123')
            user.first_name = 'John'
            user.last_name = 'Doe'
            user.save()
            self.stdout.write(self.style.SUCCESS('User created: john_doe'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('User john_doe already exists'))

        # Create a superuser
        try:
            superuser = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('Superuser admin already exists'))

        # Create groups
        group_admin, created = Group.objects.get_or_create(name='Admins')
        group_editor, created = Group.objects.get_or_create(name='Editors')
        group_reader, created = Group.objects.get_or_create(name='Readers')

        if created:
            self.stdout.write(self.style.SUCCESS('Groups created: Admins, Editors, Readers'))

        # Add a user to a group
        user.groups.add(group_admin)  # Add to Admins
        self.stdout.write(self.style.SUCCESS(f'User {user.username} added to group Admins'))

        # Modify a group (e.g., rename)
        group_admin.name = 'Super Admins'
        group_admin.save()
        self.stdout.write(self.style.SUCCESS(f'Group modified: {group_admin.name}'))

        # Delete a user
        try:
            user_to_delete = User.objects.get(username='john_doe')
            user_to_delete.delete()
            self.stdout.write(self.style.SUCCESS(f'User deleted: {user_to_delete.username}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING('User john_doe not found'))

        # Delete a group
        try:
            group_to_delete = Group.objects.get(name='Readers')
            group_to_delete.delete()
            self.stdout.write(self.style.SUCCESS(f'Group deleted: {group_to_delete.name}'))
        except Group.DoesNotExist:
            self.stdout.write(self.style.WARNING('Group Readers not found'))
```

Execute the script with:
```bash
python manage.py manage_users_groups
```

## 2. Migration to Manage Users, Superusers, and Groups

Automating user and group management via migrations is possible, though not common practice for these tasks. Here’s how to do it:

#### Create a migration file `0002_create_users_and_groups.py` in your app's `migrations` folder.
```python
# core/migrations/0002_create_users_and_groups.py
from django.db import migrations
from django.contrib.auth.models import User, Group

def create_users_and_groups(apps, schema_editor):
    # Create a user
    User.objects.create_user('john_doe', 'john@example.com', 'password123')

    # Create a superuser
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

    # Create groups
    group_admin, created = Group.objects.get_or_create(name='Admins')
    group_editor, created = Group.objects.get_or_create(name='Editors')
    group_reader, created = Group.objects.get_or_create(name='Readers')

def delete_users_and_groups(apps, schema_editor):
    # Delete users
    User.objects.filter(username='john_doe').delete()
    User.objects.filter(username='admin').delete()

    # Delete groups
    Group.objects.filter(name='Admins').delete()
    Group.objects.filter(name='Editors').delete()
    Group.objects.filter(name='Readers').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),  # Dependency on the initial migration
    ]

    operations = [
        migrations.RunPython(create_users_and_groups, delete_users_and_groups),
    ]
```

Apply the migration with:
```bash
python manage.py migrate
```

# Managing Permissions in Django

## 1. Script for Managing Permissions

You can manage permissions using a script. Here’s an example:
```python
# core/management/commands/manage_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from myapp.models import Post  # Replace with your app's model

class Command(BaseCommand):
    help = 'Manage permissions for users and groups'

    def handle(self, *args, **kwargs):
        # Example of getting a permission
        content_type = ContentType.objects.get_for_model(Post)  # Change Post to your model

        # Create a permission if it doesn’t exist
        permission, created = Permission.objects.get_or_create(
            codename='can_publish',
            name='Can publish posts',
            content_type=content_type
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Permission created: can_publish'))

        # Add the permission to a group
        group_admin = Group.objects.get(name='Admins')
        group_admin.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('Permission added to group Admins'))

        # Add the permission to a user
        user = User.objects.get(username='john_doe')
        user.user_permissions.add(permission)
        self.stdout.write(self.style.SUCCESS(f'Permission added to user {user.username}'))

        # Modify a permission (e.g., change the permission name)
        permission.name = 'Can publish and edit posts'
        permission.save()
        self.stdout.write(self.style.SUCCESS(f'Permission modified: {permission.name}'))

        # Remove a permission from a user
        user.user_permissions.remove(permission)
        self.stdout.write(self.style.SUCCESS(f'Permission removed from user {user.username}'))

        # Delete a permission
        permission.delete()
        self.stdout.write(self.style.SUCCESS('Permission deleted'))
```

## 2. Migration for Managing Permissions

You can manage permissions via migrations as follows:

#### Create a migration file `0003_manage_permissions.py` in your app's `migrations` folder.
```python
# core/migrations/0003_manage_permissions.py
from django.db import migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Post  # Replace with your app's model

def create_permissions(apps, schema_editor):
    content_type = ContentType.objects.get_for_model(Post)  # Change Post to your model

    # Create a permission
    permission, created = Permission.objects.get_or_create(
        codename='can_publish',
        name='Can publish posts',
        content_type=content_type
    )

def delete_permissions(apps, schema_editor):
    # Delete the permission
    Permission.objects.filter(codename='can_publish').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_create_users_and_groups'),  # Dependency on the previous migration
    ]

    operations = [
        migrations.RunPython(create_permissions, delete_permissions),
    ]
```

Apply the migration with:
```bash
python manage.py migrate
