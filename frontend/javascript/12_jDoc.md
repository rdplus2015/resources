# JSDoc

JSDoc is a markup language used to annotate JavaScript code. It provides a standardized way to document your code, making it easier for developers to understand and maintain. This guide will walk you through the basics of JSDoc, how to use it, and some best practices.


## What is JSDoc?

JSDoc is a documentation generator for JavaScript. It uses special comments in your code to generate HTML documentation. These comments are written in a specific format that JSDoc can parse and convert into readable documentation.

## Why Use JSDoc?

- **Improved Code Readability**: JSDoc comments make it easier for other developers (or your future self) to understand your code.
- **Automated Documentation**: Generate HTML documentation automatically from your code comments.
- **IDE Support**: Many IDEs and editors use JSDoc comments to provide better code completion, type checking, and inline documentation.
- **Type Checking**: JSDoc can be used to specify types, which can help catch errors early in the development process.

## Getting Started with JSDoc

To start using JSDoc, you need to install the JSDoc tool. You can install it globally using npm:

```bash
npm install -g jsdoc
```
Once installed, you can generate documentation by running:
```bash
jsdoc path/to/your/code
```

This will generate an `out` directory containing the HTML documentation.

## Basic Syntax

JSDoc comments are written using `/** ... */` blocks. Each comment block should describe a single code element (e.g., a function, class, or variable).

```javascript
/**
 * This is a JSDoc comment.
 * It can span multiple lines.
 */
function myFunction() {
    // Function implementation
}
```

## Common JSDoc Tags

JSDoc uses tags to provide additional information about the code. Here are some of the most commonly used tags:

-   `@param`: Describes a function parameter.
    
-   `@returns` or `@return`: Describes the return value of a function.
    
-   `@type`: Specifies the type of a variable.
    
-   `@typedef`: Defines a custom type.
    
-   `@class`: Indicates that a function is a constructor for a class.
    
-   `@module`: Defines a module.
    
-   `@description`: Provides a description of the code element.
    
-   `@example`: Provides an example of how to use the code element.
    

## Documenting Functions

Here’s an example of how to document a function using JSDoc:

```javascript
/**
 * Add your description 
 * @param {number} a 
 * @param {String} b 
 * @returns {number} 
 */
function add(a, b) {
    console.log(a);
    console.log(b);
    return a ;
}


/**
 * @return {{id: number, titl: string}}  give a type to a return (object in this case)
 * @return {array<string>}  give a type to a return (array in this case and type of elements inside)
 * @return {string[]} samething then the previously about arrays 
 * @return @return {{id: number, titl: string}} example : return a array of objects 
 */
function fetchPost(){
    // post
}
const a = fetchPost  // a will have auto completion 



/**
 * @typedef {Object} Post 
 * @property {number} id 
 * @property {string} title  can addcomment here 
 */

/**
 * @return {() => number} renvois une fonction contenant un number
 *  @return {(d: number, title: string) => Post} // add comment here 
 */
function fetchPost(){
    // post
}
const a = fetchPost  // a will have auto completion 

```

## Documenting Classes

JSDoc can also be used to document classes and their methods:

```javascript
/**
 * Represents a book.
 * @class
 * @property {string} title  
 */
class Book {
    /**
     * Create a book.
     * @param {string} title - The title of the book.
     * @param {string} author - The author of the book.
     */
    constructor(title, author) {
        this.title = title;
        this.author = author;
    }

    /**
     * Get the title of the book.
     * @returns {string} The title of the book.
     */
    getTitle() {
        return this.title;
    }
}

/**
 *  @type {string[]} on type la variable pour indiquéqu'il est de type tableau
 */
const b = []
```
Generating Documentation

To generate documentation from your JSDoc comments, run the following command:
```bash
jsdoc path/to/your/code
```
