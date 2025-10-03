# Exceptions in Java

## Introduction

Exceptions allow you to handle runtime errors in order to prevent the program from crashing abruptly and to make the code more robust.

## Types of errors

There are three main categories:

### Error

Serious errors that cause the program to stop (e.g. `OutOfMemoryError`).

- Usually not handled.

```java
public class Ex3_OutOfMemoryError {
    public static void main(String[] args) {
        // Illustration: tries to allocate an enormous amount of memory
        // Commented to avoid crashing your machine.
        // int size = Integer.MAX_VALUE;
        // int[] big = new int[size]; // -> OutOfMemoryError
        System.out.println("Conceptual example of an Error (OutOfMemoryError).");
    }
}
```

### Exception (checked)

Errors that **must** be handled.  
If you write a method that can throw a checked exception, you must:

- Either catch it with `try/catch`
- Or declare it with `throws` in the method signature.

Checked exceptions: warn about predictable issues related to external resources (files, network, databases).

> Example: a file may not exist, and the compiler can anticipate this → so it forces you to handle **IOException.**

```java
import java.io.FileReader;
import java.io.IOException;

public class ExempleChecked {
    public static void main(String[] args) {
        try {
            FileReader fr = new FileReader("file.txt"); // IOException possible
        } catch (IOException e) {
            System.out.println("Error: file not found");
        }
    }
}
```

Here, **`IOException`** is a _checked exception_.  
If you don’t add `try/catch` or `throws`, **the code will not compile**.

### RuntimeException (unchecked)

**Definition**: These are exceptions **not checked at compile time**, inheriting from `RuntimeException`.  
The compiler does not force you to use `try/catch` or `throws`. But if they occur at runtime, the program will crash if nothing is done.

Unchecked exceptions: relate to programming logic errors or invalid user input (not external resources).

```java
public class ExempleUnchecked {
    public static void main(String[] args) {
        int x = 10 / 0; // ArithmeticException
        System.out.println("End of program"); // never reached
    }
}
```

## Exception hierarchy

```
Throwable
├── Error
└── Exception
    ├── Checked Exceptions
    └── RuntimeException (Unchecked)
```

## Handling exceptions

### try / catch

```java
try {
    int x = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### Multiple `catch`: one per exception type

- Ideal if each exception has a specific handling strategy.
- If you only display a generic message, it’s better to use a single `catch`.

```java
import java.util.InputMismatchException;
import java.util.Scanner;

public class Ex5_MultiCatchChain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter an integer: ");
            int n = sc.nextInt();           // may throw InputMismatchException
            int res = 10 / (n - n);         // if n == 0 -> division by 0 -> ArithmeticException
            System.out.println(res);
        } catch (InputMismatchException e) {
            System.out.println("Invalid input (not an integer).");
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic error: " + e.getMessage());
        } catch (RuntimeException e) {
            System.out.println("Other runtime error: " + e);
        } finally {
            sc.close();
        }
    }
}
```

### Multi-catch: one `catch` for several exceptions

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Ex6_MultiCatch {
    public static void main(String[] args) {
        try {
            // Two different exception sources just for the example
            String content = Files.readString(Path.of("missing.txt")); // IOException (checked)
            int n = Integer.parseInt("abc");                           // NumberFormatException (unchecked)
            System.out.println(content + " " + n);
        } catch (IOException | NumberFormatException e) {
            System.out.println("Problem detected: " + e.getClass().getSimpleName() + " -> " + e.getMessage());
        }
    }
}
```

### **Parent exception**: catch a group of exceptions

- Ideal if there is no specific handling for each exception type.
- This approach is more general but makes code less readable.

```java
public class Ex7_CatchParent {
    public static void main(String[] args) {
        try {
            String s = null;
            System.out.println(s.length()); // NullPointerException (unchecked)
        } catch (Exception e) { // parent for many exceptions
            System.out.println("Exception caught by parent: " + e.getClass().getSimpleName());
        }
    }
}
```

## Creating your own exceptions

```java
class InsufficientBalanceException extends Exception {
    public InsufficientBalanceException(String message) {
        super(message); // Passes the received message to the parent class (Exception) which holds getMessage().
    }
}

class InsufficientBalanceException extends Exception {
    // Constructor without parameters
    public InsufficientBalanceException() {
        super(); // calls Exception’s constructor
    }

    // Override getMessage()
    @Override
    public String getMessage() {
        return "Insufficient balance to complete the operation.";
    }
}
```

- Override `getMessage()` (as shown).
- Or call `super("default message")` in your constructor.

```java
public class Ex8_CustomChecked {
    private static double balance = 100.0;

    public static void withdraw(double amount) throws InsufficientBalanceException {
        if (amount > balance) {
            throw new InsufficientBalanceException("Balance " + balance + " insufficient to withdraw " + amount);
        }
        balance -= amount;
    }

    public static void main(String[] args) {
        try {
            withdraw(150); // will throw custom exception
        } catch (InsufficientBalanceException e) {
            System.out.println("Business error: " + e.getMessage());
        }
    }
}
```

- **`throws`**: declares in the signature that a method may throw an exception, but the exception is not handled in that method. The JVM passes it up to the caller.
- **`throw`**: when you write `throw new Exception("...");`, the exception is created and immediately thrown. Execution jumps to the nearest `catch` block.
- **`try / catch`**:

  - Used to **wrap risky code** (`try`) and **catch exceptions** (`catch`).
  - If an exception occurs inside `try`, execution immediately jumps to the corresponding `catch`.

### Note

When you create **your own exception**, you decide whether it will be:

- a **checked exception** (extends `Exception`) → `try-catch` or `throws` required,
- an **unchecked exception** (extends `RuntimeException`) → not required.

#### Example with native exceptions

```java
import java.io.*;

public class ExemplePropagation {
    // Method that may cause an IOException
    public void readFile() throws IOException {
        FileReader fr = new FileReader("file.txt");
        BufferedReader br = new BufferedReader(fr);
        System.out.println(br.readLine());
        br.close();
    }

    // Propagation of the exception to the caller
    public void processFile() throws IOException {
        readFile();  // IOException may propagate here
    }

    // Here the exception is finally caught
    public static void main(String[] args) {
        ExemplePropagation ex = new ExemplePropagation();
        try {
            ex.processFile(); // IOException may reach here
        } catch (IOException e) {
            System.out.println("Caught error: " + e.getMessage());
        }
    }
}
```

- `readFile()` may throw an `IOException`.
- Since it doesn’t catch it, it **propagates** with `throws IOException`.
- `processFile()` also propagates it.
- Finally, `main()` catches the exception.

## Best practices

- Use specific exceptions rather than generic `Exception`.
- `try/catch` should **never** be used in business logic classes. Handle them in the main program.
- Create custom exceptions for business rules.
- If you **handle locally** → use `try/catch` (no need for `throws`).
- If you **don’t handle at all** → use `throws` to propagate upward.
- If you **handle and rethrow** → use `try/catch` **and** `throws` together.
