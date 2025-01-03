## **Polymorphism in Java**

### **Definition**

Polymorphism is the ability of an object to take multiple forms. It is a core principle of Object-Oriented Programming (OOP) and allows for flexibility and code reuse.

### **Types of Polymorphism**

1. **Method Overloading (Compile-time Polymorphism):**
    - Methods with the **same name** but **different signatures** (parameters) in the same class.

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }
}
```

2. **Method Overriding (Runtime Polymorphism):**
    - Methods with the **same signature** in the parent and child classes, allowing a child class to provide its specific implementation.

```java
public class Parent {
    public void display() {
        System.out.println("Method from Parent class");
    }
}

public class Child extends Parent {
    @Override
    public void display() {
        System.out.println("Overridden method in Child class");
    }
}
```

---

### **Polymorphism Through Inheritance**

In Java, polymorphism relies on two main mechanisms:

1. **Inheritance:** Allows child classes to inherit from parent classes.
2. **Interfaces:** Allows classes to implement multiple contracts.

#### Example with Inheritance

```java
class Animal {
    public void makeNoise() {
        System.out.println("An animal makes a noise");
    }
}

class Dog extends Animal {
    @Override
    public void makeNoise() {
        System.out.println("The dog barks");
    }
}

class Cat extends Animal {
    @Override
    public void makeNoise() {
        System.out.println("The cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog(); // Reference of type Animal, object of type Dog
        Animal myCat = new Cat(); // Reference of type Animal, object of type Cat

        myDog.makeNoise(); // Outputs: "The dog barks"
        myCat.makeNoise(); // Outputs: "The cat meows"
    }
}
```

#### Example with Interfaces

```java
interface Flyable {
    void fly();
}

class Bird implements Flyable {
    @Override
    public void fly() {
        System.out.println("The bird flies");
    }
}

class Plane implements Flyable {
    @Override
    public void fly() {
        System.out.println("The plane flies");
    }
}

public class Main {
    public static void main(String[] args) {
        Flyable myBird = new Bird();  // Reference of type Flyable, object of type Bird
        Flyable myPlane = new Plane(); // Reference of type Flyable, object of type Plane

        myBird.fly();  // Outputs: "The bird flies"
        myPlane.fly(); // Outputs: "The plane flies"
    }
}
```

---

### **Type Polymorphism vs. Object Polymorphism**

| **Characteristic**             | **Type Polymorphism**                                                              | **Object Polymorphism**                                                        |
|--------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Definition**                 | Ability of a parent-type reference to refer to child-type objects.                | Behavior where the executed method depends on the actual object type at runtime. |
| **Example**                    | Reference of type `Animal` pointing to `Dog` or `Cat`.                            | Method `makeNoise()` executing differently based on the actual object type.     |
| **Reference vs. Object**       | Reference is of parent type, object is of child type.                             | The method invoked depends on the actual object type, not the reference type.   |
| **Polymorphism Type**          | Occurs at the type level (during compilation).                                    | Occurs at the object level (during runtime).                                   |

---

### **Casting and Polymorphism**

Polymorphism in Java is closely tied to type casting. There are two types of casting:

1. **Implicit Casting (Upcasting):**
    - Automatically performed by Java when assigning a child object to a parent reference.

```java
Animal animal = new Dog();
```

2. **Explicit Casting (Downcasting):**
    - Must be performed manually when assigning a parent reference back to a child type.

```java
Animal animal = new Dog();
Dog dog = (Dog) animal;
```

#### Example of Downcasting with `instanceof`

To avoid `ClassCastException`, use the `instanceof` operator to check the object type before downcasting.

```java
Animal animal = new Dog();
if (animal instanceof Dog) {
    Dog dog = (Dog) animal;
    dog.makeNoise();
}
```

---

### **Abstract Classes and Methods**

1. **Abstract Class:**
    - Cannot create an object directly from an abstract class.
    - Serves as a blueprint for other classes.

2. **Abstract Method:**
    - Declared without an implementation, forcing subclasses to provide one.

#### Example of Abstract Class and Method

```java
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

class Rectangle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a rectangle");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape shape1 = new Circle();
        Shape shape2 = new Rectangle();

        shape1.draw(); // Outputs: "Drawing a circle"
        shape2.draw(); // Outputs: "Drawing a rectangle"
    }
}
```

---

### **Summary**

- Polymorphism enables flexibility and reuse in OOP.
- Method overloading happens at compile time, while method overriding happens at runtime.
- Type polymorphism allows for generalized coding through parent references.
- Object polymorphism ensures behavior is dictated by the actual object type at runtime.
- Abstract classes and methods enable layer-by-layer abstraction and avoid code duplication.
- Proper use of casting is crucial to leverage polymorphism effectively.
- 