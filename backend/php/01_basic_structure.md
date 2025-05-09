
# Syntax and Structures

### Variables and Constants

#### Variables

- Declared using the `$` symbol.
- Dynamically typed.
- Example:
```php
  $item = "cookies"; // str
  $sku = 25025; // int
  $meaning += 2;   // Adds 2 to $meaning
  $price = 12.95; // float
  $is_available = true; // bool
  $color = ['red', 'yellow'] // array

  echo "Name: $name";
  echo  "My name is {$name}"
  unset($item);  // destroys the variable and frees the occupied memory.
  var_dump($name); // display structured information
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

## Strict Comparison Operators

PHP provides strict comparison operators to compare both the value and the type of variables:​

-   `===` : **Identical** — Returns `true` if both operands are of the same type and value.

-   `!==` : **Not Identical** — Returns `true` if operands are of different types or values.


**Example:**

```php
$a = 5;         // Integer
$b = '5';       // String

var_dump($a === $b); // Output: bool(false) — Different types
var_dump($a !== $b); // Output: bool(true)
```
## 2. Binary (Bitwise) Operators

Binary operators perform operations on the binary representations of integers:​

-   `&` : **And** — Bits set in both operands are set.

-   `|` : **Or (Inclusive Or)** — Bits set in either operand are set.

-   `^` : **Xor (Exclusive Or)** — Bits set in one operand but not both are set.

-   `~` : **Not** — Bits that are set are not set, and vice versa.

-   `<<` : **Shift Left** — Shifts bits to the left, equivalent to multiplying by 2 for each shift.

-   `>>` : **Shift Right** — Shifts bits to the right, equivalent to dividing by 2 for each shift.


**Example:**
```php
$a = 6;      // Binary: 110
$b = 3;      // Binary: 011

echo $a & $b;  // Output: 2  (Binary: 010)
echo $a | $b;  // Output: 7  (Binary: 111)
echo $a ^ $b;  // Output: 5  (Binary: 101)
echo ~$a;      // Output: -7 (Binary: ...11111001)
echo $a << 1;  // Output: 12 (Binary: 1100)
echo $a >> 1;  // Output: 3  (Binary: 011)
```

## 3. Null Coalescing Operator (`??`)

Introduced in PHP 7, the `??` operator returns the first operand if it exists and is not `null`; otherwise, it returns the second operand. It's particularly useful for providing default values.​

**Example:**
```php
$username = $_GET['user'] ?? 'guest';
// Equivalent to:
$username = isset($_GET['user']) ? $_GET['user'] : 'guest';
```
In this example, `$username` will be assigned the value of `$_GET['user']` if it exists; otherwise, it defaults to `'guest'`.


