# Spring Boot - Maven, Build et MVC

## Introduction

Spring Boot is a Java framework built on top of Spring that makes it fast and easy to create web applications and APIs.
It removes complex configuration and provides ready-to-use defaults so you can focus on business logic instead of setup.

## Maven Wrapper — mvn vs mvnw

Commande :

```
./mvnw clean spring-boot:run
```

Run a Spring Boot app with Maven Wrapper.

### mvn vs mvnw

If you installed Maven, you can write:

```
mvn
```

If you could not install Maven, use the Maven Wrapper:

```
mvnw
```

In this course, I will continue using the wrapper.

## Maven Central Repository

The Central Maven repository contains all of the dependencies that we can leverage in a Spring Boot project:

https://central.sonatype.com/artifact/org.springframework.boot/spring-boot-starter-web/3.5.6

## Build

The command:

```
./mvnw package
```

can be used to create a JAR file.

Specifically:

- It compiles your code
- Runs tests (if any)
- Packages everything into a JAR file in the `target` directory

The JAR filename follows the pattern:

```
[artifact-id]-[version].jar
```

By default, Spring Boot adds `SNAPSHOT` to indicate a development version.

Example:

```
workbook-0.0.1-SNAPSHOT.jar
```

## Run the JAR

Drag the JAR file to your Desktop, then run:

```
java -jar workbook-0.0.1.jar
```

## Spring Boot follows the MVC Pattern

Spring Boot follows the MVC pattern:

- Model
- View
- Controller

## Spring Boot Annotations

Spring Boot uses annotations to add logic and functionality without writing extra code (add magic).

## Controller

### @Controller

```
@Controller
```

Converts a class into a controller.

The class becomes an entry point for web requests.

Each handler method can respond to requests.

### Controller Role

The controller is the entry point for web requests.

#### GET Request

GET is used when the user is requesting a resource.

### @GetMapping

```
@GetMapping
```

- Converts a method into a handler method
- The handler method can accept GET requests
- Receives a path argument

Le contrôleur utilise le chemin d’accès d’une requête pour décider de la méthode de traitement à exécuter.

## View

The view represents the visual elements that make up a webpage.

## Model

The model is the data that the controller sends to the view.

- Handler methods have direct access to the model
- The handler method can create POJO objects to create data
- The handler method can store data in model attributes

## POJO

A POJO represents a piece of data.

A POJO class can contain:

- Private fields
- Constructors
- Getters / Setters

## Combine Model and View

### Variable Expressions

Variable expressions execute on model attributes.

Example:

```
${age}
```

They can:

- Return a model attribute
- Return a value derived from a model attribute

Example with Thymeleaf:

```
th:text="${attribute}"
```

- You can execute a loop based on a model attribute.
- You can execute a utility method on a model attribute.
