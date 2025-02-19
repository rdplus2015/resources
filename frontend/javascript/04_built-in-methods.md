# JavaScript Methods: A Comprehensive Guide

## 1. **Array Methods**

### a. Element Manipulation
- **`push()`**: Adds one or more elements to the end of an array.
```javascript
let fruits = ["apple", "banana"];
fruits.push("orange");
console.log(fruits); // ["apple", "banana", "orange"]
```

- **`pop()`**: Removes the last element from an array.
```javascript
fruits.pop();
console.log(fruits); // ["apple", "banana"]
```

- **`shift()`**: Removes the first element from an array.
```javascript
fruits.shift();
console.log(fruits); // ["banana"]
```

- **`unshift()`**: Adds one or more elements to the beginning of an array.
```javascript
fruits.unshift("strawberry");
console.log(fruits); // ["strawberry", "banana"]
```

### b. Sorting and Reversing
- **`sort()`**: Sorts the elements of an array (default lexicographical order).
```javascript
let numbers = [10, 3, 25, 1];
numbers.sort();
console.log(numbers); // [1, 10, 25, 3]
```
*Usage with a comparison function for numeric sorting:*
```javascript
numbers.sort((a, b) => a - b); // Ascending order
console.log(numbers); // [1, 3, 10, 25]
```

- **`reverse()`**: Reverses the order of the elements in an array.
```javascript
numbers.reverse();
console.log(numbers); // [25, 10, 3, 1]
```

### c. Transformations
- **`join()`**: Joins all elements of an array into a string.
```javascript
let words = ["Hello", "world"];
let sentence = words.join(" ");
console.log(sentence); // "Hello world"
```

- **`slice()`**: Returns a shallow copy of a portion of an array.
```javascript
let fruits = ["apple", "banana", "orange", "kiwi"];
console.log(fruits.slice(1, 3)); // ["banana", "orange"]
```

- **`splice()`**: Adds, removes, or replaces elements in an array.
```javascript
fruits.splice(1, 1, "mango");
console.log(fruits); // ["apple", "mango", "orange", "kiwi"]
```

##  **Accessing Elements**
- **`at()`**: Access an element by index (supports negative indices for reverse lookup).
```javascript
let numbers = [10, 20, 30, 40];
console.log(numbers.at(-1)); // 40
console.log(numbers.at(1));  // 20
```

##  **Filtering and Finding Elements**
- **`filter()`**: Creates a new array with all elements that pass a test.
```javascript
let nums = [10, 20, 30, 40, 50];
let filtered = nums.filter(n => n > 25);
console.log(filtered); // [30, 40, 50]
```

- **`find()`**: Returns the first element that passes a test.
```javascript
let found = nums.find(n => n > 25);
console.log(found); // 30
```

- **`findIndex()`**: Returns the index of the first element that passes a test.
```javascript
let index = nums.findIndex(n => n > 25);
console.log(index); // 2
```

- **`findLast()`**: Returns the last element that passes a test.
```javascript
let last = nums.findLast(n => n > 25);
console.log(last); // 50
```

##  **Transformation Methods**
- **`map()`**: Creates a new array by applying a function to each element.
```javascript
let squared = nums.map(n => n * n);
console.log(squared); // [100, 400, 900, 1600, 2500]
```

- **`reduce()`**: Reduces an array to a single value.
```javascript
let sum = nums.reduce((acc, curr) => acc + curr, 0);
console.log(sum); // 150
```

- **`Array.from()`**: Creates an array from an iterable object.
```javascript
let str = "hello";
let arr = Array.from(str);
console.log(arr); // ["h", "e", "l", "l", "o"]
```

###  **Checking for Inclusion**
- **`includes()`**: Checks if an array contains a specified element.
```javascript
console.log(nums.includes(20)); // true
console.log(nums.includes(100)); // false
```

###  **Extracting a Portion of an Array**
- **`slice()`**: Returns a shallow copy of a portion of an array.
```javascript
console.log(nums.slice(1, 3)); // [20, 30]
```

