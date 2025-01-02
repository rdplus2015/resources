# CSS
- **Positioning**
- **Flexbox**
---

## Positioning

### Static Positioning (Default)
- **`position: static;`**  
  - Default position value.
  - Elements are placed in the natural document flow.`(relative to each other)`
  - Coordinates `top`, `right`, `bottom`, `left` have no effect.

### Relative Positioning
- **`position: relative;`**  
  - Positioned relative to its normal position in the document flow.
  - **Does not remove the element from the document flow.**
  - Can be shifted using `top`, `right`, `bottom`, `left`.
  - Useful for making slight adjustments and serving as a reference for absolute positioning.

```css
.relative {
  position: relative;
  top: 10px; /* Moves element 10px down */
  left: 5px; /* Moves element 5px to the right */
}
```
- example:

```html 
<div class="relative-box">
    <p>normal Content</p>
    <div class="relative-move">Relative Position </div>
</div>
```

```css
.relative-box {
    width: 200px;
    height: 150px;
    background-color: lightgreen;
}

.relative-move {
    position: relative;
    top: 10px;
    left: 10px;
    background-color: coral;
}
```
- Here, `.relative-move` is moved 10 pixels down and to the right from its normal position.


### Absolute Positioning

- **`position: absolute;`** 

  - Positioned relative to the nearest positioned ancestor (relative, absolute, fixed, or sticky), or the initial containing block if none exists.

  - **Removed from the normal document flow.** 
  - Can overlap other elements.
  - Coordinates: You can use the `top`, `right`, `bottom` and `left` properties to position the element.

```css
.absolute {
  position: absolute;
  top: 20px; /* Distance from the top of the containing block */
  right: 10px; /* Distance from the right of the containing block */
}
```

- Example 
```html 
<div class="container">
    <div class="relative-box">
        <div class="absolute-box">Position Absolue</div>
    </div>
</div>
```
```css
.container {
    position: relative;
    width: 400px;
    height: 300px;
    background-color: lightgrey;
}

.relative-box {
    position: relative;
    width: 200px;
    height: 150px;
    background-color: lightblue;
}

.absolute-box {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 100px;
    height: 50px;
    background-color: coral;
}
```
- In this example, `.absolute-box` is positioned relative to `.relative-box`, which allows for `specific placement.`


### Fixed Positioning

- **`position: fixed;`**
  - Positioned relative to the viewport.
  - Stays in the same place when the page is scrolled.
  - Useful for sticky headers, footers, or sidebars.

```css
.fixed {
  position: fixed;
  bottom: 0; /* Sticks to the bottom of the viewport */
  right: 0; /* Sticks to the right of the viewport */
}
```

### Sticky Positioning

- **`position: sticky;`**
  - Toggles between relative and fixed based on scroll position.
  - Sticks in place when a specified scroll position is reached.

```css
.sticky {
  position: sticky;
  top: 0; /* Sticks to the top of its container */
}
```

- **Coordinate Properties**
  - `top`,  `right `,  `bottom`,  `left`
       Used with relative, absolute, fixed, and sticky positioning to specify offsets.

### Z-Index

- **`z-index`**
  - Specifies the stack order of positioned elements.
  - Higher values are displayed in front of lower values.
  - Works only on positioned elements (relative, absolute, fixed, or sticky).

```css
.z-index-example {
  position: absolute;
  z-index: 10; /* Higher value means closer to the viewer */
}
```
### Box-sizing
- **`box-sizing: border-box:`** Element width includes padding and border
  - Example: Width set to 50% + 40px (padding/border) will not exceed 50%

### Float (Old Layout Method)
- **Often replaced by Flexbox and Grid in modern layouts.*** 

## Flexbox 
### **Basic Concepts**

- **Flex Container:** The parent element with `display: flex;`. It enables flex context for all direct children (flex items).
- **Flex Item:** The direct children of a flex container.

### **Flex Container Properties**
- **`display`**
  - `flex`: Defines a flex container.
  - `inline-flex`: Defines an inline flex container.

- **`flex-direction`**
  - `row`: Default. Items are placed in a row (left to right).
  - `row-reverse`: Items are placed in a row (right to left).
  - `column`: Items are placed in a column (top to bottom).
  - `column-reverse`: Items are placed in a column (bottom to top).

- **`flex-wrap`**
  - `nowrap`: Default. All items will be on one line.
  - `wrap`: Items will wrap onto multiple lines.
  - `wrap-reverse`: Items will wrap onto multiple lines in reverse order.

- **`justify-content`**
  - `flex-start`: Default. Items are aligned to the start of the container.
  - `flex-end`: Items are aligned to the end of the container.
  - `center`: Items are centered in the container.
  - `space-between`: Items are evenly distributed; the first item is at the start, and the last item is at the end.
  - `space-around`: Items are evenly distributed with equal space around them.
  - `space-evenly`: Items are distributed with equal space between them.

- **`align-items`**
  - `stretch`: Default. Items stretch to fill the container.
  - `flex-start`: Items are aligned to the start of the container.
  - `flex-end`: Items are aligned to the end of the container.
  - `center`: Items are centered along the cross-axis.
  - `baseline`: Items are aligned based on their text baseline.

- **`align-content`**
  - `stretch`: Default. Lines stretch to take up remaining space.
  - `flex-start`: Lines are packed to the start of the container.
  - `flex-end`: Lines are packed to the end of the container.
  - `center`: Lines are centered in the container.
  - `space-between`: Lines are evenly distributed; the first line is at the start, and the last line is at the end.
  - `space-around`: Lines are evenly distributed with equal space around them.
  - `space-evenly`: Lines are distributed with equal space between them.

### **Flex Item Properties**
- **`order`**
  - Defines the order of the items. Lower values are displayed first.
  - Default: `0`

- **`flex-grow`**
  - Defines how much a flex item should grow relative to the rest.
  - Default: `0` (item does not grow)

- **`flex-shrink`**
  - Defines how much a flex item should shrink relative to the rest.
  - Default: `1` (item can shrink)

- **`flex-basis`**
  - Defines the initial size of a flex item before space is distributed.
  - Can be a length (e.g., `20%`, `100px`) or `auto`.
  - Default: `auto`

- **`align-self`**
  - Allows the default alignment (or the one specified by `align-items`) to be overridden for individual flex items.
  - Default: `auto` (inherits from `align-items`)
  - Options: `auto`, `flex-start`, `flex-end`, `center`, `baseline`, `stretch`.

- **`flex` (Shorthand)**
  - `flex-grow flex-shrink flex-basis`
  - Example: `flex: 1 0 auto;`

### **Example Layout**

```css
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  align-content: flex-start;
}

.item {
  flex: 1 1 200px; /* Grow, shrink, basis */
  order: 1;
  align-self: flex-end;
}
```

