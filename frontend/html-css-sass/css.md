# CSS 
## Inheritance of Properties

- Property values can be inherited from parent elements.
- Example: If the `body` is set to red, all children elements will inherit the red color.

## Selector Priority and Specificity

- Default styles are applied in CSS unless overridden.
- When there are conflicting styles, the more specific rule takes precedence:
  - **Specificity**: ID > Class > Element
  - Example: An ID selector overrides a class selector, which in turn overrides an element selector.

### Tips:

- Override general rules with more specific ones.
- Use a simple depth level for readability and performance.
- A simple depth level makes it easy to overwrite a ruler because the latter is less specific

## CSS Selectors

### basic selectors 
```css
p{
  /* Targets all p elements */     
}
```
### Descendant and Child Selectors

```css
table h2 {
    /* Targets all h2 elements that are descendants of a table */
}

tbody > h2 {
    /* Targets all h2 elements that are direct children of tbody */
}
```

### Adjacent and General Sibling Selectors

```css
h2 + p {
    /* Targets all p elements that are immediate siblings of h2 */
}

h2 ~ p {
    /* Targets all p elements that are siblings of h2 */
}
```

### Attribute Selectors

```css
input[type='text'] {
    margin: 15px;
}
```

### Pseudo-classes

```css 
a:hover {
    /* Styles when a link is hovered */
}

div:first-child {
    /* Targets the first child element of a div */
    color: red;
}

tr:nth-child(2n) {
    /* Applies styles to every second tr element */
    background-color: #f0f0f0;
}

p:first-of-type {
    /* Targets the first p element of its type */
}
```

### Pseudo-Elements Overview

Pseudo-elements in CSS allow you to style specific parts of an element's content, such as the first letter, line, or content before/after the element. They are identified by a double colon (`::`).

### Commonly Used Pseudo-Elements

- **`::before`**  
  Inserts content before the content of an element.
  ```css
  p::before {
    content: "Note: ";
    color: red;
  }
  ```

- **`::after`**  
  Inserts content after the content of an element.
  ```css
  p::after {
    content: " (end)";
    color: blue;
  }
  ```

- **`::first-line`**  
  Styles the first line of an element's text.
  ```css
  p::first-line {
    font-weight: bold;
  }
  ```

- **`::first-letter`**  
  Styles the first letter of an element's text.
  ```css
  p::first-letter {
    font-size: 200%;
    color: green;
  }
  ```

- **`::selection`**  
  Styles the portion of text that is selected by the user.
  ```css
  ::selection {
    background: yellow;
    color: black;
  }
  ```

## Box Model
### Display Types

- **`display: block:`** Takes the full available width, cannot sit next to another element.

- **`display: inline:`** Only takes the width of its content, You cannot manually specify a width and height. the rules will not apply except image

- **`display: inline-block:`** Mix of block and inline; allows specifying width and height.

### Dimensions

1. **Single Value**
- Applies a margin to all sides `(top, right, bottom, and left)` of an element.

2. **Two Values**
- **First value**: Applies to the `top` and `bottom` margins.
- **Second value**: Applies to the `left `and `right` margins.

3. **Three Values**
- **First value**: Applies to the `top` margin.
- **Second value**: Applies to the `left` and `right` margins.
- **Third value**: Applies to the `bottom` margin.

4. **Four Values**
- **First value**: Applies to the `top` margin.
- **Second value**: Applies to the `right` margin.
- **Third value**: Applies to the `bottom` margin.
- **Fourth value** : Applies to the `left` margin.

```css
       margin: top right bottom left;
```

### Margin Collapsing

- When two adjacent elements have margins, the larger margin is used.

- If parent elements have no margin, the first child element's margin will overflow into the parent.

#### Margins on Inline Elements

- Margins top and bottom are not applied to inline or inline-block elements; only left and right margins apply.

### Spaces in HTML

- Inline and inline-block elements are affected by spaces in HTML.

## Text Styling

### Colors and Sizes

- **Color**: color: `rgba(x, y, z, a)`, `#hexadecimal`, `inherit`
- **Size**: `font-size`
- **Line Spacing**: `line-height`
- **Letter Spacing**: `letter-spacing`
- **Font Family**: `font-family`
- **Text Alignment**: `text-align: right`, `left`, `center`, `justify` (for inline or inline-block elements)

### Text Decoration and Transformation

- **`overflow-wrap`**: `break-word`(limited support) / **Alternative**: `hyphens` with `&shy;`
- **Text Decoration**: `text-decoration`
- **Font Weight**: `font-weight`
- **Font Style**: `font-style`
- **Text Indentation**: `text-indent`
- **Text Transformation**: `text-transform`

### Units of Measurement

- **Media** : media: screen, print, etc.

### Absolute Units

