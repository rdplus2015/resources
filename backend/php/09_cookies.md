
#  Understanding and Using Cookies in PHP

---

## 🔹 What is a Cookie?

A **cookie** is a small piece of data stored on the **client’s browser** and sent back to the server with each request.

- Used for storing **small data**: preferences, session identifiers, login info, etc.
- Cookies are **limited in size** (generally ~4KB per cookie).
- They are stored per domain.

---

## 🔹 Creating a Cookie in PHP

You use the `setcookie()` function **before any output** (headers must not be sent).

### Syntax:
```php
setcookie(name, value, expire, path, domain, secure, httponly);
```

### Example:
```php
// Set a cookie named "username"
setcookie("username", "JohnDoe", time() + 3600); // Expires in 1 hour
```

### Parameters:
- `name` : the name of the cookie
- `value` : the value to store
- `expire` : the expiration timestamp (use `time() + seconds`)
- `path` : the server path the cookie is available on (default "/")
- `domain` : the domain the cookie is available on
- `secure` : if true, cookie only sent over HTTPS
- `httponly` : if true, cookie not accessible via JavaScript

---

## 🔹 Reading a Cookie

PHP stores cookie values in the **superglobal** `$_COOKIE`.

```php
if (isset($_COOKIE['username'])) {
    echo "Welcome " . $_COOKIE['username'];
} else {
    echo "User not recognized.";
}
```

---

## 🔹 Modifying a Cookie

To change a cookie, you must call `setcookie()` again with the **same name** but new value and/or options.

```php
// Update the username cookie
setcookie("username", "JaneDoe", time() + 3600);
```

---

## 🔹 Deleting a Cookie

Set its expiration time in the past:

```php
setcookie("username", "", time() - 3600);
```

This instructs the browser to remove it.

---

## 🔹 Lifetime and Scope

- **Expiration**:
    - No expiration → session cookie (deleted when browser closes)
    - `time() + X` → persists for X seconds
- **Scope**:
    - Path and domain define where the cookie is accessible
    - Cross-domain cookies are restricted (security reasons)

---

## 🔹 Security Best Practices

- Use the `HttpOnly` flag to **block JavaScript access** (protection against XSS)
- Use the `Secure` flag to **force HTTPS**
- Use proper **cookie names** to avoid collisions
- Avoid storing **sensitive data** (like passwords)

---

## 🔹 Common Use Cases

- Remembering user preferences (e.g., theme, language)
- Auto-login (e.g., "remember me")
- Tracking users (analytics, ads, etc.)
- Simplifying forms (pre-filled values)

---

##  Full Example: Remember User with Cookies

### `login.php`
```php
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = $_POST["email"];
    $remember = isset($_POST["remember"]);

    if ($email === "user@example.com") {
        if ($remember) {
            setcookie("user_email", $email, time() + (86400 * 30), "/", "", false, true);
        }
        header("Location: welcome.php");
        exit;
    } else {
        echo "Invalid email";
    }
}
?>
<form method="post">
    <input type="email" name="email" required>
    <label><input type="checkbox" name="remember"> Remember me</label>
    <button type="submit">Login</button>
</form>
```

### `welcome.php`
```php
<?php
if (isset($_COOKIE["user_email"])) {
    echo "Welcome back, " . htmlspecialchars($_COOKIE["user_email"]);
} else {
    echo "Welcome, guest!";
}
?>
```

---

##  Example: Secure Cookie Setup
```php
setcookie(
    "auth_token",
    $token,
    [
        'expires' => time() + 3600,
        'path' => '/',
        'secure' => true,
        'httponly' => true,
        'samesite' => 'Strict'
    ]
);
```

---

## Summary

| Action       | Function Example |
|--------------|------------------|
| Set cookie   | `setcookie("name", "value", time() + 3600);` |
| Read cookie  | `$_COOKIE['name']` |
| Update cookie| Reuse `setcookie()` with same name |
| Delete cookie| `setcookie("name", "", time() - 3600);` |

---

Cookies are powerful for enhancing UX and storing user data — but use them responsibly and securely.