# Thymeleaf

Thymeleaf is a Java template engine primarily used to generate Web
views.
It supports HTML, XHTML, JavaScript, CSS and any text-based format.

It integrates perfectly with Spring because it supports **Spring
Expression Language (SpEL)**.

With SpEL expressions, you can:

- Access any bean by name
- Access object properties using `.`
- Use arithmetic and logical operators inside expressions


# Where Thymeleaf fits into Spring MVC

- **Controller** (Java): receives the HTTP request, prepares the data.
- **Model** (`org.springframework.ui.Model`): transports data to the view.
- **View** (Thymeleaf `*.html`): displays/composes the final HTML.

Example controller :
```java
@GetMapping("/")
public String getForm(Model model) {
  model.addAttribute("grade", new Grade());
  return "form"; // -> templates/form.html
}
```


## Enable Thymeleaf

### 1.1 Maven dependencies (pom.xml)
You need:
- `spring-boot-starter-web`
- `spring-boot-starter-thymeleaf` : Template engine 

### File locations
- Templates : `src/main/resources/templates/*.html`
- Static files (css/js/images) : `src/main/resources/static/**`

Example CSS :
`src/main/resources/static/form-stylesheet.css`
Accessible via : `/form-stylesheet.css`


##  Base of the Thymeleaf HTML file

### Namespace `th`
In your course :
```html
<html xmlns:th="http://www.thymeleaf.org">
```
This allows the use of `th:*` attributes (th:text, th:href, th:each, etc.).



### Thymeleaf Expressions (Core Concept)

  Syntax  --    Purpose
  - `${...}`   Access model variables (SpEL)
  - `@{...}`   Build URLs
  - `*{...}`   Selection expression (with `th:object`)
  - `#{...}`   Messages (i18n)
  - `~{...}`   Fragments



# Thymeleaf expressions (essential)



## `${...}` general expression with `th:text` --  Access Model Variables

`${grade}` refers to an object sent from:

``` java
model.addAttribute("grade", grade);
```

Example:

``` html
<span th:text="${grade.name}"></span>
```

### Inline display

``` html
<p>[[${message}]]</p>
```

Equivalent to:

``` html
<p th:text="${message}"></p>
```

Example :
```html
<span th:text="${grade.name}"></span>
```
---

### Types (int, float, boolean, String)

All types are automatically converted to String when using `th:text`.

``` html
<span th:text="'text'"></span>
<span th:text="123"></span>
<span th:text="true"></span>
```


##  `@{...}` expression related to `th:href` : build a URL
- `@{/}` -> "/"
- `@{/grades}` -> "/grades"
- `@{/css/style.css}` -> "/css/style.css"

Example (your menu links) :
```html
<a th:href="@{/}">Form</a>
<a th:href="@{/grades}">Grades</a>
```



## `*{...}` : expression related to `th:object`
Used in forms with `th:object`.


### Forms and Binding



```html
<form method="post" th:object="${grade}" th:action="@{/handleSubmit}">
  <input type="text" placeholder="Name" th:field="*{name}">
  <input type="text" placeholder="Score" th:field="*{score}">
  <input type="text" placeholder="Subject" th:field="*{subject}">
  <input type="hidden" th:field="*{id}">
  <input type="submit" value="Submit">
</form>
```

#### `th:object="${grade}"`
- Tells Thymeleaf : **the form object is called `grade`**
- It must come from the controller :
```java
model.addAttribute("grade", new Grade());
```

#### `th:action="@{/handleSubmit}"`
- The destination URL of the POST.
- In the controller, you must have a POST handler (typical example) :
```java
@PostMapping("/handleSubmit")
public String handleSubmit(@ModelAttribute Grade grade) {
  // ...
  return "redirect:/grades";
}
```

#### `th:field="*{name}"`
- Binds the HTML field to a property of the `grade` object.
- It does 2 things :
  1) puts the value in the input if the object already has a value (editing)
  2) generates the `name="name"` (and sometimes `id="name"`) expected by Spring for binding

Same for `score`, `subject`.

#### Hidden field `id`
```html
<input type="hidden" th:field="*{id}">
```
- Essential to distinguish :
  - **creation** (new id)
  - **editing** (existing id, keep the same)




## loop  with `th:each` (essential as soon as you have multiple rows)

If your controller sends a list :
```java
model.addAttribute("grades", studentGrades);
```

Then in HTML you do :
```html
<tr th:each="g : ${grades}">
  <td th:text="${g.name}"></td>
  <td th:text="${g.subject}"></td>
  <td th:text="${g.score}"></td>
</tr>
```

To remember :
- `${grades}` = the list
- `g` = loop variable
- `${g.name}` = field of the current grade


## Conditions : `th:if` / `th:unless` 
Display a block only if condition true :
```html
<div th:if="${grades != null and !#lists.isEmpty(grades)}">
  ...
</div>
<div th:unless="${grades != null and !#lists.isEmpty(grades)}">
  No data
</div>
```


# Simple technical summary

| Attribute | What it actually does |
| --- | --- |
| `th:object` | Defines a current object |
| `th:field` | Binds an HTML field to a property |
| `th:each` | Loop over a list |
| `th:if` | Display condition |
| `th:unless` | Reverse condition |
| `th:text` | Replaces content |
| `@{}` | Builds URL |
| `${}` | Accesses the model |
| `*{}` | Accesses the current object |




# Note 

## `#{...}` — Message Expressions (i18n)

### What is it for?

Allows displaying **external messages** stored in translation files.

Used for internationalization (i18n).


### How does it work?

You create a file :

```
src/main/resources/messages.properties
```

Example :

```
app.title=Grade Portal
form.submit=Submit
```

In your HTML :

```
<h1 th:text="#{app.title}"></h1>
<input type="submit" th:value="#{form.submit}">
```

Thymeleaf will automatically replace with the value from the file.


### Why is it useful?

- Translations (FR, EN, ES…)
- Centralize texts
- Avoid writing hard-coded text in HTML

### Multi-language example :

```
messages_fr.properties
messages_en.properties
```

Spring automatically chooses according to the browser language.

## `~{...}` — Fragment Expressions

### What is it for?

Allows including reusable template parts.

This avoids repeating header, footer, navbar, etc.


## Example

### header.html

```
<div th:fragment="header">
<nav>My Navigation</nav>
</div>
```

### In another file :

```
<div th:replace="~{header :: header}"></div>
```

What it does :

- Loads the `header.html` template
- Takes the fragment named `header`
- Inserts it here


## Why is it useful ?

- Avoid duplication
- Clean architecture
- Widely used in professional projects
