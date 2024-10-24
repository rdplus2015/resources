## **Encapsulation in Java**

**Encapsulation** is the concept of restricting direct access to some of an object’s components, meaning that its internal representation is hidden from outside the class. Instead, access is provided via public methods (getters and setters).

### Key Points:

-   **Private Fields**: Data is hidden using `private` access modifier.
-   **Public Methods**: Data is accessed and modified via public getter and setter methods.

Encapsulation allows:

-   **Data Hiding**: Protects the object's data from unauthorized access.
-   **Controlled Access**: Access to the fields is provided through controlled methods.

### Example:

```java
public class Car {
    private String name;
    private int year;

    // Constructor
    public Car(String name, int year) {
        this.name = name;
        this.year = year;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getYear() {
        return year;
    }

    // Setters
    public void setName(String name) {
        this.name = name;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // Simple method
    public String getCarInfo() {
        return "Car Name: " + name + ", Year: " + year;
    }
}
```
**Usage in the Main Class:**

```java
public class Main {
    public static void main(String[] args) {
        // Create a new Car object using encapsulation
        Car carOne = new Car("Toyota", 2015);

        // Display initial info
        System.out.println(carOne.getCarInfo()); // Output: Car Name: Toyota, Year: 2015

        // Modify attributes using setters
        carOne.setName("Nissan");
        carOne.setYear(1999);

        // Display updated info
        System.out.println(carOne.getCarInfo()); // Output: Car Name: Nissan, Year: 1999
        
        
        // Display and attributes 
        System.out.println("Name: " + carOne.getName() + ".\n" + "Price: " + carOne.getYear());

    }
}
```
### Benefits of Encapsulation:

-   **Improves Maintainability**: Changes to the internal implementation can be made without affecting other classes that use it.
-   **Increases Flexibility**: You can change how data is stored or validated without changing how it is accessed from outside the class.

This encapsulation model keeps your object's data safe and offers controlled access through methods.


--- 

