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

### Margins on Inline Elements

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
    - **When to Use**:

      - *Use px when you need precise control over dimensions, like borders or small padding/margin adjustments.* 

      - *It's ideal for fine-tuning design elements where relative scaling isn’t required.*

      - **Recommending Usage**: *Avoid using px for layout purposes, as it doesn't scale well with different screen sizes and user preferences (e.g., browser zoom).*

### Relative Units

- **%**: Relative to the container's width (not the screen)

  - **When to Use**:
    - *Use % for fluid layouts where elements need to scale relative to their parent container. For example, making an image fill 50% of its container.* 
    
    - *It’s great for making layouts responsive, as it adapts to the size of the parent container.*

    - **Recommending Usage**: *% is ideal for responsive designs, particularly for widths and heights that need to adapt to the container rather than the viewport.*


- **em**: Relative to the fontsize of the current element or parent.

  - **When to Use**:
    - *Use em for spacing (e.g., margin, padding) relative to the current font size. For example, setting padding as 2em ensures it scales with the text size.* 
    
    - *It’s useful in scenarios where you want spacing or sizing to be directly proportional to text size.*

    - **Recommending Usage**: *em is useful for typography and spacing when you want elements to scale with the text, maintaining proportionate spacing.*

- **rem**: Relative to the font size defined in the body

  - **When to Use**:
    - *Use rem for consistent, global sizing that is relative to the base font size of the document. This is especially helpful for layout components like buttons, headers, and containers (particularly in typography and layout elements).* 
    
    - *It’s useful when you want consistent sizing across the entire document that can be easily adjusted by changing the root font size.*

    - **Recommending Usage**: *em is often recommended for global and consistent scaling across a website. It is particularly effective for responsive typography and layout components.*


- **vh** and **vw** : Relative to the viewport's height and width

  - **When to Use**:
    - *Use vh and vw for full-screen or viewport-based layouts. For example, a section that always takes up 100% of the viewport height would use height: 100vh;.* 
    
    - *Useful for creating full-page layouts or ensuring elements adjust with the screen size dynamically.*

    - **Recommending Usage**: *vh and vw are ideal for full-page sections, hero banners, or elements that need to scale with the viewport dimensions. Use with caution for smaller components, as it can lead to less control over element proportions.*


### Custom Fonts with `@font-face`

The `@font-face` rule allows you to load custom fonts on your website. You can specify the font files and define how they should be used in your CSS.

### Example
```css
@font-face {
    font-family: 'MyCustomFont';
    src: url('mycustomfont.woff2') format('woff2'),
         url('mycustomfont.woff') format('woff');
    font-weight: normal; /* or 400 */
    font-style: normal;  /* or italic */
    font-display: swap; /* optional: with a shorter block period.*/
}

/* case of using */
h1, h2, h3 {
  font-family: 'OpenSans', Arial, sans-serif;
}
```
#### Best Practices

- **Font Formats**: Include multiple font formats (woff2, woff, ttf, eot) to ensure compatibility across all browsers.
- **Fallback Fonts**: Always define fallback fonts in case the custom font fails to load. This is done by listing additional fonts in the `font-family` property.
- **Font Loading Optimization**: Use `font-display: swap;` to improve font loading performance. This property controls how a font is displayed while loading.

#### Performance Considerations

- **Custom Font Size**: Custom fonts can increase the size of your CSS and slow down the initial load. Use font subsetting to reduce file size or consider loading fonts asynchronously.
- **Font Weight**: Using `font-weight: bold;` without loading a bold version of the font is generally not recommended. The browser will synthesize the bold weight, which often results in lower quality compared to an actual bold font file.

### Custom Fonts with `Google Fonts`
***Best Practices***

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

### Background Best Practices

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


## **CSS Transformations, Transitions, and Animations**

## **1. Transformations**

