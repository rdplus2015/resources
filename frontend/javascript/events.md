
# JavaScript Event Handling

## Basic Example with `addEventListener`

```javascript
// Simple event listener example

const btn = document.querySelector("button");
btn.addEventListener("click", (event) => {
    console.log(event);
    console.log(
        event.target,        // The element that was clicked
        event.currentTarget, // The element on which the listener is attached (here, the button)
        this                 // Equivalent to currentTarget unless using arrow functions
    );
});

```

## Click Handler Function

```javascript
function onButtonClick(event) {
    event.preventDefault(); // Prevents default behavior to perform other actions

    // Stops the propagation of the event. If an element and its parent both have listeners
    // on the same event, the event would normally bubble up. This method prevents that.
    event.stopPropagation();
}
```

## Adding Listeners to Multiple Buttons

```javascript
// Select all buttons and add a listener to each one
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', onButtonClick);
});
```

## Additional `addEventListener` Options

```javascript
// Third parameter: options object
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', onButtonClick, {
        once: true,    // The event will only be triggered once
        passive: true, // Improves performance (especially for scroll events)
        capture: true  // Enables capture phase (event is captured on the way down)
    });
});
```

## Practical Examples

### Example 1: Form Validation using `FormData`

```javascript
document.querySelector("form").addEventListener("submit", (e) => {
    const form = e.currentTarget;
    e.preventDefault(); // Prevent automatic form submission

    const data = new FormData(form);
    const firstname = data.get('firstname');

    if (firstname.length > 0) {
        e.preventDefault(); // Extra safeguard
    }
});
```

### Example 2: Tracking User Input

```javascript
document.querySelector("input").addEventListener("input", (e) => {
    console.log('input', e.currentTarget.value); // Displays the typed value in real-time
    // Note: preventDefault does not work on input events
});
```

### Example 3: Keyboard Shortcut Detection

```javascript
document.querySelector("input").addEventListener("keydown", (e) => {
    // Checks if Ctrl + K was pressed
    if (e.ctrlKey === true && e.key === "k") {
        e.preventDefault();
        console.log("Shortcut");
    }
    // Other useful events: keyup, keypress, focus, blur
});
```

### Example 4: Checkbox Change Event

```javascript
document.querySelector("input[type='checkbox']").addEventListener("change", (e) => {
    console.log(e.currentTarget.checked); // Returns true or false
    // React to the change in checkbox state
});
```

### Example 5: Select Element Change Event

```javascript
document.querySelector("select").addEventListener("change", (e) => {
    console.log(e.currentTarget.value); // Displays the selected option

    // For multiple selections, retrieve all selected options:
    const selectedOptions = Array.from(e.currentTarget.selectedOptions)
        .map(option => option.value);

    console.log(selectedOptions);
});
```