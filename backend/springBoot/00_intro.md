# What is Spring?

Spring is an open-source Java framework that simplifies the development of enterprise applications.

It allows developers to:

- Build applications using POJOs (Plain Old Java Objects)
- Manage dependencies through Dependency Injection (DI)
- Structure applications into layers (web, business, data)
- Avoid heavy Java EE application servers

Spring is often described as a lightweight container because it manages application components internally.

Official website: https://spring.io/

# Java EE vs Spring

## What is Java EE?

Java EE (now Jakarta EE) is a set of specifications for building enterprise Java applications.

It defines standards for:

- Servlets
- EJB
- Transactions
- Persistence (JPA)
- Security

Java EE itself does not execute applications.  
An **Application Server** implements these specifications.

Examples:

- WildFly (JBoss)
- WebLogic
- GlassFish

Application Server = engine that runs and manages Java EE applications.

## Architecture Difference

### Java EE (Application Server Model)

- Requires a full application server
- The server provides:
  - Security
  - Transactions
  - Database access
  - Resource management
- Multiple applications can run on the same server
- Infrastructure is centralized

The application depends strongly on the server.



### Spring (Lightweight Model)

- Runs on a servlet container such as Tomcat
- Embeds required services inside the application
- Uses simple Java objects (POJOs)
- Manages components via ApplicationContext

Infrastructure is integrated into the application.

Each application is autonomous.

# Why Spring Became Popular

- Java EE servers were heavy
- EJB configuration was complex
- Deployment was complicated

Spring introduced:

- Simpler programming model
- Dependency Injection
- Modular architecture
- No need for a full application server

Spring is widely used because it promotes clean, testable, and maintainable code.



## Problems with Java EE

- Application servers were heavy
- EJB development was complex
- Configuration was difficult
- Global infrastructure was always active
- Centralized administration
- Designed for multi-application hosting


## What Spring Proposed

- Simple POJO-based programming model
- Dependency Injection (DI)
- No need for a full application server
- Can run on a servlet container such as Tomcat
- Applications embed only the services they need

For this reason, Spring is often called a lightweight container.


## What is Spring Boot?

Spring Boot is a project built on top of the Spring Framework.

It simplifies the startup and development of new Spring applications by reducing configuration complexity.

Spring Boot supports embedded containers.  
This allows web applications to run independently without deployment to an external application server.



## Advantages of Spring Boot

- Significantly reduces development time
- Increases productivity
- Provides embedded HTTP servers such as Tomcat and Jetty
- Simplifies development and testing of web applications
- Integrates easily with build tools such as Maven and Gradle



## Basic Spring Boot Annotations

Spring annotations allow configuration and dependency injection directly in Java code.

#### @Controller
Marks a class as a Spring MVC controller that handles web requests.

#### @RestController
Marks a class as a REST controller.  
It combines `@Controller` and `@ResponseBody` to automatically serialize returned objects into HTTP responses (e.g., JSON).



## Java EE vs Spring Boot (Operational View)

### Java EE

- Heavy centralized server
- Global infrastructure
- Services active even if unused
- Designed for multi-application hosting

### Spring Boot

- Infrastructure embedded in the application
- Loads only required modules
- Starts faster
- Better suited for microservices and cloud environments
