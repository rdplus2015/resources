# Inheritance in Java

## Definition

**Inheritance** is a mechanism where a child class inherits methods and attributes from a parent class. It promotes code reuse and supports object-oriented architecture.

```java
// Example of Inheritance in Java
class Parent {
    void display() {
        System.out.println("This is the parent class method.");
    }
}

class Child extends Parent {
    void show() {
        System.out.println("This is the child class method.");
    }
}

public class InheritanceExample {
    public static void main(String[] args) {
        Child child = new Child();
        child.display(); // Access parent method
        child.show();    // Access child method
    }
}
```

---

## Key Points

1. **No Multiple Inheritance**:
    - Java does not support multiple inheritance to avoid ambiguity and conflicts.
    - This limitation can be addressed using interfaces.

2. **`super` Keyword**:
    - Used to call parent class methods or constructors.

---

## Class `Object`

- The **root class** of all Java classes.
- Key methods:
    - `toString()`: Returns a textual representation of an object.
    - `equals(Object obj)`: Compares two objects for equality.
    - `hashCode()`: Returns a hash code for the object.
    - `getClass()`: Returns the runtime class of the object.

---

## Constructor Behavior in Inheritance

If a parent class has an explicitly defined constructor, the child class must explicitly call it using `super()` if it defines a constructor.

### Scenarios

1. **Parent class with a default constructor**:
    - If the parent class has a no-argument constructor, it will be automatically called when creating an object of the child class.

2. **Parent class with a parameterized constructor**:
    - The child class must explicitly call the parent class constructor using `super(arguments)`.

3. **No constructor in the child class**:
    - Java automatically inserts a call to `super()` in the child class's default constructor. This works only if the parent class has a no-argument constructor.


### Examples

#### Parent Class with Parameterized Constructor

```java
// Parent Class
public class Parent {
    private int a;
    private int b;

    // Parameterized Constructor
    public Parent(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Parent initialized with a = " + a + ", b = " + b);
    }
}

// Child Class
public class Child extends Parent {
    private int c;

    // Constructor of the Child class
    public Child(int a, int b, int c) {
        super(a, b); // Explicit call to Parent constructor
        this.c = c;
        System.out.println("Child initialized with c = " + c);
    }
}
```

---

### Summary of Scenarios

| **Case**                                 | **Impact on Child Classes**                                                                              |
|------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **No constructor in parent class**       | Java automatically generates a default no-argument constructor.                                         |
| **Parameterized constructor in parent**  | Child classes are required to explicitly call the parent constructor using `super(arguments)`.          |
| **Multiple constructors in parent class**| Child classes must choose which parent constructor to call using `super(arguments)`.                    |

### Note

- If a parent class has multiple constructors and the child class calls only one of them using `super(arguments)`, the attributes initialized exclusively by the other constructors will remain uninitialized. These attributes will take on their default values.

---

## Additional Notes on Inheritance

- **Abstract Classes**:
    - Parent classes can have abstract methods, forcing child classes to provide specific implementations.

```java
abstract class Vehicle {
    private String model;

    public Vehicle(String model) {
        this.model = model;
    }

    public String getModel() {
        return model;
    }

    // Abstract method
    public abstract void move();
}

class Car extends Vehicle {
    public Car(String model) {
        super(model);
    }

    @Override
    public void move() {
        System.out.println("The car drives on roads.");
    }
}

class Boat extends Vehicle {
    public Boat(String model) {
        super(model);
    }

    @Override
    public void move() {
        System.out.println("The boat sails on water.");
    }
}
```

- **Interfaces**:
    - To achieve multiple inheritance, use interfaces.

```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Duck implements Flyable, Swimmable {
    @Override
    public void fly() {
        System.out.println("The duck can fly.");
    }

    @Override
    public void swim() {
        System.out.println("The duck can swim.");
    }
}
```
