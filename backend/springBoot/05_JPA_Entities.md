# JPA Entities and EntityManager -- Complete Structured Notes

## JPA Entities

JPA allows defining entities.

An entity is simply an instance of a class that is persistent (can be
saved to / loaded from a relational database).

An entity is marked with the `@Entity` annotation on the class.

A JPA entity must also contain one or more attributes defining an
identifier using the `@Id` annotation.\
This identifier corresponds to the primary key in the associated table.

------------------------------------------------------------------------

# Structure of a JPA Entity

## @Entity

Declares a class as a persistent entity.\
Becomes a database table.

## @Table

Allows customizing the table: - name → table name - schema -
uniqueConstraints - indexes

------------------------------------------------------------------------

# Primary Key

## @Id

Defines the primary key.

## @GeneratedValue

Used to generate the ID automatically.

With MySQL:

@GeneratedValue(strategy = GenerationType.IDENTITY)

Corresponds to AUTO_INCREMENT.

Other strategies: - AUTO - SEQUENCE - TABLE

With MySQL → IDENTITY is the most used.

------------------------------------------------------------------------

# Columns

## @Column

Allows customizing a column.

Main options: - name - nullable - unique - length - precision - scale

Frequent uses: - Prevent null - Make unique - Limit varchar size

------------------------------------------------------------------------

# Enum

## @Enumerated(EnumType.STRING)

Stores an enum as text in the database.

------------------------------------------------------------------------

# Manipulation of Entities with EntityManager (JPA)

The JPA annotations seen previously are useless if they are not used
programmatically.

In JPA, the central interface that uses these annotations is:
EntityManager

JPA is a specification.\
To use it, you need a compatible implementation.

In this context: Hibernate is used.

The JPA implementation must be configured in the file:
application.properties

------------------------------------------------------------------------

# Role of EntityManager

An EntityManager manages the lifecycle of entities: - Creation - Read -
Update - Delete - Synchronization with the database

It operates inside a Persistence Context.

------------------------------------------------------------------------

# 1. find()

Searches for an entity by primary key.

Characteristics: - May NOT trigger an SQL query - If entity already in
context → no SELECT - Otherwise → SELECT query

Used only to load an existing entity.

------------------------------------------------------------------------

# 2. persist()

Makes an entity managed.

Effects: - Places entity in persistence context - Generates primary key
(depending on @GeneratedValue) - SQL insertion not always immediate -
INSERT executed at flush or commit

Used to create a new entity.

------------------------------------------------------------------------

# 3. remove()

Deletes a managed entity.

-   Generates DELETE
-   Executed at flush / commit

Important: Entity must be managed. Otherwise → exception.

------------------------------------------------------------------------

# 4. merge()

Often misunderstood.

-   Reattaches a detached entity
-   Returns a new managed instance
-   Copies state of detached object into managed object
-   Does not directly perform UPDATE

UPDATE is triggered at commit if changes detected.

Important: Always use the object returned by merge.

------------------------------------------------------------------------

# 5. detach()

Detaches an entity from the context.

Effects: - Entity no longer tracked - Changes will not be saved

------------------------------------------------------------------------

# 6. refresh()

Reloads state from database.

Effects: - Cancels all local modifications - Reloads values from
database

------------------------------------------------------------------------

# How UPDATE Really Works

There is NO update() method.

JPA works using: Dirty Checking

If an entity is managed: - You modify fields - At commit → Hibernate
detects changes - Automatically generates UPDATE

------------------------------------------------------------------------

# Entity Lifecycle

1.  New (new Java instance)
2.  Managed (persisted or found via find)
3.  Detached (after detach or end of transaction)
4.  Removed (after remove)

------------------------------------------------------------------------

# In Practice with Spring Boot

In a Spring Boot project: - Rarely use EntityManager directly - Use
JpaRepository - Transactions managed by @Transactional - Hibernate
flushes automatically

------------------------------------------------------------------------

# Conclusion

Essential methods to understand: - find() - persist() - remove() -
merge() - refresh() - detach()

In modern Spring Boot: Entities are mostly manipulated via
repositories.\
Hibernate manages the rest automatically.

Example: Calling save()

JpaRepository calls EntityManager.persist() or merge().\
Hibernate handles the rest.

------------------------------------------------------------------------

# Role of @Transactional

-   Opens a transaction
-   Activates persistence context
-   At commit → flush → SQL executed

------------------------------------------------------------------------

# What Is a Managed Entity?

A managed entity is: An entity that Hibernate tracks inside the
Persistence Context.

Meaning: - Attached to EntityManager - Hibernate tracks changes -
Changes synchronized automatically at commit

------------------------------------------------------------------------

# Persistence Context

Temporary memory area created inside a transaction.

When an entity enters it → becomes managed.

------------------------------------------------------------------------

# Concrete Example

@Transactional public void updateUser(Long id) { User user =
repository.findById(id).get(); // MANAGED user.setName("New name"); //
modification }

No save() call.

At commit: - Hibernate compares initial state - Detects modification -
Generates UPDATE automatically

This is Dirty Checking.

------------------------------------------------------------------------

# Possible Entity States

## 1. New (Transient)

User user = new User();

-   Just a Java object
-   Not in database
-   Not tracked

## 2. Managed

-   Obtained via find()
-   Or after persist()
-   Hibernate tracks it

## 3. Detached

-   Was managed
-   Transaction ended
-   No longer tracked

If modified: Nothing saved.

## 4. Removed

-   Marked for deletion
-   DELETE at commit