### **Basic Properties**
- **`transform`**: Applies a transformation to an element (e.g., `rotate`, `scale`, `translate`, `skew`).
  - **`rotate(angle)`**: Rotates the element (e.g., `rotate(45deg)`).
  - **`scale(x, y)`**: Scales the element (e.g., `scale(1.5)`).
  - **`translate(x, y)`**: Moves the element (e.g., `translate(50px, 100px)`).
  - **`skew(x, y)`**: Skews the element (e.g., `skew(20deg, 10deg)`).

### **Example Usage**

```css
.image {
  width: 100px;
  height: 100px;
  transform: rotate(45deg) scale(1.2);
}
```


### **Perspective**

- **`perspective`**: Defines the perspective from which an element is viewed. The value is in pixels, and it affects the depth perception of 3D transformed elements.

  - **Syntax**: `perspective: value;`
  - **Example**: `perspective: 1000px;`

- **`perspective-origin`**: Defines the position of the viewer, allowing you to change the vanishing point for the 3D effect.
  
  - **Syntax**: `perspective-origin: x-axis y-axis;`
  - **Example**: `perspective-origin: 50% 50%;`

### **Example Usage of Perspective**

Here's how you might use the `perspective` property in a practical scenario:

```css
.container {
  perspective: 1000px;
}

.cube {
  width: 100px;
  height: 100px;
  transform-style: preserve-3d;
  transform: rotateX(45deg) rotateY(45deg);
}

.face {
  width: 100px;
  height: 100px;
  position: absolute;
  background: rgba(255, 165, 0, 0.8);
}

.front  { transform: translateZ(50px); }
.back   { transform: rotateY(180deg) translateZ(50px); }
.left   { transform: rotateY(-90deg) translateZ(50px); }
.right  { transform: rotateY(90deg) translateZ(50px); }
.top    { transform: rotateX(90deg) translateZ(50px); }
.bottom { transform: rotateX(-90deg) translateZ(50px); }
```

### **Explanation:**
- **`perspective: 1000px;`**: Sets the perspective for the `.container`, making the cube appear more or less 3D depending on the value.
- **`transform-style: preserve-3d;`**: Ensures the child elements of the `.cube` maintain their 3D position.
- **`transform` on `.cube`**: Applies a 3D rotation to the cube, so it rotates in 3D space.
- **`.face` classes**: Position the faces of the cube in 3D space using `translateZ` to move them along the z-axis.

This gives the illusion of a 3D cube that rotates in space when viewed on the screen.


## **2. Transitions**

### **Basic Properties**
- **`transition-property`**: Property to animate (e.g., `all`, `background-color`, `width`).
- **`transition-duration`**: Duration of the transition (e.g., `0.5s`).
- **`transition-timing-function`**: Speed curve of the transition (e.g., `ease`, `linear`).
- **`transition-delay`**: Delay before the transition starts.

### **Example Usage**

```css
.button {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.button:hover {
  background-color: green;
  transform: scale(1.1);
}
```

## **3. Animations**

### **Basic Properties**
- **`animation-name`**: Name of the keyframe to bind to the selector.
- **`animation-duration`**: Duration of the animation (e.g., `2s` for 2 seconds).
- **`animation-timing-function`**: Speed curve of the animation (e.g., `ease`, `linear`, `ease-in`, `ease-out`).
- **`animation-delay`**: Delay before the animation starts.
- **`animation-iteration-count`**: Number of times the animation should play (e.g., `infinite` for looping).
- **`animation-direction`**: Direction of the animation (e.g., `normal`, `reverse`, `alternate`).
- **`animation-fill-mode`**: Defines what styles are applied before/after the animation (e.g., `forwards`, `backwards`).

### **Keyframes**
Keyframes define the stages of the animation.

```css
@keyframes example {
  0% { transform: translateX(0); }
  50% { transform: translateX(100px); }
  100% { transform: translateX(0); }
}
```

### **Example Usage**

```css
.box {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 3s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
}
```

