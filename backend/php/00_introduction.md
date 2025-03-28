# Introduction to PHP

## 🌐 What is PHP?

PHP (Hypertext Preprocessor) is a **server-side scripting language** designed for web development. It is embedded in HTML and executed on the server, generating dynamic content before sending it to the client's browser.

### Key Characteristics:

✔ **Open-source** – Free to use and modify  
✔ **Cross-platform** – Runs on Windows, Linux, macOS  
✔ **Database-friendly** – Works well with MySQL, PostgreSQL, etc.  
✔ **Large ecosystem** – Frameworks (Laravel, Symfony), CMS (WordPress, Drupal)

### PHP/HTML Integration
```php
<?php
$title = "My PHP Website";
$message = "Welcome to my dynamic PHP website!";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $title; ?></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1><?php echo $title; ?></h1>
</header>

<main>
    <p><?php echo $message; ?></p>
    
    <h2>User List</h2>
    <ul>
        <?php
        $users = ["Alice", "Bob", "Charlie"];
        foreach ($users as $user) {
            echo "<li>$user</li>";
        }
        ?>
    </ul>
</main>

</body>
</html>
```