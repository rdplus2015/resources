
# PHP Object-Oriented Programming (OOP) with Strict Typing

## Activating Strict Typing

Strict typing is enabled by adding this line at the top of the PHP file:

```php
declare(strict_types=1);
```

This will ensure that PHP performs type checking, and it will throw errors if a type mismatch occurs.

---

## Example with Strict Typing

### Example of a class with strict typing

```php
<?php
declare(strict_types=1);

class Car {
    // Properties with strict types
    private string $make;
    private string $color;

    // Constructor with strict types
    public function __construct(string $make, string $color) {
        $this->make = $make;
        $this->color = $color;
    }

    // Method with return type
    public function displayInfo(): void {
        echo "This car is a {$this->make} and is {$this->color} in color.<br>";
    }
}

// Creating an object
$car1 = new Car("Toyota", "red");
$car1->displayInfo();  // Outputs: "This car is a Toyota and is red in color."
?>
```
**Explanation:**
- The type for properties is now defined: `private string $make;`, `private string $color;`.
- The constructor and method `displayInfo()` have strict types for their parameters and return values (`string` and `void`).
- If you try to pass an incorrect type, an error will be thrown.

---

## Encapsulation with Strict Typing

### Example of encapsulation with private properties

```php
<?php
declare(strict_types=1);

class User {
    private string $name;  // Property with type

    // Constructor with strict type
    public function __construct(string $name) {
        $this->name = $name;
    }

    // Method to get the name
    public function getName(): string {
        return $this->name;
    }
}

$user = new User("Alice");
echo $user->getName();  // Outputs: "Alice"
?>
```

---

## Inheritance with Strict Typing

### Example of inheritance with strict types

```php
<?php
declare(strict_types=1);

class Animal {
    protected string $name;

    // Constructor with strict type
    public function __construct(string $name) {
        $this->name = $name;
    }

    public function makeSound(): void {
        echo "{$this->name} makes a sound.<br>";
    }
}

// Class that inherits from Animal
class Dog extends Animal {
    public function makeSound(): void {
        echo "{$this->name} barks! 🐶<br>";
    }
}

$dog = new Dog("Rex");
$dog->makeSound();  // Outputs: "Rex barks!"
?>
```

---

## Polymorphism with Strict Typing

### Example of polymorphism with strict types

```php
<?php
declare(strict_types=1);

class Bird extends Animal {
    public function makeSound(): void {
        echo "{$this->name} sings! 🎶<br>";
    }
}

$bird = new Bird("Parrot");
$bird->makeSound();  // Outputs: "Parrot sings! 🎶"
?>
```

---

## Interface with Strict Typing

### Example of an interface with strict types

```php
<?php
declare(strict_types=1);

interface Flyable {
    public function fly(): void;
}

class Plane implements Flyable {
    public function fly(): void {
        echo "The plane is flying! ✈️<br>";
    }
}

$plane = new Plane();
$plane->fly();  // Outputs: "The plane is flying! ✈️"
?>
```

---

## Traits with Strict Typing

### Example of a trait with strict types

```php
<?php
declare(strict_types=1);

trait Identifiable {
    public function showID(): void {
        echo "ID: " . uniqid() . "<br>";
    }
}

class Product {
    use Identifiable;
}

$product = new Product();
$product->showID();  // Generates a unique ID
?>
```

---

## Autoloading with `spl_autoload_register`

### Example of autoloading with strict typing

```php
<?php
declare(strict_types=1);

// Autoloading function
spl_autoload_register(function(string $class): void {
    include $class . ".php";
});

// Creating an object, assuming that MyClass.php exists
$obj = new MyClass();
?>
```

---

## CRUD with PDO and Strict Typing

### Example of CRUD with PDO and strict typing

```php
<?php
declare(strict_types=1);

class Database {
    private PDO $pdo;

    public function __construct() {
        $this->pdo = new PDO("mysql:host=localhost;dbname=testdb", "root", "");
    }

    public function addUser(string $name): void {
        $stmt = $this->pdo->prepare("INSERT INTO users (name) VALUES (:name)");
        $stmt->execute(['name' => $name]);
        echo "User added!<br>";
    }
}

$db = new Database();
$db->addUser("Alice");
?>
```

---

## Complete Example of User Class with Strict Typing

```php
<?php
declare(strict_types=1);

class User {
    private string $name;
    private string $email;

    // Constructor with strict types
    public function __construct(string $name, string $email) {
        $this->name = $name;
        $this->email = $email;
    }

    // Introduction method
    public function introduceYourself(): string {
        return "My name is {$this->name} and my email is {$this->email}.<br>";
    }

    // Getter for name
    public function getName(): string {
        return $this->name;
    }
}

// Usage
$user = new User("Alice", "alice@example.com");
echo $user->introduceYourself();  // Outputs: "My name is Alice and my email is alice@example.com."
?>
```

---

## Summary with Strict Typing

| Concept | Description |
|---------|-------------|
| **Type for properties and methods** | Using `string`, `int`, `void` to ensure type adherence |
| **Strict typing** | Using `declare(strict_types=1);` to enforce type checking |
| **Class & Object** | Structuring classes with strict types for properties and parameters |
| **Encapsulation** | Private properties with public methods to access data |
| **Inheritance and Polymorphism** | Extending classes and overriding methods |
| **Interface & Trait** | Using interfaces and traits for modular architecture |

---
