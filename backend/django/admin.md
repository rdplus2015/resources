# Django Admin Configuration for BlogPost Model

## Simple Registration in `admin.py`

### This registers the BlogPost model with default admin options.


```python
# admin.py
from django.contrib import admin
from blog.models import BlogPost

admin.site.register(BlogPost)
```

## Advanced Configuration with admin.ModelAdmin 
### Allows for more customization using admin.ModelAdmin.


```python
# admin.py
from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
```

## Customizing Admin Display and Functionality
```python
# admin.py
from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'word_count')
    list_editable = ('author',)  # Allows editing 'author' directly from the list view
    list_display_links = ('title',)  # Makes 'title' clickable in the list view
    search_fields = ('title', 'content')  # Enables search by 'title' and 'content'
    list_filter = ('publish_date', 'author')  # Adds filters for 'publish_date' and 'author'
    empty_value_display = '-empty-'  # Displays this for empty values
    list_per_page = 10  # Controls how many items are shown per page in the list view
    # filter_horizontal = ('tags',)  # Example of using filter_horizontal for ManyToManyField
    # autocomplete_fields = ('author',)  # Example of using autocomplete_fields for ForeignKey

    # Custom method to display word count
    def word_count(self, obj):
        return len(obj.content.split())
    word_count.short_description = 'Word Count'  # Customizes the column header

    # Override model Meta options
    class Meta:
        verbose_name = 'Blog Post'  # Changes the model name display in admin

    # Custom method to get absolute URL for admin
    def get_absolute_url(self, obj):
        return reverse("blog-post", kwargs={"slug": obj.slug})
```
- [Django Admin documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
- [Django ModelAdmin options](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-options)
- [Django Admin site customization](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#adminsite-objects)