# Notes on React JSX and Components

## JSX Syntax

- JSX is regular JavaScript that allows you to write HTML-like syntax.
- It gets converted to regular JavaScript by Babel.
- Attributes are written in camelCase (exceptions: `aria-*` and `data-*`).
- `class` becomes `className` (to avoid conflict with JS `class` keyword).
- Inline styles are written as an object with camelCase CSS properties:
  ```jsx
  <div style={{width: 50, height: 50, backgroundColor: 'blue'}}/>
  ```
- Self-closing tags are required.
- Components must return a single root element (like a `div`) or use a Fragment (`<></>` or `<Fragment></Fragment>`) for a virtual wrapper.

## Variable Interpolation

- JSX allows JavaScript expressions inside `{ ... }`.

```jsx
const text = 'Hello folks';
const id = 'myId';

export function App() {
    return <h1 id={id}>{text}</h1>
}
```

## Styling in React

- Styles are JS objects.
- CSS properties become camelCase.
- Values are strings (except for unitless numbers).

```jsx
<h1 id={id} style={{color: 'red'}}>{text}</h1>

// Or using a separate object
const style = {color: 'red'}
<h1 id={id} style={style}>{text}</h1>
```

## Event Handling

React uses camelCase for event handlers and expects a function.

```jsx
function App() {
  const handleClick = () => {
    alert("Click detected!");
  };

  return <button onClick={handleClick}>Click me</button>;
}
```

Inline function:
```jsx
<button onClick={() => alert('Hi!')}>Click</button>
```

> Defining the function outside JSX is preferred for clarity and performance.

- Examples: `onClick`, `onChange`, `onSubmit`, `onMouseEnter`
- You pass a **function** or **arrow function**.

### Synthetic Events

React wraps native events with `SyntheticEvent` for consistency across platforms.

```jsx
export function App () {
  const doSomething = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  return <form onSubmit={doSomething}>Hello folks</form>;
}
```

```jsx
function App() {
  const handleClick = (event) => {
    console.log('Event:', event);
    console.log('Target:', event.target);
  };

  return <button onClick={handleClick}>Click me</button>;
}
```

### Useful Properties & Methods

- `e.target`, `e.currentTarget`, `e.preventDefault()`, `e.stopPropagation()`, `e.nativeEvent`

### Common React Events

| Event Type             | React Attribute               | JSX Example                        |
|------------------------|-------------------------------|------------------------------------|
| **Click**              | `onClick`                     | `<button onClick={...} />`        |
| **Keyboard**           | `onKeyDown`, `onKeyUp`        | `<input onKeyDown={...} />`       |
| **Form input**         | `onChange`                    | `<input onChange={...} />`        |
| **Form submission**    | `onSubmit`                    | `<form onSubmit={...} />`         |
| **Mouse**              | `onMouseEnter`, etc.          | `<div onMouseMove={...} />`       |
| **Focus / Blur**       | `onFocus`, `onBlur`           | `<input onBlur={...} />`          |
| **Context menu**       | `onContextMenu`               | `<div onContextMenu={...} />`     |
| **Drag & Drop**        | `onDragStart`, `onDrop`       | `<div onDrop={...} />`            |
| **Double click**       | `onDoubleClick`               | `<div onDoubleClick={...} />`     |
| **Clipboard**          | `onCopy`, `onPaste`           | `<input onPaste={...} />`         |
| **Scroll**             | `onScroll`                    | `<div onScroll={...} />`          |
| **Touch (mobile)**     | `onTouchStart`, etc.          | `<div onTouchStart={...} />`      |
| **Animation**          | `onAnimationEnd`, etc.        | `<div onAnimationEnd={...} />`    |

## Conditional Rendering

JSX does not support `if` statements directly.

### Valid methods

```jsx
{isVisible && <Modal/>}
{isLoading ? <Spinner/> : <Data/>}
```

Intermediate variable:
```jsx
let content;
if (isLoading) content = <Spinner/>
else content = <Data/>

return <div>{content}</div>
```

### Invalid

```jsx
return (
  <div>
    { if (isLoading) { return <Spinner /> } } //  ERROR
  </div>
);
```

| Method               | Valid in JSX | Recommended Use         |
|----------------------|--------------|--------------------------|
| `if/else` outside JSX| Yes          | For clarity              |
| Ternary `? :`        | Yes          | For short conditions     |
| Logical `&&`         | Yes          | For single elements      |
| `if` inside `{}`     | No           | Not allowed in JSX       |

## Rendering Lists with `map()`

- Transforms an array into JSX elements
- React requires a unique `key` per element

```jsx
const todos = ['Task 1', 'Task 2', 'Task 3'];

export function App() {
  return (
    <>
      <h1>My todo list</h1>
      <ul>
        {todos.map(todo => (
          <li key={todo}>{todo}</li>
        ))}
      </ul>
    </>
  );
}
```

## Functional Components in React

### A component is a function

- Named in PascalCase
- Takes `props` and returns JSX

```jsx
function Title({ color, children }) {
  return <h1 style={{ color }}>{children}</h1>;
}
```

Without destructuring:

```jsx
function Title(props) {
  return <h1 style={{ color: props.color }}>{props.children}</h1>;
}
```

### Extra Props

```jsx
function Title({ color }) {
  console.log("props color:", color);
  return (<h1 style={{ color }}>Hello +</h1>);
}

<Title color="blue" size="large"  className="title" />
```

Access all props:
```jsx
function Title(props) {
  console.log(props);
  return <h1 style={{ color: props.color }}>{props.children}</h1>;
}
```

### Spread Operator

```jsx
function Title({ color, children, ...props }) {
  return <h1 style={{ color }} {...props}>{children}</h1>;
}
```

### Using as Custom HTML Element

```jsx
export function App() {
  return (
    <>
      <Title color="red">This is a title</Title>
      <p>First paragraph</p>
    </>
  );
}
```

---

## Component-Based Benefits

- Less repetition
- Code reuse
- Better UI organization
- Easier to test and maintain

---

### Summary

| Concept               | Explanation |
|------------------------|-------------|
| Function = component   | Must be PascalCase |
| `props`                | Object of passed attributes |
| `children`             | Content between `<Title>...</Title>` |
| Destructuring          | Pull specific values from props |
| `...props`             | Capture the rest of props |