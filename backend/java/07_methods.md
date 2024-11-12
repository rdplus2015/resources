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

---

# Built-in Functions: Essential Methods in Java

Java provides many **built-in functions** through its extensive standard library. These are pre-defined methods that help developers avoid writing common logic from scratch. Some essential built-in functions include:

## String Handling Methods

| Method                                  | Description                                     | Example                                             |
|-----------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `length()`                              | Returns the length of the string                | `str.length()`                                      |
| `charAt(int index)`                     | Returns the character at the specified index    | `str.charAt(1)`                                     |
| `substring(int start, int end)`         | Returns a substring                            | `str.substring(1, 4)`                               |
| `toLowerCase()`                         | Converts all characters to lowercase           | `str.toLowerCase()`                                 |
| `toUpperCase()`                         | Converts all characters to uppercase           | `str.toUpperCase()`                                 |
| `equals(Object obj)`                    | Compares two strings                           | `str.equals("Hello")`                               |
| `equalsIgnoreCase(String anotherString)`| Compares two strings ignoring case             | `str.equalsIgnoreCase("hello")`                     |
| `trim()`                                | Removes leading and trailing whitespace        | `"  Hello ".trim()`                                 |
| `replace(char oldChar, char newChar)`   | Replaces occurrences of oldChar with newChar   | `str.replace('H', 'J')`                             |
| `contains(CharSequence sequence)`       | Checks if string contains a specific sequence  | `str.contains("ell")`                               |
| `split(String regex)`                   | Splits the string into an array based on regex | `str.split(",")`                                    |

## Math Methods

| Method                                  | Description                                     | Example                                             |
|-----------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `Math.abs(int a)`                       | Returns the absolute value of a number          | `Math.abs(-5)`                                      |
| `Math.max(int a, int b)`                | Returns the larger of two numbers               | `Math.max(5, 10)`                                   |
| `Math.min(int a, int b)`                | Returns the smaller of two numbers              | `Math.min(5, 10)`                                   |
| `Math.pow(double a, double b)`          | Returns a raised to the power of b              | `Math.pow(2, 3)`                                    |
| `Math.sqrt(double a)`                   | Returns the square root of a                    | `Math.sqrt(16)`                                     |
| `Math.random()`                         | Returns a random double between 0.0 and 1.0     | `Math.random()`                                     |
| `Math.round(double a)`                  | Rounds the value to the nearest integer         | `Math.round(4.7)`                                   |
| `Math.floor(double a)`                  | Returns the largest integer less than or equal to a | `Math.floor(4.7)`                                |
| `Math.ceil(double a)`                   | Returns the smallest integer greater than or equal to a | `Math.ceil(4.3)`                                |

## Array Methods (from `Arrays` Class)

| Method                                  | Description                                     | Example                                             |
|-----------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `Arrays.sort(int[] array)`              | Sorts the array                                 | `Arrays.sort(arr)`                                  |
| `Arrays.toString(int[] array)`          | Converts the array to a string                  | `Arrays.toString(arr)`                              |
| `Arrays.equals(int[] a, int[] b)`       | Compares two arrays                             | `Arrays.equals(arr1, arr2)`                         |
| `Arrays.fill(int[] a, int val)`         | Fills the array with a specified value          | `Arrays.fill(arr, 0)`                               |
| `Arrays.copyOf(int[] original, int newLength)` | Copies the array to a new array with a specified length | `Arrays.copyOf(arr, 5)`                |
| `Arrays.binarySearch(int[] a, int key)` | Searches for a key in a sorted array            | `Arrays.binarySearch(arr, 3)`                       |

## Collections Methods (from `Collections` Class)

| Method                                  | Description                                     | Example                                             |
|-----------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `Collections.sort(List<T> list)`        | Sorts the list                                  | `Collections.sort(list)`                            |
| `Collections.reverse(List<T> list)`     | Reverses the order of the list                  | `Collections.reverse(list)`                         |
| `Collections.shuffle(List<T> list)`     | Randomly shuffles the elements of the list      | `Collections.shuffle(list)`                         |
| `Collections.max(Collection<T> coll)`   | Returns the maximum element from the collection | `Collections.max(list)`                             |
| `Collections.min(Collection<T> coll)`   | Returns the minimum element from the collection | `Collections.min(list)`                             |
| `Collections.frequency(Collection<T> c, Object o)` | Returns the frequency of the specified element in the collection | `Collections.frequency(list, "Hello")` |

## Object Methods (from `Object` Class)

| Method                                  | Description                                     | Example                                             |
|-----------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `equals(Object obj)`                    | Compares this object with another               | `obj1.equals(obj2)`                                 |
| `hashCode()`                            | Returns a hash code value for the object        | `obj.hashCode()`                                    |
| `toString()`                            | Returns a string representation of the object   | `obj.toString()`                                    |
| `clone()`                               | Creates a clone of the object                   | `obj.clone()`                                       |
| `getClass()`                            | Returns the runtime class of the object         | `obj.getClass()`                                    |
| `notify()`                              | Wakes up a single thread that is waiting on the object's monitor | `obj.notify()`                      |
| `wait()`                                | Causes the current thread to wait until another thread invokes notify() | `obj.wait()`                            |


## Common Methods in `Scanner`

| Method                                      | Description                                             | Example                                            |
|---------------------------------------------|---------------------------------------------------------|----------------------------------------------------|
| `next()`                                    | Reads the next token as a string                        | `scanner.next()`                                   |
| `nextLine()`                                | Reads the entire line of input                          | `scanner.nextLine()`                               |
| `nextInt()`                                 | Scans the next token as an `int`                        | `int num = scanner.nextInt();`                     |
| `nextDouble()`                              | Scans the next token as a `double`                      | `double num = scanner.nextDouble();`               |
| `nextFloat()`                               | Scans the next token as a `float`                       | `float num = scanner.nextFloat();`                 |
| `nextBoolean()`                             | Scans the next token as a `boolean`                     | `boolean flag = scanner.nextBoolean();`            |
| `nextByte()`                                | Scans the next token as a `byte`                        | `byte num = scanner.nextByte();`                   |
| `nextShort()`                               | Scans the next token as a `short`                       | `short num = scanner.nextShort();`                 |
| `nextLong()`                                | Scans the next token as a `long`                        | `long num = scanner.nextLong();`                   |
| `hasNext()`                                 | Returns `true` if there is another token in the input   | `if (scanner.hasNext()) { ... }`                   |
| `hasNextInt()`                              | Returns `true` if the next token is an `int`            | `if (scanner.hasNextInt()) { ... }`                |
| `hasNextDouble()`                           | Returns `true` if the next token is a `double`          | `if (scanner.hasNextDouble()) { ... }`             |
| `hasNextLine()`                             | Returns `true` if there is another line in the input    | `if (scanner.hasNextLine()) { ... }`               |
| `useDelimiter(String pattern)`              | Sets the delimiter pattern                             | `scanner.useDelimiter(",")`                        |
| `close()`                                  | Closes the scanner                                     | `scanner.close();`                                 |
| `skip(Pattern pattern)`                     | Skips input that matches the pattern                    | `scanner.skip("\\s*")`                             |

