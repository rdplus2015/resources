# Java Functions (Methods)

## What is a Function (Method) in Java?
A function (referred to as a method in Java) is a block of code that performs a specific task. Methods in Java allow for code reusability and better organization. Every Java application must have at least one function, which is the `main` function. It serves as the entry point for running your code.

### Example: The `main` Function
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

In this example, the `main` method is executed to run the code. It is the starting point of every Java application.

## How Do Functions Work in Java?

Functions are used to encapsulate a set of instructions or operations that can be invoked when needed. They can take inputs (parameters), perform operations, and optionally return a result.

### Defining a Function
```java
public static int addNumbers(int a, int b) {
    return a + b;
}
```

This function `addNumbers` takes two integer parameters and returns their sum. It has:

-   A **return type** (`int`)
-   **Parameters** (`int a`, `int b`)
-   A **return statement** (`return a + b;`)

## Return Value and `void` in Java

### Returning a Value

Returning a value from a method means that after performing a task, the method provides a result to the caller. Good practice suggests returning values when appropriate.

### `void` - No Return Value

A method can also return nothing. When a method doesn't return a value, it is declared with the `void` keyword. Methods that primarily perform an action like printing to the console often use `void`.

```java
public static void printMessage() {
    System.out.println("This method returns nothing");
}
```
### Key Points About Return Values

-   **Bad Practice**: Handling final results directly inside the function (like performing calculations and printing results within the same function).
    
-   **Good Practice**: Methods should return a result to the caller for further processing. Printing the result should be separate from calculation logic.
    
    Example:

```java
// Good practice - Return the result for further use
public static int multiplyNumbers(int a, int b) {
    int c = a + b;
    return c ;
}

// Another method prints the result
public void displayResult(int result) {
    System.out.println("The result is: " + result);
}
```

### Rules for Returning Values

-   **Return Type**: Must always define a return type (e.g., `int`, `String`, `double`).
-   **Return Statement**: The returned value must match the defined return type.
-   **Default Behavior**: When a function is declared to return a value, it must always return something. If the method doesn't return a value, it should be declared as `void`.

## Commenting Java Functions

It is a good practice to document your functions using Java comments. This can be done using single-line comments (`//`) or multi-line comments (`/* */`), but it’s recommended to use **Javadoc** comments to describe a method’s functionality.

```java

/**
 * 
 * function name: addNUmbers
 * 
 * @param a (int)
 * @param b (int)
 * @return (int)
 * 
 * Inside the function:
 *      1. Adds two numbers and calculate the sum.
 * 
 */

public int addNumbers(int a, int b) {
    return a + b;
}

```

## Scope of Variables in Java

The **scope** of a variable refers to where in the code the variable is accessible. In Java, variables can be:

-   **Local Variables**: Declared inside a method and accessible only within that method.
-   **Instance Variables**: Declared inside a class but outside methods, accessible by all methods within the class.
-   **Class Variables (Static)**: Declared with the `static` keyword, shared across all instances of the class.

### Example: Local vs. Instance Variables
```java
public class Example {
    string message = "welcome my objects"; // shared by all instances of the class.

    int instanceVar = 10; // Instance variable

    public static void display() {
        int localVar = 5; // Local variable
        System.out.println("Instance var: " + instanceVar);
        System.out.println("Local var: " + localVar);
    }
}
```
in this example:

-   `instanceVar` is accessible across methods in the class.
-   `localVar` is only accessible within the `display` method.

## Built-in Functions: Essential Methods in Java

Java provides many **built-in functions** through its extensive standard library. These are pre-defined methods that help developers avoid writing common logic from scratch. Some essential built-in functions include:

### Example 
- `Math` Class Functions
- `String` Class Functions
- `Arrays` Class Functions
- `System` Class Functions