---

## 2. **String Methods**

### a. String Manipulation
- **`split()`**: Splits a string into an array of substrings.
```javascript
let phrase = "Hello world";
let words = phrase.split(" ");
console.log(words); // ["Hello", "world"]
```

- **`concat()`**: Concatenates two or more strings.
```javascript
let greeting = "Hello";
let name = "Alice";
console.log(greeting.concat(", ", name)); // "Hello, Alice"
```

### b. Search
- **`indexOf()`**: Returns the index of the first occurrence of a specified value.
```javascript
console.log("Hello world".indexOf("world")); // 6
```

- **`includes()`**: Checks if a string contains a specified value.
```javascript
console.log("Hello world".includes("world")); // true
```

---

## 3. **Number Methods**

- **`toFixed()`**: Formats a number with a fixed number of decimals.
```javascript
let num = 42.678;
console.log(num.toFixed(2)); // "42.68"
```

- **`parseInt()`**: Parses a string and returns an integer.
```javascript
let number = parseInt("42");
console.log(number); // 42
```

- **`parseFloat()`**: Parses a string and returns a floating point number.
```javascript
let number = parseFloat("42.5");
console.log(number); // 42.5
```

---

## 4. **Object Methods**

### a. Retrieving Keys and Values
- **`Object.keys()`**: Returns an array of an object's keys.
```javascript
let user = { name: "Alice", age: 30 };
console.log(Object.keys(user)); // ["name", "age"]
```

- **`Object.values()`**: Returns an array of an object's values.
```javascript
console.log(Object.values(user)); // ["Alice", 30]
```

- **`Object.entries()`**: Returns an array of key-value pairs.
```javascript
console.log(Object.entries(user)); // [["name", "Alice"], ["age", 30]]
```

### b. Copying Objects
- **`Object.assign()`**: Copies the values of all enumerable own properties from one or more source objects to a target object.
```javascript
let target = {};
let source = { a: 1, b: 2 };
Object.assign(target, source);
console.log(target); // { a: 1, b: 2 }
```

- **`Object.freeze()`**: Freezes an object, preventing new properties from being added to it and existing properties from being removed or changed.
```javascript
let obj = { a: 1 };
Object.freeze(obj);
obj.a = 2; // Error in strict mode
console.log(obj.a); // 1
```

---

## 5. **Math Methods**

- **`Math.random()`**: Returns a random number between 0 (inclusive) and 1 (exclusive).
```javascript
let random = Math.random();
console.log(random);
```

- **`Math.round()`**: Rounds a number to the nearest integer.
```javascript
console.log(Math.round(4.6)); // 5
```

- **`Math.max()`** and **`Math.min()`**: Returns the largest or smallest number from a list of numbers.
```javascript
console.log(Math.max(1, 2, 3)); // 3
console.log(Math.min(1, 2, 3)); // 1
```

---

## 6. **User Interaction**

- **`prompt()`**: Displays a dialog box that prompts the user for input (browser only).
```javascript
let name = prompt("What is your name?");
console.log(`Hello, ${name}!`);
```

- **`alert()`**: Displays an alert box with a message.
```javascript
alert("This is an alert!");
```

- **`confirm()`**: Displays a dialog box with a message and OK and Cancel buttons.
```javascript
let response = confirm("Do you want to continue?");
console.log(response); // true or false
```

---

## 7. **Loops and Iterations**

### a. `forEach()`
Applies a function to each element in an array.
```javascript
let numbers = [1, 2, 3];
numbers.forEach((number) => {
    console.log(number * 2);
});
```

### b. `map()`
Returns a new array with the results of a function applied to each element.
```javascript
let doubles = numbers.map((number) => number * 2);
console.log(doubles); // [2, 4, 6]
```

---

This file groups the most common and useful methods in JavaScript. If you want to explore a method further or test some of them, let me know!
