# DOM

- Browsers contain a JavaScript engine.
- Place the JS file at the bottom of the HTML page or use the `defer` attribute to prevent JavaScript from being loaded before the DOM and avoid page slowdown.
- Add a `type="module"` to support imports.

## Window

- Property: provides information about the window and the current page.
- Window can be used to pass global variables from one script to another.
- By convention, to access an attribute, we use `window.attribute`, but functions can be called directly.

```js
console.log(this)
console.log(window)
console.log(window.location) // get the entered URL
```

## DOM 

-  Document: represents the HTML structure.
- Usually, we do not write `window` before `document`.

## QuerySelector and QuerySelectorAll

- querySelector: takes a CSS selector and returns an element on which we can perform operations.
- querySelectorAll: takes a selector and returns a NodeList.
- We can use the forEach loop or access a single element by [index], but we can't use all array methods
- because NodeList does not have Array as its prototype.

```js
const divElement = document.querySelector('div')
const liElement = document.querySelectorAll('li')

console.log(liElement[0]) // a single element by index
liElement.forEach(element => {
  console.log(element) // loop through elements
})
```

## Exploring properties

```javascript

const ul = document.querySelector('ul')
console.log(
  ul.nodeName,        // Gets the name of the node
  ul.innerHTML,       // Gets the HTML structure of the element
  ul.innerText,       // Returns visible text, removes spaces and HTML code
  ul.textContent      // Returns all text content including hidden parts and space
)

// Note
ul.innerHTML = 'hello' // this structure can be modified
```

## Manipulating attributes

```javascript
const ul = document.querySelector('ul')
ul.setAttribute('hidden','hidden') // set an attribute and its value
ul.removeAttribute('hidden')       // remove an attribute
ul.getAttribute('class')           // get the class
ul.classList                       // manipulate a list of classes
ul.classList.remove('red')        // removes class "red" but retains others
ul.classList.add('red')           // adds class "red" if not already present
ul.classList.toggle('red')        // removes if found, adds if not found
```
## Modify the style of an element

```javascript
const li = document.createElement('li')
console.log(li.style)             // object with all CSS properties, empty if not defined
li.style.color = 'red'           // set the color (camelCase required)

// The .style property only reflects styles defined directly inline (via JS or in HTML), not those applied by CSS classes or style sheets.
getComputedStyle(li).color // get applied styles

// To get the styles actually applied to an element, even those inherited from a CSS class, you must use:
getComputedStyle(li).getPropertyValue('color') // get applied styles (even style in a css stylesheet)
```

## Add an element to the DOM

```javascript
const newli = document.createElement('li')  // create li
newli.innerHTML = 'Bonjour le gens'         // set content
document.querySelector('ul').append(newli)  // add li at the end
document.querySelector('ul').prepend(newli) // add li at the beginning

/* Note: When an element is added to the DOM, the same reference is used.
If found, it is removed and added where requested. An element cannot be in multiple places. */

ul.insertAdjacentElement('beforeend', li) // add an element before or after another element
```

## Manipulate children

- It is possible to select child elements by nesting querySelector calls, but this approach can keep references to elements that were removed from the DOM, which may lead to unexpected behavior or bugs.
- By using `.children`, we get a live HTMLCollection — meaning it always reflects the current state of the DOM in real time.

```javascript

const ul = document.querySelector('ul')
window.a = ul.children         // returns an HTMLCollection of elements
window.a = ul.childNodes       // returns a NodeList including spaces and non-HTML nodes

console.log(
  ul.firstChild,              // first node (can be a space)
  ul.firstElementChild,       // first HTML element
  ul.childElementCount,       // number of child elements
  ul.children.length          // same as childElementCount
)
```

##  Select the parent
```javascript
const li = document.querySelector('ul li')
console.log(
  li.parentNode,             // parent node
  li.parentElement,          // parent element
  li.nextSibling,            // next node (can be text)
  li.nextElementSibling,     // next HTML element
  li.previousElementSibling  // previous HTML element
)
```

##  Clone an element
```javascript
ul.append(li.cloneNode(true)) // clone the element and all its children
console.log(
  ul.contains(li)             // check if ul contains li
)
```