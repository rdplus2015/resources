# Tailwind Installation for Spring Boot

## Install curl and other tools
```bash
sudo apt update
sudo apt install -y curl
```

### Remove older Node versions
```bash
rm -rf node_modules package-lock.json
```

### Install nvm
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install 20
nvm use 20
node -v
```

### Initialize a Node application
```bash
npm init -y
```

This creates a package.json file to manage your Node.js dependencies.

## Install Tailwind CSS v4

Install the required Tailwind packages as development dependencies.

### Bash
```bash
npm install -D tailwindcss @tailwindcss/cli
```

## Create Your Source CSS File

This is the most important step. It is best practice to keep your source CSS file separate from your generated static assets.

1. Create a new folder: `src/main/resources/css`
2. Inside that folder, create a file named `input.css`

Note: We are creating this css folder outside the static folder. The static folder should only contain the final generated style.css file that Spring Boot serves to the browser. input.css is your source file.

Now add the following content to `src/main/resources/css/input.css`.

### CSS
```css
/* 1. Import all Tailwind core styles */
@import "tailwindcss";

/* 2. Point Tailwind to your Spring Boot templates */
@source "../src/main/resources/templates/**/*.html";

/* 3. (Optional) Add custom theme values */
@theme {
  --color-brand: #3b82f6;
  --font-display: "Inter", "sans-serif";
}

/* 4. (Optional) Add custom base styles */
@layer base {
  h1 {
    @apply text-2xl font-bold;
  }
}
```

## Step 4: Configure npm Scripts in package.json

Open your package.json file and replace the entire "scripts" section with the following. This tells Tailwind where to find your input.css (input) and where to generate style.css (output).

### JSON
```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "build-css": "npx @tailwindcss/cli -i ./src/main/resources/css/input.css -o ./src/main/resources/static/css/style.css --minify",
  "watch-css": "npx @tailwindcss/cli -i ./src/main/resources/css/input.css -o ./src/main/resources/static/css/style.css --watch"
}
```

- `-i` (Input): points to your source file.
- `-o` (Output): points to the final file served by Spring Boot.

## Step 5: Link the Generated CSS in Your HTML

Go to your Thymeleaf template (for example: `src/main/resources/templates/home-page.html`) and add the following link inside the `<head>` tag.

This `th:href` path works because Spring Boot automatically serves files from the `src/main/resources/static/` directory.

### HTML
```html
<head>
  <meta charset="UTF-8">
  <title>My Spring App</title>

  <link rel="stylesheet" th:href="@{/css/style.css}">
</head>
```

## Start the Development Workflow

You will need two terminals running.

### 1. Terminal 1 (Tailwind watcher)
From your project root, run:
```bash
npm run watch-css
```

This watches input.css and your .html files for changes and automatically rebuilds style.css.

### Production build
To build the final CSS file:
```bash
npm run build-css
```

### 2. Terminal 2 (Spring Boot)
In another terminal (or your IDE), run your Spring Boot application as usual.

Any time you add a Tailwind class (for example: `bg-blue-500`) to your HTML files and save, the watcher will rebuild style.css automatically. Refresh your browser to see the changes.



## Example Files

### input.css
```css
@import "tailwindcss";
@source "../resources/templates/**/*.html";

/* 3. (Optional) Add custom theme values */
@theme {
  --color-brand: #3b82f6;
  --font-display: "Inter", "sans-serif";
}

/* 4. (Optional) Add custom base styles */
@layer base {
  h1 {
    @apply text-2xl font-bold;
  }
}
```

### package.json
```json
{
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build-css": "npx @tailwindcss/cli -i ./input.css -o ../resources/static/css/style.css --minify",
    "watch-css": "npx @tailwindcss/cli -i ./input.css -o ../resources/static/css/style.css --watch"
  }
}
```

### HTML
```html
<head>
    <meta charset="UTF-8">
    <!-- Tailwind CSS -->
    <link rel="stylesheet" th:href="@{/css/style.css}">
</head>
```
