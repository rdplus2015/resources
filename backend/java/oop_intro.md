# Java: Object-Oriented

## Key OOP Concepts

###  Classes and Objects
- **Class**: A blueprint for creating objects (template).
- **Object**: An instance of a class.
  - Object is a thing that contains fields
  - object is a thing that perform a task


- **Define a new class**

```java
public class Car {
  String name;
  int year;
  float price;
}
```
- **Create a new Object of the class**
```java
public class Main {
    public static void main(String[] args) {
        // Create a new Car object
        Car carOne = new Car();
        System.out.println("Name: " + carOne.name + ".\n" + "Price: " + carOne.year); // Will print nothing

        // Initialize attributes
        carOne.name = "Toyota";
        carOne.year = 2015;
        carOne.price = 1000.00F;

        System.out.println("Name: " + carOne.name + ".\n" + "Price: " + carOne.year); // Will print all values
    }
}
```
```java
    /* new Car("Dodge", 8500, 2019, "blue", new String[] {"tires", "keys"})); In java you can create an object without store it in a variable */
Car[] cars = new Car[] {
        new Car("Nissan", 5000, 2020, "red", new String[] {"tires", "keys"}),
        new Car("Dodge", 8500, 2019, "blue", new String[] {"tires", "keys"})
};
```

###  Classes and Objects with a constructor 
A **constructor** in Java is a special method used to initialize objects when they are created. It is called automatically when you create a new instance of a class using the `new` keyword. The constructor sets up the initial state of the object by assigning values to its fields.

### Key Features of a Constructor:

-   **Same name as the class**: The constructor must have the same name as the class.
-   **No return type**: Unlike regular methods, constructors do not have a return type, not even `void`.
-   **Called automatically**: A constructor is called automatically when an object is created.
-   **Can be overloaded**: You can have multiple constructors with different parameters (constructor overloading).
-   **If you don’t define a constructor in your class, Java provides a **default constructor** that takes no arguments and initializes fields with default values (like `0` for numbers and `null` for objects).**
-   **Multiple constructors allow you to create an object with different levels of detail.**


```java
public class Car {
    String name;
    int year;
    float price;

    // Constructor with all parameters
    public Car(String name, int year, float price ) {
        this.name = name;
        this.year = year;
        this.price = price;
    }

    // Constructor with fewer parameters
    public Car(String name) {
        this.name = name;
        this.year = 0;
        this.price = 0;
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        // Create a new Car object with the first 
        Car carOne = new Car("Toyota", 2015, 100.000F);
        System.out.println("Name: " + carOne.name + ".\n" + "Price: " + carOne.year); // Will print nothing
      
        // Update (Without Encapsulation)
        carOne.name = "Honda";
        carOne.price = 5000.00F;
        System.out.println("Name: " + carOne.name + ".\n" + "Price: " + carOne.year); // Will print all values
      

        // Create a new Car object with the second 
        Car carTwo = new Car("Nissan");
        System.out.println("Name: " + carTwo.name + ".\n" + "Price: " + carTwo.year); // Will print nothing

    }
}
```

### Note: Not Using Encapsulation May Be Acceptable:

In some very simple programs or small projects where you're confident that data doesn't need to be protected or modified in controlled ways, encapsulation might seem unnecessary. For example, in **POJOs (Plain Old Java Objects)** or **data transfer objects**, you might not care about the encapsulation.
However, in most professional codebases and larger projects, encapsulation is essential for maintainability, flexibility, and robustness.
