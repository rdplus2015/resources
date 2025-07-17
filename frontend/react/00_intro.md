# What is React?

**React** is a JavaScript library developed by Meta (Facebook) for building modern, dynamic, and responsive user interfaces (UI).  
It allows you to create **reusable components**, manage an application's state, and improve performance thanks to the **Virtual DOM**.

## Why use React?

- **Reusable components**: structure your app with logical building blocks  
- **Fast** thanks to the Virtual DOM  
- **Automatic UI updates** when data changes  
- **Rich ecosystem** (React Router, Redux, Tailwind CSS, etc.)  
- **Highly in demand** in the industry (modern frontend)

## Install React with Vite

### Step 1 – Create a new project

```bash
npm create vite@latest project-name
cd project-name
```

> Replace `project-name` with the name of your app (e.g., cinequest)

### Step 2 – Install dependencies

```bash
npm install
```

### Step 3 – Start the development server

```bash
npm run dev
```

Your app will be available at:

```
http://localhost:5173
```

### Initial project structure

```
project-name/
├── public/
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
├── index.html
├── vite.config.js
└── package.json
```

---

### Scalable structure
```text
src/
├── components/         # All reusable components (buttons, cards, etc.)
├── pages/              # Full pages (if you're using React Router or Next.js)
├── layouts/            # Global layouts (Navbar + Footer, etc.)
├── hooks/              # Custom hooks (e.g., useForm, useAuth)
├── context/            # Context API for global state management
├── assets/             # Images, icons, static files
├── styles/             # CSS files or custom Tailwind styles
├── utils/              # Utility functions (date formatting, etc.)
├── services/           # API calls or business logic (e.g., authService.js)
├── App.js              # Root component
└── index.js            # Application entry point
```