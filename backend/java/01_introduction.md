
# Java

## How Java Works: Overview of Compilation and Execution
Java is a platform-independent, high-level programming language. Its execution involves the following key steps:
### **1. Writing Code**
- **Source Code**: Java programs are written in `.java` files using human-readable syntax.
### **2. Compilation**
- **Java Compiler (`javac`)**: The `.java` file is compiled into **bytecode** (.class files), which is an intermediate, platform-independent representation of the code.
- **Error Checking**: During compilation, syntax errors and some logical errors are detected.
### **3. Execution**
- **Java Virtual Machine (JVM)**: Executes the bytecode on a specific machine.
    - The JVM translates bytecode into **machine code** using a **Just-In-Time (JIT)** compiler.
    - The JVM is platform-specific, but bytecode is universal.
### **4. Platform Independence**
- Java achieves its "Write Once, Run Anywhere" promise because:
    - The **bytecode** is the same regardless of the operating system.
    - The JVM adapts the bytecode to the specific OS and hardware.
---

## Keywords

- **Java SE** (Standard Edition): The core platform for general-purpose applications.
- **Java EE** (Enterprise Edition): Extensions for enterprise applications.
- **JVM** (Java Virtual Machine): Executes Java bytecode on any platform.
- **JDK** (Java Development Kit): Includes JRE + development tools.
- **JRE** (Java Runtime Environment): Executes Java applications.

## Java Versions

- **OpenJDK**: The open-source implementation of Java SE, free to use.
- **Oracle JDK**: Oracle's version, including commercial features.
- **Java Corretto**: Amazon's free, open-source distribution of the JDK, optimized for AWS.
- **Latest LTS Versions**: Java 11, Java 17.
- **Java 22 & others**: Available in OpenJDK, offering new language features.

## Installation

### Windows/Linux/Mac

1. **Download OpenJDK**: 
   - Visit [AdoptOpenJDK](https://adoptopenjdk.net/) or [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html).
   - Visit Amazon for  [Amazon corretto 17](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/generic-linux-install.html)
   - Download the appropriate installer.

2. **Install**:
   - Follow the installation instructions.
   - Set the `JAVA_HOME` environment variable.
   - Add Java to your system's PATH.

### Verify Installation

```bash
java -version
```

## Hello world
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

## Explanation

### The `main` Method

The `main` method is a special method in Java that serves as the entry point for any standalone Java application. It is where the program begins execution.

- **`public`**: The method must be accessible from outside its class, hence it is `public`.
- **`static`**: The method is static, meaning it belongs to the class rather than instances of the class. This is necessary because the method is called by the JVM without creating an instance of the class.
- **`void`**: The method does not return any value.
- **`main`**: This is the name of the method, which is predefined by the JVM as the entry point of the program.
- **`String[] args`**: The method takes a single argument: an array of `String` objects. This array can hold any command-line arguments that are passed when the program is run.

### Why is the `main` Method Important?

The `main` method is crucial because it is the starting point of every Java application. Without it, the Java Virtual Machine (JVM) wouldn't know where to begin executing the program, and the application wouldn't run.

## Java Essentials: Quotes, Comments, and New Lines

## Quotes

- **Double Quotes (`"`)**: For `String` literals.
```java
  String message = "Hello, World!";
```

- **Single Quotes (`'`)**: For `char` literals.
```java
char letter = 'A';
```
- **Incorrect Usage**:
```java
String message = 'Hello, World!'; // Error: incompatible types
char letter = "A"; // Error: incompatible types
char emptyChar = ''; // Error: empty character literal
```
## Comments

-   **Single-Line Comments**:
```java
// Comment
int number = 10; // Inline comment
```
- **Multi-Line Comments**:
```java 
/*
 * Multi-line comment
 */
int number = 10;
```
- **Documentation Comments**:
```java
/**
 * Documentation comment
 */
public class Example {
    // Code
}
```
## New Lines

-   **Using `\n`**: Adds a new line in strings.
```java
System.out.println("Hello,\nWorld!");
```
- **Using `System.out.println()`**: Adds a new line automatically.
```java
System.out.println("Hello, World!");
```

# Java API: Key Concepts

## What is an API in Java?

The Java API (Application Programming Interface) is a collection of classes, interfaces, and libraries that allow Java developers to interact with the system or an application without needing to understand its internal details. This simplifies application development by reusing already written functionalities.

## Components of the Java API

The Java API is divided into several components:

- **Classes**: They represent objects and provide reusable functionality. For example, the `String` class for manipulating text.
  
- **Interfaces**: These define methods without implementing them. Classes that implement an interface provide their own implementation. For example, the `List` interface is implemented by `ArrayList` and `LinkedList`.

- **Methods**: Blocks of code that perform a specific action. For example, the `add()` method in the `ArrayList` class adds an element to the list.

- **Packages**: Packages organize classes and interfaces into logical groups. For example:
  - `java.lang`: Core classes like `String`, `Math`, `Object`.
  - `java.util`: Utility classes like `ArrayList`, `HashMap`, `Date`.
  - `java.io`: Classes for input/output operations like `File`, `InputStream`.

## Why use the Java API?

- **Reusability**: You don’t need to reinvent the wheel for common functionalities like handling collections or file manipulation.
- **Portability**: Java is designed to be portable. By using the API, you ensure your code is compatible across platforms that support Java.
- **Standardization**: The Java API follows well-established standards, making code easier to maintain and understand.

## Major Java APIs

1. **Java Standard Edition (Java SE)**: It contains the core libraries of the Java language. For example:
   - **Collections API**: To manage data structures like lists, sets, and maps (`List`, `Set`, `Map`).
   - **Streams API**: To perform operations on data streams (`InputStream`, `OutputStream`).
   - **Concurrency API**: To manage multithreading and asynchronous operations.

2. **Java Enterprise Edition (Java EE)**: Used to develop enterprise-level applications, it includes features like:
   - **Servlet API**: To handle HTTP requests in web applications.
   - **JPA (Java Persistence API)**: For database management.

3. **JavaFX API**: For building rich graphical user interfaces (GUIs).

4. **Spring Framework** (third-party API): Although not included in Java SE/EE, it is widely used for developing Java applications, providing features for dependency injection, transaction management, and more.
