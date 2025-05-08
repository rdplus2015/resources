# Form Handling

## Basic Form Processing

```html
<!-- form.html -->
<form action="process.php" method="post">
    Name: <input type="text" name="name"><br>
    Email: <input type="email" name="email"><br>
    <input type="submit" value="Submit">
</form>
```

```php
<!-- process.php -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
    
    if ($email === false) {
        echo "Invalid email format";
    } else {
        echo "Thank you, $name! Your email ($email) has been registered.";
    }
}
?>
```

## Native Methods

- **Superglobals** (`$_SERVER`, `$_POST`, etc.) → Access to HTTP data.
- **`filter_var()`** → Validation and sanitization.
- **Security functions** (`htmlspecialchars()`, `password_hash()`, etc.).

### Useful PHP Superglobals

| Variable | Description | Example |
| -- | --- | -- |
| `$_POST` | Data from forms sent by POST. | `$_POST['email']` |
| `$_GET` | Data passed in the URL (GET). | `$_GET['id']` |
| `$_SERVER` | Server and query information. | `$_SERVER['REQUEST_METHOD']` |
| `$_SESSION` | Data storage between pages. | `$_SESSION['user_id']` |
| `$_COOKIE` | Accesses browser cookies. | `$_COOKIE['lang']` |

### Validation Filters (return `false` if invalid)

| Filter | Example Usage |
| --- | --- |
| **`FILTER_VALIDATE_EMAIL`** | `filter_var($email, FILTER_VALIDATE_EMAIL)` |
| **`FILTER_VALIDATE_URL`** | Validates a URL (e.g., `https://example.com`). |
| **`FILTER_VALIDATE_IP`** | Validates an IPv4 or IPv6 address. |
| **`FILTER_VALIDATE_INT`** | `filter_var($age, FILTER_VALIDATE_INT)` |

### Sanitization Filters (Data Cleansing)

| Filter | Effect |
| --- | --- |
| **`FILTER_SANITIZE_EMAIL`** | Removes illegal characters from an email. |
| **`FILTER_SANITIZE_NUMBER_INT`** | Keeps only numbers and `+ -`. |
| **`FILTER_SANITIZE_URL`** | Removes illegal characters from a URL. |


## Other Useful Security Features

| Function | Use |
| --- | --- |
| **`htmlspecialchars()`** | Converts special characters to HTML entities (`<` → `&lt;`). |
| **`strip_tags()`** | Removes **all** HTML tags. |
| **`password_hash()`** | Encrypts a password. |
| **`mysqli_real_escape_string()`** | Escapes SQL-unsafe characters (⚠️ Less secure than PDO). |

**Example**
```php
// Display 
$dirty_input = "<script>alert('Hack')</script>";
$clean_input = htmlspecialchars(strip_tags($dirty_input), ENT_QUOTES, 'UTF-8');
echo $clean_input; // Display: &lt;script&gt;alert('Hack')&lt;/script&gt;

// Store 
$name = strip_tags(trim($_POST['name'])); // nettoyage simple
$pdo->prepare("INSERT INTO users (name) VALUES (?)")->execute([$name]);

/*
    <strip_tags() → removes all HTML (useful if you don't want any tags)
    htmlspecialchars() → prevents the interpretation of remaining special characters (XSS security)
*/
```

**Example with `password_hash()`:**
```php
$password = "myPassword123";
$hashed_password = password_hash($password, PASSWORD_BCRYPT);
// Store $hashed_password in database.
```
**Note**
- `filer_var`, `filter_input` is generally used to sanitize input before storing or processing data
- `htmlspecialchars()` is used when outputting data into HTML to prevent by ensuring that user input is safely displayed.

## Secure Form Handling Example

```php
<?php
session_start();

// 1. Check CSRF Token
if ($_SERVER['REQUEST_METHOD'] !== 'POST' || 
    !isset($_POST['csrf_token']) || 
    $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
    die("CSRF validation failed!");
}

// 2. Sanitize & Validate Inputs
function clean_input($input) {
    return htmlspecialchars(trim(strip_tags($input ?? '')), ENT_QUOTES, 'UTF-8');
}

$name = clean_input($_POST['name'] ?? '');
$email = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);
$message = clean_input($_POST['message'] ?? '');

// 3. Validate Data
$errors = [];
if (empty($name)) {
    $errors[] = "Name is required.";
}
if (!$email) {
    $errors[] = "Invalid email format.";
}
if (empty($message)) {
    $errors[] = "Message cannot be empty.";
}

// 4. If errors, display them
if (!empty($errors)) {
    foreach ($errors as $error) {
        echo "<p>Error: $error</p>";
    }
    exit;
}

// 5. Securely Store in Database (PDO - Anti-SQL Injection)
try {
    $pdo = new PDO("mysql:host=localhost;dbname=test", "user", "password");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $stmt = $pdo->prepare("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)");
    $stmt->execute([$name, $email, $message]);

    echo "Thank you! Your message has been sent.";
} catch (PDOException $e) {
    die("Database error: " . htmlspecialchars($e->getMessage()));
}
?>
```

## Key Difference Between XSS and CSRF

| | XSS (Cross-Site Scripting) | CSRF (Cross-Site Request Forgery) |
| --- | --- | --- |
| **Type of Attack** | Injecting malicious code **into your site**. | Exploiting your session **on another site**. |
| **Target** | Your site visitors. | You (as an admin/logged-in user). |
| **Protection** | `htmlspecialchars()`, `strip_tags()` | CSRF token |

## File Uploads
```php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["file"])) {
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["file"]["name"]);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
    
    // Check if file is an actual image
    $check = getimagesize($_FILES["file"]["tmp_name"]);
    if ($check !== false) {
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
    
    // Check file size (500KB max)
    if ($_FILES["file"]["size"] > 500000) {
        echo "File is too large.";
        $uploadOk = 0;
    }
    
    // Allow certain file formats
    if (!in_array($imageFileType, ["jpg", "jpeg", "png"])) {
        echo "Only JPG, JPEG, PNG files are allowed.";
        $uploadOk = 0;
    }
    
    if ($uploadOk == 1) {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
            echo "File uploaded successfully.";
        } else {
            echo "Error uploading file.";
        }
    }
}
```

## Best Practices

1. **Always escape output** (`htmlspecialchars()`).
2. **Use HTTPS** to avoid MITM attacks.
3. **Limit form submissions** (rate limiting, tokens).
4. **Store passwords securely** (`password_hash()`).
5. **Clean up file uploads** (and validate file type/size).