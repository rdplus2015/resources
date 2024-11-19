# CSS
- **Text Styling**
- **Units of Measurement**
- **fonts management**
- **background management**
---

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

--- 

## Units of Measurement

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

    - **Recommending Usage**: *% is ideal for responsive designs, particularly for widths and (heights) that need to adapt to the container rather than the viewport.*


- **vh** and **vw** : Relative to the viewport's height and width

  - **When to Use**:
    - *Use vh and vw for full-screen or viewport-based layouts. For example, a section that always takes up 100% of the viewport height would use height: 100vh;.*

    - *Useful for creating full-page layouts or ensuring elements adjust with the screen size dynamically.*

    - **Recommending Usage**: *vh and vw are ideal for full-page sections, hero banners, or elements that need to scale with the viewport dimensions. Use with caution for smaller components, as it can lead to less control over element proportions.*

  
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

----

## Custom Fonts with `@font-face`

The `@font-face` rule allows you to load custom fonts on your website. You can specify the font files and define how they should be used in your CSS.

### Sample
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

### Example
```css
@font-face {
    font-family: 'Roboto';
    src: url('fonts/Roboto-Regular.woff2') format('woff2'),
         url('fonts/Roboto-Regular.woff') format('woff'),
         url('fonts/Roboto-Regular.ttf') format('truetype'); /*  TTF fornat */
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'Roboto';
    src: url('fonts/Roboto-Bold.woff2') format('woff2'),
         url('fonts/Roboto-Bold.woff') format('woff'),
         url('fonts/Roboto-Bold.ttf') format('truetype'); /* TTF format */
    font-weight: bold;
    font-style: normal;
}

body {
    font-family: 'Roboto', sans-serif;
}
```

### Custom Fonts with `Google Fonts`


```html
<!-- Normal laoding -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&dis play=swap" rel="stylesheet">
<!-- Manually Adding font-display:swap to Google Fonts if it's not  -->

<!-- Preloading-->
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"></noscript>
</head>
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

#### Best Practices

- **Preconnect**: Use the `rel="preconnect"` attribute to establish early connections to the Google Fonts servers, speeding up the font loading.

- **Preload**: Consider preloading the font files to reduce loading times and Preventing Flash of Unstyled Text (FOUT)

- **Font Loading Optimization**: Use `font-display: swap;` to improve font loading performance. This property controls how a font is displayed while loading.

- **Font Formats**: Include multiple font formats (woff2, woff, ttf) to ensure compatibility across all browsers.

### Performance Considerations

Choosing between a local font and Google Fonts depends on your priorities for performance, control, and privacy. Google Fonts is easy to integrate with a simple link, offers shared caching, and provides quick access to font variations. However, hosting fonts locally can improve performance by reducing external requests, provide greater control over files, and enhance privacy by avoiding requests to third-party services.

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

### Shorthand Background Property

- Order:
  - `background-color` - `background-image` - `background-repeat` - `background-attachment` - `background-position/background-size` - `background-origin` - `background-clip.`

```css
.background-shorthand-example {
  background: #f0f0f0 url('image.jpg') no-repeat center/cover;
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

### Background Best Practices

- Optimize Images: Use optimized image formats (like WebP) and sizes to improve page loading times.
- Use SVG for Patterns: SVGs scale well and are lightweight, perfect for backgrounds.
- Combine Images and Gradients: Combine images with gradients for enhanced visual effects.
- Responsive Design: Adjust background properties for different screen sizes using media queries.