# QUERIES

## Create

### method 1
```python
from myapp.models import ModelName  # Import your model

# Create an instance of ModelName by specifying the values of required attributes
object = ModelName(attr1=value1, attr2=value2)

# Save the object to the database using the save() method
object.save()
```

### method 2
```python
object = ModelName.objects.create(attr1=value1, attr2=value2)
```

## Read 

### Creating a QuerySet:
```python
queryset = ModelName.objects.all()  # Select all objects
```

### Sorting
```python
queryset = ModelName.objects.order_by('field_name')  # Ascending sort
queryset = ModelName.objects.order_by('-field_name')  # Descending sort
```

### Limiting and offsetting
```python
queryset = ModelName.objects.all()[:5]  # Limit results to 5
queryset = ModelName.objects.all()[5:10]  # Skip the first 5 results and take the next 5
```

### Exclusion
```python
from django.db.models import ModelName

queryset = ModelName.objects.exclude(field_name=value)
```

### Filtering
```python
queryset = ModelName.objects.filter(field_name=value)
queryset = ModelName.objects.filter(field1=value1, field2=value2)  # Filtering with multiple conditions
queryset = ModelName.objects.filter(Q(field1=value1) | Q(field2=value2))  # Filtering with logical operators
```

### Retrieving a single object::
```python
object = ModelName.objects.get(field_name=value)
object = ModelName.objects.first()  # Select the first object
object = ModelName.objects.last()  # Select the last object
```

### Filters can be combined
```python
queryset = Modelname.objects.filter(date__year='2020', title='abcde').exclude(published=True)
```

### Counting results:
```python
count = ModelName.objects.count()
```

### Others
- Joins
- Aggregation
- Raw queries
- Full-text search
- Distinct fields
- Conversion to list
- Specific fields

## Update
```python
object = ModelName.objects.get(pk=id)
object.attr = new_value
object.save()
```

## Delete
```python
object.delete()  # Delete a specific object
ModelName.objects.filter(attr=value).delete()  # Delete filtered objects
ModelName.objects.all().delete()  # Delete all objects
```
[Documentation](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
