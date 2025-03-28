# Functions

### Defining and Returning Values

```php
// Simple function
function greet($name) {
    return "Hello, $name!";
}
echo greet("Alice"); // Hello, Alice!

// Function with default parameter
function say($message = "Hello World") {
    echo $message;
}
say(); // Hello World
say("Good morning!"); // Good morning!

// Type declarations (PHP 7+)
function addNumbers(int $a, int $b): int {
    return $a + $b;
}
echo addNumbers(5, 10); // 15
```

### Passing Parameters

#### By Value (Default)

```php
function increment($num) {
    $num++;
    echo "Inside function: $num\n"; // 6
}

$value = 5;
increment($value);
echo "Outside function: $value\n"; // 5
```

#### By Reference
you give the function direct access to the original variable rather than a copy of its value.
```php
function incrementRef(&$num) {
    $num++;
    echo "Inside function: $num\n"; // 6
}

$value = 5;
incrementRef($value);
echo "Outside function: $value\n"; // 6
```

### Variable Functions

```php
function sayHello() {
    echo "Hello!";
}

function sayGoodbye() {
    echo "Goodbye!";
}

$func = "sayHello";
$func(); // Hello!

$func = "sayGoodbye";
$func(); // Goodbye!
```

### Anonymous Functions (Closures)

```php
$greet = function($name) {
    return "Hello, $name!";
};
echo $greet("Bob"); // Hello, Bob!

// Use variables from parent scope
$prefix = "Mr. ";
$greetFormal = function($name) use ($prefix) {
    return "Hello, $prefix$name!";
};
echo $greetFormal("Smith"); // Hello, Mr. Smith!
```

## callbacks

```php
function processNumbers(array $numbers, callable $callback) {
    foreach ($numbers as $number) {
        echo $callback($number) . " ";
    }
}

$numbers = [1, 2, 3, 4];
processNumbers($numbers, function($n) { return $n * 2; }); // 2 4 6 8
```

# String and Array Manipulation

### String Functions

```php
// Basic string operations
$str = "Hello World";
echo strlen($str); // 11
echo strtoupper($str); // HELLO WORLD
echo strtolower($str); // hello world
echo ucfirst("hello"); // Hello
echo ucwords("hello world"); // Hello World

// Searching
echo strpos($str, "World"); // 6
echo strstr($str, "World"); // World
echo substr($str, 6, 5); // World

// Replacement
echo str_replace("World", "PHP", $str); // Hello PHP
echo substr_replace($str, "PHP", 6, 5); // Hello PHP

// Formatting
printf("Name: %s, Age: %d", "John", 30); // Name: John, Age: 30
$formatted = sprintf("Price: $%.2f", 19.99); // Price: $19.99

// Regular Expressions
if (preg_match("/^[a-zA-Z ]*$/", "John Doe")) {
echo "Valid name";
}
$words = preg_split("/\s+/", "Hello   World"); // ["Hello", "World"]
```

### Array Functions
```php


// Creating arrays
$indexed = [1, 2, 3];
$assoc = ["name" => "John", "age" => 30];
$multi = [
["name" => "John", "age" => 30],
["name" => "Jane", "age" => 25]
];

// Adding elements
$indexed[] = 4; // [1, 2, 3, 4]
array_push($indexed, 5, 6); // [1, 2, 3, 4, 5, 6]
$assoc["email"] = "john@example.com";

// Removing elements
array_pop($indexed); // Removes last element
array_shift($indexed); // Removes first element
unset($assoc["age"]); // Removes specific element

// Array processing
$numbers = [1, 2, 3, 4, 5];

// array_map
$squared = array_map(function($n) { return $n * $n; }, $numbers); // [1, 4, 9, 16, 25]

// array_filter
$evens = array_filter($numbers, function($n) { return $n % 2 == 0; }); // [2, 4]

// array_reduce
$sum = array_reduce($numbers, function($carry, $item) {
return $carry + $item;
}, 0); // 15

// Sorting
sort($numbers); // Sorts in ascending order
rsort($numbers); // Sorts in descending order
asort($assoc); // Sorts associative array by values
ksort($assoc); // Sorts associative array by keys

// Merging
$merged = array_merge($indexed, [7, 8, 9]); // [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

----------
