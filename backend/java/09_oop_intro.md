# Java: Object-Oriented

## Key OOP Concepts

### **1. Encapsulation**

-   **Definition:** Bundling data (fields) and methods (functions) that operate on the data into a single unit, typically a class.
-   **Key Principle:** Data hiding is enforced by using access modifiers (`private`, `protected`, `public`).

----------

### **2. Inheritance**

-   **Definition:** Allows a class (child) to acquire the properties and methods of another class (parent).
-   **Key Benefit:** Promotes code reuse.
-   **Syntax:** Use the `extends` keyword.

----------

### **3. Polymorphism**

-   **Definition:** The ability of an object to take on multiple forms.
-   **Types:**
  1.  **Compile-time (Method Overloading):** Methods with the same name but different parameters.
  2.  **Runtime (Method Overriding):** A subclass modifies a parent class's method.

----------

### **4. Abstraction**

-   **Definition:** Hiding implementation details and showing only the functionality to the user.
-   **Implementation:** Use `abstract` classes or `interfaces`.

----------

### **5. Classes and Objects**

-   **Class:** A blueprint for creating objects.
-   **Object:** An instance of a class.

----------

### **6. Access Modifiers**

-   **Definition:** Control access to classes, methods, and fields.
-   **Types:**
  -   `public`: Accessible everywhere.
  -   `private`: Accessible only within the class.
  -   `protected`: Accessible in the package and subclasses.
  -   Default (no modifier): Accessible within the package.

----------

### **7. Keywords in OOP**

-   `class`: Declares a class.
-   `new`: Creates an object.
-   `this`: Refers to the current object.
-   `super`: Refers to the parent class's methods or constructors.
-   `final`: Prevents modification (e.g., inheritance or overriding).
-   `static`: Belongs to the class rather than any object.

----------



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

### Note: Not Using Encapsulation May Be Acceptable

In some very simple programs or small projects where you're confident that data doesn't need to be protected or modified in controlled ways, encapsulation might seem unnecessary. For example, in **POJOs (Plain Old Java Objects)** or **data transfer objects**, you might not care about the encapsulation.
However, in most professional codebases and larger projects, encapsulation is essential for maintainability, flexibility, and robustness.

# **Summary: Types of Classes, Methods, Attributes, and Access Modifiers in Java**

| **Element**               | **Type/Modifier**               | **Description**                                                                                     | **Use Case**                                                                                             |
|---------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Classes**               | **Public**                     | A class accessible from any package.                                                               | Entry point of an application, public APIs.                                                             |
|                           | **Package-private**            | A class with no modifier, accessible only within the same package.                                 | Utility or internal classes specific to a module.                                                       |
|                           | **Abstract**                   | A class that can have both abstract and concrete methods. Cannot be instantiated.                  | Provides a base for subclasses while enforcing the implementation of certain methods.                   |
|                           | **Static nested**              | A nested class accessible without an instance of the enclosing class.                              | Utility or helper classes closely related to another class.                                             |
|                           | **Inner (non-static)**         | A nested class that requires an instance of the enclosing class.                                   | Handles logic tied to the state of the enclosing instance.                                              |
|                           | **Anonymous**                  | A class with no name, defined at the point of instantiation.                                        | Quick implementations, often for interfaces or abstract classes.                                        |
| **Interfaces**            | **Interface**                  | A set of abstract methods (all public by default) to be implemented by other classes.              | Defines a contract, ensures uniform implementation (e.g., Java Collections API).                        |
| **Methods**               | **Instance**                   | A method associated with a specific instance.                                                      | Manipulates an object’s attributes (e.g., `getters`, `setters`).                                        |
|                           | **Static**                     | A method independent of any instance.                                                              | Utility or global methods (e.g., `Math.sqrt`).                                                          |
|                           | **Abstract**                   | A method declared without an implementation, to be defined in subclasses.                          | Enforces specific behavior in subclasses.                                                               |
|                           | **Final**                      | A method that cannot be overridden in subclasses.                                                  | Preserves the original logic in subclasses.                                                             |
|                           | **Synchronized**               | A method ensuring thread-safe access to shared resources.                                          | Used in concurrent programming.                                                                         |
| **Attributes**            | **Instance**                   | Data specific to each instance of the class.                                                       | Stores properties unique to an object.                                                                 |
|                           | **Static**                     | Data shared by all instances of a class.                                                           | Constants or global information (e.g., instance counters).                                              |
|                           | **Final**                      | An attribute with a fixed value after initialization.                                              | Defines immutable constants (e.g., `PI`).                                                              |
|                           | **Transient**                  | An attribute ignored during serialization.                                                         | Excludes sensitive or unnecessary data from persistence (e.g., passwords, caches).                      |
| **Access Modifiers**      | **Public**                     | Accessible everywhere.                                                                              | Public APIs, globally accessible methods or classes.                                                    |
|                           | **Private**                    | Accessible only within the class where it is defined.                                               | Strict encapsulation, protects internal data (e.g., attributes).                                        |
|                           | **Protected**                  | Accessible within the same package and by subclasses.                                               | Enables inheritance with controlled access.                                                             |
|                           | **Package-private** (default)  | Accessible only within the package.                                                                | Internal elements specific to a module.                                                                |

---

### **Organization by Importance and Frequency of Use**

1. **Public and Package-private Classes**: Commonly used to organize applications.
2. **Instance and Static Methods**: Essential for business logic and utilities.
3. **Interfaces**: Widely used to define contracts or APIs.
4. **Private and Constant Attributes**: Crucial for encapsulation and data management.
5. **Abstract Classes**: Less frequent but important for shared behavior.
6. **Access Modifiers**: Always necessary for managing visibility.
7. **Nested, Inner, or Anonymous Classes**: Less common but useful in specific scenarios.
