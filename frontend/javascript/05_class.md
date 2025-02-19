# Prototypes and Classes

## Understanding Prototypes

In JavaScript, every object has an internal property called `[[Prototype]]`, which is a reference to another object. This forms a chain called the prototype chain. When you access a property or method on an object, JavaScript looks up the prototype chain to find it.

- **String > String.prototype > Object.prototype**

For example, strings have their own methods, but they also inherit methods from `String.prototype`, which in turn inherits from `Object.prototype`.

### Example:
```javascript
let str = "Hello";
console.log(str.toUpperCase()); // Method from String.prototype
```

### System of Inheritance in JavaScript

1. **Prototype Functions**: 
   - Prototypes in JavaScript are themselves objects that can have their own methods and properties.
   - The type of a prototype is `function`.

2. **Static Methods and Properties**: 
   - Defined using the `static` keyword.
   - These are available on the class itself and not on instances of the class.

3. **Extending Classes**:
   - JavaScript allows you to create classes that extend other classes using the `extends` keyword.
   - This enables inheritance, allowing the child class to use properties and methods from the parent class.

4. **Overriding Methods**:
   - Child classes can override methods of parent classes to provide specific implementations.

5. **Super Keyword**:
   - Used to call the constructor of the parent class.
   - Can also be used to call parent class methods.

6. **Private Properties**:
   - Can be defined using `#` before the property name.
   - Access to private properties is typically done through getters and setters.

---

## Step 6: Classes in JavaScript

### 1. Defining a Class

Classes are blueprints for creating objects with predefined properties and methods. You can define a class using the `class` keyword.

```javascript
class Person {
    constructor(name, age) {
        this.name = name; // Property
        this.age = age;   // Property
    }

    // Method
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}

// Creating an object
const person1 = new Person("Alice", 30);
person1.greet(); // Hello, my name is Alice and I am 30 years old.
```

### 2. Methods and Properties

Properties define the characteristics of a class, while methods define the behaviors. You can access and modify properties like so:

```javascript
person1.name = "Charlie";
console.log(person1.name); // Charlie
```

### 3. Inheritance

Inheritance allows a class to inherit properties and methods from another class using the `extends` keyword.

```javascript
// Parent class
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a noise.`);
    }
}

// Child class
class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}

const animal = new Animal("Creature");
animal.speak(); // Creature makes a noise.

const dog = new Dog("Rex");
dog.speak(); // Rex barks.
```

### 4. Getters and Setters

Getters and setters allow you to control access to properties and perform additional logic when getting or setting a property.

```javascript
class Circle {
    constructor(radius) {
        this.radius = radius;
    }

    // Getter
    get diameter() {
        return this.radius * 2;
    }

    // Setter
    set diameter(value) {
        this.radius = value / 2;
    }
}

const circle = new Circle(10);
console.log("Diameter:", circle.diameter); // 20
circle.diameter = 50;
console.log("New radius:", circle.radius); // 25
