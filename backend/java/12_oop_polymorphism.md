## Polymorphism in Java

### **Definition**

Polymorphism is the ability of an object to take multiple forms. It is a core principle of Object-Oriented Programming (OOP) and allows for flexibility and code reuse.

### **Types of Polymorphism**

### 1. **Method Overloading (Compile-time Polymorphism or Static polymorphism):**

- Methods with the **same name** but **different signatures** (parameters) in the same class.
- Decided on compilation.

```java
class Calculator {
    // addition of two integers
    int addition(int a, int b) {
        return a + b;
    }

    // addition of three integers
    int addition(int a, int b, int c) {
        return a + b + c;
    }

    // addition of two doubles
    double addition(double a, double b) {
        return a + b;
    }
}

public class TestOverloading {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.addition(2, 3));       // 5
        System.out.println(calc.addition(2, 3, 4));    // 9
        System.out.println(calc.addition(2.5, 3.5));   // 6.0
    }
}
```
- Here, the `addition` method has **multiple forms** depending on the parameters → this is **polymorphism by overloading**.
> **Overloading** is the creation of **several different methods**, with the **same name**, but with different **parameters** (type, number, or order).
  The **choice of which method** to execute is made **by the compiler** (static linking), based on the **arguments passed**.
  This can be done **in the same class** or in a **child class**.

### 2. **Method Overriding (Runtime Polymorphism, Object Polymorphism, Dynamic polymorphism):**
>Methods with the **same signature** in the parent and child classes, allowing a child class to provide its specific implementation.
This is the override mechanism in action. The JVM always calls the version (method) of the actual object, never the one of the parent type (reference type).
It determines which version of the method is actually executed at runtime.

```java
class Animal {
    void speak() {
        System.out.println("An animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("The dog barks");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("The cat meows");
    }
}

public class TestPolymorphism {
    public static void main(String[] args) {
        Animal a1 = new Dog(); // Dog object seen as an Animal
        Animal a2 = new Cat(); // Cat object seen as an Animal

        a1.speak(); // The dog barks 
        a2.speak(); // The cat meows 
        
        Dog a1 = new Dog(); // Dog object seen as an Animal
        Cat a2 = new Cat(); // Cat object seen as an Animal

        a1.speak(); // The dog barks 
        a2.speak(); // The cat meows 
    }
}
```


### 3. Type Polymorphism (subtyping, )

This is a **language/compiler rule**. It simply says: "A variable of type parent can contain a child object.". This means that a **variable of type parent** can reference an **object of a child class**. This is what allows you to manipulate several different objects through the **same generic type**

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
>Casting is necessary when a parent reference points to a child object, because the parent reference only provides access to methods and properties defined in the parent; to use those specific to the child, you must cast. for example: When you create a `Dog` object with an `Animal` reference, you can only call the methods defined in `Animal`, but if one of those methods is overridden in `Dog`, the `Dog` version will be executed.


**Note 1 :** Polymorphism can be used through Inheritance (class) or through Interface
- **Inheritance:** Allows child classes to inherit from parent classes.
- **Interfaces:** Allows classes to implement multiple contracts.

**Note 2 :** 
- **Reference** = what the compiler sees (what you wrote before the `=`).
  - This is the **declared type** of the variable.
  - It determines **what the compiler allows** (which methods/properties you can call).

- **Actual object** = what the JVM creates with `new`.
  - It determines **which version of the method is actually executed at runtime**.

- **Reference type** = compile-time → which methods are accessible.
- **Actual type** = run-time → which version of the method is executed.
  - Compilation → depends on the **reference type**.
  - Runtime → depends on the **actual type of the object**.
- Polymorphism of type allow you to put multiple subtypes in the same collection and process them in a loop.

    
### **Type Polymorphism vs. Object Polymorphism**

| **Characteristic**             | **Type Polymorphism**                                                              | **Object Polymorphism**                                                        |
|--------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Definition**                 | Ability of a parent-type reference to refer to child-type objects.                | Behavior where the executed method depends on the actual object type at runtime. |
| **Example**                    | Reference of type `Animal` pointing to `Dog` or `Cat`.                            | Method `makeNoise()` executing differently based on the actual object type.     |
| **Reference vs. Object**       | Reference is of parent type, object is of child type.                             | The method invoked depends on the actual object type, not the reference type.   |
| **Polymorphism Type**          | Occurs at the type level (during compilation).                                    | Occurs at the object level (during runtime).                                   |


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

#### Note 
- Before casting: you only have access to methods of the parent type (Animal).
- After casting: you can call methods of both the parent and the child type (Dog).