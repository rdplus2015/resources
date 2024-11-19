# Loops in Java

Loops allow you to repeat a block of code multiple times based on a condition. Java provides several types of loops, each serving a specific use case.

## For Loop

The `for` loop is typically used when you know in advance how many times you want to repeat a block of code.

#### Syntax:

```java
for (initialization; condition; update) {
    // Code to be executed
}
```
#### Key Notes:

-   **Start iterations from 0**: In Java, arrays are 0-indexed, meaning the first element is at index 0. It’s common to start a loop at 0 when iterating over an array or a list.
    
-   **Prefer starting at 0** unless there’s a specific reason not to. This makes array traversal straightforward and consistent.

### Example
```java
int[] numbers = {10, 20, 30};
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}
```

## Foreach Loop
```java
for (Variable type: collection) {
        // Instructions to execute for each element
        }
        
/* Example */ 

int[] numbers = {1, 2, 3, 4, 5};

for (int number: numbers) {
        System.out.println(number);
}
```
- **Type**: The type of elements in the collection or array.
- **variable**: A temporary variable that represents each element at each iteration.
- **collection**: The collection or table to browse.

## While Loop

The `while` loop repeats a block of code as long as a given condition is true.

#### Syntax:
```java
while (condition) {
    // Code to be executed
}
```
#### Example: Random Number Guessing Game
```java
Random random = new Random();
int target = random.nextInt(10);  // Random number between 0 and 9
int guess = -1;

while (guess != target) {
    guess = userInput();  // Assume this method gets input from the user
    System.out.println("Guess: " + guess);
}
System.out.println("You guessed it!");
```

### Special Forms of `while`:

-   **`while(true)`**: This creates an infinite loop, which will continue until explicitly stopped by a `break` statement.

#### Example: Infinite Loop with Break

```java
while (true) {
    int num = random.nextInt(10);
    System.out.println(num);
    if (num == 5) {
        break;  // Exit the loop when the number is 5
    }
}
```
#### Control Flow Keywords:

-   **`break`**: Exits the loop immediately.
-   **`continue`**: Skips the current iteration and continues with the next one.

#### Example with `continue`:

```java 
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;  // Skip even numbers
    }
    System.out.println(i);  // Print only odd numbers
}
```

## Nested Loops

You can use loops inside other loops. This is particularly useful for working with multi-dimensional arrays or performing more complex iterations.

#### Example:
```java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++) {
        System.out.println("i: " + i + ", j: " + j);
    }
}
```
## Do-While Loop

The `do-while` loop is similar to the `while` loop, but it guarantees that the code inside the loop will be executed at least once, even if the condition is false from the start.

#### Syntax:
```java
do {
    // Code to be executed
} while (condition);
```

#### Example

```java
int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 5);
```
### Summary

-   Use **for loops** when you know the exact number of iterations, and prefer starting the counter from `0` when working with arrays.
-   Use **while loops** for indefinite iteration, especially when the number of repetitions depends on dynamic conditions.
-   **`break` and `continue`** are useful for controlling the flow within loops.
-   **Nested loops** allow you to iterate over complex structures like multi-dimensional arrays.
-   Use **do-while** loops when you need to ensure the loop body runs at least once.