### **4. Concrete Example: Animated Button with Transformations and Transitions**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .animated-button {
      padding: 15px 30px;
      background-color: #3498db;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease, transform 0.3s ease;
      animation: pulse 2s infinite;
    }

    .animated-button:hover {
      background-color: #2980b9;
      transform: translateY(-5px) scale(1.1);
    }

    @keyframes pulse {
      0%, 100% {
        transform: scale(1);
        box-shadow: 0 0 0 rgba(52, 152, 219, 0.7);
      }
      50% {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(52, 152, 219, 0.7);
      }
    }
  </style>
</head>
<body>

<button class="animated-button">Hover Me!</button>

</body>
</html>
```

In this example:
- The button has a subtle pulse animation using keyframes.
- A transition changes the background color and scale when the button is hovered over.
- The `transform` property is used to slightly lift and enlarge the button when hovered.


## CSS grid 
       
## Basic Grid Properties

- **`grid-template-columns`**: Defines the number and size of columns.
  - Example: `grid-template-columns: 1fr 5fr 1fr;`
    - This divides the grid into 7 parts (1 + 5 + 1).

- **`grid-template-columns`**: Repeat columns.
  - Example: `grid-template-columns: repeat(2, 50%);` or `grid-template-columns: repeat(2, 1fr);`
    - This creates two equal columns.

- **`grid-template-rows`**: Defines the number and size of rows.
  - Example: `grid-template-rows: 100px 200px;`
    - Creates two rows with specified heights.

- **`grid-gap`**: Sets the space between columns and rows.
  - Example: `grid-gap: 10px;`

## Grid Item Placement

- **`grid-column-start`**: Defines where a grid item starts.
  - Example: `grid-column-start: 1;` (Starts at the first column)

- **`grid-column-end`**: Defines where a grid item ends.
  - Example: `grid-column-end: 3;` (Ends at the third column)

- **`grid-column`**: Shorthand for setting both start and end points.
  - Example: `grid-column: 1 / 2;` (Starts at column 1 and ends at column 2)

- **`grid-column`**: With `span`.
  - Example: `grid-column: 1 / span 2;` (Starts at column 1 and spans 2 columns)

- **`grid-auto-columns` / `grid-auto-rows`**: Defines sizes of implicitly created columns/rows.
  - Example: `grid-auto-columns: 1fr;` or `grid-auto-rows: minmax(100px, auto);`

## Advanced Grid Features

- **`grid-template-areas`**: Defines named grid areas for easier layout management.
  - Example:
    ```css
    grid-template-areas:
      "header header header"
      "sidebar content content"
      "footer footer footer";
    ```

- **`align-items`**: Aligns grid items along the block (column) axis.
  - Example: `align-items: center;`

- **`justify-items`**: Aligns grid items along the inline (row) axis.
  - Example: `justify-items: end;`

- **`grid-template-rows: minmax(100px, auto);`**: Ensures that rows are at least 100px but can grow to fit their content.

## Additional Notes

- **`grid-column` Shorthand**: 
  - Example: `grid-column: 1 / 2;` (Point of departure and arrival)
  - Example: `grid-column: 1 / span 2;` (Includes span)

- **Margins in Grid Layout**: With `display: grid`, child element margins do not overflow the parent container. The parent does not inherit these margins.


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Grid Layout Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="grid-container">
        <header class="header">Header</header>
        <aside class="sidebar">Sidebar</aside>
        <main class="main">Main Content</main>
        <footer class="footer">Footer</footer>
    </div>
</body>
</html>
```
```css
/* Basic grid container setup */
.grid-container {
    display: grid;
    grid-template-columns: 1fr 3fr 1fr; /* Three columns with different sizes */
    grid-template-rows: auto 1fr auto;  /* Three rows with flexible heights */
    grid-template-areas:
        "header header header"
        "sidebar main main"
        "footer footer footer";
    gap: 10px; /* Space between grid items */
}

/* Grid item styling */
.header {
    grid-area: header;
    background-color: #f4a261;
    padding: 10px;
}

.sidebar {
    grid-area: sidebar;
    background-color: #2a9d8f;
    padding: 10px;
}

.main {
    grid-area: main;
    background-color: #264653;
    color: white;
    padding: 10px;
}

.footer {
    grid-area: footer;
    background-color: #e9c46a;
    padding: 10px;
}
```


