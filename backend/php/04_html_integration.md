## PHP/HTML Integration

### Basic Embedding

```php
<!DOCTYPE html>
<html>
<head>
    <title>PHP in HTML</title>
</head>
<body>
    <h1><?php echo "Current Date: " . date("Y-m-d"); ?></h1>

    <?php if (date("H") < 12): ?>
        <p>Good morning!</p>
    <?php else: ?>
        <p>Good afternoon!</p>
    <?php endif; ?>
    
    <ul>
        <?php foreach (["Apple", "Banana", "Cherry"] as $fruit): ?>
            <li><?= htmlspecialchars($fruit) ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

### Template Separation

```php
<!-- config.php -->
<?php
$title = "Product Page";
$products = [
    ["name" => "Laptop", "price" => 999.99],
    ["name" => "Phone", "price" => 699.99]
];
?>

<!-- header.php -->
<!DOCTYPE html>
<html>
<head>
    <title><?= htmlspecialchars($title) ?></title>
    <style>
        .product { border: 1px solid #ccc; padding: 10px; margin: 10px; }
    </style>
</head>
<body>
    <header>
        <h1><?= htmlspecialchars($title) ?></h1>
    </header>
    <main>

<!-- products.php -->
<?php foreach ($products as $product): ?>
    <div class="product">
        <h2><?= htmlspecialchars($product['name']) ?></h2>
        <p>Price: $<?= number_format($product['price'], 2) ?></p>
    </div>
<?php endforeach; ?>

<!-- footer.php -->
    </main>
    <footer>
        <p>&copy; <?= date('Y') ?> My Store</p>
    </footer>
</body>
</html>

<!-- index.php -->
<?php
require 'config.php';
include 'header.php';
include 'products.php';
include 'footer.php';
?>
```

### Output Buffering
```php

<?php ob_start(); ?>

<h1>Welcome to my page</h1>
<p>This content will be buffered.</p>

<?php
$content = ob_get_clean();
// Now we can modify $content before outputting
$content = str_replace("my page", "our website", $content);
echo $content;
?>
```

### Best Practices

1.  **Always escape output**:
```php
    echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');
```
2.  **Separate logic and presentation**:
```php
// Bad
    <?php 
    $users = getUsersFromDatabase();
    foreach ($users as $user) {
        echo "<div class='user'>{$user['name']}</div>";
    }
    ?>

    // Good
    <?php 
    $users = getUsersFromDatabase();
    include 'user_list_template.php';
    ?>
```

3.  **Use alternative syntax for control structures in templates**:
```php
    <?php if ($is_admin): ?>
        <div class="admin-panel">Admin tools</div>
    <?php endif; ?>
```

4.  **Consider using template engines** (Twig, Blade) for complex projects.
