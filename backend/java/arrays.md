
# Java Arrays 

## Definition

An array is a container object that holds a fixed number of values of a single type. The length of an array is established when the array is created.

## Declaration

```java
// Syntax
dataType[] arrayName; // Preferred way
dataType arrayName[]; // Valid but not recommended

// Example
int[] numbers; // Preferred
int numbers[]; // Valid
```

## Initialization

```java
// Static initialization
int[] numbers = {1, 2, 3, 4, 5};

// Dynamic initialization
int[] numbers = new int[5]; // Creates an array of size 5
numbers[0] = 1; // Assigning values

// Example with other types
String[] names = new String[3]; // Array of Strings
names[0] = "Alice";
```

## Accessing Elements

```java
int firstNumber = numbers[0]; // Accessing first element
System.out.println(numbers[1]); // Prints second element
```

```java
int length = numbers.length; // Gets the length of the array
```

## Looping Through Arrays

```java

// Using for loop
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

// Using enhanced for loop (for-each)
for (int num : numbers) {
    System.out.println(num);
}
```

- **Difference Between Loops**

    - **`For Loop`**: You have access to the index, allowing you to modify elements or know their positions.
    - **`For-each Loop`**: Simpler and more readable, but you don’t have access to the index. Useful for reading values without modifying them.

## Multidimensional Arrays

```java

// Declaration and Initialization
int[][] matrix = new int[3][3]; // 2D array (3x3)

matrix[0][1] = 100; // method 1

int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};  // method 2 

// Accessing elements
int element = matrix[1][2]; // Accessing element in the second row, third column
```

## Arrays vs. ArrayLists

- `Arrays` are fixed-size and can hold primitive types and objects.
- `ArrayLists` are resizable and provide more built-in methods for manipulation.

## Copying Arrays

- **Apart from `Arrays.copyOf()`, you can also use:**

```java
int[] newArray = new int[original.length];
System.arraycopy(original, 0, newArray, 0, original.length);
```

## Updating an Array

Arrays in Java have a fixed size and cannot be updated directly. To "update" an array, you can create a new array and copy the elements from the old one.

```java

int[] newNumbers = new int[numbers.length];
// Copy elements from numbers to newNumbers
for (int i = 0; i < numbers.length; i++) {
    newNumbers[i] = numbers[i];
}
// Now you can update newNumbers
newNumbers[0] = 10; // Updates the first element
```

## Reference Trap

In Java, when you copy an array, you only copy the reference. Modifying one array will also affect the other.

```java
int[] array1 = {1, 2, 3};
int[] array2 = array1; // Reference copy

array2[0] = 10; // Modifies array2
System.out.println(Arrays.toString(array1)); // Prints [10, 2, 3]
```

- **Using Arrays.copyOf**

To avoid the reference trap, you can use Arrays.copyOf() to create a copy of an array.

```java
int[] array3 = Arrays.copyOf(array1, array1.length);
array3[0] = 20; // Only modifies array3
System.out.println(Arrays.toString(array1)); // Prints [10, 2, 3]
System.out.println(Arrays.toString(array3)); // Prints [20, 2, 3]
```

### Example

```java

import java.util.Arrays;

public class ArrayExample {
    public static void main(String[] args) {
        // Declare and initialize an array
        int[] numbers = {10, 20, 30, 40, 50};

        // Print all elements
        for (int number : numbers) {
            System.out.println(number);
        }

        // Sort the array
        Arrays.sort(numbers);

        // Print sorted array
        System.out.println("Sorted Array:");
        for (int number : numbers) {
            System.out.println(number);
        }
    }
}
```

## Best Practices

-   **Use ArrayLists** for dynamic data that may change in size.
-   **Always check** the length of an array before accessing its elements.
-   **Document your code** when using arrays, especially if you use multidimensional arrays or complex data structures.

### Note
- **If you try to access an index that is out of bounds (less than 0 or greater than or equal to the length of the array), you will get an `ArrayIndexOutOfBoundsException`.**

- **Common Array Methods (Java 8+)**
  - **`Sorting`: Arrays.sort(array);**
  - **`Searching`: Arrays.binarySearch(array, key);**
  - **`Copying`: Arrays.copyOf(original, newLength);**
  - **`Equality`: Arrays.equals(array1, array2);**