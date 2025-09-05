# **Interfaces in Java**

## **Definition**

An **interface** defines a contract: all methods are implicitly public and abstract. A class can implement multiple interfaces.

### Example:

```java
public interface Animal {
    void makeSound(); // Abstract and public by default
}

public interface Pet {
    void play();
}

public class Dog implements Animal, Pet {
    @Override
    public void makeSound() {
        System.out.println("The dog barks.");
    }

    @Override
    public void play() {
        System.out.println("The dog plays.");
    }
}
```

## **Key Points**

- All methods in an interface are implicitly **public** and **abstract**.
- Attributes in an interface are implicitly **public static final**.
- A class can implement multiple interfaces using the keyword **`implements`**.

### **Methods with Bodies (Java 8 and later)**

Starting from Java 8, interfaces can define default methods with an implementation:

```java
interface Animal {
    default void eat() {
        System.out.println("The animal eats");
    }

    void makeSound(); // Always abstract
}
```

- Interfaces cannot have constructors because they cannot be instantiated directly.
- Methods in interfaces are always **public**, regardless of the declared modifier.

## **Difference Between Interfaces and Abstract Classes**

While interfaces and abstract classes may appear similar, their uses differ significantly:

> An abstract parent class enforces a strict “is a” relationship, while an interface expresses a “can do” capability, making the code more flexible and generic.

| Feature                  | Interface                             | Abstract Class                   |
|--------------------------|---------------------------------------|-----------------------------------|
| Methods                  | All methods are abstract (before Java 8) | Can have both abstract and concrete methods |
| Inheritance              | A class can implement multiple interfaces | A class can inherit only one abstract class |
| Constructor              | No constructor                       | Can have a constructor for shared state |
| Attributes               | Implicitly public static final        | Can have instance variables      |
| Use Case                 | Define contracts and general behaviors | Reuse code and share common behaviors |

## **When to Use Interfaces and Abstract Classes**

### **Interface**
- Use interfaces to define a contract without any common implementation.
- Ideal for scenarios requiring multiple inheritance of types.
- Promotes loose coupling between components.

### **Abstract Class**
- Use abstract classes to share code and enforce a base implementation for subclasses.
- Ideal when common state or behavior needs to be shared.
- Provides a shared base for related classes.

### Example: Interface vs. Abstract Class

#### **Interface Example**

```java
interface Movable {
    void move(); // Abstract method
}

class Car implements Movable {
    @Override
    public void move() {
        System.out.println("The car drives!");
    }
}

class Airplane implements Movable {
    @Override
    public void move() {
        System.out.println("The airplane flies!");
    }
}
```

#### **Abstract Class Example**

```java
abstract class Vehicle {
    String model;

    Vehicle(String model) {
        this.model = model;
    }

    void displayModel() {
        System.out.println("Model: " + model);
    }

    abstract void move();
}

class Car extends Vehicle {
    Car(String model) {
        super(model);
    }

    @Override
    void move() {
        System.out.println("The car drives!");
    }
}

class Airplane extends Vehicle {
    Airplane(String model) {
        super(model);
    }

    @Override
    void move() {
        System.out.println("The airplane flies!");
    }
}
```

## **Advantages of Interfaces**

1. **Multiple Inheritance of Type**: A class can implement multiple interfaces, achieving multiple inheritance.
2. **Polymorphism**: Interfaces enforce consistent behavior, enabling polymorphism across unrelated classes.
3. **Loose Coupling**: Interfaces decouple the implementation from its use, promoting modular design.

## **Practical Example: Flexible Implementations**

```java
interface Car {
    void start();
    void stop();
}

class ManualCar implements Car {
    @Override
    public void start() {
        System.out.println("Manual car starts.");
    }

    @Override
    public void stop() {
        System.out.println("Manual car stops.");
    }
}

class AutomaticCar implements Car {
    @Override
    public void start() {
        System.out.println("Automatic car starts.");
    }

    @Override
    public void stop() {
        System.out.println("Automatic car stops.");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new ManualCar();
        car.start(); // "Manual car starts."

        car = new AutomaticCar(); // Reassign to another implementation
        car.start(); // "Automatic car starts."
        car.stop();  // "Automatic car stops."
    }
}
```

## **Key Concepts Summary**

- **Interfaces are contracts**: They define behaviors without prescribing how they must be implemented.
- **Multiple inheritance**: Classes can implement multiple interfaces but only extend one abstract class.
- **Default and static methods (from Java 8)**: Interfaces can provide concrete implementations for default behavior.
- **Loose coupling**: Interfaces promote modularity and flexibility in software design.

By distinguishing between interfaces and abstract classes, you can design robust, extensible, and maintainable systems.

