# Error Handling Tutorial

## Introduction
In JavaScript, handling errors effectively is crucial to building robust and reliable applications. This guide will cover the primary methods for error handling in JavaScript, including using the `throw` statement, custom error classes, and the `try...catch` block.

## Throwing Errors

### Using `throw` to Generate Errors
The `throw` statement allows you to create your own errors. You can throw an error when a function receives invalid parameters or when an unexpected situation occurs.

#### Example:
```javascript
function setNotes(notes) {
    if (!Array.isArray(notes)) {
        throw new Error('Notes must be an array');
    }
    this.notes = notes;
}
```
The `Error` object is constructed with a string describing the reason for the error. You can also pass an object with a `cause` property to provide more information about the error.

### Example with `cause`:
```javascript
try {
    // Code that may throw errors
} catch (e) {
    throw new Error("Action failed", { cause: e });
}
```

## Using `try...catch` to Handle Errors

### Basic Syntax
The `try...catch` block is used to capture and handle errors that occur during code execution.

#### Syntax:
```javascript
try {
  // Code that might throw an error
  let result = riskyOperation();
  console.log(result);
} catch (error) {
  // Code executed in case of an error
  console.error("An error occurred:", error.message);
} finally {
  // Code that runs regardless of an error
  console.log("Finally block executed.");
}
```

### Key Points:
- **`try`**: Contains code that may throw an error.
- **`catch`**: Captures and handles the error.
- **`finally`**: (Optional) Executes code after `try` and `catch`, regardless of an error.

## Custom Error Classes

You can create custom error classes to define and identify specific types of errors.

### Example of a Custom Error Class:
```javascript
class PromptError extends Error {
    constructor(originalPrompt) {
        super("Invalid input", { cause: originalPrompt });
    }
}
```

### Using the Custom Error Class:
```javascript
function promptInt(msg) {
    const n = prompt(msg) * 1;
    if (Number.isNaN(n)) {
        throw new PromptError("The number is not valid", { cause: msg });
    }
    return n;
}
```

## Best Practices
1. **Always capture errors**: Prevent unhandled errors from stopping your program.
2. **Provide clear error messages**: Help developers and users understand what went wrong.
3. **Re-throw errors with context**: Use the `cause` property to maintain original error context.
4. **Use custom error classes**: For better error identification and handling.

By following these practices, you can handle errors in JavaScript efficiently, leading to more stable and maintainable code.

