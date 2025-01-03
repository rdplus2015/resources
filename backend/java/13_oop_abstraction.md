## Abstraction in Java

### **Abstract Class**

- **Definition**: An abstract class is a class that cannot be instantiated directly. It is designed to serve as a blueprint for other classes.
- **Purpose**: To provide a base for subclasses with shared behavior, while allowing for customization through abstract methods.
- **Key Points**:
    - Can contain both **concrete methods** (with implementation) and **abstract methods** (without implementation).
    - Cannot be instantiated directly.
    - May include constructors to initialize common fields shared by subclasses.

#### Example:

```java
abstract class Shape {
    abstract void draw(); // Abstract method (no implementation)
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape circle = new Circle();
        circle.draw(); // Output: Drawing a circle
    }
}
```

### **Abstract Methods**

- **Definition**: Methods declared without an implementation. Subclasses must provide their own implementation.
- **Syntax**:

```java
abstract class Animal {
    public abstract void makeSound(); // Abstract method
}
```

#### Example:

```java
abstract class Animal {
    public abstract void makeSound();

    public void eat() {
        System.out.println("This animal eats.");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("The dog barks: Woof Woof!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal dog = new Dog();
        dog.makeSound();  // Output: The dog barks: Woof Woof!
        dog.eat(); // Output: This animal eats.
    }
}
```

### **When to Use Abstract Classes**

1. **Shared Implementation**: Use when subclasses share common behavior.
2. **Heterogeneous Subclasses**: Use when subclasses must define specific behavior for certain methods.
3. **State Initialization**: Use when shared fields or constructors are required.

---

### **Interface vs Abstract Class**

| Feature                     | Interface                                 | Abstract Class                              |
| --------------------------- | ----------------------------------------- | ------------------------------------------- |
| **Methods**                 | Only abstract methods (before Java 8)     | Can have both abstract and concrete methods |
| **Default Implementations** | Allowed (from Java 8 onwards)             | Can include concrete methods                |
| **Constructors**            | Not allowed                               | Allowed                                     |
| **Inheritance**             | A class can implement multiple interfaces | A class can extend only one abstract class  |
| **Purpose**                 | Define a contract                         | Share common behavior                       |

#### Example of Interface:

```java
interface Vehicle {
    void move();
}

class Car implements Vehicle {
    @Override
    public void move() {
        System.out.println("The car drives!");
    }
}

class Airplane implements Vehicle {
    @Override
    public void move() {
        System.out.println("The airplane flies!");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle car = new Car();
        Vehicle airplane = new Airplane();
        car.move(); // Output: The car drives!
        airplane.move();   // Output: The airplane flies!
    }
}
```

### **When to Use Interfaces**

1. **Contract Definition**: When you need to define a set of methods that must be implemented.
2. **Multiple Inheritance**: When a class needs to inherit from multiple sources of behavior.
3. **Decoupling**: When you want to define behavior independent of the implementation.

---

### **Advantages of Abstraction**

1. **Avoid Duplication**: Reduces code redundancy by allowing shared behavior to reside in one place.
2. **Layered Abstractions**: Enables building layered systems by defining higher-level abstract concepts and implementing specific details in subclasses.
3. **Flexibility**: Allows future extensions by adding new concrete implementations without modifying existing code.

### **Complete Example of Abstraction**

#### Scenario:

We want to model a course with different types of evaluations (e.g., exams and assignments).

```java
abstract class Evaluation {
    String title;
    int grade;

    public Evaluation(String title, int grade) {
        this.title = title;
        this.grade = grade;
    }

    abstract void displayDetails();
}

class Exam extends Evaluation {
    public Exam(String title, int grade) {
        super(title, grade);
    }

    @Override
    void displayDetails() {lasses, tu utiliserais une classe abstraite :
        System.out.println("Exam: " + title + ", Grade: " + grade);
    }
}

class Assignment extends Evaluation {
    public Assignment(String title, int grade) {
        super(title, grade);
    }

    @Override
    void displayDetails() {
        System.out.println("Assignment: " + title + ", Grade: " + grade);
    }
}

class Course {
    String name;
    List<Evaluation> evaluations = new ArrayList<>();

    public Course(String name) {
        this.name = name;
    }

    public void addEvaluation(Evaluation evaluation) {
        evaluations.add(evaluation);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Course: " + name + "\n");
        for (Evaluation e : evaluations) {
            e.displayDetails();
        }
        return sb.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Course course = new Course("Computer Science");

        Evaluation exam1 = new Exam("End-of-term Exam", 80);
        Evaluation assignment1 = new Assignment("Homework 1", 95);

        course.addEvaluation(exam1);
        course.addEvaluation(assignment1);

        System.out.println(course);
    }
}
```

Output:

```
Course: Computer Science
Exam: End-of-term Exam, Grade: 80
Assignment: Homework 1, Grade: 95
```
---

### **Abstract Classes vs Interfaces: Key Differences**

#### Abstract Classes

-   Can have members with any access modifier (public, protected, private).

-   Can provide default implementation for some methods.

-   Useful for sharing common behaviors and state among subclasses.

-   Allows constructors and instance variables.


#### Interfaces

-   Define a contract without shared state or implementation.

-   Allow multiple inheritance by enabling a class to implement several interfaces.

-   Ideal for decoupling functionalities and specifying behavior contracts.

-   Cannot have constructors or maintain state.


----------

### **When to Choose Abstract Classes or Interfaces**

#### Use an Abstract Class if:

1.  You want to provide default implementations for some methods.

2.  You want all subclasses to share common behavior.

3.  You need constructors or shared attributes in child classes.


#### Use an Interface if:

1.  You want to define a contract without sharing code.

2.  You need multiple inheritance of behavior.

3.  You aim to decouple functionalities for better modularity.


**In Summary**: Abstract classes are better for shared behavior and state, while interfaces are ideal for defining contracts and enabling multiple inheritance.
