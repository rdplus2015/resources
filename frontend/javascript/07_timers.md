# Asynchronous Function in JavaScript: Using Timers

JavaScript has an **asynchronous** side, meaning it can execute multiple tasks at the same time without blocking the rest of the program's execution. This is made possible with functions like **`setTimeout`** and **`setInterval`**.

## 1. `setTimeout`: Delay Before Code Execution

- **Purpose**: Sets a delay before executing a block of code.
- **Syntax**: 
    ```javascript
    setTimeout(callback, delay)
    ```
    - `callback`: The function to execute after the delay.
    - `delay`: The time in milliseconds before executing the callback.

### Example 1:

```javascript
setTimeout(() => {
    console.log('Executed after 2 seconds');
}, 2000);
```

### Example 2

```javascript
console.log("Start");

for (let i = 0; i < 5; i++) {
    setTimeout(() => {
        console.log("i =", i);
    }, 1000);
}

console.log("End");
```

### Example 3

```javascript
function countdown(n) {
  if (n === 0) {
    console.log(" Go !");
    return;
  } else {
    console.log(n); // <-- Display here
    setTimeout(() => {
      countdown(n - 1); // Continue after 1 second
    }, 1000); // Shorter delay for testing
  }
}

countdown(5); // Start the countdown from 5
```

-   **Problem**: Using **`setTimeout`** can sometimes lead to **callback hell** (nested callbacks), making the code harder to maintain.
    
-   **Solution**: Use **promises** to handle asynchronous functions more effectively without nesting multiple callbacks.


## 2.  `setInterval`: Repeated Execution at Regular Intervals

-   **Purpose**: Executes a task at regular time intervals.
-   **Syntax**:

```javascript
setInterval(callback, interval)
```
-   `callback`: The function to execute after each interval.
-   `interval`: The time in milliseconds between each execution.

```javascript
function countdown(n) {
    const t = setInterval(() => {
        n--;
        console.log(n);
        if (n === 0) {
            clearInterval(t); // Stop the countdown
        }
    }, 1000);
}

countdown(5);
```
`clearInterval()` allows you to cancel an ongoing **`setInterval`**. It takes the timer ID returned by `setInterval` as a parameter.

## Key Principles of Timers in JavaScript

- **Asynchronous**: `setTimeout` and `setInterval` do not block the program’s execution. They allow tasks to be **put aside** to be executed later or at regular intervals.
-   **Event Queue**: The code inside `setTimeout` or `setInterval` is **put on hold** until the program finishes executing the main code. Even with a delay of 0 milliseconds, the code won’t be executed until the main program is complete.

There are other techniques to handle asynchrony without blocking execution, such as: **Promises**, **Async/Await**, **Events** (e.g. a click event that triggers a callback), **Asynchronous API calls** via `fetch`