## CSS Variables 

### Declaring Variables

CSS variables, also known as Custom Properties, are declared with the syntax `--variable-name` and can be used throughout your CSS with the `var()` function.

### Declaration Syntax

```css
/* :root is commonly used for global variables.*/
:root {
    --main-bg-color: #f0f0f0; /* Variable declaration */
    --main-text-color: #333;
    --header-height: 60px;
} 
```
### Usage Syntax
```css
body {
    background-color: var(--main-bg-color); /* Using the variable */
    color: var(--main-text-color);
}

header {
    height: var(--header-height);
}

button {
   /* #fff est la valeur par défaut */
   /* Fallback value */
    background-color: var(--main-bg-color, #fff); 
}

/* Override for a specific class */
.alert-button {
    --secondary-color: #e74c3c; /* New specific value */
}

```

## Responsive Images Cheatsheet

## `srcset`

The `srcset` attribute allows you to specify a list of images for different device resolutions and sizes. This helps browsers choose the most appropriate image based on the device’s screen size and resolution.

### Basic Syntax

```html
<img src="default-image.jpg" 
     srcset="small.jpg 600w, medium.jpg 1200w, large.jpg 1800w" 
     sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 33vw" 
     alt="Responsive image">`` 
```

-   **`src`**: Fallback image used if `srcset` is not supported.
-   **`srcset`**: List of images with their respective sizes. The format is `image-source widthDescriptor` where `widthDescriptor` is in pixels (`w`).
-   **`sizes`**: Defines how much space the image should take up in different viewport sizes.

### Example Explained

-   **`src`**: `default-image.jpg` – This is the image used if `srcset` is not supported by the browser.
-   **`srcset`**:
    -   `small.jpg 600w` – Image for viewports 600 pixels wide.
    -   `medium.jpg 1200w` – Image for viewports 1200 pixels wide.
    -   `large.jpg 1800w` – Image for viewports 1800 pixels wide.
-   **`sizes`**:
    -   `(max-width: 600px) 100vw` – For viewports up to 600px wide, use 100% of viewport width.
    -   `(max-width: 1200px) 50vw` – For viewports up to 1200px wide, use 50% of viewport width.
    -   `33vw` – For viewports larger than 1200px, use 33% of viewport width.
    - `sizes`: The `sizes` attribute helps the browser determine which image from `srcset` to download based on the viewport width.

### Common Patterns

-   **Full Width Images**

```html
<img src="image.jpg" 
     srcset="image-600w.jpg 600w, image-1200w.jpg 1200w" 
     sizes="100vw" 
     alt="Full width image">
```
- **Images in a Sidebar**
```html
<img src="sidebar-image.jpg" 
     srcset="sidebar-image-small.jpg 400w, sidebar-image-large.jpg 800w" 
     sizes="(max-width: 600px) 50vw, 25vw" 
     alt="Sidebar image">
```
### `picture` Element

For more complex responsive image scenarios, use the `<picture>` element to provide multiple sources and conditions.

```html
<picture>
  <source srcset="image-480w.jpg" media="(max-width: 480px)">
  <source srcset="image-800w.jpg" media="(max-width: 800px)">
  <img src="image.jpg" alt="Responsive image">
</picture>
```
-   **`<source>`**: Specifies different image sources and media conditions.
-   **`<img>`**: The fallback image for browsers that don’t support the `<picture>` element.

### Performance Tips

-   **Use WebP Format**: For better compression and quality.
-   **Lazy Loading**: Use `loading="lazy"` to delay loading images until they are in the viewport.

```html
<img src="image.jpg" 
     srcset="image-small.jpg 600w, image-large.jpg 1200w" 
     sizes="(max-width: 600px) 100vw, 50vw" 
     loading="lazy" 
     alt="Lazy loaded image">
```


## Responsive Design with CSS Media Queries 

### 1. Basics of Media Queries

Media queries allow you to apply different styles based on the device’s characteristics like width, height, resolution, etc.

