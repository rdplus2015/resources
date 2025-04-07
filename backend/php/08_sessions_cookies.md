# Sessions and Cookies in PHP 

##  Overview

Cookies and sessions are two key tools in PHP for maintaining state across pages in a web application. This document will help you understand how to use them, where to use each, and how to build secure and functional PHP applications with them.

---

## What Are Sessions and Cookies?

| Feature     | Cookies                          | Sessions                             |
|-------------|----------------------------------|---------------------------------------|
| Stored in   | Client-side (browser)            | Server-side                           |
| Size limit  | ~4KB                             | Depends on server configuration       |
| Security    | Less secure                      | More secure (not directly exposed)    |
| Lifetime    | Set manually                     | Until browser closes or timeout       |
| Use cases   | Remember user preferences        | Logged-in user tracking, shopping cart |

---

## When to Use Sessions vs Cookies

| Use Case                            | Best Tool   |
|------------------------------------|-------------|
| Remember theme or language         | Cookie      |
| User login/session                 | Session     |
| Shopping cart                      | Session     |
| Remember me (persistent login)     | Both        |
| Store temporary data across pages  | Session     |

---

##  Working with Cookies in PHP

###  Create a Cookie

```php
setcookie("username", "john_doe", time() + 3600, "/");
```

### 🔍 Read a Cookie

```php
if (isset($_COOKIE["username"])) {
    echo "Welcome " . $_COOKIE["username"];
}
```

###  Update a Cookie

```php
setcookie("username", "jane_doe", time() + 3600, "/");
```

### Delete a Cookie

```php
setcookie("username", "", time() - 3600, "/");
```

---

##  Working with Sessions in PHP

###  Start a Session

```php
session_start();
```

###  Create/Set Session Data

```php
$_SESSION["user_id"] = 42;
```

###  Read Session Data

```php
echo $_SESSION["user_id"];
```

### Update Session Data

```php
$_SESSION["user_id"] = 99;
```

###  Delete Session Data

```php
unset($_SESSION["user_id"]);
```

### Destroy Entire Session

```php
session_unset(); // Clear all variables
session_destroy(); // End session
```

---

##  Managing Sessions: VRUD Pattern

| Operation | Action                                | Code Example |
|----------|----------------------------------------|--------------|
| **View** | Show session data                      | `print_r($_SESSION);` |
| **Read** | Access specific session value          | `echo $_SESSION['key'];` |
| **Update** | Change session data                  | `$_SESSION['key'] = 'new';` |
| **Delete** | Remove or destroy session variables  | `unset($_SESSION['key']);` or `session_destroy();` |

---

##  Real-World Use Case: Authentication System

###  Features

- Register user and save credentials (simplified)
- Login and create session
- Access dashboard
- Logout

---

###  `register.php`

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $users = [];
    if (file_exists("users.json")) {
        $users = json_decode(file_get_contents("users.json"), true);
    }

    $username = $_POST["username"];
    $password = password_hash($_POST["password"], PASSWORD_DEFAULT);

    $users[$username] = $password;

    file_put_contents("users.json", json_encode($users));
    echo "Registration successful. <a href='login.php'>Login here</a>";
}
?>
```

**Form:**
```html
<form method="POST">
  <input name="username" placeholder="Username" required>
  <input type="password" name="password" placeholder="Password" required>
  <button type="submit">Register</button>
</form>
```

---

###  `login.php`

```php
<?php
session_start();
$users = json_decode(file_get_contents("users.json"), true);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    if (isset($users[$username]) && password_verify($password, $users[$username])) {
        $_SESSION["user"] = $username;
        header("Location: dashboard.php");
    } else {
        echo "Invalid credentials";
    }
}
?>
```

**Form:**
```html
<form method="POST">
  <input name="username" placeholder="Username" required>
  <input type="password" name="password" placeholder="Password" required>
  <button type="submit">Login</button>
</form>
```

---

### `dashboard.php`

```php
<?php
session_start();
if (!isset($_SESSION["user"])) {
    header("Location: login.php");
    exit;
}
echo "Welcome " . $_SESSION["user"];
echo "<br><a href='logout.php'>Logout</a>";
?>
```

---

###  `logout.php`

```php
<?php
session_start();
session_destroy();
header("Location: login.php");
?>
```

---

##  Secure Session and Cookie Practices

- Always use `session_start()` before any output.
- Use `session_regenerate_id()` after login to avoid session fixation.
- Use `httponly` and `secure` flags on cookies:

```php
setcookie("token", $value, time()+3600, "/", "", true, true);
```

- Use HTTPS to protect both cookies and session data.
- Always validate user input on login.

---

##  Advanced: Store Sessions in a Database

```php
ini_set('session.save_handler', 'user');
// Use custom session handlers for scalable systems
```

You can use libraries like Redis or databases like MySQL to store sessions for larger, scalable applications.

---

##  Debugging Tips

- Use `print_r($_SESSION);` or `var_dump($_COOKIE);` to inspect values.
- Clear browser cookies and sessions often during testing.
- Use browser dev tools > Application > Storage > Cookies to inspect them.

---

##  Summary

- Use **Cookies** for long-term, client-side storage (preferences, themes).
- Use **Sessions** for short-term, server-side storage (login, cart).
- Implement VRUD for managing session/cookie data safely.
- Apply best practices to keep your application secure and user-friendly.

---

##  Resources

- [PHP Manual - Cookies](https://www.php.net/manual/en/function.setcookie.php)
- [PHP Manual - Sessions](https://www.php.net/manual/en/book.session.php)
- [OWASP Secure Session Management](https://owasp.org/www-project-cheat-sheets/cheatsheets/Session_Management_Cheat_Sheet.html)

---