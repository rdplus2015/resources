
# CSS
- **CSS grid**
- **CSS Variables**
- **Responsive Design with CSS Media Queries**
---

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

## Parent vs. Child in CSS Grid

| **Role**             | **Applies To**                 | **Key Properties**                                |
|-----------------------|--------------------------------|--------------------------------------------------|
| **Grid Layout**       | Parent (Grid Container)       | `display: grid`, `grid-template-columns`, `grid-template-rows`, `gap` |
| **Item Placement**    | Children (Grid Items)         | `grid-column`, `grid-row`, `justify-self`, `align-self` |
| **Alignment**         | Both (Parent and Children)    | Parent: `justify-items`, `align-items` <br> Child: `justify-self`, `align-self` |

-   **Parent**: Defines the grid structure (columns, rows, spacing).
-   **Child**: Controls how items are placed within the grid (position, span).
-   Use parent styles to control the overall layout, and child styles to customize individual items' behavior.

### Example 

**define equal columns and don't modify the children’s placement, each child will automatically occupy a single column.**

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
    gap: 10px;
}

.child {
    background-color: lightblue;
    padding: 20px;
    text-align: center;
}

```
**Even if the columns are equal, you can use the grid-column property on child elements to make them span multiple columns (or parts of columns).**
```css
.child:nth-child(1) {
    grid-column: 1 / 3; /* Spans the first and second columns */
}
.child:nth-child(2) {
    grid-column: 2 / 4; /* Spans the second and third columns */
}
.child:nth-child(3) {
    grid-column: 3 / 4; /* Occupies the last column */
}

```
-   The first child spans across the first and second columns.
-   The second child spans across the second and third columns.
-   The third child only occupies the last column.


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

## Responsive Design with CSS Media Queries 

### 1. Basics of Media Queries

Media queries allow you to apply different styles based on the device’s characteristics like width, height, resolution, etc.

**Syntax:**
```css
@media (condition) {
    /* CSS rules */
}
```


## Sample 
```css
/* Mobile (small screens, < 767px) */
@media screen and (max-width: 767px) { }

/* Tablets (768px - 1024px) */
@media screen and (min-width: 768px) and (max-width: 1024px) { }

/* Desktops (1025px - 1280px) */
@media screen and (min-width: 1025px) and (max-width: 1280px) { }

/* Large screens (1281px - 1600px) */
@media screen and (min-width: 1281px) and (max-width: 1600px) { }

/* Extra large screens (> 1600px) */
@media screen and (min-width: 1601px) { }
```