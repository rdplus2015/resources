
## **4. Interfaces**

### Définition

-   Une **interface** définit un contrat : toutes les méthodes sont implicitement publiques et abstraites.
-   Une classe peut implémenter plusieurs interfaces.

```java
public interface Animal {
    void makeSound(); // Méthode abstraite et publique par défaut
}

public interface Pet {
    void play();
}

public class Dog implements Animal, Pet {
    @Override
    public void makeSound() {
        System.out.println("Le chien aboie.");
    }

    @Override
    public void play() {
        System.out.println("Le chien joue.");
    }
}

```

### Points Clés

-   Toutes les méthodes d’une interface sont implicitement **public** et **abstract**.
-   Les attributs d’une interface sont implicitement **public static final**.
-   Une classe peut implémenter plusieurs interfaces avec le mot-clé **`implements`**.



Dans une interface, jusqu'à Java 7, toutes les méthodes étaient implicitly abstractes et ne pouvaient pas avoir de corps. À partir de Java 8, il est possible de définir des méthodes par défaut dans les interfaces avec une implémentation :
```java
interface Animal {
    default void manger() {
        System.out.println("L'animal mange");
    }
    void faireDuBruit(); // Toujours abstraite
}

```
Une interface ne peut pas avoir de constructeur, car elle ne peut pas être instanciée directement.
Les interfaces exigent que les méthodes soient public, car les méthodes dans une interface sont implicitement publiques, quel que soit leur modificateur.









Les classes abstraites et les interfaces peuvent sembler similaires parce qu'elles imposent toutes deux des méthodes à implémenter dans les classes dérivées, mais elles ont des usages différents. Une classe abstraite est plus appropriée lorsqu'on a besoin de partager des comportements et des états communs, tandis qu'une interface est idéale pour découpler des fonctionnalités et permettre une extension multiple des comportements.


Qu’est-ce qu’une interface et une implémentation ?

    Une interface en Java est comme un contrat qui définit ce que quelque chose peut faire (les méthodes qu’elle offre), sans dire comment cela fonctionne en interne.
    Une implémentation, par contre, est la manière concrète dont ce contrat est respecté, avec un code qui réalise effectivement les méthodes définies dans l’interface.

En Java, cela correspond à l’interface List :

List<String> listeDeCourses;

Ici, List est le contrat : il dit "cette chose peut ajouter, retirer et lire des éléments".

L’implémentation concrète :

    Maintenant, pour faire ta liste, tu peux choisir d'utiliser :
        Une feuille de papier (correspond à ArrayList).
        Un tableau blanc (correspond à LinkedList).
    Les deux suivent le même contrat (ajouter, retirer, lire), mais leurs façons de fonctionner sont différentes.

En Java, cela donne :

List<String> listeDeCourses = new ArrayList<>();

Ici, tu dis :

    "Je veux une liste (abstraite)."
    "Je vais utiliser une ArrayList (implémentation concrète)."

Pourquoi séparer interface et implémentation ?

    Flexibilité : Si tu as utilisé List comme type, tu peux facilement changer l'implémentation sans changer le reste de ton code :


Interface vs Classe Abstraite : Quand utiliser l’une plutôt que l’autre ?

    Une interface définit uniquement des méthodes abstraites (sans implémentation) et peut être implémentée par n'importe quelle classe. Une interface est comme un contrat que tu donnes à une classe pour qu’elle implémente des méthodes spécifiques.

    Une classe abstraite peut définir des méthodes abstraites (comme une interface), mais elle peut aussi fournir des méthodes concrètes (avec implémentation). Une classe abstraite est plus comme une base partagée d’où d’autres classes peuvent hériter, tout en ayant des comportements par défaut ou des fonctionnalités communes.