- **px**: 1 pixel of the screen

### Relative Units

- **%**: Relative to the container's width (not the screen)

- **em**: Relative to the font size of the current element or parent. **1em** = current font size
Ideal for margins, depending on the element or parent.

- **rem**: Relative to the font size defined in the body
- **vh** and **vw** : Relative to the viewport's height and width



### Custom Fonts with `@font-face`

The `@font-face` rule allows you to load custom fonts on your website. You can specify the font files and define how they should be used in your CSS.

### Example
```css
@font-face {
    font-family: 'MyCustomFont';
    src: url('mycustomfont.woff2') format('woff2'),
         url('mycustomfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-display: swap; /* optional: with a shorter block period.*/
}
```
### Google Fonts Best Practices

- Preconnect: Use the `rel="preconnect"` attribute to establish early connections to the Google Fonts servers, speeding up the font loading.

- Preload: Consider preloading the font files to reduce loading times

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

<!-- Manually Adding font-display to Google Fonts -->
 <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">

```
#### Using Local Fonts Before Google Fonts
```css
@font-face {
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    src: local('Roboto'), url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap') format('woff2');
}
```

## Background 

### Combined Background Properties Example

```css
.background-example {
  background-color: #f0f0f0; /*Accepts color values like `hex`, `rgb`, `rgba`, `hsl`, and color names. */

  background-image: url('image.jpg'); /* Image as background. Use url() to specify the image path. */

  background-repeat: no-repeat; /* Values: repeat, repeat-x, repeat-y, no-repeat, space, round. */

  background-size: cover; /* Image scales to cover entire area. Values: auto, cover, contain, specific sizes (e.g., 100px, 50%). */

  background-position: center; /* Values: left, center, right, top, bottom, or specific positions (10px 20px */

  background-attachment: fixed; /* Values: scroll, fixed, local. */

  background-origin: padding-box; /* Values: padding-box, border-box, content-box. */

  background-clip: border-box; /* Values: border-box, padding-box, content-box, text. */
}
```

### Multiple Backgrounds

```css

.multiple-backgrounds-example {
  background-image: url('image1.jpg'), url('image2.png');
  background-position: top left, bottom right;
  background-repeat: no-repeat;
}
```

### Shorthand Background Property

- Order: 
  - `background-color`
  - `background-image` 
  - `background-repeat` 
  - `background-attachment` 
  - `background-position/background-size` 
  - `background-origin` 
  - `background-clip.`

```css
.background-shorthand-example {
  background: #f0f0f0 url('image.jpg') no-repeat center/cover;
}
```

### Background Gradients
  #### Linear Gradient
  - Creates a gradient between two or more colors along a straight line.
  - Syntax: linear-gradient(direction, color-stop1, color-stop2, ...)

```css
.linear-gradient-example {
  background: linear-gradient(to right, #ff0000, #00ff00); /* Red to green */
}
```

  #### Radial Gradient
  - Creates a gradient radiating from an origin.
  - Syntax: radial-gradient(shape size at position start-color, ..., last-color).

```css
.radial-gradient-example {
  background: radial-gradient(circle, #ff0000, #00ff00); /* Circular red to green */
}
```

### CSS Variables for Backgrounds
- Define custom properties to reuse color values across backgrounds.

```css
:root {
  --primary-color: #3498db;
}

.background-variables-example {
  background-color: var(--primary-color);
}

```

### Responsive background
```css
@media (max-width: 600px) {
  .responsive-background {
    background-size: contain; /* Adjust for smaller screens */
  }
}
```

## Background Best Practices

- Optimize Images: Use optimized image formats (like WebP) and sizes to improve page loading times.
- Use SVG for Patterns: SVGs scale well and are lightweight, perfect for backgrounds.
- Combine Images and Gradients: Combine images with gradients for enhanced visual effects.
- Responsive Design: Adjust background properties for different screen sizes using media queries.


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
       - content here
## Css grid 
       - content here 

## Tips and Best Practices

- **Use Positioning Sparingly**: Overusing absolute and fixed positioning can lead to complex layouts that are hard to maintain.

- **Prefer Flexbox and Grid**: For most modern layouts, use Flexbox or Grid for easier management of responsive designs.

- **Use Relative for Position References**: When using absolute positioning, set the parent to relative to create a reference point.

- **Manage Z-Index Carefully**: Avoid arbitrarily high z-index values; instead, manage stacking context logically.

- **useful links**
  - [complete guide to flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

   - [complete guide to Css grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

   - [Flexbox Froggy](https://flexboxfroggy.com/#fr)

   - [Can i use](https://caniuse.com/)
   
   - [Autoprefixer](https://autoprefixer.github.io/)
   
   - [Fontsquirrel](https://www.fontsquirrel.com/)

   
