
# Java Mathematical Operations 

## 1. Basic Arithmetic Operators

| Operator | Symbol | Description | Example |
|----------|--------|-------------|---------|
| Addition | `+`    | Adds two values together | `int result = 5 + 3; // 8` |
| Subtraction | `-`  | Subtracts one value from another | `int result = 5 - 3; // 2` |
| Multiplication | `*` | Multiplies two values | `int result = 5 * 3; // 15` |
| Division | `/`   | Divides one value by another | `int result = 6 / 2; // 3` |
| Modulus | `%`    | Returns the remainder of division | `int result = 5 % 3; // 2` |

## 2. Increment and Decrement Operators

| Operator | Symbol | Description | Example |
|----------|--------|-------------|---------|
| Increment | `++`  | Increases value by 1 | `int a = 5; a++; // 6` |
| Decrement | `--`  | Decreases value by 1 | `int b = 5; b--; // 4` |

**Note**: 
- `a++` (post-increment) increments **after** using the value.
- `++a` (pre-increment) increments **before** using the value.

Example:
```java
int x = 5;
System.out.println(x++); // Prints 5, then x becomes 6
System.out.println(++x); // Increments first, then prints 7
```

## 3. Compound Assignment Operators

| Operator | Symbol | Description | Example |
|----------|--------|-------------|---------|
| Addition Assignment | `+=`  | Adds and assigns | `int a = 5; a += 3; // a = 8` |
| Subtraction Assignment | `-=` | Subtracts and assigns | `int a = 5; a -= 2; // a = 3` |
| Multiplication Assignment | `*=` | Multiplies and assigns | `int a = 5; a *= 3; // a = 15` |
| Division Assignment | `/=` | Divides and assigns | `int a = 6; a /= 2; // a = 3` |
| Modulus Assignment | `%=` | Applies modulus and assigns | `int a = 5; a %= 3; // a = 2` |

## 4. Integer Division

In Java, integer division truncates the result. There is no specific `//` operator for floor division in Java, but you can use integer division directly:
```java
int result = 7 / 2; // result is 3 (truncates decimal)
```

If you need a floating-point result, you can cast one of the numbers to `double`:
```java
double result = (double) 7 / 2; // result is 3.5
```

## 5. Example Code

```java
public class Main {
    public static void main(String[] args) {
        // Basic arithmetic
        int addition = 5 + 3;       // 8
        int subtraction = 5 - 3;    // 2
        int multiplication = 5 * 3; // 15
        int division = 6 / 2;       // 3
        int modulus = 5 % 3;        // 2
        
        // Increment and decrement
        int x = 5;
        x++;  // x becomes 6
        x--;  // x becomes 5 again
        
        // Compound assignments
        int a = 5;
        a += 3;  // a = a + 3, so a is 8
        a -= 2;  // a = a - 2, so a is 6
        a *= 2;  // a = a * 2, so a is 12
        a /= 3;  // a = a / 3, so a is 4
        a %= 2;  // a = a % 2, so a is 0
        
        // Division with casting for floating-point result
        double result = (double) 7 / 2; // 3.5
        
        System.out.println("Result: " + result);
    }
}
```

## Note 
-   **Without parentheses**, concatenation happens left to right, which can lead to unexpected results if you're mixing numbers and strings.
-   **With parentheses**, you control the order of operations, ensuring mathematical expressions are evaluated before concatenation.

```java
String result = "Sum: " + (a + b); // Output: "Sum: 15" (math is done first)
```

**Casting** in Java allows you to convert a variable from one data type to another, either widening or narrowing its type. This is particularly important when dealing with different types in expressions (e.g., converting an `int` to a `double` for precision).

### Types of Casting in Java

1.  **Widening Casting (Automatic)**: Converting a smaller type to a larger type, done automatically by Java without losing data.
    
    -   **byte → short → int → long → float → double**
2.  **Narrowing Casting (Manual)**: Converting a larger type to a smaller type, which requires explicit casting because data loss may occur.
    
    -   **double → float → long → int → short → byte**

### Widening Casting (Automatic)

Widening happens implicitly (automatically) when you convert a smaller type into a larger type. For example:


```java 
int myInt = 9;
double myDouble = myInt; // Automatic casting: int to double
System.out.println(myDouble); // Output: 9.0
```

In this case, Java automatically converts `myInt` from an `int` to a `double`.

### Narrowing Casting (Manual)

Narrowing must be done manually because converting a larger type into a smaller type can lead to loss of data (e.g., losing precision or truncating values).

To perform narrowing casting, you need to specify the target type in parentheses before the value:

```java
double myDouble = 9.78;
int myInt = (int) myDouble; // Manual casting: double to int
System.out.println(myInt); // Output: 9
```

Here, `myDouble` is cast to an `int`, and the fractional part (`.78`) is truncated, resulting in `9`.

### Why Use Casting?

1.  **For Compatibility**: When dealing with mixed data types (e.g., combining integers and floating-point numbers), casting can be necessary to ensure proper calculations or to match method signatures.
    
2.  **To Avoid Loss of Precision**: When performing mathematical operations where precision is critical, you might cast integers to floating-point numbers (e.g., `int` to `double`).
    

### Example: Casting and Mathematical Operations
```java
int a = 5;
int b = 2;

// Without casting, integer division truncates the result
double result1 = a / b; // Output: 2.0, not 2.5

// With casting, the division is performed with precision
double result2 = (double) a / b; // Output: 2.5
```

In this example, casting one of the operands (`a`) to `double` ensures that the division produces a floating-point result rather than an integer result.

- **Note**: **In Java, during an arithmetic operation between primitive types like byte, the values ​​are automatically promoted to int for calculation.**

### Casting with Strings

You can also cast numbers to strings indirectly by using concatenation or methods like `String.valueOf()`:

```java
int number = 42;
String str = String.valueOf(number); // Converts int to String
```
