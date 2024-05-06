
/* 

- js est language de script pour rendre la page plus dynamique : example = affichage hello word
- pour integrer js dans nos pages html on peut le faire soit par un ficher xterne ou soit directement dans le code html
- la syntaxe est simple, espace permis, caracteres speciaux, indentation,  commentaire...
- recommender de placer le code js a la fin pour accelerer le chargement de la page 
- https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference
- https://jsfiddle.net/
*/

1. VARIABLE

// syntaxe

	var ridi;
	ridi = 2;
	var ridi = 2;

	var ridi = 2; var jason = 3; var naomie = 3;
	var ridi = 2, jason = 3,  naomie = 3;

// type des données

	var age = 4; // integer

	var prix = 3.2; // float

	var nom = 'ridi', text = 'c\'est bien',  nom = "ridi"; // string

	var isTrue = true, isFalse = false; // booléens (boolean)

// pour verifier le type des données d'une variables ou son existences : 

	alert(typeof nom_de_la_variable );


2. OPERATEUR ARITHMETIQUES

	/*

	+ : addition
	- : soustraction
	/ : division 
	% : division

	*/

	var number1 = 3, number2 = 2, result;
	result = number1 * number2;
	alert(result); // Affiche : « 6 »


// incrementation 

	var number = 3;
	number = number + 5;
	alert(number); // Affiche : « 8 »

	var number = 3;
	number += 5;
	alert(number); // Affiche : « 8 »

	 // +=  -=  *=  /=  %=  le principe est simple



// concaténation des types des données

	var hi = 'bonjour ', name = 'toi';
	var result = hi + toi;
	alert(result);

	var text = 'Bonjour ';
	text += 'toi';
	alert(text); // Affiche « Bonjour toi ».

	var text = 'Voici un nombre : ', number = 42, result;
	result = text + number;
	alert(result); // Affiche : « Voici un nombre : 42 »

// interagir avec les visiteurs grace a la fonction alert et prompt

	var usr = prompt('entrez votre nom : ')
	alert(usr);

// conversion des types des donnees 

	var first, second, result;

	first = prompt('Entrez le premier chiffre :');
	second = prompt('Entrez le second chiffre :');
	result = parseInt(first) + parseInt(second); // une chaine en nombre

	alert(result);


3. conditions 

	// bolean

	var num1 = 4, num2 = 4, num3 = 5, result;
	result = num1 == num2;
	result(result);

	var number = 4, text = '4', result;

	result = number == text;
	alert(result); // Affiche  « true » alors que « number » est un nombre et « text » une chaîne de caractères

	result = number === text;
	alert(result); // Affiche « false » car cet opérateur compare aussi les types des variables en plus de leurs valeurs

	// operateurs logique

	&& // et
	|| // ou
	! // non


	// conditions

	var age = 18;
	var age_visiteur = parseInt(prompt('entrez votre age : '));

	if (age_visiteur == age ) 
	{
		alert('vous etes majeur');
	}

	else if (age_visiteur >=  age)
	{
		alert('heuu, grand grand');
	}

	else
	{
		alert('non non');
	}


	var nombre = parseInt(prompt('entre un nombre'));

	 switch(nombre)
	 {
	 	case 1 :
	 	alert('charly');
	 	break;
	 	case 2 :
	 	alert('naomie');
		break;
	 	case 3 :
	 	alert('ridi');
	 	break;
	 	default :
	 	alert('rien');
	 } /* switc lui fonctionne sur le type de l'element entrer */
	 

	var startMessage = 'Votre catégorie : ',
	    endMessage,
	    adult = confirm('Êtes-vous majeur ?');

	endMessage = adult ? '18+' : '-18';

	alert(startMessage + endMessage);


