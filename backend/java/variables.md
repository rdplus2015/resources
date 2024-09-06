# Java Variables 

## 1. Introduction to Variables

- **Definition**: A variable is a storage location that holds data.
- **Declaration**: To declare a variable in Java, specify the data type followed by the variable name.
- **Initialization**: Assign a value to the variable when you declare it or later in the code.

```java
public class Main {
    public static void main(String[] args) {

        // Declaration
        int number;

        // Initialization
        number = 5;

        // Declaration and Initialization
        int count = 10;

        // Declaration and initialization of a float variable. 
        // the f is important before by default java understand float as double
        float myFloat = 3.14f;
        System.out.println("Float value: " + myFloat);

        // Declaration and initialization of a double variable
        // Perform division with more precision. And double takes up more memory
        double myDouble = 3.141592653589793;
        System.out.println("Double value: " + myDouble);

        // Declaration and initialization of a char variable
        char myChar = 'A';
        System.out.println("Char value: " + myChar);

        // Declaration and initialization of a String variable
        String myString = "Hello, World!";
        System.out.println("String value: " + myString);

        // Long literal, using L suffix
        // The L suffix tells the compiler to treat the literal as a long, not as an int. 
        long myLong = 2147483648L; // Value exceeds int range, within long range
 
        // Comparison between the numbers to obtain booleans
        int a = 10;
        int b = 20;

        boolean isAGreaterThanB = a > b; // Returns false because 10 is not greater than 20
        boolean isAEqualToB = a == b; // Returns false because 10 is not equal to 20
        boolean isALessThanOrEqualToB = a <= b; // Returns true because 10 is less than or equal to 20
```

## 2. Naming Variables

-   Begin with a lowercase letter.
-   Use camelCase for multiple words (e.g., `totalAmount`, `personCount`).


## 3. Primitive Data Types and Maximum Capacity

-   **int**: Stores integers. **Capacity**: -2,147,483,648 to 2,147,483,647 (32-bit signed integer).

-   **long**: Stores large integers. **Capacity**: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (64-bit signed integer).

-   **short**: Stores smaller integers. **Capacity**: -32,768 to 32,767 (16-bit signed integer).

-   **byte**: Stores very small integers. **Capacity**: -128 to 127 (8-bit signed integer).

-   **float**: Stores floating-point numbers with fractional parts. **Capacity**: Approximately ±3.40282347E+38 (32-bit IEEE 754 floating-point).

-   **double**: Stores large floating-point numbers. **Capacity**: Approximately ±1.79769313486231570E+308 (64-bit IEEE 754 floating-point).

-   **char**: Stores a single character/letter or ASCII values. **Capacity**: 0 to 65,535 (16-bit Unicode character).

-   **boolean**: Stores `true` or `false`. **Capacity**: 1 bit.

**Rule**: Use the smallest amount of memory possible for efficiency. For example, to count people in a bus, `int` is sufficient.


## 4. Different Ways to Print in Java

```java
int a = 10;
String name = "Alice";

// Simple Print
System.out.print("Hello, World!");

// Print with a newline
System.out.println("Hello, World!");

// Printing a variable
System.out.println("The value of a is: " + a);

// Formatting output
System.out.printf("Name: %s, Age: %d%n", name, a);

String myage = name + "a " +  a + "ans";

```

## 5. Wrapper Classes 

Wrapper classes in Java allow primitive data types (like `int`, `double`, etc.) to be used as objects. This is essential because, unlike primitive types, objects provide more functionalities, such as being stored in collections like `ArrayList`, which can only hold objects.

## Primitive Types and Their Corresponding Wrapper Classes
Here is a list of primitive types and their corresponding wrapper classes:

- `byte` → `Byte`
- `short` → `Short`
- `int` → `Integer`
- `long` → `Long`
- `float` → `Float`
- `double` → `Double`
- `char` → `Character`
- `boolean` → `Boolean`

## Why Use Wrapper Classes?

