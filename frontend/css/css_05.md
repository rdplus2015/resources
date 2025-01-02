
# CSS
- **Transformations**
- **Transitions**
- **Animations**

---

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

