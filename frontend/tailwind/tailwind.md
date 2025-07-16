## Installation de Tailwind CSS avec React + Vite 

**utilisation de la methode officielle avec le plugin `@tailwindcss/vite`**, sans utiliser `npx tailwindcss init`.


### Étape 1 – Créer un projet React avec Vite

```bash
npm create vite@latest projectName -- --template react
cd projectName
npm install
```


### Étape supplementaire 
- Installer Tailwind CSS avec le plugin Vite
- Configurer le plugin dans `vite.config.js`
- Ajouter Tailwind dans votre fichier CSS
- Importer ce CSS dans votre application React
- Lancer le serveur de développement

```bash
npm run dev
```

> Tailwind (via le plugin `@tailwindcss/vite` ou PostCSS) **analyse tous tes fichiers HTML/JSX**, trouve toutes les classes comme `text-3xl`, `bg-blue-500`, etc., et **génère dynamiquement le CSS final** contenant **uniquement les classes que tu as utilisées**.

- [Documentation](https://tailwindcss.com/docs/installation/using-vite)
## Ajouter une configuration personnalisée ``


- **In-line Customization**: You can add custom values inline using square brackets for colors, sizes, and other utilities (e.g., `text-[color]`, `p-[size]`).

- **Directives**: Tailwind supports directives like `@apply`, `@layer`, and `@utility` to streamline how styles are applied and organized.
 
    - `import`, `theme`, `utilities`, `variant`, `source`, `reference`, `apply`, `custom variante`

**Example**
Customization directly in CSS file 

```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));

@theme{
        --color-mainBlack: #131316; 
        --color-secondaryBlack: #1c1c21; 
}
```
- [Documentation](https://tailwindcss.com/docs/adding-custom-styles)


- **Component Libraries**: Using libraries like [ShadCN](https://ui.shadcn.com/docs/installation) can enhance your Tailwind experience with pre-defined components that still allow customization.


## Flexbox, Grid et Media Queries <avec Tailwind CSS>


## FLEXBOX

###  Exemple de base

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

###  Propriétés principales

| Classe Tailwind | Fonction (CSS)  |
| --------------- | --------------- |
| `flex`          | `display: flex` |
| `flex-row`      |                 |

| *(default)*               | `flex-direction: row`                      |
| ------------------------- | ------------------------------------------ |
| `flex-col`                | `flex-direction: column`                   |
| `items-center`            | `align-items: center`                      |
| `justify-center`          | `justify-content: center`                  |
| `space-x-*` / `space-y-*` | espace horizontal / vertical entre enfants |
| `gap-*`                   | Espace entre les éléments (`gap`)          |
| `flex-wrap`               | `flex-wrap: wrap`                          |

---

## GRID

###  Exemple simple

```html
<div class="grid grid-cols-3 gap-4">
  <div class="bg-red-500 h-16"></div>
  <div class="bg-blue-500 h-16"></div>
  <div class="bg-green-500 h-16"></div>
</div>
```

### Propriétés importantes

| Classe Tailwind      | Fonction (CSS)                          |
| -------------------- | --------------------------------------- |
| `grid`               | `display: grid`                         |
| `grid-cols-3`        | `grid-template-columns: repeat(3, 1fr)` |
| `col-span-2`         | `grid-column: span 2 / span 2`          |
| `row-span-2`         | `grid-row: span 2 / span 2`             |
| `gap-4`              | `gap: 1rem`                             |
| `place-items-center` | `align-items + justify-items: center`   |

---

## MEDIA QUERIES (Mobile-First)

### Principe fondamental

Tailwind CSS utilise une approche **mobile-first** :

- Styles sans préfixe = s'appliquent aux petits écrans (mobile).
- Ensuite, on **ajoute des préfixes** pour les écrans plus larges : `sm:`, `md:`, etc.

### Breakpoints par défaut

| Préfixe | Min-width | Exemple Tailwind |
| ------- | --------- | ---------------- |
| `sm:`   | `640px`   | `sm:bg-red-500`  |
| `md:`   | `768px`   | `md:text-lg`     |
| `lg:`   | `1024px`  | `lg:grid-cols-4` |
| `xl:`   | `1280px`  | `xl:px-12`       |
| `2xl:`  | `1536px`  | `2xl:text-2xl`   |

> Approche min-width = style appliqué **si l'écran est plus large que la valeur**.

### Exemple

```html
<div class="bg-blue-300 sm:bg-green-400 md:bg-red-500">
  <p class="text-white">Hello world</p>
</div>
```
```jsx
<div class="bg-white sm:bg-amber-500 md:bg-amber-900">
```

<div class="bg-white sm:bg-amber-500 md:bg-amber-900">

-   `bg-white` s’applique **par défaut** (mobile)

-   `sm:bg-amber-500` s’applique **si largeur ≥ 640px**

-   `md:bg-amber-900` s’applique **si largeur ≥ 768px**


**La règle la plus grande écrase les plus petites** si plusieurs sont vraies.

---

##  Utilisation de `max-`

```html
<div class="max-sm:bg-yellow-200 max-md:bg-red-200">
  <p class="text-white">Contenu</p>
</div>
```
```jsx
<div class="max-sm:bg-amber-500 max-md:bg-amber-900">
```

| Préfixe   | Fonction           |
| --------- | ------------------ |
| `max-sm:` | `max-width: 640px` |
| `max-md:` | `max-width: 768px` |

>  Moins utilisé, car **contradiction avec l'approche mobile-first**.
-   `max-sm:` = **s’applique uniquement si largeur ≤ 640px**

-   `max-md:` = **s’applique uniquement si largeur ≤ 768px**

---

## Exemple Responsive avec `flex-col` + `flex-row`

```html
<div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
  <div class="w-full md:w-1/3 bg-blue-500 h-16"></div>
  <div class="w-full md:w-1/3 bg-green-500 h-16"></div>
  <div class="w-full md:w-1/3 bg-red-500 h-16"></div>
</div>
```



## Résumé : Mobile First

```
Mobile (par défaut)
│
├── sm: ≥ 640px
├── md: ≥ 768px
├── lg: ≥ 1024px
├── xl: ≥ 1280px
└── 2xl: ≥ 1536px
```

> N’utilise **jamais **`sm`** pour définir un style mobile**, il est utilisé pour les **écrans au-dessus de mobile**.

### Astuces 

```jsx
<div class="min-h-screen flex flex-col">
  <header class="h-16 bg-blue-500">Header</header>
  <main class="flex-1 bg-white">Contenu qui grandit</main>
  <footer class="h-12 bg-gray-800 text-white">Footer</footer>
</div>
```

-   `min-h-screen` = layout remplit l’écran

-   `flex-col` = empile les sections verticalement

-   `flex-1` = le `main` prend tout l’espace vertical dispo

### Utiliser la structure recommander (ordre logique )
```jsx
<div class="
  [styles de base] 
  sm:[styles sm] 
  md:[styles md] 
  lg:[styles lg]
">
```


### Approche `min-width` (standard)

-   **S'applique quand la largeur est ÉGALE ou SUPÉRIEURE au breakpoint**

-   **Comportement** : "À partir de cette taille et au-dessus"

-   **Logique** : Mobile-first (on part du petit écran et on ajoute pour les grands)


### Approche `max-width` (alternative)

-   **S'applique quand la largeur est INFÉRIEURE au breakpoint**

-   **Comportement** : "Jusqu'à cette taille exclus"

-   **Logique** : Desktop-first (on part du grand écran et on adapte pour les petits)


### Tableau comparatif des breakpoints Tailwind

| Breakpoint | min-width (standard) | max-width (alternative) |
|------------|-----------------------|---------------------------|
| `sm`       | 640px et +            | 0 – 639px                 |
| `md`       | 768px et +            | 0 – 767px                 |
| `lg`       | 1024px et +           | 0 – 1023px                |
| `xl`       | 1280px et +           | 0 – 1279px                |
| `2xl`      | 1536px et +           | 0 – 1535px                |