1. **Collections (e.g., `ArrayList`)**: Collections in Java, such as lists, can only store objects. Therefore, to store primitive types, wrapper classes are required.
   
   Example:
   ```java
   ArrayList<Integer> numbers = new ArrayList<>();
   numbers.add(10); // Here, 10 is an int, but it is automatically converted to an Integer (autoboxing)
   ```

2. **Additional Functionality**: Wrapper classes provide additional utility methods. For instance, the `Integer` class offers methods like `parseInt` to convert a string to an integer.
   
   Example:
   ```java
   String s = "123";
   int number = Integer.parseInt(s); // Convert the string "123" to an integer
   ```

3. **Autoboxing and Unboxing**:
   - **Autoboxing**: The automatic conversion of a primitive type into its corresponding wrapper class.
     Example: 
     ```java
     int primitive = 10;
     Integer obj = primitive; // Autoboxing: the primitive int is converted into an Integer object
     ```
   - **Unboxing**: The reverse conversion, from a wrapper class back into its primitive type.
     Example:
     ```java
     Integer obj = 10;
     int primitive = obj; // Unboxing: Integer is converted back into int
     ```

## Complete Example

```java
public class WrapperExample {
    public static void main(String[] args) {
        int primitive = 5;
        Integer obj = primitive; // Autoboxing

        System.out.println("Value of Integer object: " + obj);

        int primitiveAgain = obj; // Unboxing
        System.out.println("Value after Unboxing: " + primitiveAgain);
    }
}
```

## Summary
Wrapper classes allow primitive types to be "wrapped" in objects, which is useful for collections and taking advantage of the utility methods provided by wrapper classes.

## 6. Getting User Input (Using Scanner Class)

- To retrieve input from the user, use the `Scanner` class.

```java
import java.util.Scanner; // Import the Scanner class to take user input

public class Main {
    public static void main(String[] args) {
        // Create a new Scanner object to get input from the console
        Scanner scanner = new Scanner(System.in);
        
        // Get an integer input
        System.out.print("Enter your age (int): ");
        int age = scanner.nextInt(); // Read an integer
        
        // Get a float input
        System.out.print("Enter your height (float): ");
        float height = scanner.nextFloat(); // Read a float value

        // Get a double input
        System.out.print("Enter your weight (double): ");
        double weight = scanner.nextDouble(); // Read a double value

        // Get a boolean input
        System.out.print("Are you a student? (true/false): ");
        boolean isStudent = scanner.nextBoolean(); // Read a boolean value

        // Get a byte input
        System.out.print("Enter your grade (byte): ");
        byte grade = scanner.nextByte(); // Read a byte value

        // Get a long input
        System.out.print("Enter your phone number (long): ");
        long phoneNumber = scanner.nextLong(); // Read a long value
        
        // Get a string input (word)
        System.out.print("Enter your fullname (String): ");
        scanner.nextLine(); // Clear the buffer
        String fullname = scanner.next(); // Reads the next token (a single word or caracter)

        // Get a string input
        System.out.print("Enter your name (String): ");
        scanner.nextLine(); // Clear the buffer
        String name = scanner.nextLine(); // Read a string value
        
        // Display the collected inputs
        System.out.println("\n---User Details---");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        System.out.println("Weight: " + weight);
        System.out.println("Is a student: " + isStudent);
        System.out.println("Grade: " + grade);
        System.out.println("Phone Number: " + phoneNumber);
    }
}
```
-   **` scanner.close()`** close the `Scanner` when done to avoid resource leaks. For console input, it is not always critical but is a good practice.

-   **`Scanner`** is the name of the class.

-   **`scanner`** is the name of the variable (the instance of the `Scanner` class).

-   **`new Scanner(System.in)`** creates a new object of the `Scanner` class that takes user input from the console (using `System.in`).
## NextLine Trap 

To avoid the `nextLine` trap, always consume the newline character left by previous Scanner methods before calling `nextLine()`.
Adding `scanner.nextLine()` after `nextInt()` and `others` ensures that any leftover newline characters are consumed, allowing `nextLine()` to work correctly.
