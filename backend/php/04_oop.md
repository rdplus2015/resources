
# Introduction to Object-Oriented Programming (OOP) in PHP

## Introduction to OOP

OOP is a programming paradigm that organizes code into objects, which are instances of classes. A class defines the properties (variables) and methods (functions) associated with an object.

## Defining a Class and an Object

A class is a blueprint for creating objects. Here's a simple example:

### Example of a Class

```php
<?php
class Car {
    // Properties
    public $make;
    public $color;

    // Constructor
    public function __construct($make, $color) {
        $this->make = $make;
        $this->color = $color;
    }

    // Method
    public function displayInfo() {
        echo "This car is a {$this->make} and is {$this->color} in color.<br>";
    }
}

// Creating an object
$car1 = new Car("Toyota", "red");
$car1->displayInfo();  // Outputs: "This car is a Toyota and is red in color."
?>
```

**Explanation:**
- `class Car`: Defines a class named `Car`.
- Properties: `$make`, `$color` store the object’s information.
- Methods: `__construct()` is automatically called when an object is created.
- `$this`: Refers to the current object.

## Encapsulation: Public, Private, and Protected

Encapsulation controls access to properties and methods:

Accessible in child classes

| Modifier |  Accessible in the class | Accessible outside  | Accessible in child classes|
|----------|--------------------------|---------------------|-------------------------- |

| **public**   | ✅                              | ✅                         | ✅                                        |
|--------------|--------------------------------|---------------------------|------------------------------------------|

| **private** | ✅                               | ❌                         | ❌                                        |
|-------------|---------------------------------|---------------------------|------------------------------------------|

|**protected**| ✅                               | ❌                         | ✅                                        |
|-------------|---------------------------------|---------------------------|------------------------------------------|

```php
<?php
class User {
    private $name; // Accessible only within the class

    public function __construct($name) {
        $this->name = $name;
    }

    public function getName() {
        return $this->name; // Allows access to the private property
    }
}

$user = new User("Alice");
// echo $user->name; // Error (because it's private)
echo $user->getName(); // Correct: "Alice"
?>
```

## Inheritance: Reusing Code

Inheritance allows a class to inherit properties and methods from another.

### Example of Inheritance

```php
<?php
class Animal {
    protected $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function makeSound() {
        echo "{$this->name} makes a sound.<br>";
    }
}

// Class inheriting from Animal
class Dog extends Animal {
    public function makeSound() {
        echo "{$this->name} barks! <br>";
    }
}

$dog = new Dog("Rex");
$dog->makeSound(); // Outputs: "Rex barks! "
?>
```
**Note**: The `Dog` class inherits from `Animal` and can override the `makeSound()` method.

### Magic Methods

PHP provides special methods that start with `__`.

```php
class Person {
    public function __construct(private string $name) {
        echo "Creation of $name";
    }
    
    public function __destruct() {
        echo "Destruction of {$this->name}";
    }
    
    public function __toString(): string {
        return "My name is {$this->name}";
    }
}

$p = new Person("Alice"); // Output: "Creation of Alice"
echo $p; // Output: "My name is Alice"
unset($p); // Output: "Destruction of Alice" (calls the destructor)



## 5. Polymorphism: Overriding Methods

Polymorphism allows modifying an inherited method to change its behavior.

### Example

```php
<?php
class Bird extends Animal {
    public function makeSound() {
        echo "{$this->name} sings! 🎶<br>";
    }
}

$bird = new Bird("Parrot");
$bird->makeSound(); // Outputs: "Parrot sings! 🎶"
?>
```

## Abstract Classes and Interfaces (Contracts to Follow)

- Abstract class: A class that cannot be instantiated directly.
- An interface requires implementing methods in the classes.

### Example of an Interface

```php
<?php
interface Flyable {
    public function fly();
}

class Plane implements Flyable {
    public function fly() {
        echo "The plane is flying! ✈️<br>";
    }
}

$plane = new Plane();
$plane->fly(); // Outputs: "The plane is flying! ✈️"
?>
```

A class can implement multiple interfaces, unlike simple inheritance.

```php
abstract class Animal {
abstract public function speak(): string;
}

class Cat extends Animal {
public function speak(): string {
return "Meow!";
}
}

$cat = new Cat();
echo $cat->speak(); // "Meow!"
```

## Traits: Avoiding Code Duplication

Traits allow sharing code across multiple classes. (multiple inheritance)

### Example of a Trait

```php
<?php
trait Identifiable {
    public function showID() {
        echo "ID: " . uniqid() . "<br>";
    }
}

class Product {
    use Identifiable;
}

$product = new Product();
$product->showID(); // Generates a unique ID
?>
```

## Namespace: Organizing Code

Namespaces avoid name conflicts in large applications.

### Example of Namespace

```php
<?php
namespace MyApp;

class Client {
    public function greet() {
        echo "Hello from MyApp!<br>";
    }
}

$client = new Client();
$client->greet();
?>
```

## utoloading with `spl_autoload_register`

Autoloading automatically loads classes.

### Example

```php
<?php
spl_autoload_register(function($class) {
    include $class . ".php";
});

$object = new MyClass(); // Automatically loads "MyClass.php"
?>
```
```php
// With Composer (composer.json file)
{
"autoload": {
"psr-4": {
"MyProject\": "src/"
        }
    }
}
```

## CRUD with OOP and MySQL

Using PDO for database connection and queries.

### Example: Connection and Insert into Database

```php
<?php
class Database {
    private $pdo;

    public function __construct() {
        $this->pdo = new PDO("mysql:host=localhost;dbname=testdb", "root", "");
    }

    public function addUser($name) {
        $stmt = $this->pdo->prepare("INSERT INTO users (name) VALUES (:name)");
        $stmt->execute(['name' => $name]);
        echo "User added!<br>";
    }
}

$db = new Database();
$db->addUser("Alice");
?>
```

## Summary

| Concept           | Description                                               |
|-------------------|-----------------------------------------------------------|
| **Class & Object** | Basic structure of OOP                                    |
| **Encapsulation**  | Protects access to properties                             |
| **Inheritance**    | Reuses code from another class                            |
| **Polymorphism**   | Overrides methods to adapt behavior                       |
| **Interface**      | Defines a contract for classes                            |
| **Trait**          | Reuses code without inheritance                           |
| **Namespace**      | Organizes classes                                         |
| **Autoloading**    | Automatically loads files                                 |
| **CRUD with PDO**  | Manages database with OOP principles                      |