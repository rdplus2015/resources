# Promises in JavaScript

## What is a Promise?

A **Promise**  est un **bloc de code** (ou une logique) que tu définis pour exécuter une tâche, souvent asynchrone (comme une requête réseau, une lecture de fichier, etc.).

- **les `Promise` sont asynchrones** : elles s'exécutent **en arrière-plan** pendant que le reste du code continue.
    
-   Tu décides **quoi faire** une fois que cette tâche est terminée, en fonction de son résultat :
    
    -   Si elle réussit (`resolve`), tu utilises `.then()` pour traiter le résultat.
        
    -   Si elle échoue (`reject`), tu utilises `.catch()` pour gérer l'erreur.
    
    -   On peut résoudre avec la fonction `(resolve)` ou rejeter avec la fonction `(reject)` n'importe quelle valeur : Un nombre, une chaîne, un objet, un tableau, même une autre Promesse.

### Syntax:
```javascript
const maPromesse = new Promise((resolve, reject) => {
  // Logique à exécuter
  const succes = true; // Par exemple, une condition
  if (succes) {
    resolve("Ça a marché !"); // La promesse est tenue
  } else {
    reject("Ça a échoué !"); // La promesse est rejetée
  }
});

maPromesse
  .then((resultat) => {
    console.log("Succès :", resultat); // "Succès : Ça a marché !"
  })
  .catch((erreur) => {
    console.error("Erreur :", erreur); // "Erreur : Ça a échoué !"
  });
```
### Example 

```javascript
const maPromesse = new Promise((resolve, reject) => {
    // Opération asynchrone (ex: appel API, lecture de fichier, timeout...)
    setTimeout(() => {
        resolve("Succès !"); // Résolution avec une chaîne
        // reject("Erreur !"); // Rejet avec une chaîne (décommenter pour tester)
    }, 1000);
});
```

#### **2. `.then()` et `.catch()` : Gestion des résultats**

**`.then()`**

-   Reçoit **le 1er argument** (la valeur de `resolve`).

-   Le nom du paramètre est **facultatif** (ici `result`).

    ```javascript
    maPromesse.then((result) => {
        console.log(result); // "Succès !" (valeur passée à resolve())
    });
    ```
    
**`.catch()`**

-   Reçoit **le 2nd argument** (la valeur de `reject`).

-   Le nom du paramètre est **facultatif** (ici `error`).

    ```javascript
        maPromesse.catch((error) => {
        console.error(error); // "Erreur !" (valeur passée à reject())
        });
    ```
-   **`resolve(value)`**: Indicates the promise was successfully completed, passing the result (`value`) to the next `.then()` block.
-   **`reject(error)`**: Indicates the promise failed, passing the error (`error`) to the next `.catch()` block.



### Example complet 1 

```javascript
const asyncOperation = new Promise((resolve, reject) => {
    const success = true; // Changer à false pour tester reject()
    setTimeout(() => {
        if (success) resolve(42); // Nombre arbitraire
        else reject("Échec !");
    }, 1000);
});

asyncOperation
    .then((number) => console.log("Résultat :", number)) // 42
    .catch((message) => console.error("Erreur :", message)); // "Échec !"
```

### Example complet 2

```javascript
function recupererUtilisateur() {
  return new Promise((resolve, reject) => {
    // Simule une requête asynchrone (2 secondes de délai)
    setTimeout(() => {
      const utilisateur = { nom: "Alice", age: 25 }; // Données à retourner
      const requeteReussie = true; // Simule un succès ou un échec

      if (requeteReussie) {
        resolve(utilisateur); // La promesse est tenue avec les données utilisateur
      } else {
        reject("Erreur : Impossible de récupérer l'utilisateur"); // La promesse est rejetée
      }
    }, 2000); // Délai de 2 secondes
  });
}

// Utilisation de la promesse
console.log("1. Avant d'appeler recupererUtilisateur()"); // 1

recupererUtilisateur()
  .then((utilisateur) => {
    console.log("4. Utilisateur récupéré :", utilisateur); // 4 (après 2 secondes)
  })
  .catch((erreur) => {
    console.error("4. Erreur :", erreur); // 4 (en cas d'erreur)
  });

console.log("2. Après avoir appelé recupererUtilisateur()"); // 2

// Simule une autre tâche synchrone
for (let i = 0; i < 3; i++) {
  console.log(`3. Tâche synchrone en cours... (${i + 1}/3)`); // 3
}
```

```bash
1. Avant d'appeler recupererUtilisateur()
2. Après avoir appelé recupererUtilisateur()
3. Tâche synchrone en cours... (1/3)
3. Tâche synchrone en cours... (2/3)
3. Tâche synchrone en cours... (3/3)
4. Utilisateur récupéré : { nom: 'Alice', age: 25 }
```

