# Control Structures

Control structures allow making decisions or repeating actions based on certain conditions.

## 1. Conditions: `if`, `else`, `else if`

The `if` statement executes a block of code if a condition is true. You can use `else` or `else if` for other cases.

```javascript
let age = 20;

if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}

let hour = 15;

if (hour < 12) {
    console.log("Good morning!");
} else if (hour < 18) {
    console.log("Good afternoon!");
} else {
    console.log("Good evening!");
}
```

## 2. `switch` Statement

The `switch` statement is useful for comparing a variable to multiple possible values.

```javascript
let day = "Tuesday";

switch (day) {
    case "Monday":
        console.log("Start of the week.");
        break;
    case "Tuesday":
    case "Wednesday":
        console.log("Middle of the week.");
        break;
    case "Friday":
        console.log("Almost the weekend!");
        break;
    default:
        console.log("Unknown day.");
}
```

## 3. Loops: `for`, `while`, `do...while`

### `for` Loop

Used to repeat a block of code a specific number of times.

```javascript
for (let i = 1; i <= 5; i++) {
    console.log("Iteration number:", i);
}
```
### `for...in` loop

The `for in` statement allows you to iterate over enumerable elements. It will allow you to retrieve the keys of an array or the properties of an object.

```javascript
const object = { a: 1, b: 2, c: 3 };

for (const property in object) {
  console.log(property) // will alternately display: a, b, c
  console.log(object[property]) // access to the values 
}
```

### `for...of` Loop

The `for...of` loop allows iterating over elements of iterable objects (like arrays, strings, sets, or maps). It provides a simple way to access values directly.

```javascript
const fruits = ["apple", "banana", "orange"];

for (const fruit of fruits) {
    console.log(fruit);
}
// Output:
// apple
// banana
// orange
```

### `while` Loop

Repeats as long as a condition is true.

```javascript
let counter = 1;

while (counter <= 3) {
    console.log("Counter:", counter);
    counter++;
}
```

### `do...while` Loop

Executes at least once, then checks the condition.

```javascript
let x = 1;

do {
    console.log("Value of x:", x);
    x++;
} while (x <= 3);
```