**Syntax:**
```css
@media (condition) {
    /* CSS rules */
}
```

```css
/* Ultra Small Devices (Portrait Phones, 320px to 479px) */
@media (min-width: 320px) and (max-width: 479px) {
  /* Styles for very small phones */
}

/* Extra Small Devices (Phones, up to 600px) */
@media (max-width: 599px) { 
  /* Styles for phones */
}

/* Small Devices (Tablets, 600px to 767px) */
@media (min-width: 600px) and (max-width: 767px) { 
  /* Styles for tablets in portrait orientation */
}

/* Medium Devices (Small Tablets, 768px to 991px) */
@media (min-width: 768px) and (max-width: 991px) { 
  /* Styles for small tablets and small laptops */
}

/* Large Devices (Desktops, 992px to 1199px) */
@media (min-width: 992px) and (max-width: 1199px) { 
  /* Styles for desktops */
}

/* Extra Large Devices (Large Desktops, 1200px and up) */
@media (min-width: 1200px) { 
  /* Styles for large desktops */
}

/* Landscape Orientation (up to 767px) */
@media (max-width: 767px) and (orientation: landscape) {
  /* Styles for small devices in landscape orientation */
}

/* Landscape Tablets (768px to 1024px) */
@media (min-width: 768px) and (max-width: 1024px) and (orientation: landscape) {
  /* Styles for tablets in landscape orientation */
}

/* High Resolution Screens (Retina Displays) */
@media (-webkit-min-device-pixel-ratio: 2), 
       (min-resolution: 192dpi) {
  /* Styles for high-resolution (retina) screens */
}

/* Print Styles */
@media print {
  /* Styles for printing */
}
```

## Example 

```css
/* Base Styles (Mobile First) */
.container {
  width: 100%;
  padding: 10px;
}

/* Small Devices (Phones) */
@media (max-width: 599px) { 
  .container {
    width: 100%;
    padding: 10px;
  }
}

/* Medium Devices (Tablets) */
@media (min-width: 600px) and (max-width: 767px) { 
  .container {
    width: 80%;
    padding: 20px;
  }
}

/* Landscape Orientation (Phones) */
@media (max-width: 767px) and (orientation: landscape) {
  .container {
    padding: 15px;
  }
}

/* Large Devices (Desktops) */
@media (min-width: 992px) { 
  .container {
    width: 60%;
    padding: 30px;
  }
}

/* High Resolution Screens (Retina Displays) */
@media (-webkit-min-device-pixel-ratio: 2), 
       (min-resolution: 192dpi) {
  .container {
    border: 1px solid #333;
  }
}

/* Print Styles */
@media print {
  .container {
    width: 100%;
    padding: 0;
    border: none;
  }
}
```

## **Useful Links**

- [Mozilla Developer Network (MDN) CSS Documentation](https://developer.mozilla.org/fr/docs/Web/CSS)
  - [CSS Documentation on DevDocs](https://devdocs.io/css)

- [Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
  - [Flexbox Froggy](https://flexboxfroggy.com/#fr)

- [Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
  - [CSS Grid Garden](https://cssgridgarden.com/#fr)
  - [Mozilla Developers CSS Grid Playground](https://mozilladevelopers.github.io/playground/css-grid/)

- [Media queries](https://web.dev/learn/design/media-queries)

- [FontSquirrel](https://www.fontsquirrel.com/)
  - [Transfonter](https://transfonter.org/) - Convert font formats.

- [Can I Use](https://caniuse.com/)
  - [Autoprefixer](https://autoprefixer.github.io/)
  - [Preset Env](https://preset-env.cssdb.org/) - Generate code for older browsers using CSS variables.

- [Meyerweb Reset CSS](https://meyerweb.com/eric/tools/css/reset/) - A popular CSS reset stylesheet.
- [Mini Reset CSS](https://jgthms.com/minireset.css/) - A minimal CSS reset.
- [Normalize CSS](https://necolas.github.io/normalize.css/) - A modern CSS reset.
