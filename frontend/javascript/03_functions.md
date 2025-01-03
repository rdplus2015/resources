Étape 5 : Fonctions

Les fonctions permettent de regrouper des blocs de code réutilisables. On peut les définir, les appeler avec des paramètres, et récupérer des valeurs grâce à un retour.


1. Définir et appeler une fonction

Une fonction est définie avec le mot-clé function :

```javascript
// Définition
function saluer() {
    console.log("Bonjour !");
}

// Appel
saluer();
```
2. Fonction avec paramètres

Les fonctions peuvent accepter des paramètres pour personnaliser leur comportement :

```javascript
function saluerUtilisateur(nom) {
    console.log(`Bonjour, ${nom} !`);
}

saluerUtilisateur("Alice"); // Bonjour, Alice !
saluerUtilisateur("Bob");   // Bonjour, Bob !
```
3. Fonction avec une valeur de retour

On utilise return pour renvoyer une valeur :

```javascript
function addition(a, b) {
    return a + b;
}

let resultat = addition(5, 3);
console.log("Résultat :", resultat); // 8
```

Génial, passons maintenant aux fonctions en JavaScript ! 🎯
Étape 5 : Fonctions

Les fonctions permettent de regrouper des blocs de code réutilisables. On peut les définir, les appeler avec des paramètres, et récupérer des valeurs grâce à un retour.
1. Définir et appeler une fonction

Une fonction est définie avec le mot-clé function :
```javascript
// Définition
function saluer() {
    console.log("Bonjour !");
}

// Appel
saluer();

2. Fonction avec paramètres

Les fonctions peuvent accepter des paramètres pour personnaliser leur comportement :

function saluerUtilisateur(nom) {
    console.log(`Bonjour, ${nom} !`);
}

saluerUtilisateur("Alice"); // Bonjour, Alice !
saluerUtilisateur("Bob");   // Bonjour, Bob !

3. Fonction avec une valeur de retour

On utilise return pour renvoyer une valeur :

function addition(a, b) {
    return a + b;
}

let resultat = addition(5, 3);
console.log("Résultat :", resultat); // 8

4. Fonctions fléchées (arrow functions)

Syntaxe simplifiée pour les fonctions :
```

```javascript
// Fonction classique
function multiplier(x, y) {
    return x * y;
}

// Fonction fléchée
const multiplier2 = (x, y) => x * y;

console.log(multiplier(2, 3));  // 6
console.log(multiplier2(4, 5)); // 20
```

