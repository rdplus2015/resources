# Variables and Data Types

### Declaring Variables with `var`, `let`, and `const`

```javascript
// Using var (old method, should be avoided today)
var age = 25;

// Using let (recommended for variables that can change)
let name = "Alice";

// Using const (for constants or fixed values)
const PI = 3.14;
```

### Scope of Variables

Variables declared with `var` have a functional scope, meaning they are accessible throughout the function where they are declared, even outside a block (if, for, etc.). In comparison, `let` and `const` have block scope, meaning they are only accessible within the block `{ ... }` where they were declared.

```javascript
if (true) {
    var x = 10; // Accessible outside the block
    let y = 20; // Accessible only within the block
}

console.log(x); // 10
console.log(y); // Error: y is not defined
```

### Hoisting with `var`

Variables declared with `var` are "hoisted" to the top of their scope, but without their initial value. This can lead to unexpected behavior.

```javascript
console.log(a); // undefined (not an error, but surprising)
var a = 5;

console.log(b); // Error: b is not defined
let b = 10;
```

With `var`, the declaration is hoisted, but the initialization is not, which can be confusing.

### Redeclaration Issues

A `var` variable can be declared multiple times in the same scope without an error, which can lead to hard-to-detect bugs. With `let` and `const`, this generates an error.

```javascript
var name = "Alice";
var name = "Bob"; // No error, but this can be problematic

let firstName = "Alice";
let firstName = "Bob"; // Error: already declared
```

### Why Use `let` and `const`?

- `let`: Used for variables that can change (block scope, predictable behavior).
- `const`: Used for constants or values that do not change (enhances readability and reliability).

**General Rule:**

- Use `const` by default.
- Use `let` only if the value needs to be modified.

### Constants with Primitive Types

For primitive types like `number`, `string`, or `boolean`, the value is truly fixed and cannot be modified or reassigned.

```javascript
const x = 5;
x = 10; // Error: Assignment to constant variable

const message = "Hello";
// message = "Hi"; // Error
```

### Constants with Objects or Arrays

For objects and arrays, the reference (the location where the object is stored in memory) is fixed, but the contents of the object or array can change.

```javascript
const user = { name: "Alice", age: 30 };

// Modify a property
user.age = 31; // No error
console.log(user); // { name: "Alice", age: 31 }

// Reassign the object
// user = { name: "Bob" }; // Error: Assignment to constant variable
```

Example with an array:

```javascript
const numbers = [1, 2, 3];

// Add an element
numbers.push(4);
console.log(numbers); // [1, 2, 3, 4]

// Modify an element
numbers[0] = 10;
console.log(numbers); // [10, 2, 3, 4]

// Reassign the array
// numbers = [5, 6]; // Error: Assignment to constant variable
```

### Constants in Calculations

A constant can be used in a calculation, but its value itself does not change.

```javascript
const rate = 0.2;
let amount = 100;

let tax = amount * rate; // The constant `rate` is used in a calculation
console.log(tax); // 20

// rate = 0.25; // Error: Assignment to constant variable
```

### Common Data Types

```javascript
// String (text)
let message = "Hello!";

// Number (numbers)
let year = 2024;
let temperature = -5.5;

// Boolean (logical values)
let isActive = true;
let isEmpty = false;

// Null (no value)
let nothing = null;

// Undefined (not defined)
let unknown;

// Object (complex data)
let user = {
    name: "Alice",
    age: 30
};

// Array (arrays)
let colors = ["red", "green", "blue"];
```

## Operators

### Arithmetic Operators

These operators allow for calculations:

```javascript
let a = 10;
let b = 3;

console.log("Addition:", a + b); // 13
console.log("Subtraction:", a - b); // 7
console.log("Multiplication:", a * b); // 30
console.log("Division:", a / b); // 3.333...
console.log("Modulo (remainder):", a % b); // 1
```

### Comparison Operators (== vs ===)

These operators compare two values and return `true` or `false`:

```javascript
let x = 5;
let y = 10;

console.log("x equal to y:", x == y); // false
console.log("x not equal to y:", x != y); // true
console.log("x strictly equal to y:", x === y); // false
console.log("x strictly not equal to y:", x !== y); // true
console.log("x greater than y:", x > y); // false
console.log("x less than or equal to y:", x <= y); // true
```

**Note:**

- `==` (loose equality) compares values after type conversion.

```javascript
console.log(5 == "5"); // true ("5" is converted to number)
console.log(true == 1); // true (true is converted to 1)
console.log(false == 0); // true (false is converted to 0)
console.log(null == undefined); // true
```

- `===` (strict equality) compares both values and types.

```javascript
console.log(5 === "5"); // false
console.log(true === 1); // false
console.log(false === 0); // false
console.log(null === undefined); // false
```

### String Comparison

```javascript
console.log("hello" == "hello"); // true
console.log("hello" === "hello"); // true
console.log("hello" == "Hello"); // false
console.log("42" === 42); // false
```

### Logical Operators

These operators combine multiple conditions:

```javascript
let a = true;
let b = false;

console.log("Logical AND (&&):", a && b); // false
console.log("Logical OR (||):", a || b); // true
console.log("Logical NOT (!):", !a); // false
```

### Assignment Operators

They assign and modify a value:

```javascript
let num = 10;

num += 5; // Equivalent to: num = num + 5
console.log("After +=:", num); // 15

num *= 2; // Equivalent to: num = num * 2
console.log("After *=:", num); // 30
```

## String Manipulation

### Concatenation

Using `+` or template literals `${}` to join strings.

```javascript
let a = "Hello";
let b = "world";
let message1 = a + " " + b; // Concatenation with space
console.log(message1); // Displays: Hello world

let message2 = `${a} ${b}`; // Modern syntax
console.log(message2); // Displays: Hello world
```

### Newline

Using `\n` (classic) or template literals for multiline strings.

```javascript
let text1 = "Line 1\nLine 2";
console.log(text1);

let text2 = `Line 1
Line 2`;
console.log(text2);
```

### Single and Double Quotes

```javascript
let singleQuotes = 'This is a string with single quotes.';
console.log(singleQuotes);

let doubleQuotes = "This is a string with double quotes.";
console.log(doubleQuotes);

let mixedQuotes = 'He said: "Hello everyone"';
console.log(mixedQuotes);
```

### Escaping Characters

```javascript
let escapedText = "He said: \"It's a beautiful day.\"";
console.log(escapedText);

let specialChars = "Line 1\nLine 2\tTabulation\\Backslash";
console.log(specialChars);
```

