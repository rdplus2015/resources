# Notes sur React JSX et les composants

## Syntaxe JSX

- Le JSX est du JavaScript classique qui permet d'ajouter du HTML
- Il sera converti en syntaxe JavaScript normale par Babel
- Les attributs sont écrits en camelCase (exceptions : `aria-*` et `data-*`)
- `class` s'écrit `className` (pour éviter les conflits avec le mot-clé `class` en JS)
- Le style s'écrit sous forme d'objet avec propriétés CSS en camelCase :
  ```jsx
  <div style={{width: 50, height: 50, backgroundColor: 'blue'}}/>
  ```
-  Fermeture de balise obligatoire
- En React, chaque composant doit retourner un seul élément racine `(ex: div)`  ou utiliser un Fragment (`<></>` ou `<Fragment></Fragment>`) qui n'ajoute rien dans le DOM, mais permet quand même d’avoir un `élément parent virtuel`

## Interpolation de variables

- Dans du JSX, on ouvre du JavaScript dans ton HTML. 
- Tout ce qui est entre `{ ... }` est du code JavaScript.

```jsx
const text = 'Hello les gens'
const id = 'monId'

export function App() {
    return <h1 id={id}>{text}</h1>
}
```
## Style 
- Le style de React attend un `objet JS`.
- Les **propriétés CSS** deviennent du **camelCase** (`background-color` → `backgroundColor`)
-   Les **valeurs** sont des **chaînes de caractères** (sauf pour les nombres sans unité)

```jsx
<h1 id={id} style={{color: 'red'}}>{text}</h1>

// Ou avec un objet séparé
const style = {color: 'red'}
<h1 id={id} style={style}>{text}</h1>
```

## Gestion des événements
les événements directement dans les balises JSX, en camelCase, avec une fonction JS.

```jsx
function App() {
  const handleClick = () => {
    alert("Clic détecté !");
  };

  return <button onClick={handleClick}>Clique-moi</button>;
}
```
Tu peux aussi mettre une fonction inline :
```jsx
<button onClick={() => alert('Salut !')}>Clique</button>
```
Mais pour garder ton code propre et performant, on conseille plutôt de définir la fonction en dehors du JSX, comme dans l’exemple précédent.


