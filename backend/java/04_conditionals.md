# Booleans and Conditionals in Java

Java provides a variety of conditional structures to control the flow of a program based on conditions. Here's an overview of key concepts related to Boolean logic and conditionals.

## 1. Comparison Operators

Comparison operators are used to compare two values and return a boolean result (`true` or `false`). Here are the common comparison operators:

- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

### Example:
```java
int a = 5;
int b = 10;

System.out.println(a > b);  // (a>b): is the condition or the expression => false
```

## 2. Comparing Numbers

When comparing numbers (integers, floating-point numbers), you can use the comparison operators directly.

### Example:

```java
int x = 7;
int y = 3;

if (x > y) {
    System.out.println("x is greater than y");
} else {
    System.out.println("x is less than or equal to y");
}
```

### 3. Comparing Strings (equals and not equals)

In Java, strings are compared using the .equals() method for equality and !equals() for inequality, instead of using ==, which compares memory addresses.

### Example:

```java
String str1 = "Hello";
String str2 = "World";

if (str1.equals(str2)) {
    System.out.println("Both strings are equal");
} else {
    System.out.println("Strings are not equal");
}

if (!str1.equals(str2)) {
    System.out.println("Strings are different");
}
```
### Comparing Strings: `equals()` vs `compareTo()`

- **`equals()`** checks if two strings are exactly the same, returning `true` if they are equal and `false` otherwise.
- **`compareTo()`** compares two strings lexicographically (alphabetical order). It returns:
  - `0` if the strings are equal,
  - a **negative** number if the first string is lexicographically **less** than the second,
  - a **positive** number if the first string is lexicographically **greater** than the second.

Use `equals()` for strict equality and `compareTo()` when you need to compare or sort strings.


## 4. if and else if Statements

The if statement evaluates a condition and executes the block of code if the condition is true. You can use else if to check multiple conditions.
Syntax:

```java

if (condition1) {
    // Executes if condition1 is true
} else if (condition2) {
    // Executes if condition2 is true
} else {
    // Executes if none of the above conditions are true
}
```

### Example:

```java
int number = 15;

if (number > 20) {
    System.out.println("Number is greater than 20");
} else if (number == 15) {
    System.out.println("Number is exactly 15");
} else {
    System.out.println("Number is less than 15");
}
```

## 5. Logical Operators

Logical operators allow you to combine multiple boolean expressions:

- **&& (AND)** : Returns true if both conditions are true
- **|| (OR)** : Returns true if at least one condition is true
- **! (NOT)** : Reverses the result of the condition (true becomes false, false becomes true)

### Example:

```java
boolean isAdult = true;
boolean hasPermission = false;

if (isAdult && hasPermission) {
    System.out.println("You are allowed entry.");
} else {
    System.out.println("Entry denied.");
}

if (!isAdult) {
    System.out.println("Not an adult.");
}
```

## 6. switch Statement and break Keyword

The switch statement is used to select one of many code blocks to execute, based on the value of a variable or expression. Each case ends with a break to prevent fall-through.
Syntax:

```java
switch (expression) {
    case value1:
        // Code block for value1
        break;
    case value2:
        // Code block for value2
        break;
    default:
        // Code block if none of the cases match
}
```

### Example:

```java
int day = 3;

switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Invalid day");
}
```

### Note:

- **The `break` statement is essential to exit the switch case. Without it, the program will continue to execute the subsequent cases (fall-through).**
- **The `default` case is optional but is used to handle values that don't match any case.**

## 7. Ternary Operator

The ternary operator is a shorthand for simple if-else conditions.
Syntax:

```
condition ? expression1 : expression2;
```

## Example:

```java
int age = 18;
String result = (age >= 18) ? "Adult" : "Minor";
System.out.println(result); // Output: Adult
```