-   Les étapes **1, 2, et 3** sont **synchrones** et s'exécutent immédiatement.
    
-   La promesse est **asynchrone** : elle attend 2 secondes avant de se résoudre.
    
-   Pendant ces 2 secondes, le code continue à s'exécuter (d'où les messages de la boucle `for`).
    
-   Enfin, la promesse se résout, et le `.then()` ou `.catch()` s'exécute.


## Chaining Promises example 2 

One of the main benefits of using promises is the ability to chain multiple `.then()` methods. Each `.then()` block handles the result of the previous promise and can return a new value to the next `.then()`.

```javascript
let myPromise = new Promise((resolve, reject) => {
    let success = true;

    if (success) {
        resolve("Operation 1 was successful.");
    } else {
        reject("Error in operation 1.");
    }
});

myPromise
    .then(result => {
        console.log(result);  // "Operation 1 was successful."
        return "Operation 2 will start now.";
    })
    .then(result => {
        console.log(result);  // "Operation 2 will start now."
    })
    .catch(error => {
        console.log(error);
    });
```
-   The first `.then()` handles the result of the first operation and passes `(the return)` a new message to the next `.then()`.
-   If any error occurs at any stage, the `.catch()` block will handle it.

#### Example 2 

```javascript
maPromesse
    .then((res) => res.toUpperCase()) // Transforme le résultat
    .then((modifiedRes) => console.log(modifiedRes)) // "SUCCÈS !"
    .catch((err) => console.error(err));
```

## Async/Await: A Syntactic Sugar for Promises

In modern JavaScript, you can use **async/await** to write asynchronous code in a more synchronous-like manner, making it more readable and easier to understand.

### `async` and `await`:

-   **`async`**: est utilisé pour définir une fonction asynchrone. Cela signifie que la fonction peut contenir des opérations qui prennent du temps (comme des appels réseau, des lectures de fichiers, etc.) sans bloquer l'exécution du reste du programme. meaning it will always return a promise.
-   **`await`**: Pauses the execution of the async function until the promise resolves or rejects. le code après await ne s'exécute pas avant que la promesse ne soit résolue

```javascript
function simulerConnexion() {
    return new Promise((resolve, reject) => {
        console.log("Connexion en cours...");
        setTimeout(() => {
            const success = true; // Change à false pour tester le reject
            if (success) {
                resolve("Connecté avec succès !");
            } else {
                reject("Échec de la connexion.");
            }
        }, 2000); // Simule un délai de 2 secondes pour la connexion
    });
}

async function seConnecter() {
    try {
        console.log("Début du programme");

        // "await" attend que la promesse "simulerConnexion" soit résolue ou rejetée
        const resultat = await simulerConnexion();
        console.log(resultat); // Affiche "Connecté avec succès !" si la promesse est résolue

        console.log("Fin du programme");
    } catch (error) {
        console.log("Erreur :", error); // Si la promesse est rejetée, affiche l'erreur
    }
}

seConnecter();
```
```bash
Début du programme
Connexion en cours...
Connecté avec succès !
Fin du programme
``` 
```bash
Début du programme
Connexion en cours...
Erreur : Échec de la connexion.
```





## Notes 
### **Cas 1 : Une Promise sans `await` ni `.then()`**

Si tu crées une fonction qui simule une connexion réseau avec une `Promise` mais que tu **n'utilises ni `await` ni `.then()`**, JavaScript ne va **pas attendre**. Il va continuer à exécuter le reste du code immédiatement.
```javascript
function connect() {
    return new Promise(resolve => {
        console.log("Connexion en cours...");
        setTimeout(() => {
            resolve("Connecté !");
        }, 10000);
    });
}

console.log("Début du programme");
connect(); // Rien ne force l'attente ici
console.log("Fin du programme");
``` 
```bash
Début du programme
Connexion en cours...
Fin du programme
``` 
Ici, **JavaScript ne bloque pas l'exécution** et continue tout de suite sans attendre la fin de la connexion. La `Promise` est bien **asynchrone**, mais personne ne s'occupe de son résultat.


### **Cas 2 : Utiliser `.then()`**

Avec `.then()`, on **attend le résultat** mais sans bloquer le reste du code.

```javascript
console.log("Début du programme");

connect().then(result => {
    console.log(result); // S'exécute après 10 sec
});

console.log("Fin du programme");
```
```bash
Début du programme
Connexion en cours...
Fin du programme
(10 sec plus tard...)
Connecté !
```
Ici, la connexion est **mise de côté**, et le programme continue jusqu'à `"Fin du programme"`, puis quand la `Promise` est résolue, `"Connecté !"` s'affiche.


