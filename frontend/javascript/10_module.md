# JavaScript Modules

JavaScript modules allow you to split code into separate files, making it easier to maintain and reuse. This guide covers how to create and import custom modules (not built-in modules).

## 1. Creating a Module

A JavaScript module is simply a file that exports functions, objects, or variables. You can create a module using the `export` keyword.

### Example: Creating a module (math.js)

```js
// math.js - A simple module
export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export const PI = 3.14159;
```

## 2. Importing a Module

You can import a module in another JavaScript file using the `import` statement.

### Example: Importing a module (app.js)

```js
// Import specific functions
import { add, subtract, PI } from './math.js';

console.log(add(5, 3));       // Output: 8
console.log(subtract(10, 4)); // Output: 6
console.log(PI);              // Output: 3.14159
```

### Importing Everything from a Module

You can import all exports from a module using `*`.

```js
import * as MathUtils from './math.js';

console.log(MathUtils.add(2, 3));    // Output: 5
console.log(MathUtils.PI);           // Output: 3.14159
```

## 3. Default Exports

A module can have a default export, which allows importing it with any name.

### Example: Default export in `greet.js`

```js
// greet.js
export default function greet(name) {
    return `Hello, ${name}!`;
}

// export default (){
    console.log('Hi everyone')
}
```

### Importing a Default Export

```js
import greet from './greet.js';
import anynamehere from './greet.js';
// import {default as anynamehere} from './greet.js';

console.log(greet('Alice')); // Output: Hello, Alice!
anynamehere(); // Output: Hi everyone
```

## 4. Using Modules in the Browser

To use modules in the browser, include `type="module"` in your script tag.

```html
<script type="module" src="app.js"></script>
```

### Note:

- Module files must be served via a web server (e.g., `localhost`), not opened directly.
- Use `.js` file extensions in import statements.
- You can import a module inside a module&#x20;
- You can export from a file  an imported module&#x20;
