
# Syntax and Structures

### Variables and Constants

#### Variables

- Declared using the `$` symbol.
- Dynamically typed.
- Example:
```php
  $item = "cookies"; // str
  $sku = 25025; // int
  $price = 12.95; // float
  $is_available = true; // bool
  $color = ['red', 'yellow'] // array

  echo "Name: $name";
  unset($item);  // destroys the variable and frees the occupied memory.
```

#### Constants

- Declared using `define()` or `const`.
- Immutable after definition.
- Example:
```php
  // Old style (global scope)
  define("PI", 3.14159);
  define("GREETING", "Hello World", true); // case-insensitive

  // New style (namespace aware, PHP 5.3+)
  const DB_HOST = "localhost";
  const DB_NAME = "test_db";

  // Magic constants
  echo __LINE__; // Current line number
  echo __FILE__; // Full path and filename
```

### Conditional Statements

#### `if-else`

```php
$score = 85;

if ($score >= 90) {
    $grade = 'A';
} elseif ($score >= 80) {
    $grade = 'B';
} elseif ($score >= 70) {
    $grade = 'C';
} else {
    $grade = 'F';
}

echo "Your grade is $grade";
```

#### `switch`

```php
$day = "Monday";

switch ($day) {
    case "Monday":
        echo "Start of work week";
        break;
    case "Friday":
        echo "Weekend is coming!";
        break;
    case "Saturday":
    case "Sunday":
        echo "It's the weekend!";
        break;
    default:
        echo "Regular work day";
}
```

### Loops

#### `for` loop

```php
// Count from 1 to 10
for ($i = 1; $i <= 10; $i++) {
    echo $i . " ";
}

// Countdown from 10 to 1
for ($i = 10; $i >= 1; $i--) {
    echo $i . " ";
}
```

#### `while` loop

```php
// Basic while
$count = 1;
while ($count <= 5) {
    echo "Count: $count\n";
    $count++;
}

// With break
while (true) {
    $rand = rand(1, 10);
    echo "$rand ";
    if ($rand == 5) {
        echo "Found 5!";
        break;
    }
}
```

#### `foreach` loop

```php
// Indexed array
$colors = ["red", "green", "blue"];
foreach ($colors as $color) {
    echo "$color ";
}

// Associative array
$user = ["name" => "John", "age" => 30, "email" => "john@example.com"];
foreach ($user as $key => $value) {
    echo "$key: $value\n";
}

// Modifying array values by reference
$numbers = [1, 2, 3, 4];
foreach ($numbers as &$number) {
    $number *= 2;
}
print_r($numbers); // [2, 4, 6, 8]
unset($number); // Important to break reference
```

---