3. boucle 

	// while

	while( condition )
	{
		// instruction ;
	}

	// do while 

	do {
	    instruction_1;
	    instruction_2;
	    instruction_3;
	} while (condition);


	// for 

	for (initialisation; condition; incrémentation) {
	    instruction_1;
	    instruction_2;
	    instruction_3;
	}

	for (var iter = 0; iter < 5; iter++) {
	    alert('Itération n°' + iter);
	}


4. fonction

	// simple

	function myFunction(arguments) {
	    // Le code que la fonction va devoir exécuter
	}

	// anonyme

	var instruction = function() {
	    // Du code…
	};

	// isolée

	(function() {
	    // Code isolé
	})();


	/* 

	- parseInt
	- toUpperCase()
	- toLowerCase()
	- length


	*/

5. les Arrays

	var myarray = [1, 2, 'trois', 'quatre', 5] // syntax appréciée
	var myarray = new array(1, 2, 'trois', 'quatre', 5) // ancienne syntax


	myArray.push('Ludovic'); // Ajoute « Ludovic » à la fin du tableau / unshift() fait l'inverse

	/*

	Les méthodes shift() et pop() retirent 
	respectivement le premier et le dernier élément du tableau.

	*/

	// parcours des arrays 


	ident = ['ridi', 'jason', 'jenny'];

	for (var i = 0, c = ident.length; i < c; i++) {

		alert(ident[i])
	}


	//  objets litteraux

	var myObject = {
	    item1: 'Texte 1',
	    item2: 'Texte 2'
	};

	// acces

	family.sister; // first way
	amily['sister']; // second  way

	myArray['length'] // pour récupérer le nombre d'items.

	// add 

	family['uncle'] = 'Didier';
	familly.uncle = 'ridi'

	// parcours

	for (var id in family) 
	{
   	 alert(family[id]);	
	}

	// utilisation simple 

	function getCoords() {
	    return {
	        x: 12,
	        y: 21
	    };
	}

	var coords = getCoords();

	alert(coords.x); // 12
	alert(coords.y); // 21


	/* debogage 

	le kit de developpement F12

	- consol.log(objet a afficher)

	*/
	

	6. LES CLASSES 

	/* js n'a pas systeme de la classe, il utilse un systeme de prototype, on peut creer des methodes a partir des nos bjets */
	/* en js on peut avoir une instance d'une variable, d'un object (prototype), ...*/

	var eleve = 
	{
		nom: 'eleve', 

		moyenne: function()
		{
			return 30
		},

		present: function()
		{
			return this.nom + "present"
		}
	}

	var ridi = Object.create(eleve)
	ridi.nom = 'ridi'

	// sur js on peut definir une methode sur une instance 

	ridi.parler = function (){return 'salut'}

	// on peut directement modifier le prototype à tout moment 

	eleve.prensent = function(){return 'salut'}

	// creer un constructeur 

	var eleve2 = function (nom)
	{
		this.nom = nom
	}

	/*  
		si on veux utiliser le constructeur -> 
		nathan ainsi que les autres ne sont pas des objets mais des instances 
		de la variable eleve(construteur)

		il faut savoir que le variable utiliser comme constructeur ont un prototype :
		variable.prototypee
		cette variable aufait est un objet contenant un constructeur et un prototype

		cequi fait que les instances nathans seront des objet qui auront pour prototype
		le prototype de la l'objet eleve2

		et si on veux ajouter des methodes -> 

		si vous modifier directement  la methode d'un objet cela n'affecte pas les autres, 
		si non il faudrais modifier la mettode  dans le prototype lui meme

	*/

	eleve2.prototype.moyenne = function(){return 30}
	eleve2.prototype.parler = function(){return 'blablabla'}

	/* automatiquement les objects nathans herites des methodes et attributs du prototype 
	de leurs constructeur */

	var nathan = new eleve2('jean')
	var nathan = new eleve2('jean')

	// example plus concret de la structure php en js

	var eleve = function(nom)
	{
		this.nom = nom
	}

	eleve.prototype.present = function(){return this.nom + ' est present'}
	eleve.prototype.parler = function(){return 'blablabla'}


	var ridi = new eleve('ridi')

	// principe des chaines de caracteres 

	/*
		les chaines de caracteres ont aussi un prototype en js, qui lui a son tour a plusieurs
		methodes, nous pouvons modifier ce protottype et ajouter nos methodes, ainsi
		toute nos chaines pourrons utiliser ce methodes 

		'ma_chaine'.__proto__ : pour afficher le prototype, = String
		 maintenent que nous connaissons le proto on peut donc e modifier
		 ceci n"est pas possible en php de modifier un object native du language
	*/

	String.prototype.lol = function(){return 'je suis un lol'}

	// le principe  d'encapsulation n'existe pas en js

	// la notion du static en js fonctionne comme un object normal, contrairement a php

	var session =
	{
		get: function(){ return 'get'}
	}

	session.get() 

	// les objet mathematique 

	/* en js il existe un gros objet qui s'appel math, et on peut y acceder directement */

	Math.PI 
	Math.round(34,78)

	// gerer l 'heritage en js 

	var eleve = function(nom)
	{
		this.nom = nom
	}

	eleve.prototype.present = function(){return this.nom + ' est present'}
	eleve.prototype.parler = function(){return 'blablabla'}


	var deleguer = function(nom)
	{
		eleve.call(this, nom)
		this.role = 'deleguer'
		
		// il utilise le constructeur eleve
	}

	deleguer.prototype = Object.create(eleve.prototype
	delegueer.prototype.constructor = deleguer
	deleguer.prototype.moyenne = function(){return 23}
	
	
	// les interfaces et traits ,'existent pas en javascript

	// les namespace

	/* ça n'existe pas vraiment en javascript, on utilise des functions specifiques 
	pour rendre la porter locales */

	(function(){})


	7. Gestion des erreurs 

	// bloc try catch

	var a = {
		nom: 'ridi',
		salutation: function()
		{
			return 'salut'
		}
	}

	try {

	a.salutation()
	a.nom
	a.prenom()

	} catch (error) {
	console.log('il y aune erreur')
	} finally {
	console.log('execute quand meme le code')
	}
	
	// lever une exception

	demo = function(nombre)
	   {
		   if (nombre > 5) {
			  throw new error('votre nombre est superieur a 5')
		   } 
	   }
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   1.  le DOM

	/*
	Le Document Object Model (abrégé DOM) est une interface de programmation pour les documents XML et HTML.

	Une interface de programmation, qu'on appelle aussi une API (pour Application Programming Interface), est un ensemble d'outils qui permettent de faire communiquer entre eux plusieurs programmes ou, dans le cas présent, différents langages. Le terme API reviendra souvent, quel que soit le langage de programmation que vous apprendrez.

	Le DOM est donc une API qui s'utilise avec les documents XML et HTML, et qui va nous permettre, via le JavaScript, d'accéder au code XML et/ou HTML d'un document. C'est grâce au DOM que nous allons pouvoir modifier des éléments HTML (afficher ou masquer un<div>par exemple), en ajouter, en déplacer ou même en supprimer.*/

	- le document 
	/*
	L'objetdocumentest un sous-objet dewindow, 
	l'un des plus utilisés. Et pour cause, il représente la page Web 
	et plus précisément la balise<html>. C'est grâce à cet élément-là 
	que nous allons pouvoir accéder aux éléments HTML et les modifier. 
	*/

	- Objet window 
	/*
		- lorsqu'on declare une variable elle devient directement une propier de window
		- une variable declarer dans une fonction isolée a une porter locale donc elle ne seras unne proprieter de window
		- si une variable est declarée sanss le mot clz var dans une fonction isolée, elle devient automatiquement une propriété de window

	*/

	- Accéder aux éléments

	/*

	L'accès aux éléments HTML via le DOM est assez simple 
	mais demeure actuellement plutôt limité. 
	L'objetdocumentpossède trois méthodes principales
	:getElementById(),getElementsByTagName() et getElementsByName().

	*/

	- getElementById()

	/*

	Cette méthode permet d'accéder à un élément en connaissant son ID 
	qui est simplement l'attribut id de l'élément. 
	Cela fonctionne de cette manière :


	<div id="myDiv">
	<p>Un peu de texte <a>et un lien</a></p>
	</div>

	<script>
	var div = document.getElementById('myDiv');

	alert(div);
	</script>

	*/
	- getElementsByTagName()

	/*

	Cette méthode permet de récupérer, sous la forme d'un tableau, tous les éléments de la famille. Si, dans une page, on veut récupérer tous les<div>, il suffit de faire comme ceci :

	var divs = document.getElementsByTagName('div');

	for (var i = 0, c = divs.length ; i < c ; i++) {
	alert('Element n° ' + (i + 1) + ' : ' + divs[i]);
	}

	*/

	- getElementsByName()

	/*

	Cette méthode est semblable àgetElementsByTagName()
	et permet de ne récupérer que les éléments qui possèdent un attribut
	name que vous spécifiez. 
	L'attributnamen'est utilisé qu'au sein des formulaires, 
	et est déprécié depuis la spécification HTML5 
	dans tout autre élément que celui d'un formulaire. 
	Par exemple, vous pouvez vous en servir pour un élément<input>

	*/

	- querySelector() et querySelectorAll()

	/*

	Ces deux méthodes sont querySelector() et querySelectorAll() 
	et ont pour particularité de grandement simplifier la sélection d'éléments 
	dans l'arbre DOM grâce à leur mode de fonctionnement. 
	Ces deux méthodes prennent pour paramètre un seul argument : 
	une chaîne de caractères !

	Cette chaîne de caractères doit être un sélecteur CSS 
	comme ceux que vous utilisez dans vos feuilles de style. Exemple :

	*/

	/*

	<div id="menu">

	<div class="item">
		<span>Élément 1</span>
		<span>Élément 2</span>
	</div>

	<div class="publicite">
		<span>Élément 3</span>
		<span>Élément 4</span>
	</div>

	</div>

	<div id="contenu">
	<span>Introduction au contenu de la page...</span>
	</div>

	<script>

	var query = document.querySelector('#menu .item span'),
	queryAll = document.querySelectorAll('#menu .item span');

	alert(query.innerHTML); // Affiche : "Élément 1"

	alert(queryAll.length); // Affiche : "2"
	alert(queryAll[0].innerHTML + ' - ' + queryAll[1].innerHTML); // Affiche : "Élément 1 - Élément 2"

	</script>

	*/

	- getAttribute() et setAttribute()

	/* 

	permettant respectivement de récupérer et d'éditer un attribut. 
	Le premier paramètre est le nom de l'attribut, et le deuxième, 
	dans le cas desetAttribute()uniquement, 
	est la nouvelle valeur à donner à l'attribut. Petit exemple :

	<body>
	<a id="myLink" href="http://www.un_lien_quelconque.com">Un lien modifié dynamiquement</a>

	<script>
		var link = document.getElementById('myLink');
		var href = link.getAttribute('href'); // On récupère l'attribut « href »

		alert(href);

		link.setAttribute('href', 'http://www.siteduzero.com'); // On édite l'attribut « href »
	</script>
	</body>

	*/

	-  les classes en HTML
	

	<script>
		document.getElementById('mydiv').className  = 'rouge bleu';

        var body = document.querySelector('body')
        body.className = 'jaune'

	</script>
    
   
	
    var div = document.querySelector('div');

    //lister les classes
    div.classList

	// Ajoute une nouvelle classe
	div.classList.add('new-class');

	// Retire une classe
	div.classList.remove('new-class');

	// Retire une classe si elle est présente ou bien l'ajoute si elle est absente
	div.classList.toggle('toggled-class');

	// Indique si une classe est présente ou non
	if (div.classList.contains('old-class')) {
	alert('La classe .old-class est présente !');
	}

	// Parcourt et affiche les classes CSS
	var result = '';

	for (var i = 0; i < div.classList.length; i++) {
	result += '.' + div.classList[i] + '\n';
	}

	alert(result);


    - style 

    //  on peut directement modifier le style dinamiquement 

    nom_de_l\'element.style.fontSize = '20px'




2. MANIPULATION DU CODE HTML AVANCER

var ul = document.querySelector('ul') // on recupère un element
ul.children // on recupere les noeuds enfants, navique entre les noeuds
ul.childNodes //  recupere tout  les noeuds meme les noeuds texte
ul.childElementCount // compte seulment les enfants qui sont des elements
ul.firstChild / ul.lastChild // recupere respectivement les premeirs et les derniers elements dans le sens global
ul.firstElementChild / ul.lastElementChild // recupere respectivement les premeir et les dernier element qui sont dans l'elemeent

ul.querySelector('il') // on peut faire appel dddirectement a ses selecteurs comment sur le document 
ul.querySelector('il:nth-chil(3)') on recupère precisement le 3eme element avec le selecteur css AVANCER

li.nextSibling : // noeud suivant au sens global
li.previousSibling : // noeud precedent au sens global

ul.nextElementSibling // noeud suivant
ul.previousElementSibling // noeud precedent

li.parentNode // noeud parent 
li.parentElement // element parent

li.parentElement.removeChild(li) // supprimer l'element
document.body.appendChild(li) // renvoyé un element sur lee body

var li2 = li.cloneNode(true) // cloner un element 
li.parentElement.appendChild(l2)

3. les evenements

/*

var b = document.querySelector('body')
b.classList.add('jaune')
var event = function(){
    b.classList.toggle('bleu')
}
b.addEventListener('click', event)

*/


/*

var ps = document.querySelectorAll('p')
for (i = 0; i < ps.length; i++) {
    p = ps[i];

    var jaunir = function(){
        this.classList.toggle('jaune')
    }
    p.addEventListener('click', jaunir)
}

*/

/*

var external = document.querySelectorAll('.external')

for (i = 0; i < external.length; i++) {
   ext = external[i]

    ext.addEventListener('click', function ver(reponse){
        ans = window.confirm('voulez-vous vraiment quitter le site web ?')
        if (ans === false) {
            reponse.preventDefault();
        }
    })   
}

*/

/*

var external = document.querySelectorAll('.external')

for (i = 0; i < external.length; i++) {
   ext = external[i]

    ext.addEventListener('click', function ver(reponse){
        reponse.stopPropagation()
        ans = window.confirm('voulez-vous vraiment quitter le site web ?')
        if (ans === false) {
            reponse.preventDefault();
        }
    })   
}

var ps = document.querySelectorAll('p')
 for (i = 0; i < ps.length; i++) {
     p = ps[i];

    var rouge = function(){
        p.classList.add('rouge')
    }
    
    p.addEventListener('click', rouge)
}

*/

/*

document.querySelector('#form').addEventListener('submit', function (e){
    var nom = document.querySelector('#name')
    if (nom.value.length < 2) {
        alert('mauvaise valeur')
        
    }
})



document.querySelector('#form').addEventListener('submit', function (e){
    var mentions = document.querySelector('#mentions')
    if (mentions.checked === false) {
        alert('vous devew accepter les conditions d\'utilisations')
        e.preventDefault()
        
    }
})



// age.options : donne toute les options
// age.selectedIndex : donne l'element selectionner
// age.selctedOptions : toutes les options selectionner
// age.selctedOptions[0] : selectionner l'index
// demo.focus : focuser sur l'element au chargement 
//demo.blur : fonction opposé de focus

document.addEventListener('DOMContentLoaded', function(){
    // function a exsecuter
})  // permet d'ecouter sur Le DOM si les pages js sont chargée

*/















