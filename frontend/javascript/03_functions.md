# Functions

Functions allow us to group reusable blocks of code. We can define them, call them with parameters, and retrieve values through return statements.

## 1. Defining and Calling a Function

A function is defined using the `function` keyword:

```javascript
// Definition
function greet() {
    console.log("Hello!");
}

// Call
greet();
```

## 2. Function with Parameters

Functions can accept parameters to customize their behavior:

```javascript
function greetUser(name) {
    console.log(`Hello, ${name}!`);
}

greetUser("Alice"); // Hello, Alice!
greetUser("Bob");   // Hello, Bob!
```

## 3. Function with Return Value

We use `return` to send back a value:

```javascript
function add(a, b) {
    return a + b;
}

let result = add(5, 3);
console.log("Result:", result); // 8
```

## 4. Arrow Functions

A simplified syntax for defining functions:

```javascript
// Classic function
function multiply(x, y) {
    return x * y;
}

// Arrow function
const multiply2 = (x, y) => x * y;

console.log(multiply(2, 3));  // 6
console.log(multiply2(4, 5)); // 20
```

### Notes on Functions:

- Functions can be called before their definition due to JavaScript's hoisting, except when the function is stored in a variable.
  - Use function definitions without variables for functions intended for global use and with variables for functions used in loops or conditions.
- Functions can modify variables defined outside of their scope, but be cautious with variables sharing the same name as parameters, as the parameter will take precedence.
- Passing arrays or objects as parameters allows the function to modify the original data.
- Functions can be called without parameters and use `this`, referring to the object it belongs to.
- Arrow functions often use `this` with classes.

```javascript
// Function to calculate the area of a rectangle
function calculateArea(length, width) {
    return length * width;
}

let area = calculateArea(5, 3);
console.log("Rectangle area:", area); // 15

// Function to display a personalized message
const displayMessage = (firstName, age) => {
    console.log(`Hi ${firstName}, you are ${age} years old.`);
};

displayMessage("John", 25); // Hi John, you are 25 years old.

// Function to check if a number is even
const isEven = (number) => number % 2 === 0;

console.log("4 is even:", isEven(4)); // true
console.log("7 is even:", isEven(7)); // false
```

