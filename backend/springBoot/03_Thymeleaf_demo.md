```html
<!DOCTYPE html>
<html lang="fr" xmlns:th="http://www.thymeleaf.org">
  <head>
    <meta charset="UTF-8" />
    <title>Thymeleaf – Démonstration pédagogique</title>

    <!-- Feuille de style -->
    <link rel="stylesheet" th:href="@{/css/style.css}" />
  </head>

  <body>
    <!-- ===================== HEADER ===================== -->
    <header class="site-header">
      <div class="container brand">
        <img th:src="@{/images/logo.png}" alt="Logo" />
        <div>
          <h1>Thymeleaf – Vue Spring Boot MVC</h1>
          <div class="subtitle">
            Démonstration pédagogique – variables, conditions, boucles
          </div>
        </div>
      </div>
    </header>

    <!-- ===================== CONTENU ===================== -->
    <main class="container">
      <div class="card">
        <!-- ==================================================
         CONCEPT 1 : AFFICHAGE (print / echo)
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">
            1) Afficher une variable (équivalent print / echo)
          </h2>

          <!--
        Les données viennent du Model (Controller → Vue).
        ${...} est évalué côté serveur par Spring Expression Language.
        [[...]] est une écriture inline plus courte.
      -->
          <p th:text="${message}">Message par défaut</p>
          <p>Inline : <strong>[[${message}]]</strong></p>
        </section>

        <!-- ==================================================
         CONCEPT 2 : LITTÉRAUX
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">
            2) Littéraux (String, Number, Boolean, null)
          </h2>

          <p>Chaîne : <span th:text="'Bonjour Thymeleaf'"></span></p>
          <p>Nombre : <span th:text="123"></span></p>
          <p>Booléen : <span th:text="true"></span></p>
          <p>Null : <span th:text="null"></span></p>
        </section>

        <!-- ==================================================
         CONCEPT 3 : LISTES / TABLEAUX
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">3) Listes / Tableaux (accès par index)</h2>

          <p th:text="${nombres[0]}"></p>
          <p th:text="${nombres[1]}"></p>
          <p th:text="${nombres[2]}"></p>

          <h3 class="demo-subtitle">Variable locale (th:with)</h3>

          <!--
        th:with crée une variable locale utilisable uniquement
        à l’intérieur de ce bloc.
      -->
          <div th:with="msg = 'Variable locale Thymeleaf'">
            <p>[[${msg}]]</p>
          </div>
        </section>

        <!-- ==================================================
         CONCEPT 4 : BOUCLES
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">4) Boucle (équivalent foreach)</h2>

          <!--
        th:each = variable : collection
        La variable est locale à chaque itération.
      -->
          <ul>
            <li th:each="nom : ${noms}">[[${nom}]]</li>
          </ul>
        </section>

        <!-- ==================================================
         CONCEPT 5 : OBJETS
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">5) Objet (accès aux propriétés)</h2>

          <!--
        th:object définit l’objet courant.
        *{...} équivaut à ${etudiant.propriete}
      -->
          <div th:object="${etudiant}">
            <p>Nom : <span th:text="*{nom}"></span></p>
            <p>Âge : <span th:text="*{age}"></span></p>

            <p>toString: <span th:text="${etudiant.toString}"></span></p>

            <h3 class="demo-subtitle">Valeur par défaut (Elvis)</h3>
            <p th:text="*{competences} ?: 'Aucune compétence'"></p>

            <h3 class="demo-subtitle">Ternaire (if / else court)</h3>
            <p
              th:text="${etudiant.active} ? 'Étudiant actif' : 'Étudiant inactif'"
            ></p>

            <!-- Changement de couleur selon la note -->
            <h2>Note de l'Étudiant</h2>
            <p
              th:text="${etudiant.note}"
              th:classappend="${etudiant.note < 60} ? 'text-danger' : 'text-success'"
            ></p>
          </div>
        </section>

        <!-- ==================================================
         CONCEPT 6 : CONDITIONS
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">6) Conditions (if -unless , switch)</h2>

          <!--
        Thymeleaf n’a pas th:else.
        On utilise th:if + th:unless.
      -->
          <h3>If – Unless</h3>
          <p>
            <span th:if="${etudiant.gender == 'F'}">Genre : Femme</span>
            <span th:unless="${etudiant.gender == 'F'}">Genre : Homme</span>
          </p>

          <p th:if="${etudiant.age >= 18 and etudiant.active}">
            Étudiant majeur et actif
          </p>
          <p th:unless="${etudiant.age > 18 or etudiant.active}">
            Étudiant mineur ou inactif.
          </p>

          <!-- Vérification de la présence d'une compétence -->
          <p th:if="${etudiant.competences != null}">
            Compétences : [[${etudiant.competences}]]
          </p>
          <p th:unless="${etudiant.competences != null}">
            Aucune compétence définie.
          </p>

          <!-- Vérification si la liste des cours est vide -->
          <div th:if="${#lists.isEmpty(etudiant.courses)}">
            Aucun cours disponible.
          </div>

          <h3>Switch – Case</h3>
          <div th:switch="${#lists.size(etudiant.courses)}">
            <span th:case="'0'">PAS DE COURS!</span>
            <span th:case="'1'" th:text="${etudiant.courses[0]}"></span>
            <div th:case="*">
              <div
                th:each="course:${etudiant.courses}"
                th:text="${course}"
              ></div>
            </div>
          </div>

          <div th:switch="${etudiant.specialite}">
            <p th:case="'Informatique'">Il étudie l'informatique</p>
            <p th:case="'Math'">Il est les Maths</p>
            <p th:case="'Science'">Il étudie les Sciences</p>
            <!-- * for default case -->
            <p th:case="*">Il étudie autre chose</p>
          </div>
        </section>

        <!-- ==================================================
         CONCEPT 7 : BOUCLES AVANCÉES
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">7) Boucle avancée (index, first, last)</h2>

          <ul>
            <li th:each="course, stat : ${etudiant.courses}">
              [[${stat.index}]] - [[${course}]]
              <span th:if="${stat.first}">(Premier)</span>
              <span th:if="${stat.last}">(Dernier)</span>
            </li>
          </ul>

          <h3>Cours commençant par "Math"</h3>
          <ul>
            <li
              th:each="course : ${etudiant.courses}"
              th:if="${course.startsWith('Math')}"
            >
              [[${course}]]
            </li>
          </ul>

          <h3>Numéros de 1 à 10</h3>
          <ul>
            <li th:each="i : ${#numbers.sequence(1, 10)}">[[${i}]]</li>
          </ul>

          <h3>Utilisation de th:block</h3>
          <th:block th:each="course : ${etudiant.courses}">
            <p th:text="${course}"></p>
          </th:block>

          <table>
            <tr>
              <th>#</th>
              <th>Cours</th>
              <th>Info</th>
            </tr>

            <tr
              th:each="cours, stat : ${etudiant.courses}"
              th:class="${stat.odd} ? 'ligne-impair' : 'ligne-pair'"
            >
              <td>[[${stat.count}]]</td>
              <td>[[${cours}]]</td>
              <td>
                <span th:if="${stat.first}">Premier</span>
                <span th:if="${stat.last}">Dernier</span>
              </td>
            </tr>
          </table>
        </section>

        <!-- ==================================================
         CONCEPT 8 : MAP
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">8) Map (clé → valeur)</h2>

          <ul>
            <li th:each="entry : ${etudiant.notes}">
              [[${entry.key}]] : [[${entry.value}]]
            </li>
          </ul>
        </section>

        <!-- ==================================================
         CONCEPT 9 : IMAGE DYNAMIQUE
    ================================================== -->
        <section class="section">
          <h2 class="demo-title">9) Image dynamique (ressources statiques)</h2>

          <img
            th:src="${etudiant.gender == 'F'} ? @{/images/avatar-f.png} : @{/images/avatar-m.png}"
            alt="Avatar"
            width="90"
          />
        </section>
      </div>
    </main>

    <footer class="site-footer">Démo Thymeleaf – Cours Spring Boot MVC</footer>
  </body>
</html>
```