### **Cas 3 : Utiliser `await`**

Si on met `await`, JavaScript va attendre que la `Promise` soit résolue **avant** de passer à la ligne suivante, **mais sans bloquer tout le programme**.

```javascript
async function main() {
    console.log("Début du programme");
    let result = await connect(); // Ici, on attend la fin de la connexion
    console.log(result);
    console.log("Fin du programme");
}

main();
```
```bash
Début du programme
Connexion en cours...
(10 sec plus tard...)
Connecté !
Fin du programme
```

Ici, `"Fin du programme"` n'apparaît **qu'après la fin de la connexion**, car `await` **suspend** l'exécution de la fonction `main()` en attendant le résultat.

--- 

## Resumé 

### Resolve, Reject, Resultat, Error 


Dans une promesse, `resolve` est à la fois un **paramètre de la fonction callback** et **une fonction fournie automatiquement par JavaScript**. Lorsqu'on crée une promesse, JavaScript passe cette fonction en argument à la callback. On pourrait renommer ce paramètre comme `res` ou autre, car **son nom n'a pas d'importance** : ce qui compte, c'est que JavaScript comprend ce paramètre comme une fonction et l'utilise pour signaler la résolution de la promesse.

Dans une promesse :

-   **Le premier paramètre**, souvent nommé `resolve`, est utilisé pour indiquer que l'opération asynchrone s'est bien terminée avec succès.
-   **Le deuxième paramètre**, `reject`, sert à signaler une erreur ou un échec de l'opération.

`resolve` et `reject` permettent de contrôler l'état d'une promesse et de transmettre un résultat ou une erreur. Ces valeurs sont ensuite récupérées :

-   **Dans `.then()`** pour gérer le succès, via un paramètre (`resultat`) passé à la callback.
-   **Dans `.catch()`** pour gérer les erreurs, via un paramètre (`erreur`) passé à la callback.


### Async / wait 

Le but de `async`/`await` est de **simplifier la gestion du code asynchrone**. Plus besoin de créer des promesses explicitement partout ni de gérer les `.then()` et `.catch()` enchaînés. Avec `async`/`await`, on peut écrire du code **de manière plus linéaire et lisible** tout en exécutant des opérations asynchrones.

Lorsqu'une fonction est déclarée avec `async`, elle **retourne toujours une promesse**. Cela signifie que tu peux l'utiliser avec `await` à l'intérieur d'une autre fonction `async`, ce qui permet d'exécuter du code de manière plus fluide et synchrone en apparence, sans avoir à manipuler directement les `.then()` et `.catch()`.

**`async`/`await` est une approche plus moderne et lisible pour gérer les promesses.**

Cependant, si tu appelles une fonction `async` dans le programme principal **sans utiliser `await` ou `.then()`**, **rien ne s'affichera immédiatement** car la fonction retournera une promesse qui ne sera pas consommée. Pour voir le résultat, il faut soit attendre explicitement avec `await` dans une fonction `async`, soit gérer la promesse avec `.then()`.


## others promise methodes 

 l'objet Promise en JavaScript possède plusieurs méthodes qui permettent de gérer plusieurs promesses en parallèle, de manière à combiner ou suivre la résolution de plusieurs promesses simultanément.

#### **`Promise.all()`**

-   **Fonctionnement :** Cette méthode prend un tableau de promesses et renvoie une **nouvelle promesse** qui est résolue lorsque **toutes les promesses** dans le tableau sont résolues. Si **une seule promesse échoue (rejette)**, la promesse retournée par `Promise.all()` sera rejetée immédiatement.

#### 2. **`Promise.allSettled()`**

-   **Fonctionnement :** Cette méthode prend un tableau de promesses et renvoie une promesse qui est **résolue lorsque toutes les promesses** sont terminées, qu'elles soient résolues ou rejetées. Elle retourne un tableau d'objets qui décrivent l'état de chaque promesse (résolue ou rejetée).

#### 3. **`Promise.any()`**

-   **Fonctionnement :** Cette méthode prend un tableau de promesses et renvoie une promesse qui est résolue **dès qu'une seule promesse** est résolue. Si **toutes les promesses échouent**, alors la promesse retournée sera rejetée.
 
 #### 4. **`Promise.race()`**

-   **Fonctionnement :** Cette méthode prend un tableau de promesses et renvoie une promesse qui est résolue **dès qu'une promesse** parmi le tableau est résolue ou rejetée. Elle retourne **la première promesse** qui termine (résolue ou rejetée), les autres sont ignorées.