Différences entre Interface et Classe Abstraite
Caractéristique	Interface	Classe Abstraite
Méthodes	Toutes les méthodes sont abstraites (avant Java 8)	Peut avoir des méthodes abstraites et concrètes
Héritage	Une classe peut implémenter plusieurs interfaces (héritage multiple)	Une classe peut hériter d'une seule classe abstraite
Constructeur	Pas de constructeur (pas d'état propre)	Peut avoir un constructeur pour initialiser des données
Utilisation principale	Pour des contrats et des comportements généraux	Pour réutiliser du code et partager des comportements communs
(tableau)


```java
interface Deplacable {
    void deplacer();  // La méthode est abstraite, sans implémentation
}

class Voiture implements Deplacable {
    @Override
    public void deplacer() {
        System.out.println("La voiture roule !");
    }
}

class Avion implements Deplacable {
    @Override
    public void deplacer() {
        System.out.println("L'avion vole !");
    }
}

```
Ici, Deplacable est une interface. Les classes Voiture et Avion doivent implémenter la méthode deplacer, car c’est exigé par l’interface. Une interface est utile quand tu veux imposer un comportement commun à toutes les classes qui l'implémentent, mais sans fournir de logique commune dans l'interface.
2. Classe Abstraite : Utilisation de logique partagée

lasses, tu utiliserais une classe abstraite :

abstract class Vehicule {
String modele;

    Vehicule(String modele) {
        this.modele = modele;
    }
    
    // Méthode concrète (avec implémentation)
    void afficherModele() {
        System.out.println("Modèle : " + modele);
    }
    
    // Méthode abstraite (sans implémentation)
    abstract void deplacer();
}

class Voiture extends Vehicule {
Voiture(String modele) {
super(modele);
}

    @Override
    void deplacer() {
        System.out.println("La voiture roule !");
    }
}

class Avion extends Vehicule {
Avion(String modele) {
super(modele);
}

    @Override
    void deplacer() {
        System.out.println("L'avion vole !");
    }
}

Ici, Vehicule est une classe abstraite qui contient une méthode concrète (afficherModele()) pour afficher le modèle du véhicule. Elle contient également une méthode abstraite (deplacer()), que chaque sous-classe doit implémenter. La classe Vehicule donne une base de fonctionnalités communes (comme la gestion du modèle), mais chaque type de véhicule peut définir son propre comportement pour la méthode deplacer().



    Utiliser une interface :
        Si tu veux définir un contrat que plusieurs classes doivent suivre, mais sans partager de code commun.
        Si tu veux hériter de plusieurs interfaces (Java permet l’héritage multiple d'interfaces, mais pas de classes).
    Utiliser une classe abstraite :
        Si tu veux partager du code entre plusieurs classes tout en forçant certaines méthodes à être définies dans les sous-classes.
        Si tu veux utiliser un constructeur pour initialiser des variables communes.

Quand choisir une interface ou une classe abstraite ?

    Utiliser une interface :
        Si tu veux définir un contrat que plusieurs classes doivent suivre, mais sans partager de code commun.
        Si tu veux hériter de plusieurs interfaces (Java permet l’héritage multiple d'interfaces, mais pas de classes).
    Utiliser une classe abstraite :
        Si tu veux partager du code entre plusieurs classes tout en forçant certaines méthodes à être définies dans les sous-classes.
        Si tu veux utiliser un constructeur pour initialiser des variables communes.

3. Quand utiliser une classe abstraite ?

Une classe abstraite est idéale dans les cas suivants :

    Partage d'implémentation : Lorsqu'il y a des comportements partagés entre plusieurs sous-classes, mais que vous voulez forcer certaines méthodes à être implémentées.

    Héritage simple : Lorsque vous souhaitez qu'une classe dérivée hérite de comportements partagés et vous permette de définir certains comportements par défaut (méthodes concrètes).

    Maintenir un état interne commun : Lorsqu'il est nécessaire d'avoir des attributs partagés entre les sous-classes, comme des variables d'instance.

    Contrat avec implémentation partielle : Lorsque vous voulez fournir une implémentation de certaines méthodes, mais laisser d'autres méthodes abstraites pour être définies dans les sous-classes.

2. Quand utiliser une interface ?

Une interface est idéale dans les cas suivants :

    Contrat sans implémentation : Lorsqu'il s'agit de définir un contrat sans imposer une implémentation concrète. Par exemple, si vous voulez définir des comportements attendus par différentes classes mais que chaque classe les implémente de manière différente (sans nécessité d'héritage).

    Héritage multiple : Lorsque vous souhaitez qu'une classe puisse implémenter plusieurs comportements différents venant de différentes interfaces.

    Abstraction totale : Lorsqu'il n'y a pas d'implémentation commune


good example : 
```java
// Interface Voiture
interface Voiture {
    void démarrer();
    void arrêter();
}

// Classe VoitureManuelle implémentant Voiture
class VoitureManuelle implements Voiture {
    @Override
    public void démarrer() {
        System.out.println("Voiture manuelle démarre.");
    }

    @Override
    public void arrêter() {
        System.out.println("Voiture manuelle s'arrête.");
    }
}

// Classe VoitureAutomatique implémentant Voiture
class VoitureAutomatique implements Voiture {
    @Override
    public void démarrer() {
        System.out.println("Voiture automatique démarre.");
    }

    @Override
    public void arrêter() {
        System.out.println("Voiture automatique s'arrête.");
    }
}

public class Main {
    public static void main(String[] args) {
        // Initialisation d'une voiture manuelle
        Voiture voiture = new VoitureManuelle();
        voiture.démarrer();  // Affiche "Voiture manuelle démarre."
        
        // Changement de type d'objet (Réaffectation de la variable)
        voiture = new VoitureAutomatique();  // Changer pour une voiture automatique
        voiture.démarrer();  // Affiche "Voiture automatique démarre."
        
        // On peut maintenant appeler les méthodes spécifiques à la nouvelle voiture
        voiture.arrêter();  // Affiche "Voiture automatique s'arrête."
    }
}

```

Interface:
- une interface est un contrat de comportement de sortes que les classes sont tenus de surcharger toutes les methodes qu'elles contiennent, cela permet le polymorphism
car toutes classes qui implemente cette interface est assuré  d'avoir une implementation concrete de cette interface
- Tight Coupling
- Why not Abstract class and why interface ...
Une interface =
 Liste de méthodes dont on donne seulement la signature
 Représente un "contrat", ce qu'on attend d'un objet
 Peut être implémentée par une ou plusieurs classes qui doivent donner une
implémentation pour chacune des méthodes annoncées (et éventuellement
d'autres).
 Une classe peut implémenter plusieurs interfaces (permettant un héritage
multiple, en les séparant par des virgules après le mot implements).
 Toutes les méthodes d'une interface sont implicitement abstraites.
 Une interface n'a pas de constructeurs
 Une interface ne peut avoir de champs sauf si ceux-ci sont statiques.
 Une interface peut être étendue par une ou plusieurs autre(s) interface(s).
En fait, une interface est une classe abstraite dont toutes les méthodes sont
abstraites et dont tous les attributs sont constants (des constantes, voir le mot-clé
final).
rincipe du couplage faible entre applications.
  / / i need a complete english md file based on this, you can structured, make clear, corrected and add things if you think is essentials