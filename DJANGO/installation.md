# Virtual Environment
Organize your work and guarantee the portability of your projects.
A virtual environment isolates your project dependencies,
meaning you can have different versions of packages for different projects without conflicts.

When you move your project folder to a server or other location, the virtual environment you created (if it is included 
in your project folder) does not automatically move with it. Only files and directories present in your project folder 
will be moved. However, you can easily recreate the virtual environment on the new system with the requirement file.

### create a Python environment in the folder 
- `python3.xx -m venv .envname`

### activate the environment
- `source .envname/bin/activate` 

### deactivate the environment
- `deactivate` 

### delete the environment
- `rm -rf .env` 

# Django Installation

- `pip install --upgrade pip` -  upgrade pip before installing Django
- `pip install django==x.x.x` -  install a specific version of Django
- `python -m django --version` -  check the Django version

- `pip freeze > requirements.txt` -  write all dependencies to the requirement file
- `pip install -r requirements.txt` -  reinstall Django and all dependencies
- `cat requirements.txt` -  read the requirement file

- `django-admin startproject project_name` -  initialize a new project with Django structure
- `django-admin --help` -  get help on django-admin
- `python manage.py runserver` -  run the server
- `python manage.py migrate` - make the first migration 

