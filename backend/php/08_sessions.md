
#  Understanding PHP Sessions

---

##  🔹What is a Session?

> **A session is:**  
> The period between the creation of a `session_id` (using `session_start()`) and its destruction (using `session_destroy()`).

- 1 session = 1 connected user = 1 browser
- It allows you to **store server-side data** related to a user.

---

##  🔹General Functioning
### Double Creation on `session_start()`
When PHP runs `session_start()` for the first time:

#### 1. Server Side (Session File)
- Creates a file in `session.save_path` (e.g., `/tmp/`)  
  - Filename: `sess_[ID]` (e.g. `sess_abc123def456`)  
  - Initial content: empty (waits for `$_SESSION` data)  
- When you modify `$_SESSION`, data is **serialized and stored**

#### 2. Client Side (Cookie)
Sends a `PHPSESSID` cookie to the browser

1. The server creates a unique identifier (`session_id`)
2. This ID is sent to the browser via a **cookie** (`PHPSESSID`)
3. On every following request, the browser sends back this cookie
4. PHP uses this cookie to find and load the **session data** associated

#### Example:
```php
// First call to session_start()
session_start(); 

// Result:
// - Server: Creates /tmp/sess_abc123def456 (empty)
// - Client: Receives PHPSESSID=abc123def456
```
### Analogy: Secret Badge

➤ When user logs in, they get a **secret badge** (`PHPSESSID`)  
➤ The badge is sent with every request  
➤ Server verifies ID and session data  
➤ If valid → access granted
---

## 🔹Session Data (`$_SESSION`)

`$_SESSION` is a **global PHP array** that stores persistent data.

Typical data stored:

- **User Info**: `username`, `user_id`, `email`, `role`
- **Connection State**: `is_connected`, `logged_in`
- **Temporary Data**: `cart`, `csrf_token`, `flash_message`
- **Preferences**: `language`, `theme`, etc.

---
## 🔹Practical Example: Session and Login

### Steps

#### 1. Anonymous Session
```php
session_start();
$_SESSION['cart'][] = 'apple';
```
> User browses and adds items to the cart → stored in `$_SESSION`

#### 2. Authentication
```php
session_start();
if ($ok) {
    session_regenerate_id(true); // prevent session fixation
    $_SESSION['user_id'] = 42;
    $_SESSION['username'] = 'John';
}
```
> You add user info to the session → it becomes **identified**

---

##  🔹Session Lifetime

- Default: expires **when the browser is closed**
- You can set a custom expiration:
```ini
session.gc_maxlifetime = 1440 ; // 24 minutes
```

---

##  🔹Session File

###  Location

- Usually in `/tmp`, file name: `sess_<session_id>`

###  Content

> This file contains **what you put in `$_SESSION`**


---

##  🔹Why a File?

Because **HTTP is stateless**: each request is independent.

Without session file:
- You log in
- You move to another page
- PHP forgets everything

With session file:
- PHP remembers the user via the ID
- Reloads data into `$_SESSION`

---

##  🔹Detailed Flow

```php
session_start();
```

Does:

1. Reads `PHPSESSID` cookie from browser
2. Finds the session file on the server or create it
3. Loads the data into `$_SESSION`

---

##  🔹Login Example

### HTML Form
```php
<form method="POST" action="login.php">
  <input type="text" name="email">
  <input type="password" name="password">
  <button type="submit">Log In</button>
</form>
```

### Processing `login.php`
```php
session_start();

if ($_POST['email'] == 'test@example.com' && $_POST['password'] == '1234') {
    $_SESSION['email'] = $_POST['email'];
    $_SESSION['is_connected'] = true;
    header('Location: profile.php');
    exit;
} else {
    echo "Invalid credentials";
}
```

---

## 🔹Session Security

- Sensitive data is **not sent to the browser**  
- Only `session_id` is stored in a cookie  
- Actual data is **stored server-side**

### Recommendations:

- `session_regenerate_id(true);` after login
- Log out after inactivity
- Set expiration (`session.gc_maxlifetime`)
- Check `$_SESSION['is_connected']` in secure pages
- `session_destroy();` on logout

---

## 🔹Protect Sensitive Pages

> PHP **does not remember login state** between pages.

- Always call `session_start();` at the top
- Otherwise `$_SESSION` will be empty

```php
session_start();
if (!isset($_SESSION['is_connected']) || $_SESSION['is_connected'] !== true) {
    header('Location: login.php');
    exit;
}
```
---

##  🔹Direct Access to Sensitive Files

### Problem:
- A user can access `dashboard.php` directly without going through `login.php`

### Solutions:

- Use a **single entry point** (e.g. `index.php` controller)  
- Protect controllers with `$_SESSION` checks  
-  Use `.htaccess` to block direct access

---


## 🔹Complete Example with Access Control

### `login.php`
```php
session_start();

$email = $_POST['email'];
$password = $_POST['password'];

if ($email == 'test@example.com' && $password == '1234') {
    session_regenerate_id(true); //  security
    $_SESSION['email'] = $email;
    $_SESSION['is_connected'] = true;
    header('Location: profile.php');
    exit;
}
```

### `profile.php`
```php
session_start();

if (!isset($_SESSION['is_connected']) || $_SESSION['is_connected'] !== true) {
    header('Location: login.php');
    exit;
}

echo "Welcome " . $_SESSION['email'];
```

---

##  🔹`.htaccess` (optional for MVC)

> Block direct access to everything except your front controller `index.php`

### In `/app/views/`, `/app/models/`, etc.

```
# Prevent direct file access
Deny from all
```

### In root directory (if redirection is needed)

```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^ index.php [QSA,L]
```

---

##  🔹Advanced: Store Sessions in a Database

```php
ini_set('session.save_handler', 'user');
// Use custom session handlers for scalable systems
```

You can use libraries like Redis or databases like MySQL to store sessions for larger, scalable applications.

---

##  🔹 Debugging Tips

- Use `print_r($_SESSION);` or `var_dump($_COOKIE);` to inspect values.
- Clear browser cookies and sessions often during testing.
- Use browser dev tools > Application > Storage > Cookies to inspect them.


---

##  🔹 Resources

- [PHP Manual - Cookies](https://www.php.net/manual/en/function.setcookie.php)
- [PHP Manual - Sessions](https://www.php.net/manual/en/book.session.php)
- [OWASP Secure Session Management](https://owasp.org/www-project-cheat-sheets/cheatsheets/Session_Management_Cheat_Sheet.html)

---