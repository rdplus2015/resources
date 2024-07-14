
## One-to-One 
- Each person has a single passport.
- Each passport is associated with a single person.

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

class Passport(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20)
```
```python
# Creating objects
person = Person.objects.create(name="John")
passport = Passport.objects.create(person=person, passport_number="ABC123")

# Query to get a person's passport
johns_passport = person.passport

# Modifying an object
johns_passport.passport_number = "XYZ456"
johns_passport.save()

# Deleting an object
johns_passport.delete()
```
### Other examples 
- `User and Profile`: Each user has an associated profile with additional information (e.g., address, date of birth).
- `Car and Registration Certificate`: Each car has a unique registration certificate.

## One-to-Many 
- A manufacturer can produce several cars.
- Each car has a single manufacturer.

```python
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
```
```python
# Creating objects
manufacturer = Manufacturer.objects.create(name="Toyota")
car1 = Car.objects.create(manufacturer=manufacturer, model_name="Camry")
car2 = Car.objects.create(manufacturer=manufacturer, model_name="Corolla")

# Query to get all cars of a manufacturer
toyota_cars = manufacturer.car_set.all()

# Adding a car for a manufacturer
car3 = Car.objects.create(manufacturer=manufacturer, model_name="Rav4")

# Deleting a car
car1.delete()
```

### Other examples
- `Author and Book` : An author can write multiple books, but each book is associated with a single author.
- `Category and Products` : A category can contain multiple products, but each product belongs to a single category.
- `Blog and Comments` : A blog post can have several comments, but each comment is associated with a single post.

## Many-to-Many
- A student can be enrolled in multiple courses.
- A course can have multiple students enrolled.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```
```python
# Creating objects
student1 = Student.objects.create(name="Alice")
student2 = Student.objects.create(name="Bob")

course = Course.objects.create(name="Math")

# Adding students to a course
course.students.add(student1, student2)

# Query to get all courses of a student
alice_courses = student1.course_set.all()

# Removing a student from a course
course.students.remove(student2)
```
### Other examples
- `Students and Courses` : A student can take multiple courses, and each course can have multiple students.
- `Articles and Tags` : A blog post can have multiple tags, and each tag can be used on multiple posts.
- `Users and Groups` : A user can belong to multiple groups, and each group can have multiple users.

## Many-to-One
- An author may have written several books.
- Each book is written by a single author.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```
```python
# Creating objects
author = Author.objects.create(name="J.K. Rowling")
book = Book.objects.create(author=author, title="Harry Potter")

# Query to get the author of a book
harry_potter_author = book.author

# Changing the author of a book
new_author = Author.objects.create(name="Stephen King")
book.author = new_author
book.save()
```

### Others examples
- `Comments and Articles` : Multiple comments can be associated with a single blog post.
- `Orders and Customers` : A customer can place multiple orders, but each order is associated with a single customer.
- `Products and Suppliers` : Multiple products can be supplied by a single supplier.

## Reverse Relationships (Relations Inverses)
- A parent can have multiple children.
- Each child has a single parent.
- To access a parent's children, use parent.children.all()

```python
from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)

class Child(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

```
```python
# Creating objects
parent = Parent.objects.create(name="Alice")
child1 = Child.objects.create(name="Bob", parent=parent)
child2 = Child.objects.create(name="Charlie", parent=parent)

# Query to get a child's parent
bobs_parent = child1.parent

# Accessing all children of a parent
parents_children = parent.children.all()

# Deleting a child
child1.delete()
```

### Other examples
- `Company and Employees` : A company can have multiple employees, but each employee belongs to a single company
- `School and Students` : A school can have multiple students, but each student is associated with a single school.
- `Author and Books` : An author can write multiple books, and the reverse relationship allows access to the books of an author.

[Documentation](https://docs.djangoproject.com/en/5.0/topics/db/models/)