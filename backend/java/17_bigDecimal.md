# BigDecimal in Java

## Overview
`BigDecimal` is a class in the `java.math` package designed to handle immutable arbitrary-precision decimal numbers. It is ideal for scenarios requiring exact decimal calculations, such as financial and scientific computations.

---

## Key Features
- **Arbitrary Precision**: Avoids rounding errors by providing control over precision.
- **Immutable**: Operations return a new instance, ensuring immutability.
- **Rounding Modes**: Supports multiple rounding strategies (`java.math.RoundingMode`).
- **Math Operations**: Provides methods for addition, subtraction, multiplication, division, scaling, and more.
- **String Representation**: Constructing `BigDecimal` with a `String` is recommended to avoid precision loss.

---

## Usage Examples

### Creating a `BigDecimal`
```java
import java.math.BigDecimal;

public class BigDecimalExample {
    public static void main(String[] args) {
        // Create BigDecimal from String
        BigDecimal bd1 = new BigDecimal("123.456");
        
        // Create BigDecimal from int or double
        BigDecimal bd2 = BigDecimal.valueOf(123.456);

        System.out.println("BigDecimal from String: " + bd1);
        System.out.println("BigDecimal from valueOf: " + bd2);
    }
}
```

---

### Common Operations
```java
import java.math.BigDecimal;
import java.math.RoundingMode;

public class BigDecimalOperations {
    public static void main(String[] args) {
        BigDecimal num1 = new BigDecimal("10.50");
        BigDecimal num2 = new BigDecimal("2.30");

        // Addition
        BigDecimal sum = num1.add(num2);
        System.out.println("Sum: " + sum);

        // Subtraction
        BigDecimal diff = num1.subtract(num2);
        System.out.println("Difference: " + diff);

        // Multiplication
        BigDecimal product = num1.multiply(num2);
        System.out.println("Product: " + product);

        // Division with Rounding
        BigDecimal quotient = num1.divide(num2, 2, RoundingMode.HALF_UP);
        System.out.println("Quotient: " + quotient);

        // Scaling
        BigDecimal scaled = num1.setScale(3, RoundingMode.HALF_UP);
        System.out.println("Scaled: " + scaled);
    }
}
```

---

## Rounding Modes
`BigDecimal` supports various rounding modes defined in `RoundingMode`:

- **HALF_UP**: Rounds towards the nearest neighbor, breaking ties upward.
- **HALF_DOWN**: Rounds towards the nearest neighbor, breaking ties downward.
- **HALF_EVEN**: Rounds towards the nearest neighbor, breaking ties to the even number.
- **UP**: Always rounds up.
- **DOWN**: Always rounds down.

---

## Benefits
- Avoids floating-point precision issues.
- Precise control over rounding and scaling.
- Best for financial and high-precision requirements.

## Limitations
- **Performance**: Slower than primitive types like `double`.
- **Complexity**: More verbose syntax.
