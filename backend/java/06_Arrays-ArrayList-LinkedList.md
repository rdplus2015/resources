
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
String[] infos = new String[] {"Tires", "Keys"}; // new String[] {"tires", "keys"} if you want to pass it like an arg.

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

## Copying Arrays

- **Using Arrays.copyOf**

To avoid the reference trap, you can use Arrays.copyOf() to create a copy of an array.

```java
int[] array1 = {1, 2, 3, 4, 5};
int[] array3 = Arrays.copyOf(array1, array1.length);
array3[0] = 20; // Only modifies array3
System.out.println(Arrays.toString(array1)); // Prints [1, 2, 3, 4, 5]
System.out.println(Arrays.toString(array3)); // Prints [20, 2, 3, 4, 5]
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
  - **`toString`: method in Java can be used to display an array as a string, providing a human-readable representation of the array's contents.**
--- 

# ArrayList in Java

In Java, an **ArrayList** is a dynamic data structure that is part of the `java.util` package. Unlike regular arrays, an `ArrayList` can change its size dynamically, meaning it can grow or shrink automatically based on additions and deletions of elements. It's very useful when you want to store a list of items and don't know the size in advance.

## Key Features of an `ArrayList`:
- It is **resizable**.
- Elements can be **accessed by their index**, similar to arrays.
- It can only contain objects (primitive types like `int`, `char`, etc., must be wrapped in their object versions, such as `Integer` for `int`).
- It **maintains insertion order**.

## Basic Usage Example:

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create an ArrayList that stores strings
        ArrayList<String> fruits = new ArrayList<>();

        // Add elements
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        // Access an element by index
        System.out.println("First fruit: " + fruits.get(0)); // Apple

        // Size of the ArrayList
        System.out.println("Size of the list: " + fruits.size()); // 3

        // Remove an element
        fruits.remove("Banana");

        // Display all elements
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

## Summary of Key Methods

| Method | Description                                                            |
|--------|------------------------------------------------------------------------|
| `add(E e)` | Adds an element to the end of the `ArrayList`.                         |
| `get(int index)` | Returns the element at the specified index.                            |
| `set(int index, E element)` | Replaces the element at the specified position with the specified element. |
| `remove(int index)` | Removes the element at the specified index.                            |
| `remove(Object o)` | Removes the first occurrence of the specified object from the list.    |
| `size()` | Returns the number of elements in the `ArrayList`.                     |
| `clear()` | Removes all elements from the `ArrayList`.                             |
| `contains(Object o)` | Checks if the `ArrayList` contains a specific object.                  |
| `isEmpty()` | Checks if the `ArrayList` is empty (returns `true` or `false`).        |
| `indexOf()`     | allows you to find the first occurrence of an element in a collection. |


The **ArrayList** is a very flexible and simple-to-use structure for storing and manipulating dynamic collections of objects in Java.

# ArrayList vs LinkedList in Java

In Java, `ArrayList` and `LinkedList` are both implementations of the `List` interface, but they are optimized for different use cases. Here is a comparison to help you decide which to use.

## ArrayList
- **Storage**: Uses a dynamic array to store elements, allowing fast access by index.
- **Element Access**: Very fast for accessing elements by their position (O(1)), as elements are stored contiguously in memory.
- **Adding Elements at the End**: Efficient (amortized O(1)), but resizing the array when it's full requires copying all elements (O(n)).
- **Adding/Removing Elements in the Middle**: Slow (O(n)) as elements need to be shifted to maintain order.
- **Memory Usage**: More memory-efficient compared to `LinkedList` since there’s no overhead for pointers between elements.

## LinkedList
- **Storage**: Uses a doubly linked list where each element points to the previous and the next elements.
- **Element Access**: Slower (O(n)) because the list must be traversed from the beginning or end to reach an element.
- **Adding/Removing Elements at the Beginning or Middle**: Fast (O(1)) since only pointers need to be adjusted.
- **Adding/Removing Elements at the End**: Relatively fast (O(1)) for doubly linked lists.
- **Memory Usage**: More memory-intensive due to the overhead of storing two pointers (previous and next) for each element.

## Key Differences Summary

| Feature                            | ArrayList                 | LinkedList                |
|------------------------------------|---------------------------|---------------------------|
| **Index Access**                   | Fast (O(1))               | Slow (O(n))               |
| **Insertion/Removal at End**       | Fast (amortized O(1))     | Fast (O(1))               |
| **Insertion/Removal at Beginning/Middle** | Slow (O(n))       | Fast (O(1))               |
| **Memory Usage**                   | More efficient            | More memory-intensive     |

## Choosing Between ArrayList and LinkedList
- Use **ArrayList** if you need frequent access by index or if you mostly add elements at the end.
- Use **LinkedList** if you frequently add or remove elements at the beginning or middle of the list, and fast access by index is not crucial.

## Example of Using LinkedList

Below is an example of using `LinkedList` in Java to add, remove, and access elements.

```java
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<>();

        // Adding elements to the LinkedList
        linkedList.add("Apple");
        linkedList.add("Banana");
        linkedList.add("Cherry");

        // Adding an element at the beginning
        linkedList.addFirst("Mango");

        // Adding an element at the end
        linkedList.addLast("Orange");

        // Inserting an element at a specific position
        linkedList.add(2, "Peach");

        // Removing elements
        linkedList.remove("Banana"); // Remove by value
        linkedList.remove(3);        // Remove by index
        linkedList.removeFirst();    // Remove first element
        linkedList.removeLast();     // Remove last element

        // Accessing elements
        String firstElement = linkedList.getFirst();
        String lastElement = linkedList.getLast();
        String secondElement = linkedList.get(1);

        // Display the LinkedList
        System.out.println("LinkedList: " + linkedList);
        System.out.println("First Element: " + firstElement);
        System.out.println("Second Element: " + secondElement);
        System.out.println("Last Element: " + lastElement);
    }
}
