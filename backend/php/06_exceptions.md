# Managing Exceptions in PHP

## Introduction

Exception handling in PHP provides a structured way to handle runtime errors. Instead of using error codes or messages scattered throughout your code, exceptions allow you to centralize error handling and make your code more readable and maintainable.

---

## Table of Contents

1. [Basic Concepts](#basic-concepts)
2. [The `try`, `catch`, and `finally` Blocks](#the-try-catch-and-finally-blocks)
3. [Throwing Exceptions](#throwing-exceptions)
4. [Exception Hierarchy in PHP](#exception-hierarchy-in-php)
5. [Creating Custom Exceptions](#creating-custom-exceptions)
6. [Best Practices](#best-practices)
7. [Common Use Cases](#common-use-cases)
8. [Useful Built-in Exception Classes](#useful-built-in-exception-classes)
9. [Conclusion](#conclusion)

---

## Basic Concepts

- **Exception**: An object representing an error or unexpected behavior.
- **Throwing**: Raising an exception using the `throw` keyword.
- **Catching**: Handling the exception using a `catch` block.
- **Try Block**: The block of code that might throw an exception.
- **Finally Block**: A block that always executes, whether or not an exception is thrown.

---

## The `try`, `catch`, and `finally` Blocks

### Syntax

```php
try {
    // Code that may throw an exception
} catch (ExceptionType $e) {
    // Code to handle the exception
} finally {
    // Code that always runs
}
```

### Example

```php
try {
    $divisor = 0;
    if ($divisor === 0) {
        throw new Exception("Cannot divide by zero.");
    }
    echo 10 / $divisor;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} finally {
    echo " - Execution complete.";
}
```

---

## Throwing Exceptions

You can throw an exception using the `throw` keyword followed by an instance of the `Exception` class.

```php
throw new Exception("Something went wrong!");
```

You can also specify a custom error code:

```php
throw new Exception("File not found", 404);
```

---

## Exception Hierarchy in PHP

All exceptions in PHP must extend the `Throwable` interface.

```
Throwable
├── Exception
│   └── LogicException
│   └── RuntimeException
│   └── InvalidArgumentException
└── Error
    └── TypeError
    └── ParseError
```

- `Exception`: Base class for all user exceptions.
- `Error`: Used for fatal errors like syntax issues or type mismatches.

---

## Creating Custom Exceptions

### Basic Example

```php
class MyCustomException extends Exception {}

try {
    throw new MyCustomException("Custom error occurred");
} catch (MyCustomException $e) {
    echo "Caught custom exception: " . $e->getMessage();
}
```

### With Additional Properties

```php
class ApiException extends Exception {
    private $statusCode;

    public function __construct($message, $statusCode) {
        parent::__construct($message);
        $this->statusCode = $statusCode;
    }

    public function getStatusCode() {
        return $this->statusCode;
    }
}
```

---

## Best Practices

- **Catch specific exceptions first**: Order matters. Catch more specific exceptions before general ones.
- **Use meaningful messages**: Help with debugging and logging.
- **Don't suppress exceptions silently**: Always log or rethrow.
- **Avoid using exceptions for normal flow control**.
- **Use `finally` for cleanup tasks**: e.g., closing DB connections, releasing locks.

---

## Common Use Cases

### File Handling

```php
if (!file_exists("data.txt")) {
    throw new Exception("File not found");
}
```

### Database Operations

```php
try {
    $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
} catch (PDOException $e) {
    echo "Database connection failed: " . $e->getMessage();
}
```

### Input Validation

```php
function validateAge($age) {
    if ($age < 0) {
        throw new InvalidArgumentException("Age cannot be negative");
    }
    return true;
}
```

---

## Useful Built-in Exception Classes

- `Exception`
- `InvalidArgumentException`
- `RuntimeException`
- `LengthException`
- `OutOfBoundsException`
- `LogicException`
- `DomainException`
- `PDOException`
- `TypeError`
- `ErrorException`

---

## Conclusion

Exception handling in PHP is essential for building robust and maintainable applications. By using try-catch blocks, custom exceptions, and adhering to best practices, you can create more stable and secure software.

---

# Custom Exceptions in a PHP CRUD Application

## Introduction

In a well-structured CRUD (Create, Read, Update, Delete) application, exception handling plays a key role. Instead of relying on generic `Exception` classes, you can define custom exceptions to reflect specific issues like validation failures, resource not found errors, or database issues. This results in cleaner, more expressive, and easier-to-maintain code.

---

## Why Use Custom Exceptions?

- **Improved readability**: Easier to understand the nature of the error.
- **Centralized error handling**: Catch and handle specific exceptions cleanly.
- **Better debugging**: Custom exceptions carry precise messages and metadata.
- **Separation of concerns**: Business logic and error management are well-separated.

---

##  Step 1: Define a Base Exception

```php
// AppException.php
class AppException extends Exception {}
```

---

##  Step 2: Define Specific Exceptions

```php
// NotFoundException.php
class NotFoundException extends AppException {}

// ValidationException.php
class ValidationException extends AppException {
    private array $errors;

    public function __construct($message = "Validation failed", array $errors = []) {
        parent::__construct($message);
        $this->errors = $errors;
    }

    public function getErrors(): array {
        return $this->errors;
    }
}

// UnauthorizedException.php
class UnauthorizedException extends AppException {}

// DatabaseException.php
class DatabaseException extends AppException {}
```

---

##  Step 3: Use Exceptions in CRUD Operations

### Example: `UserService.php`

```php
require_once "NotFoundException.php";
require_once "ValidationException.php";
require_once "DatabaseException.php";

class UserService {
    public function findUserById(int $id): array {
        // Simulated database result
        $user = $this->mockDatabaseFind($id);
        if (!$user) {
            throw new NotFoundException("User with ID $id not found.");
        }
        return $user;
    }

    public function createUser(array $data): bool {
        $errors = [];

        if (empty($data['email'])) {
            $errors[] = "Email is required.";
        }
        if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
            $errors[] = "Email is invalid.";
        }

        if (!empty($errors)) {
            throw new ValidationException("User creation failed", $errors);
        }

        // Simulate database save
        if (!$this->mockDatabaseSave($data)) {
            throw new DatabaseException("Failed to save user.");
        }

        return true;
    }

    private function mockDatabaseFind(int $id): ?array {
        return $id === 1 ? ['id' => 1, 'email' => 'test@example.com'] : null;
    }

    private function mockDatabaseSave(array $data): bool {
        return true;
    }
}
```

---

##  Step 4: Handle Exceptions in a Controller or Frontend

```php
require_once "UserService.php";

$service = new UserService();

try {
    $user = $service->findUserById(2);
    echo "User: " . $user['email'];
} catch (NotFoundException $e) {
    echo "404 Not Found: " . $e->getMessage();
} catch (ValidationException $e) {
    echo "Validation errors: " . implode(", ", $e->getErrors());
} catch (AppException $e) {
    echo "App Error: " . $e->getMessage();
}
```

---

## Best Practices

- **Throw early, catch late**: Throw exceptions where the error occurs, but handle them at the top level (controller).
- **Group related exceptions**: Use a parent class like `AppException`.
- **Add context**: Pass extra data like error codes or error arrays to your exceptions.
- **Keep it readable**: Don’t overcomplicate your exception hierarchy.

---

## Use Cases Recap

| Exception Type       | When to Use                                      |
|----------------------|--------------------------------------------------|
| `NotFoundException`  | When a resource is not found (e.g. user, post)   |
| `ValidationException`| When input data fails business rules             |
| `UnauthorizedException`| When access is denied or unauthenticated      |
| `DatabaseException`  | For low-level DB issues (e.g. connection failure)|
| `AppException`       | Catch-all for application-specific errors        |

---

## Conclusion

Custom exceptions improve clarity, reduce boilerplate error-checking code, and help build more robust and maintainable applications. In a CRUD system, separating exceptions by type is a best practice that will scale well as your application grows.
