
# PHP Database Access with PDO & DAO

## What is PDO?

**PDO (PHP Data Objects)** is a database access abstraction layer. It allows you to interact with various databases (MySQL, PostgreSQL, SQLite...) using the same API.

**Benefits:**
- Security (protection against SQL injection)
- Clean syntax
- Multi-database support

---

##  Database Connection with PDO

```php
<?php
$host = 'localhost';
$dbname = 'testdb';
$user = 'root';
$password = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Show SQL errors
    echo " Connected successfully!";
} catch (PDOException $e) {
    die(" Connection failed: " . $e->getMessage());
}
?>
```

---

##  Prepared Statements

Prepared statements protect your application from **SQL injection**.

###  Basic Example

```php
// BAD (insecure)
$email = $_POST['email'];
$stmt = $pdo->query("SELECT * FROM users WHERE email = '$email'");

$email = $_POST['email']; // Assume the user enters: ' OR 1=1 --
$pdo->query("SELECT * FROM users WHERE email = '$email'");
// → Risque : La requête devient SELECT * FROM users WHERE email = '' OR 1=1 --' et renvoie tous les utilisateurs !


// GOOD (secure)
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$_POST['email']]);
```

###  Named Parameters

```php
$stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
$stmt->execute([
    ':name' => 'John Doe',
    ':email' => 'john@example.com'
]);
```

---

## Fetching Data: `fetch()` vs `fetchAll()`

| Method       | Use Case                    | Returns                   |
|--------------|-----------------------------|----------------------------|
| `fetch()`    | Get **one row**             | Single associative array   |
| `fetchAll()` | Get **all matching rows**   | Array of associative arrays|

```php
// fetch()
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([1]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

// fetchAll()
$stmt = $pdo->query("SELECT * FROM users");
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);
```

By default, `fetch()` returns **both an associative and indexed array** (duplicates):
```php
$stmt = $pdo->query("SELECT name, email FROM users");
$row = $stmt->fetch();
print_r($row);
```
```php
[
"name" => "Jean", // Assoc
0 => "Jean", // Indexed (useless duplicate)
"email" => "jean@example.com",
1 => "jean@example.com"
]
```
- **Solution : `FETCH_ASSOC`**
- **Avoids duplicates** → returns only named keys.
- **More readable and efficient**.
##  Transactions

Use transactions to execute multiple SQL statements **atomically** (all or nothing).

```php
try {
    $pdo->beginTransaction();

    $pdo->prepare("UPDATE accounts SET balance = balance - 100 WHERE id = 1")->execute();
    //     $pdo->exec("UPDATE compte SET solde = solde - 100 WHERE id = 1");
    
    $pdo->prepare("UPDATE accounts SET balance = balance + 100 WHERE id = 2")->execute();
    //  $pdo->exec("UPDATE compte SET solde = solde + 100 WHERE id = 2");
    
    $pdo->commit();
} catch (Exception $e) {
    $pdo->rollBack();
    echo " Error: " . $e->getMessage();
}
```

---

##  DAO: Data Access Object Pattern

A **DAO** is a PHP class responsible for interacting with a specific table in the database.

###  Benefits
- Code organization
- Reusability
- Separation of concerns (no SQL in HTML files)

---

## Example: UserDAO

**Folder structure:**

```
project/
│
├── connection.php
└── dao/
    └── UserDAO.php
```

### connection.php

```php
<?php
$pdo = new PDO("mysql:host=localhost;dbname=testdb;charset=utf8", "root", "");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
```

### dao/UserDAO.php

```php
<?php
class UserDAO {
    private $pdo;

    public function __construct(PDO $pdo) {
        $this->pdo = $pdo;
    }

    public function create($name, $email) {
        $stmt = $this->pdo->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
        return $stmt->execute([$name, $email]);
    }

    public function read($id) {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    public function update($id, $name, $email) {
        $stmt = $this->pdo->prepare("UPDATE users SET name = ?, email = ? WHERE id = ?");
        return $stmt->execute([$name, $email, $id]);
    }

    public function delete($id) {
        $stmt = $this->pdo->prepare("DELETE FROM users WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function readAll() {
        $stmt = $this->pdo->query("SELECT * FROM users");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
```

### test.php

```php
<?php
require_once 'connection.php';
require_once 'dao/UserDAO.php';

$userDAO = new UserDAO($pdo);

$userDAO->create("Alice", "alice@example.com");
$user = $userDAO->read(1);
print_r($user);

$all = $userDAO->readAll();
print_r($all);
```

---

##  Best Practices

|  DO this                                | ❌ Don’t do this                            | Why?                                   |
|-------------------------------------------|---------------------------------------------|----------------------------------------|
| Use `PDO`                                 | Avoid `mysql_*` or raw `mysqli`             | Modern, secure, and flexible           |
| Use `prepare()` + `execute()`             | Avoid direct variable interpolation         | Prevents SQL injection                 |
| Use `PDO::FETCH_ASSOC`                    | Avoid default fetch (creates duplicates)    | Returns clean associative arrays       |
| Use a `DAO` to organize your SQL logic    | Don’t mix SQL and HTML                      | Clean and maintainable architecture    |

- **Preferred**: `prepare()` + `execute()` **in 99% of cases** (security required).
- **Restricted cases for `exec()`**:
  - **Static** queries (e.g., table creation).
  - Internal scripts **without user variables**.
---

##  Summary

- **PDO** = Database connection and execution tool
- **Prepared Statements** = Prevent SQL injection
- **fetch() vs fetchAll()** = Get 1 or many rows
- **DAO** = Organize your database code in classes

---

