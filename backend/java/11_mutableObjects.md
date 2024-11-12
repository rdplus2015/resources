
# Primitives, Immutable and mutable

### **Primitives**:

-   Primitives are the most basic data types in Java, designed to store simple values (e.g., `int`, `char`, `boolean`, `float`).
-   They store the value directly in memory, making them more efficient in terms of memory and speed.
-   Primitives are not objects and cannot call methods on them.

### **Immutable Objects**:

-   Immutable objects are objects whose state cannot be modified after they are created. For example, `String` in Java is immutable.
-   Once an immutable object is created, any change requires creating a new object, which prevents unintended changes or side effects.
-   **Memory Efficiency**: While immutable objects may seem to require more memory due to frequent object creation, modern JVM optimizations, like string interning, can help manage memory efficiently.

### **Difference Between Primitives and Immutable Objects**:

-   **Primitives** store values directly in memory and are not considered objects, while **Immutable Objects** are full-fledged objects that behave consistently, preventing state changes after creation.
-   Primitives are faster and consume less memory compared to objects (including immutable ones) but lack flexibility and object-like behavior (e.g., calling methods).

### **Why Use Immutable Objects**:

-   **Thread Safety**: Immutable objects can be shared across multiple threads without synchronization, as their state cannot change.
-   **Reliability**: Immutability ensures that once an object is created, its state remains consistent, making programs easier to reason about and debug.
-   **Avoiding Side Effects**: Since immutable objects cannot be modified, there’s no risk of one part of the code unintentionally modifying the object’s state when passed by reference.

### **Mutable Objects**:

-   Mutable objects allow changes to their internal state after they have been created (e.g., `ArrayList`, `HashMap`).
-   **Reference Trap**: Mutable objects store references, and changes to one reference affect all other references pointing to the same object. This can lead to unintended side effects, where changes in one part of the code might alter the state of the object elsewhere.
-   Mutability requires careful handling in multi-threaded environments to avoid issues like inconsistent states or race conditions.


---

# Reference Trap and Copying in Java

## 1. **What is the Reference Trap?**

- **Definition**: The "Reference Trap" occurs when multiple references point to the same object in memory. This can lead to undesirable side effects when one of the objects is modified.
- **Problem**: Changes made to the object through one reference can affect other references pointing to the same object.

### Example of Reference Trap with Mutable Objects

```java
import java.util.Arrays;

public class Car {
    private String name;
    private String[] othersInfos;

    // Constructor
    public Car(String name, String[] othersInfos) {
        this.name = name;
        this.othersInfos = Arrays.copyOf(othersInfos, othersInfos.length); // Copy to avoid reference trap
    }

    public String[] getOthersInfos() {
        return Arrays.copyOf(othersInfos, othersInfos.length); // Copy to avoid reference trap
    }
    
    // toString
    @Override
    public String toString() {
        return "Car{name='" + name + "', othersInfos=" + Arrays.toString(othersInfos) + "}";
    }
}
```

### Note

- **Without `Arrays.copyOf()`**: If you don't make a copy, any modification to `othersInfos` will affect all instances sharing the same reference.

## 2. **Copying with a Mutable Array of Primitives**

- **Using `Arrays.copyOf()`**: For arrays containing primitive types (like `int`, `char`, etc.), `Arrays.copyOf()` is sufficient because primitives are not mutable.

```java
public class IntContainer {
    private int[] numbers;

    // Constructor
    public IntContainer(int[] numbers) {
        this.numbers = Arrays.copyOf(numbers, numbers.length); // Copy to avoid reference trap
    }

    public int[] getNumbers() {
        return Arrays.copyOf(numbers, numbers.length); // Copy to avoid reference trap
    }

    @Override
    public String toString() {
        return "IntContainer{" + "numbers=" + Arrays.toString(numbers) + '}';
    }
}
```

### Note

- **Primitives**: Primitive types do not suffer from reference traps, but it’s good practice to make a copy to avoid unintended side effects during modification.

## 3. **Deep Copy with Mutable Objects Containing Mutables**

- **Definition**: A deep copy involves creating a new instance of an object and all the objects it references. This is necessary when mutable objects are involved.

### Example of Deep Copy

```java
class MutableObject {
    private String value;

    public MutableObject(String value) {
        this.value = value;
    }

    public MutableObject(MutableObject source) {
        this.value = source.value; // Shallow copy
    }

    // Getters
    public String getValue() {
        return value;
    }

    // Setter
    public void setValue(String value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "MutableObject{" + "value='" + value + ''' + '}';
    }
}

public class ComplexCar {
    private String name;
    private MutableObject[] extras;

    public ComplexCar(String name, MutableObject[] extras) {
        this.name = name;
        this.extras = new MutableObject[extras.length];
        for (int i = 0; i < extras.length; i++) {
            this.extras[i] = new MutableObject(extras[i]); // Deep copy
        }
    }

    public ComplexCar(ComplexCar source) {
        this.name = source.name;
        this.extras = new MutableObject[source.extras.length];
        for (int i = 0; i < source.extras.length; i++) {
            this.extras[i] = new MutableObject(source.extras[i]); // Deep copy
        }
    }

    // Getter with deep copy
    public MutableObject getExtra(int index) {
        return new MutableObject(extras[index]); // Return a deep copy of the mutable object
    }
    
    // Setter with deep copy

    public void setExtra(int index, MutableObject newExtra) {

        extras[index] = new MutableObject(newExtra); // Set a deep copy of the mutable object

    }


    @Override
    public String toString() {
        return "ComplexCar{" +
                "name='" + name + ''' +
                ", extras=" + Arrays.toString(extras) +
                '}';
    }
}
```

### Note

- **Deep Copy**: By using a copy constructor, we ensure that each instance of `MutableObject` in the `extras` array is a new instance, avoiding the reference trap.

## 4. **Accessing Private Attributes**

- **Accessing Private Attributes**: In Java, methods within a class can access all attributes (including private ones) of that class.

### Example

```java
public class Dealer {
    private ComplexCar[] cars; // Private attribute

    public Dealer(ComplexCar[] cars) {
        this.cars = cars; // Stores the array of cars
    }

    @Override
    public String toString() {
        return "Dealer{" + "cars=" + Arrays.toString(cars) + '}';
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        MutableObject[] extras = { new MutableObject("Sunroof"), new MutableObject("Leather Seats") };
        ComplexCar car = new ComplexCar("Nissan", extras);
        Dealer dealer = new Dealer(new ComplexCar[]{ car });
        System.out.println(dealer); // Accesses private attributes via toString()
    }
}
```

### Notes

- **Encapsulation**: Using `private` helps protect data, and access to these data should be done only through methods of the class.
- **Using `toString()`**: The `toString()` method allows for displaying the details of objects while accessing private attributes.