


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

