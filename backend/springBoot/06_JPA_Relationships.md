# JPA Relationships -- Complete Modern Guide

## Introduction

In relational databases, tables are linked together using relationships.
In JPA, these relationships exist between entities and are mapped using
annotations.

An ORM like Hibernate automatically translates object relationships into
database relationships.

JPA supports four main types of relationships: 

- `One-to-One`
- `Many-to-One` 
- `One-to-Many` 
- `Many-to-Many`

Each relationship can be: - Unidirectional - Bidirectional



## Core Relationship Annotations

JPA defines relationships using: 
- `@OneToOne` 
- `@ManyToOne` 
- `@OneToMany` 
- `@ManyToMany`

These annotations define how entities are linked and how foreign keys
are generated.


# 1. One-to-One Relationship

## Definition

One entity is linked to exactly one other entity.

`Example: User ↔ Profile`

Each user has one profile. Each profile belongs to one user.

## Behavior

`@OneToOne` means: A foreign key exists in one of the tables.

By default: JPA creates a column named: OTHERENTITY_ID

To customize: Use `@JoinColumn.`

## Key Points

-   Usually implemented with a foreign key
-   Can be bidirectional
-   Often used for extension tables (profile, settings)

## Modern Best Practice

Use OneToOne only when truly necessary. Often replaced by ManyToOne with
unique constraint for flexibility.


# 2. Many-to-One Relationship (Most Important)

## Definition

Many entities reference one entity.

Example: Many Orders → One Customer

This is the most common relationship in enterprise apps.

## Behavior

`@ManyToOne` creates: A foreign key column in the table.

Example: ORDER table contains: customer_id

## Why It Is Important

Most real-world systems use: - User → Role - Order → Customer - Product
→ Category - Invoice → Client

## Modern Best Practice

ManyToOne should be: - Default EAGER avoided - Use LAZY instead

Always prefer: fetch = FetchType.LAZY

Because EAGER causes performance issues.


# 3. One-to-Many Relationship

## Definition

One entity contains multiple other entities.

Example: Customer → Orders

`@OneToMany` must use a collection: 
- List 
- Set

## Database Reality

The foreign key is NOT in the OneToMany side. It exists in the ManyToOne
side.

So: @ManyToOne is the real owner.

## mappedBy

Used in bidirectional relationships.

mappedBy tells JPA: "This side is NOT the owner"

`Example: @OneToMany(mappedBy = "customer")`

Means: Customer does NOT own relation. Order owns it.

## Modern Best Practice

Always: Make ManyToOne the owner Use mappedBy on OneToMany

Avoid unidirectional OneToMany with JoinColumn (bad design).



# 4. Many-to-Many Relationship

## Definition

Many entities linked to many others.

Example: Students ↔ Courses

## Behavior

Requires: A join table.

Table contains: student_id course_id

## Join Table

By default: JPA generates automatically.

To customize: Use @JoinTable

## Modern Best Practice (IMPORTANT)

Avoid ManyToMany in real enterprise systems.

Instead: Create a join entity.

Example: Enrollment entity between Student and Course.

Why: 
- Allows extra fields 
- Better control 
- Better performance 
- Easier debugging

ManyToMany is acceptable only for simple cases.


# Owning Side vs Inverse Side

In bidirectional relationships: Only ONE side owns relation.

Owning side: Contains foreign key. Controls database update.

Inverse side: Uses mappedBy.

Example:

Order (owning side): @ManyToOne Customer customer

Customer (inverse): @OneToMany(mappedBy="customer")

If you update only inverse side: Nothing happens in DB.

Always update owning side.

------------------------------------------------------------------------

# JoinColumn

Used to define foreign key column.

Example options: - name - nullable - unique

Example: @JoinColumn(name="customer_id")

------------------------------------------------------------------------

# JoinTable

Used for: ManyToMany or special mapping.

Defines: - Table name - Join columns - Inverse join columns

------------------------------------------------------------------------

# Cascade Operations

## Purpose

Propagates operations to related entities.

Types: - PERSIST - MERGE - REMOVE - REFRESH - DETACH - ALL

Example: Saving parent saves children automatically.

## Modern Best Practice

Use cascade carefully.

Recommended: - PERSIST - MERGE

Avoid: CascadeType.REMOVE on large graphs.

------------------------------------------------------------------------

# Fetch Strategies

## FetchType.EAGER

Loads relation immediately.

Problems: - Heavy queries - Performance issues - N+1 problems

Default for: - ManyToOne - OneToOne

## FetchType.LAZY

Loads only when accessed.

Default for: - OneToMany - ManyToMany

## Modern Rule

Always force LAZY everywhere.

Example: @ManyToOne(fetch = FetchType.LAZY)

Use JOIN FETCH in queries when needed.

------------------------------------------------------------------------

# JOIN FETCH (Very Important)

Used in JPQL to load relations in one query.

Prevents: N+1 problem

Improves performance.

------------------------------------------------------------------------

# N+1 Problem

Most common JPA performance issue.

Example: Load 100 orders. Each order loads customer separately.

Result: 101 queries.

Solution: JOIN FETCH or DTO query.

------------------------------------------------------------------------

# Best Modern Architecture Rules

## Rule 1

Always use LAZY fetch by default.

## Rule 2

Prefer ManyToOne + OneToMany over ManyToMany.

## Rule 3

Avoid EAGER except for very small relations.

## Rule 4

Always define owning side correctly.

## Rule 5

Use DTOs in complex queries.

## Rule 6

Control cascade carefully.

## Rule 7

Never expose entities directly in APIs.

------------------------------------------------------------------------

# Entity Relationship Performance Checklist

Before production: - Check LAZY usage - Remove unnecessary EAGER - Test
N+1 queries - Use JOIN FETCH - Avoid large cascades - Avoid ManyToMany

------------------------------------------------------------------------

# How Spring Boot Uses Relationships

In modern Spring Boot: - Entities define relations - JpaRepository
handles persistence - Hibernate manages SQL - Transactions handled by
@Transactional

Developer focus: Correct mapping + performance tuning.
