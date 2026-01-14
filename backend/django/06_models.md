# Models
## 1. Create a model

```python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date = models.DateField(blank=True)
```
[Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)

## Create and apply migrations
```bash
python manage.py makemigrations # python manage.py makemigrations appName
python manage.py migrate

python manage.py sqlmigrate blog migrationName # To see the sql code
```
[Documentation](https://docs.djangoproject.com/fr/5.0/ref/models/fields/#field-types)

## Model Fields
`CharField` to store strings of a predefined maximum length (defined by the max_length parameter).
`TextField` to store strings of unlimited length.
`SlugField` to store strings as slugs.
`IntegerField` and FloatField to store integers and decimal numbers.
`BooleanField` to store a boolean value (True or False).
`EmailField` to store email addresses.
`DateField` and DateTimeField to store dates.
`URLField` to store URLs.


## Properties and Method overloading
Adding properties (methods and attributes) to our classes allows us to not always 
Create fields to display personalized messages or items.

```python

@property 
def publish_string(self):
    if self.published:
        return "the article was published"
    return "Article not found"

#  Method overloading
def save(self, *args, **margs):
    if not self.slug:
        self.slug = slugify(self.title)
    super().save(*args, **margs)
```
[Documentations](https://docs.djangoproject.com/fr/5.0/ref/models/fields/#field-types)