- Les noms d’événements sont en camelCase : `onClick`, `onChange`, `onSubmit`, `onMouseEnter`, etc.
- Tu donnes une **fonction** (ou une fonction fléchée) comme valeur.
- Vous pouvez explorer les **autres types d’événements** (`onChange`, `onMouseEnter`, `onKeyDown`

### Les événements en React sont "synthetic"
- React **n’utilise pas directement les événements natifs** du navigateur.  
  Il les **entoure** avec un objet appelé **SyntheticEvent**.
- Cela permet à React de rendre la gestion d'événements **uniforme et cohérente**, quelle que soit la plateforme :
  -   navigateur web (React DOM)
  -   application mobile (React Native)
  -   ou autre environnement
  - Tu peux utiliser des méthodes comme `e.preventDefault()` et `e.stopPropagation()`, tout comme avec les événements natifs.
  - `e.nativeEvent` → pour récupérer l’événement **brut** du navigateur


```jsx
export function App () {
  const doSomething = (e) => {
    e.preventDefault();      // Empêche l'envoi réel du formulaire
    e.stopPropagation();     // Empêche la propagation de l'événement
  };

  return <form onSubmit={doSomething}>Bonjour les gens</form>;
}
```
### Le handler reçoit automatiquement l’événement en paramètre
```jsx
function App() {
  const handleClick = (event) => {
    console.log('Événement reçu :', event);
    console.log('Cible :', event.target);
  };

  return <button onClick={handleClick}>Clique-moi</button>;
}
```

Le `event` ici est un **objet `SyntheticEvent`** (événement synthétique), mais il a **presque toutes les mêmes méthodes** que les événements natifs :
### Propriétés & méthodes utiles :

- `e.target` → l’élément HTML qui a déclenché l’événement
- `e.currentTarget` → l’élément sur lequel l’événement est actuellement attaché
- `e.preventDefault()` → empêche le comportement par défaut (ex : rechargement d’un formulaire)
- `e.stopPropagation()` → empêche la remontée de l’événement dans le DOM
- `e.nativeEvent` → l’événement natif brut du navigateur


### Liste des événements React les plus courants

| Type d’événement       | Attribut React               | Exemple JSX                       |
|------------------------|------------------------------|-----------------------------------|
| **Clic**               | `onClick`                    | `<button onClick={...} />`       |
| **Saisie clavier**     | `onKeyDown`, `onKeyUp`       | `<input onKeyDown={...} />`      |
| **Saisie formulaire**  | `onChange`                   | `<input onChange={...} />`       |
| **Envoi de formulaire**| `onSubmit`                   | `<form onSubmit={...} />`        |
| **Souris**             | `onMouseEnter`, `onMouseLeave`, `onMouseMove` | `<div onMouseMove={...} />` |
| **Focus / Blur**       | `onFocus`, `onBlur`          | `<input onBlur={...} />`         |
| **Contexte (clic droit)** | `onContextMenu`           | `<div onContextMenu={...} />`    |
| **Drag & Drop**        | `onDragStart`, `onDrop`, `onDragOver` | `<div onDrop={...} />`     |
| **Double clic**        | `onDoubleClick`              | `<div onDoubleClick={...} />`    |
| **Copier / Coller**    | `onCopy`, `onPaste`, `onCut` | `<input onPaste={...} />`        |
| **Scroll**             | `onScroll`                   | `<div onScroll={...} />`         |
| **Touch (mobile)**     | `onTouchStart`, `onTouchEnd`, `onTouchMove` | `<div onTouchStart={...} />` |
| **Animation / Transition** | `onAnimationEnd`, `onTransitionEnd` | `<div onAnimationEnd={...} />` |

## Conditions et rendu conditionnel
En React, **tu ne peux pas utiliser directement des `if` dans le JSX**, car le JSX ne permet que des **expressions**, pas des **instructions** comme `if` ou `for`.

### Méthodes courantes

```jsx
// 1. Opérateur logique &&
{isVisible && <Modal/>}

<div>
    {isLoading && <Spinner />}
    {!isLoading && <Data />}
</div>

// 2. Ternaire
{hasError ? <ErrorMsg/> : <SuccessMsg/>}

// 3. Variables intermédiaires (VERSION COURTE)
let content
if (isLoading) content = <Spinner/>
else content = <Data/>
return <div>{content}</div>
```



---

### Ce qui fonctionne

#### Variables intermédiaires (style JS classique :VERSION LONGUE)

```jsx
function App() {
  let content;

  if (isLoading) {
    content = <Spinner />;
  } else {
    content = <Data />;
  }

  return <div>{content}</div>;
}
```

>  C’est **clair**, **lisible** et très utilisé pour des conditions un peu longues.

###  Ce qui ne fonctionne PAS

```jsx
return (
  <div>
    { if (isLoading) { return <Spinner /> } } //  ERREUR !
  </div>
);
```

> ❌ JSX n’autorise pas les instructions `if` directement à l’intérieur d’un bloc `{}`.

---

### Résumé 
| Méthode                      | Valide en React ? | Utilisation recommandée |
|-----------------------------|-------------|--------------------------|
| `if/else` en dehors du JSX  |  Oui        | Lisibilité, logique claire |
| Ternaires `? :`             | Oui         | Conditions simples dans le JSX |
| `&&` logique                | Oui         | Pour un seul composant conditionnel |
| `if` dans `{}` dans JSX     |  Non        | JSX ne permet pas les instructions |


## Utilisation de `map()` pour un rendu dynamique

-   C’est une méthode JavaScript qui permet de **transformer un tableau** en un **autre tableau**.
-   cette fonction prend un tableau en entrer et pour chaque element de ce tableau elle effectue une fonction de transformation
-   En React, on l’utilise pour **générer dynamiquement plusieurs composants JSX**.

React **a besoin d’une clé unique** pour chaque élément d’une liste. Cela lui permet de :
-   Savoir quels éléments ont changé, été ajoutés ou supprimés
-   Optimiser le **Virtual DOM**

> Dans ce cas : `todos.map(...)` retourne une liste de `<li>...</li>` dynamiques.

```jsx
// Un tableau de chaînes de caractères (simule une liste de tâches)
const todos = [
  'Tâche 1',
  'Tâche 2',
  'Tâche 3'
];

export function App() {
  return (
    <>
      <h1>Ma todolist</h1>
      <ul>
        {todos.map(todo => (
          <li key={todo}>{todo}</li>
        ))}
      </ul>
    </>
  );
}
```

## Composants fonctionnels en React

###  Un composant = Une fonction

En React, un **composant** est simplement une **fonction JavaScript** qui recoit plusieurs attributs sous forme `d'objet` et  retourne du **JSX**.  
Il doit être **nommé en PascalCase** (ex: `Title`, `MonComposant`, `UserCard`).

---

###  Exemple de base

```jsx
function Title({ color, children }) {
  return <h1 style={{ color: color }}>{children}</h1>;
}
```

> Ici, on utilise la **déstructuration** dans les paramètres pour récupérer directement ce dont on a besoin depuis `props`.

- **Les **props** (abréviation de **properties**) sont un **objet** passé à un composant React lorsqu’il est utilisé.Ce sont les **paramètres d'entrée** d'un composant, comme les paramètres d’une fonction.**
### Variante sans déstructuration

```jsx
function Title(props) {
  return <h1 style={{ color: props.color }}>{props.children}</h1>;
}
```

>  Fonctionne aussi, mais moins lisible quand il y a beaucoup de props.

- **Tu peux envoyer autant de props que tu veux, même si tu ne les as pas toutes listées dans la déstructuration.**
- **Example**
```jsx
function Title({ color }) {
  console.log("props color:", color);
  return (<h1 style={{ color }}>Hello +</h1>);
}

<Title color="blue" size="large"  className="titre" />
```

-   Ici, `Title` **reçoit aussi** `size` et `className`, **mais ne les utilise pas**.
-   **Aucune erreur !** React n’est pas strict : **tu choisis ce que tu utilises.**


### Accéder à toutes les props
Tu peux ne pas déstructurer et garder l’objet entier : 

```jsx
function Title(props) {
  console.log(props); // { color: "blue", size: "large", className: "titre" }
  return <h1 style={{ color: props.color }}>{props.children}</h1>;
}
```

### Utilisation de `...props` (spread operator)

En utilisant props, on accède à toutes les propriétés passées au composant, mais on doit les extraire une à une via props.nomAttribut, ce qui est moins lisible.
Avec la déstructuration, on accède directement aux attributs spécifiés dans les paramètres de la fonction, mais on n'a accès qu'à ceux qu’on a explicitement nommés.
Pour combiner les deux, on peut utiliser la déstructuration avec le spread operator ...props afin de récupérer à la fois les attributs nécessaires et tout le reste que l’utilisateur pourrait passer.

```jsx
function Title({ color, children, ...props }) {
  return <h1 style={{ color }} {...props}>{children}</h1>;
}
```
-   Tu prends `color` et `children`,
-   Et tu récupères **toutes les autres props restantes** dans `props` (comme `className`, `id`, `onClick`...),
-   Puis tu les **injectes** dans la balise via `{...props}` → super utile !

##  Utilisation comme un élément HTML personnalisé

```jsx
export function App() {
  return (
    <>
      <Title color="red">Ceci est un titre</Title>
      <p>Premier paragraphe</p>
    </>
  );
}
```

> Tu peux insérer `<Title>` comme si c'était une balise HTML. C’est ce qui rend React puissant et modulaire.


---

## Avantage du découpage en composants

- Réduction des répétitions
- Réutilisabilité du code
- Meilleure organisation de l’interface
- Plus simple à maintenir/tester

---


### Résumé

| Concept               | Explication |
|------------------------|-------------|
| Fonction = composant   | En PascalCase |
| `props`                | Objet contenant tous les attributs passés au composant |
| `children`             | Ce qu’on écrit entre `<Title> ... </Title>` |
| Déstructuration        | Récupérer directement les valeurs utiles dans les paramètres |
| `...props`             | Capturer toutes les props restantes |

---
