tape 4 : Structures de Contrôle

Les structures de contrôle permettent de prendre des décisions ou de répéter des actions en fonction de certaines conditions.
1. Conditions : if, else, else if

La condition if exécute un bloc de code si une condition est vraie. On peut utiliser else ou else if pour d'autres cas.

```javascript

let age = 20;

if (age >= 18) {
    console.log("Vous êtes majeur.");
} else {
    console.log("Vous êtes mineur.");
}

let heure = 15;

if (heure < 12) {
    console.log("Bonjour !");
} else if (heure < 18) {
    console.log("Bon après-midi !");
} else {
    console.log("Bonsoir !");
}
```

Top ! Continuons avec les structures de contrôle. 🚦
Étape 4 : Structures de Contrôle

Les structures de contrôle permettent de prendre des décisions ou de répéter des actions en fonction de certaines conditions.
1. Conditions : if, else, else if

La condition if exécute un bloc de code si une condition est vraie. On peut utiliser else ou else if pour d'autres cas.

let age = 20;

if (age >= 18) {
    console.log("Vous êtes majeur.");
} else {
    console.log("Vous êtes mineur.");
}

let heure = 15;

if (heure < 12) {
    console.log("Bonjour !");
} else if (heure < 18) {
    console.log("Bon après-midi !");
}

2. Le switch

Le switch est utile pour comparer une variable à plusieurs valeurs possibles.

```javascript
let jour = "mardi";

switch (jour) {
    case "lundi":
        console.log("Début de la semaine.");
        break;
    case "mardi":
    case "mercredi":
        console.log("Milieu de la semaine.");
        break;
    case "vendredi":
        console.log("Presque le week-end !");
        break;
    default:
        console.log("Jour inconnu.");
}
```





3. Boucles : for, while, do...while

    for : Utilisée pour répéter un bloc un nombre précis de fois.

```javascript
    for (let i = 1; i <= 5; i++) {
    console.log("Itération numéro :", i);
}
```

Le for...of est une boucle en JavaScript qui permet d'itérer sur des éléments d'objets itérables (comme des tableaux, des chaînes de caractères, des ensembles (Set), ou des cartes (Map)). C'est une manière simple et élégante d'accéder directement aux valeurs.
élément : Chaque valeur de l'objet itérable est assignée à cette variable à chaque itération.
iterable : Un objet itérable, comme un tableau, une chaîne de caractères, un Set, ou un Map.
```javascript
const fruits = ["pomme", "banane", "orange"];

for (const fruit of fruits) {
    console.log(fruit);
}
// Résultat :
// pomme
// banane
// orange
```

while : Répète tant qu'une condition est vraie.

```javascript
let compteur = 1;

while (compteur <= 3) {
    console.log("Compteur :", compteur);
    compteur++;
}
```
do...while : Exécute au moins une fois, puis vérifie la condition.

```javascript
let x = 1;

do {
    console.log("Valeur de x :", x);
    x++;
} while (x <= 3);
```
e