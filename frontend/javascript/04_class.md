
javascript, fonction avec les prototypes (systeme)

str >> String.prototpe >> Object.
prototype: en gros, une chaine peut avoir ses propres methodes et ensuiteelle a un protoype qui contient des methodes, et ce prototype aura lui meme les methodesde l'objec => system d'heritage de javascript. 

les classes nous permet de creer nos propres prototypes
        -  le prototype sont des fonctions (typeof)
        - avec static definit des attributs qui seront disponible dans l'object et nonn dans le prototype.
        - extends 
        - redefinition 
        - super keywords
        - #proprietéprivé: acces avec getters et setters (_ par convention) 

---

Étape 6 : Les Classes

Une classe est un modèle pour créer des objets avec des propriétés et des méthodes. Cela permet de mieux structurer le code et de le rendre réutilisable.
1. Définir une classe

On utilise le mot-clé class pour définir une classe. Ensuite, on peut créer des objets basés sur cette classe avec le mot-clé new.

```javascript
class Personne {
    constructor(nom, age) {
        this.nom = nom; // Propriété
        this.age = age; // Propriété
    }

    // Méthode
    saluer() {
        console.log(`Bonjour, je m'appelle ${this.nom} et j'ai ${this.age} ans.`);
    }
}

// Créer un objet
const personne1 = new Personne("Alice", 30);
personne1.saluer(); // Bonjour, je m'appelle Alice et j'ai 30 ans.

const personne2 = new Personne("Bob", 25);
personne2.saluer(); // Bonjour, je m'appelle Bob et j'ai 25 ans.
```
2. Méthodes et propriétés

Les propriétés définissent les caractéristiques d'une classe, tandis que les méthodes définissent les comportements.

    On peut accéder ou modifier les propriétés :

```javascript
personne1.nom = "Charlie";
console.log(personne1.nom); // Charlie
```

3. Héritage

Une classe peut hériter d'une autre, ce qui permet de réutiliser le code.

```javascript
// Classe parent
class Animal {
    constructor(nom) {
        this.nom = nom;
    }

    parler() {
        console.log(`${this.nom} fait un bruit.`);
    }
}

// Classe enfant
class Chien extends Animal {
    parler() {
        console.log(`${this.nom} aboie.`);
    }
}

const animal = new Animal("Créature");
animal.parler(); // Créature fait un bruit.

const chien = new Chien("Rex");
chien.parler(); // Rex aboie.
```
4. Getters et Setters

Les getters et setters permettent de contrôler l'accès aux propriétés.

```javascript
class Cercle {
    constructor(rayon) {
        this.rayon = rayon;
    }

    // Getter
    get diametre() {
        return this.rayon * 2;
    }

    // Setter
    set diametre(valeur) {
        this.rayon = valeur / 2;
    }
}

const cercle = new Cercle(10);
console.log("Diamètre :", cercle.diametre); // 20
cercle.diametre = 50;
console.log("Nouveau rayon :", cercle.rayon); // 25
```
