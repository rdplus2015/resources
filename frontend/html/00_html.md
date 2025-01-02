## Basic Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

## Common Tags and Their Attributes
## Text Formatting
- `<p>`: Paragraph
- `<h1> - <h6>`: Headings (h1 is the largest, h6 the smallest)
- `<strong>`: Bold text
- `<em>`: Italic text
- `<br>`: Line break
- `<hr>`: Horizontal rule
***
- `<a>`: Anchor (link)
  - `href`: URL
  - `target`: _blank (new tab), _self (same tab), etc.
***
- `<ul>`: Unordered list
- `<ol>`: Ordered list
  - `<li>`: List item
***

## Images and Multimedia
## Images
### `<img src="url" alt="description">`: Image
- `src`: Image source URL
- `alt`: Alternative text
- `width, height`: Dimensions

## Audio
### `<audio controls>`: Audio

- `src`: audio source URL
- `controls`: Show playback controls
- `width, height`: Dimensions

## Video 
### `<video controls>`: Video
- `src`: Video source URL
- `controls`: Show playback controls
- `width, height`: Dimensions

## Forms
### `<form action="url" method="POST|GET">`: Form
- `action`: URL to send form data
- `method`: Submission method (GET or POST)

### `<input>` Text input
- `type`: Input type (text, password, email, submit, etc.)
- `name`: Name of the input field
- `placeholder`: Placeholder text
- `value`: Default value
- `required`: Makes the input mandatory
### `<select>` Dropdown list
- `<option>` Option in the dropdown
### `<textarea>` Multi-line text input
###  `<label>` Label for an input


# Table Elements

### `<table>` Table

- `<tr>` Table row
- `<td>` Table cell
- `<th>` Table header cell
- `<thead>` Table header group
- `<tbody>` Table body group
- `<tfoot>` Table footer group

# Semantic HTML5 Tags

- `<header>` Document or section header
- `<nav>` Navigation links
- `<main>` Main content of the document
- `<section>` Section of content
- `<article>` Self-contained content
- `<aside>` Content aside from the main content
- `<footer>` Document or section footer
- `<figure>` Image with optional caption
  - `<figcaption>` Caption for a `<figure>`

# Document Metadata
### `<meta>` Metadata about the document
- **charset:** Character encoding
- **name:** Name of the metadata
- **content:** Metadata content

### `<link>` Link to external resources
- **rel:** Relationship between document and resource (e.g., stylesheet)
- **href:** URL of the resource

### `<title>` Document title

### Common Attributes
- `class`: CSS class name(s)
- `id`: Unique identifier
- `style`: Inline CSS styles
- `data-*`: Custom data attributes
- `src`: Source URL (used in `<img>`, `<script>`, etc.)
- `alt`: Alternative text (for `<img>`)
- `href`: URL reference (for `<a>`, `<link>`)
- `target`: Specifies where to open the linked document (for `<a>`)

## Responsive Images

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
## Best Practices
- Use Semantic Tags: Make use of HTML5 semantic tags to improve accessibility and SEO.
- Validate HTML: Use validators to ensure the HTML is well-formed and adheres to standards.
- Optimize Images: Use appropriate formats and sizes for images to enhance loading times.
- Use ARIA Attributes: Improve accessibility for users with disabilities.
- Avoid Inline Styles: Use external CSS files for styling to keep HTML clean and maintainable.
- Yes, combining <picture> and srcset allows for highly dynamic images. For optimization, you can leverage a CDN and image libraries such as:`Cloudinary or Imgix` - `ImageMagick or Sharp (Node.js) for server-side processing.`