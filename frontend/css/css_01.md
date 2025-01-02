
# CSS
- **Selectors**
- **Box model**
- **Dimension and spacing rules** 

---

## CSS Selectors

### basic selectors 
```css
p{
  /* Targets all p elements */     
}links
```
### Descendant and Child Selectors

```css
div h2 {
  /* 
Targets all h2 elements that are descendants of a div, no matter their level in the DOM hierarchy (children, grandchildren, etc.)

good for global style inside a parent
  */
}

div > h2 {
    /* Targets all h2 elements that are direct children of div */
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

/*
- h2 + p
<h2>Title</h2>
<p>This will be targeted.</p>
<p>Not targeted because not immediately after h2.</p>

- h2 ~ p  
<h2>Title</h2>
<p>This will be targeted.</p>
<p>This too will be targeted.</p>
*/
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
  /* targets the first child of a parent that is a <div> element. This means that the <div> must be the first child in its container. */
  color: red;
}

tr:nth-child(2n)  {
  /* Applies styles to every second tr element This selector targets. The 2n means that elements 2, 4, 6, etc. will be stylized.*/

  /* tr:nth-child (2) */
  background-color: #f0f0f0;
}

p:first-of-type {
    /* Targets the first p element of its type */
  /*
  <div>
    <span>Text in a span</span>
    <p>This paragraph will be targeted because it is the first p.</p>
    <p>This paragraph will not be targeted.</p>
  </div>
  */
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

```css
.child1 {
    margin-bottom: 30px; /* Marge de 30px */
}

.child2 {
    margin-top: 20px; /* Marge de 20px */
}

```
- If parent elements have no margin, the first child element's margin will overflow into the parent.

```css
.parent {
    /* No margin, padding or border => the parent will have a 50px of margin-top  */
}

.child {
    margin-top: 50px; /* Top margin of 50px */
}
```
### Margins on Inline Elements

- Margins top and bottom are not applied to inline or inline-block elements; only left and right margins apply.

### Spaces in HTML

- Inline and inline-block elements are affected by spaces in HTML.
