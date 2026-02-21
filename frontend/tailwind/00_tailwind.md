# Installing Tailwind CSS with React + Vite

**Using the official method with the `@tailwindcss/vite` plugin**, without using `npx tailwindcss init`.

---

## Step 1 – Create a React project with Vite

```bash
npm create vite@latest projectName -- --template react
cd projectName
npm install
```

---

## Additional Steps

- Install Tailwind CSS with the Vite plugin
- Configure the plugin in `vite.config.js`
- Add Tailwind in your CSS file
- Import this CSS into your React app
- Start the development server

```bash
npm run dev
```

> Tailwind (via the `@tailwindcss/vite` plugin or PostCSS) **scans all your HTML/JSX files**, finds all the classes like `text-3xl`, `bg-blue-500`, etc., and **dynamically generates the final CSS** containing **only the classes you actually used**.

- [Documentation](https://tailwindcss.com/docs/installation/using-vite)

---

## Adding Custom Configuration

- **In-line Customization**: You can add custom values inline using square brackets for colors, sizes, and other utilities (e.g., `text-[color]`, `p-[size]`).

- **Directives**: Tailwind supports directives like `@apply`, `@layer`, and `@utility` to streamline how styles are applied and organized.

  - Keywords: `import`, `theme`, `utilities`, `variant`, `source`, `reference`, `apply`, `custom variant`

**Example**
Customization directly in CSS file:

```css
@import 'tailwindcss';

@custom-variant dark (&:where(.dark, .dark *));

@theme {
  --color-mainBlack: #131316;
  --color-secondaryBlack: #1c1c21;
}
```

- [Documentation](https://tailwindcss.com/docs/adding-custom-styles)

- **Component Libraries**: Using libraries like [ShadCN](https://ui.shadcn.com/docs/installation) can enhance your Tailwind experience with pre-built components that are still fully customizable.

---

## Flexbox, Grid, and Media Queries with Tailwind CSS

### FLEXBOX

#### Basic Example

```html
<div class="flex justify-center mt-2 space-x-6">
  <div class="h-16 w-16 rounded-full bg-blue-500 "></div>
  <div class="h-16 w-16 rounded-full bg-green-500 "></div>
  <div class="h-16 w-16 rounded-full bg-red-500 "></div>
</div>
```

```jsx
<div class="flex flex-col items-center space-y-6 mt-15">
  <div class="h-16 w-16 rounded-full bg-blue-500 "></div>
  <div class="h-16 w-16 rounded-full bg-green-500 "></div>
  <div class="h-16 w-16 rounded-full bg-red-500 "></div>
</div>
```

#### Main Properties

| Tailwind Class            | CSS Function                  |
| ------------------------- | ----------------------------- |
| `flex`                    | `display: flex`               |
| `flex-row` _(default)_    | `flex-direction: row`         |
| `flex-col`                | `flex-direction: column`      |
| `items-center`            | `align-items: center`         |
| `justify-center`          | `justify-content: center`     |
| `space-x-*` / `space-y-*` | horizontal / vertical spacing |
| `gap-*`                   | Gap between elements          |
| `flex-wrap`               | `flex-wrap: wrap`             |

---

### GRID

#### Simple Example

```html
<div class="grid grid-cols-3 gap-4">
  <div class="bg-red-500 h-16"></div>
  <div class="bg-blue-500 h-16"></div>
  <div class="bg-green-500 h-16"></div>
</div>
```

#### Important Properties

| Tailwind Class       | CSS Function                            |
| -------------------- | --------------------------------------- |
| `grid`               | `display: grid`                         |
| `grid-cols-3`        | `grid-template-columns: repeat(3, 1fr)` |
| `col-span-2`         | `grid-column: span 2 / span 2`          |
| `row-span-2`         | `grid-row: span 2 / span 2`             |
| `gap-4`              | `gap: 1rem`                             |
| `place-items-center` | `align-items + justify-items: center`   |

---

## MEDIA QUERIES (Mobile-First)

### Fundamental Principle

Tailwind CSS uses a **mobile-first** approach:

- Styles without prefix = apply to small screens
- Add **prefixes** for larger screens: `sm:`, `md:`, etc.

### Default Breakpoints

| Prefix | Min-width | Example Tailwind |
| ------ | --------- | ---------------- |
| `sm:`  | 640px     | `sm:bg-red-500`  |
| `md:`  | 768px     | `md:text-lg`     |
| `lg:`  | 1024px    | `lg:grid-cols-4` |
| `xl:`  | 1280px    | `xl:px-12`       |
| `2xl:` | 1536px    | `2xl:text-2xl`   |

> Min-width = style applies **if the screen is at least that wide**

#### Example

```html
<div class="bg-blue-300 sm:bg-green-400 md:bg-red-500">
  <p class="text-white">Hello world</p>
</div>
```

```jsx
<div class="bg-white sm:bg-amber-500 md:bg-amber-900">
```

---

## Using `max-` Prefix

```html
<div class="max-sm:bg-yellow-200 max-md:bg-red-200">
  <p class="text-white">Content</p>
</div>
```

```jsx
<div class="max-sm:bg-amber-500 max-md:bg-amber-900">
```

| Prefix    | Meaning            |
| --------- | ------------------ |
| `max-sm:` | `max-width: 640px` |
| `max-md:` | `max-width: 768px` |

> Less common, may contradict the mobile-first logic

---

## Responsive Example with `flex-col` + `flex-row`

```html
<div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
  <div class="w-full md:w-1/3 bg-blue-500 h-16"></div>
  <div class="w-full md:w-1/3 bg-green-500 h-16"></div>
  <div class="w-full md:w-1/3 bg-red-500 h-16"></div>
</div>
```

---

## Mobile-First Summary

```
Mobile (default)
│
├── sm: ≥ 640px
├── md: ≥ 768px
├── lg: ≥ 1024px
├── xl: ≥ 1280px
└── 2xl: ≥ 1536px
```

> **Never use `sm` for mobile styles**, it's used for **screens above mobile**

---

## Tips & Tricks

### Fullscreen Layout

```jsx
<div class="min-h-screen flex flex-col">
  <header class="h-16 bg-blue-500">Header</header>
  <main class="flex-1 bg-white">Expanding content</main>
  <footer class="h-12 bg-gray-800 text-white">Footer</footer>
</div>
```

- `min-h-screen` = full height layout
- `flex-col` = vertical stacking
- `flex-1` = main section fills remaining space

---

### Recommended Style Order

```jsx
<div class="
  [base styles]
  sm:[sm styles]
  md:[md styles]
  lg:[lg styles]
">
```

---

### Min-width Approach (standard)

- Applies when width is **greater than or equal** to the breakpoint
- Behavior: "From this size and up"
- Logic: Mobile-first

### Max-width Approach (alternative)

- Applies when width is **less than** the breakpoint
- Behavior: "Up to this size"
- Logic: Desktop-first

---

### Tailwind Breakpoints Comparison

| Breakpoint | min-width (standard) | max-width (alternative) |
| ---------- | -------------------- | ----------------------- |
| `sm`       | 640px and up         | 0 – 639px               |
| `md`       | 768px and up         | 0 – 767px               |
| `lg`       | 1024px and up        | 0 – 1023px              |
| `xl`       | 1280px and up        | 0 – 1279px              |
| `2xl`      | 1536px and up        | 0 – 1535px              |

---

## Extra Tricks

### Accent Colors

```jsx
<label><input type="checkbox" checked /> Browser default</label>
<label><input class="accent-pink-500" type="checkbox" checked /> Customized</label>
```

---

### Fluid Typography

```jsx
<p className="text-[clamp(1rem,1vw,1.3rem)] leading-tight">
  This text resizes fluidly based on screen width.
</p>
```

**`clamp(min, preferred, max)`** explanation:

- `1rem` → Minimum text size (~16px)
- `1vw` → Viewport-based value (1% of screen width)
- `1.3rem` → Maximum text size (~20.8px)

---

### File Input Customization

```jsx
<input
  type="file"
  class="file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-violet-700 hover:file:bg-violet-100 dark:file:bg-violet-600 dark:file:text-violet-100 dark:hover:file:bg-violet-500 ..."
/>
```

---

### Text Selection & Caret

```jsx
<div className="selection:bg-red-900 selection:text-white caret-pink-yellow">
```

---

### Open/Close State

```jsx
<details
  class="border border-transparent open:border-black/10 open:bg-gray-100 ..."
  open
>
  <summary class="text-sm leading-6 font-semibold text-gray-900 select-none">
    Why do they call it Ovaltine?
  </summary>
  <div class="mt-3 text-sm leading-6 text-gray-600">
    <p>The mug is round. The jar is round. They should call it Roundtine.</p>
  </div>
</details>
```

### Ressources

- [ShadcnUI](https://ui.shadcn.com/): A set of beautifully designed components
