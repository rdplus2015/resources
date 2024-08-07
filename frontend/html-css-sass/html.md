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

## Best Practices
- Use Semantic Tags: Make use of HTML5 semantic tags to improve accessibility and SEO.
- Validate HTML: Use validators to ensure the HTML is well-formed and adheres to standards.
- Optimize Images: Use appropriate formats and sizes for images to enhance loading times.
- Use ARIA Attributes: Improve accessibility for users with disabilities.
- Avoid Inline Styles: Use external CSS files for styling to keep HTML clean and maintainable.