- les fonction peut etre appeler avant leurs definition (meme s'il sont dans un bloc if ), car javascript en eecute va d'abord commencer par chercher la definitio et puis effectuer son appl. a l'exception que la fonction ne  soit pas dans une variable
        - utiliser la definition sans varibale pour les fonctions qu'on souhaite utilisé globalement dans tout le systeme et avec une variable pour les fonctions qui  doivent etre utilsé dans une boucle ou dans une condtion 

- la fonction a la capacité de modifier une varaible definit a l'eterieur (attention au variable qui a le meme om que le parametre, il modifiera le parametre)

-en passant un tableau  ou un object a une fonction en parametre, la fonction modifiera le parametre ainsi que lestableaux ou l'object d'origine 

- on peut appeler une fonctionn sans rien lui passer en parametre et utilisé this, qui fait reference a l'object 

-fonction fléché 
-  le this est souvent utilisé avec les classes 

```javascript
// Fonction pour calculer l'aire d'un rectangle
function calculerAire(longueur, largeur) {
    return longueur * largeur;
}

let aire = calculerAire(5, 3);
console.log("Aire du rectangle :", aire); // 15

// Fonction pour afficher un message personnalisé
const afficherMessage = (prenom, age) => {
    console.log(`Salut ${prenom}, tu as ${age} ans.`);
};

afficherMessage("Jean", 25); // Salut Jean, tu as 25 ans.

// Fonction pour vérifier si un nombre est pair
const estPair = (nombre) => nombre % 2 === 0;

console.log("4 est pair :", estPair(4)); // true
console.log("7 est pair :", estPair(7)); // false
```

# JavaScript Methods: A Comprehensive Guide

## 1. **Array Methods**

### a. Manipulation des éléments
- **`push()`**: Ajoute un ou plusieurs éléments à la fin du tableau.
```javascript
let fruits = ["pomme", "banane"];
fruits.push("orange");
console.log(fruits); // ["pomme", "banane", "orange"]
```

- **`pop()`**: Supprime le dernier élément du tableau.
```javascript
fruits.pop();
console.log(fruits); // ["pomme", "banane"]
```

- **`shift()`**: Supprime le premier élément du tableau.
```javascript
fruits.shift();
console.log(fruits); // ["banane"]
```

- **`unshift()`**: Ajoute un ou plusieurs éléments au début du tableau.
```javascript
fruits.unshift("fraise");
console.log(fruits); // ["fraise", "banane"]
```

### b. Tri et inversion
- **`sort()`**: Trie les éléments du tableau (ordre lexicographique par défaut).
```javascript
let nombres = [10, 3, 25, 1];
nombres.sort();
console.log(nombres); // [1, 10, 25, 3]
```
*Utilisation avec fonction de comparaison pour tri numérique :*
```javascript
nombres.sort((a, b) => a - b); // Tri croissant
console.log(nombres); // [1, 3, 10, 25]
```

- **`reverse()`**: Inverse l'ordre des éléments.
```javascript
nombres.reverse();
console.log(nombres); // [25, 10, 3, 1]
```

### c. Transformations
- **`join()`**: Combine les éléments en une seule chaîne.
```javascript
let mots = ["Bonjour", "tout", "le", "monde"];
let phrase = mots.join(" ");
console.log(phrase); // "Bonjour tout le monde"
```

- **`slice()`**: Extrait une portion d'un tableau.
```javascript
let fruits = ["pomme", "banane", "orange", "kiwi"];
console.log(fruits.slice(1, 3)); // ["banane", "orange"]
```

- **`splice()`**: Ajoute, remplace ou supprime des éléments.
```javascript
fruits.splice(1, 1, "mangue");
console.log(fruits); // ["pomme", "mangue", "orange", "kiwi"]
```

---

## 2. **String Methods**

### a. Manipulation des chaînes
- **`split()`**: Divise une chaîne en un tableau.
```javascript
let phrase = "Bonjour tout le monde";
let mots = phrase.split(" ");
console.log(mots); // ["Bonjour", "tout", "le", "monde"]
```

- **`concat()`**: Combine des chaînes.
```javascript
let salut = "Bonjour";
let nom = "Alice";
console.log(salut.concat(", ", nom)); // "Bonjour, Alice"
```

### b. Recherche
- **`indexOf()`**: Trouve l'index de la première occurrence d'une sous-chaîne.
```javascript
console.log("Bonjour tout le monde".indexOf("tout")); // 8
```

- **`includes()`**: Vérifie si une chaîne contient une sous-chaîne.
```javascript
console.log("Bonjour tout le monde".includes("tout")); // true
```

---

## 3. **Number Methods**

- **`toFixed()`**: Formate un nombre avec un nombre fixe de décimales.
```javascript
let num = 42.678;
console.log(num.toFixed(2)); // "42.68"
```

- **`parseInt()`**: Convertit une chaîne en entier.
```javascript
let nombre = parseInt("42");
console.log(nombre); // 42
```

- **`parseFloat()`**: Convertit une chaîne en nombre décimal.
```javascript
let nombre = parseFloat("42.5");
console.log(nombre); // 42.5
```

---

## 4. **Object Methods**

### a. Récupérer les clés et les valeurs
- **`Object.keys()`**: Retourne un tableau des clés d'un objet.
```javascript
let utilisateur = { nom: "Alice", age: 30 };
console.log(Object.keys(utilisateur)); // ["nom", "age"]
```

- **`Object.values()`**: Retourne un tableau des valeurs d'un objet.
```javascript
console.log(Object.values(utilisateur)); // ["Alice", 30]
```

- **`Object.entries()`**: Retourne un tableau de paires clé-valeur.
```javascript
console.log(Object.entries(utilisateur)); // [["nom", "Alice"], ["age", 30]]
```

### b. Copier des objets
- **`Object.assign()`**: Copie les propriétés d'un ou plusieurs objets dans un autre objet.
```javascript
let cible = {};
let source = { a: 1, b: 2 };
Object.assign(cible, source);
console.log(cible); // { a: 1, b: 2 }
```

- **`Object.freeze()`**: Empêche les modifications d'un objet.
```javascript
let obj = { a: 1 };
Object.freeze(obj);
obj.a = 2; // Erreur en mode strict
console.log(obj.a); // 1
```

---

## 5. **Math Methods**

- **`Math.random()`**: Génère un nombre aléatoire entre 0 (inclus) et 1 (exclus).
```javascript
let aleatoire = Math.random();
console.log(aleatoire);
```

- **`Math.round()`**: Arrondit au plus proche entier.
```javascript
console.log(Math.round(4.6)); // 5
```

- **`Math.max()`** et **`Math.min()`**: Trouve le plus grand ou le plus petit nombre.
```javascript
console.log(Math.max(1, 2, 3)); // 3
console.log(Math.min(1, 2, 3)); // 1
```

---

## 6. **Interaction avec l'utilisateur**

- **`prompt()`**: Demande une entrée utilisateur (navigateur uniquement).
```javascript
let nom = prompt("Quel est votre nom ?");
console.log(`Bonjour, ${nom} !`);
```

- **`alert()`**: Affiche une boîte de message.
```javascript
alert("Ceci est une alerte !");
```

- **`confirm()`**: Demande une confirmation (retourne `true` ou `false`).
```javascript
let reponse = confirm("Voulez-vous continuer ?");
console.log(reponse); // true ou false
```

---

## 7. **Boucles et Itérations**

### a. `forEach()`
Applique une fonction à chaque élément d'un tableau.
```javascript
let nombres = [1, 2, 3];
nombres.forEach((nombre) => {
    console.log(nombre * 2);
});
```

### b. `map()`
Retourne un nouveau tableau avec les résultats d'une fonction appliquée à chaque élément.
```javascript
let doubles = nombres.map((nombre) => nombre * 2);
console.log(doubles); // [2, 4, 6]
```

---

Ce fichier regroupe les méthodes les plus courantes et utiles en JavaScript. Si tu souhaites approfondir une méthode ou en tester certaines, fais-moi signe !

