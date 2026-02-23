# Data Layer in Spring Boot

## JPA (Java Persistence API)

### Type

Official Java specification (standard Java API).

### Role

JPA defines how to map Java objects to a relational database.

It contains: - A set of interfaces and annotations - A standard for
performing ORM in Java - No real execution logic - Requires an
implementation

> JPA alone does not work. It needs an implementation.

### Common Implementations

-   Hibernate (most widely used)
-   EclipseLink

In Spring Boot → Hibernate is used by default.

### Core JPA Concepts

-   `@Entity`
-   `EntityManager`
-   `@Id`
-   `@OneToMany`, `@ManyToOne`, etc.

### JPA Entities

JPA allows you to define entities.

An entity is simply an instance of a class that is persistent (it can be
saved to / loaded from a relational database).

An entity is marked with the `@Entity` annotation on the class.

------------------------------------------------------------------------

## Hibernate

### Type

JPA implementation (ORM provider)

### Role

-   Transforms Java objects into SQL.
-   Hibernate is the real engine.

### Features

-   Automatic SQL generation
-   Cache management
-   Lazy loading
-   Relationship management
-   Object → table mapping

In Spring Boot → Hibernate is the default JPA provider.

------------------------------------------------------------------------

## Databases

### H2

Type: Lightweight relational database\
Usage: Development / testing

Characteristics: - Can run in-memory - Very fast - Starts instantly -
Ideal for unit testing

### MySQL

Type: Relational server database\
Usage: Production

Characteristics: - Persistent - Stable - Scalable - Widely used in
enterprise environments

------------------------------------------------------------------------

## Spring Data

### Definition

A family of Spring modules for data access.

Goal: Standardize and simplify database access.

### Features

-   Repositories
-   Pagination
-   Sorting
-   Derived queries
-   Multi-database integration

### Existing Modules

-   Spring Data JPA
-   Spring Data MongoDB
-   Spring Data Redis
-   etc.

------------------------------------------------------------------------

## Spring Data JPA

### Definition

Spring Data module specialized for SQL/JPA.

Used with: - MySQL - PostgreSQL - Oracle - etc.

Based on: - JPA - Hibernate

### What It Provides

#### Automatic Repositories

-   `JpaRepository`
-   `CrudRepository`

#### Derived Queries

-   `findByEmail`
-   `findByStatus`
-   `findByDateAfter`

#### `@Query`

Supports JPQL or native SQL.

#### Pagination / Sorting

-   `Pageable`
-   `Sort`

#### Transactions

Often via `@Transactional`.

#### Direct Integration with JPA Entities

Spring Data JPA = Simplified JPA

------------------------------------------------------------------------

## EntityManager --- The JPA Engine

If you use pure JPA, you must use `EntityManager`.

It manages: - persist - merge - remove - queries - transactions

Without EntityManager → JPA is useless.

------------------------------------------------------------------------

## Spring Data JPA --- The Simplifier

Spring recognized that EntityManager is verbose.

So they created: `JpaRepository`

JpaRepository uses EntityManager internally.

------------------------------------------------------------------------

## Pure JPA vs Modern Spring Boot

### Pure JPA

Direct use of EntityManager: - persist - merge - remove - queries -
transactions

Requires a lot of boilerplate code.

### Modern Spring Boot

Use of `JpaRepository`: - save() - findById() - findAll() - delete() -
pagination - automatic SQL generation

Spring uses EntityManager internally.

------------------------------------------------------------------------

# JpaRepository

Main interface used by the developer.

Example:

interface UserRepository extends JpaRepository\<User, Long\>

Spring automatically generates: - save() - findById() - findAll() -
delete() - count() - pagination - sorting - dynamic queries

------------------------------------------------------------------------

# Internal Flow During save()

userRepository.save(user);

Flow:

JpaRepository\
↓\
Spring Data JPA\
↓\
EntityManager\
↓\
Hibernate\
↓\
Database

------------------------------------------------------------------------

# Responsibilities Overview

## JPA Entity

-   Represents a table
-   Holds data

## JpaRepository

-   Interface used by the developer
-   Provides automatic CRUD

## Spring Data JPA

-   Generates implementation automatically
-   Uses EntityManager internally

## EntityManager

Core JPA engine: - Persistence - Cache - Queries - Entity management

## Hibernate

-   JPA implementation
-   Transforms objects → SQL

## Database

Final data storage
