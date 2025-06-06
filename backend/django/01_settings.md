# Configuration (settings.py)

###  BASE_DIR
```python
    from pathlib import Path
      
    BASE_DIR = Path(__file__).resolve().parent.parent
```

###  TEMPLATES
```python
    TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              # Others configuration
          },
      },
  ]
```
### Best Practices for Using Static Files in Django

### `{% static %}` Tag
Use the `{% static %}` tag to reference static files in your Django templates. This ensures that the URLs of static files are properly managed, including in production.

Example:
```html
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### STATIC_URL, MEDIA_URL, STATICFILES_DIRS
```python

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
   BASE_DIR / 'static', 
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### INSTALLED_APPS 
```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'myapp',  # Add your appname Here 
]
```

### MIDDLEWARE 
```python
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # add your middlewares here 
]
```
# Environment Variables Configuration (.env)

## Security Parameters

- **DEBUG**
  - *Description:* Enables or disables debug mode.
  - *Syntax:* `DEBUG=True` (in development) or DEBUG=False (in production).
  - *Best Practice:* Always disable debug mode in production.

- **SECRET_KEY**
  - *Description:* Secret key used to secure sessions and cookies.
  - *Syntax:* `SECRET_KEY=mysecretkey123`
  - *Best Practice:* Generate a strong and unique secret key for each environment.

- **ALLOWED_HOSTS**
  - *Description:* List of allowed hosts that can access the Django application.
  - *Syntax:* `ALLOWED_HOSTS=localhost,127.0.0.1`
  - *Best Practice:* Limit allowed hosts to prevent request injection attacks.

- **SECURE_SSL_REDIRECT**
  - *Description:* Redirects all HTTP connections to HTTPS.
  - *Syntax:* `SECURE_SSL_REDIRECT=True`
  - *Best Practice:* Enable to ensure a secure connection to the application.

- **SESSION_COOKIE_SECURE**
  - *Description:* Enables secure transmission of session cookies.
  - *Syntax:* `SESSION_COOKIE_SECURE=True`
  - *Best Practice:* Enable to protect user sessions from Man-in-the-Middle attacks.

- **CSRF_COOKIE_SECURE**
  - *Description:* Enables secure transmission of CSRF cookies.
  - *Syntax:* `CSRF_COOKIE_SECURE=True`
  - *Best Practice:* Enable to protect against CSRF attacks.

- **SECURE_BROWSER_XSS_FILTER**
  - *Description:* Enables the browser's built-in XSS protection.
  - *Syntax:* `SECURE_BROWSER_XSS_FILTER=True`
  - *Best Practice:* Enable to prevent XSS attacks.

- **SECURE_CONTENT_TYPE_NOSNIFF**
  - *Description:* Forces the browser to respect the declared content type.
  - *Syntax:* `SECURE_CONTENT_TYPE_NOSNIFF=True`
  - *Best Practice:* Enable to prevent MIME sniffing attacks.
    
- **DATABASE_URL**
  - *Description:* Database connection URL.
  - *Syntax:* DATABASE_URL=postgres://username:password@localhost/db_name
  - *Best Practice:* Use a unique and secure connection URL for the database.

### Setup 

```bash
pip install django-environ
```

```text
# Environment Variables Configuration (.env)
    
# Security Parameters
DEBUG=True
SECRET_KEY=mysecretkey123
ALLOWED_HOSTS=localhost,127.0.0.1
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
    
# Database Configuration
# For SQLite
DATABASE_URL=sqlite:///path/to/your/db.sqlite3

# For PostgreSQL
DATABASE_URL=postgres://your_database_user:your_password@localhost:5432/your_database_name
```

```python
import os
import environ

# Initialize environ
env = environ.Env()

# Load environment variables from .env file
environ.Env.read_env('.yourfilename')

# DEBUG mode
DEBUG = env.bool('DEBUG', default=False)

# Secret key
SECRET_KEY = env('SECRET_KEY')

# Allowed hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# Security settings
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)
SECURE_BROWSER_XSS_FILTER = env.bool('SECURE_BROWSER_XSS_FILTER', default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool('SECURE_CONTENT_TYPE_NOSNIFF', default=True)

# Database configuration
DATABASES = {
    'default': env.db(),
}

# Other Settings
    # Add other custom settings here...     
```

# .gitignore template

```text
# Ignore Django migration files
*/migrations/*.pyc
*/migrations/*.py

# Ignore compiled Python files
*.pyc
__pycache__/

# Ignore local SQLite database
*.sqlite3

# Ignore log files
*.log

# Ignore macOS specific hidden files
.DS_Store

# Ignore JetBrains IntelliJ IDEA specific directory
.idea/

# Ignore Visual Studio Code specific directory
.vscode/

# Ignore Python and JavaScript dependency directories
venv/
env/
node_modules/

# Ignore test coverage files
htmlcov/
.coverage

# Ignore compiled static files directory
static/

# Ignore environment configuration files or folder
.env/
.env 

```
