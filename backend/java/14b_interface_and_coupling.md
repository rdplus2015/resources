# Interfaces: Contract of Behaviour

An **interface** is a contract that dictates a specific set of methods
that a class must implement. When a class implements an interface, it's
essentially signing a contract, vowing to provide concrete
implementations for every method declared by the interface. The
interface itself doesn't care how these methods are implemented, merely
that they must be.

------------------------------------------------------------------------

## Problem: Tight Coupling

Imagine a Main class responsible for invoking methods from a service
class, BankPayment, that handles payment processing:

``` java
class BankPayment {
    public void process(double amount) {
        // Business logic to process bank payment
        System.out.println("Processed bank payment of: " + amount);
    }
}

class Main {
    public static void main(String[] args) {
        BankPayment bankPayment = new BankPayment();
        bankPayment.process(100.0);
    }
}
```

However, in light of recent financial trends, our company has decided to
switch from bank-based payments to cryptocurrency payments.
Consequently, the BankPayment class gets phased out and replaced by a
new class, CryptoPayment:

``` java
class CryptoPayment {
    public void process(double amount) {
        // Business logic to process crypto payment
        System.out.println("Processed crypto payment of: " + amount);
    }
}
```

In a tightly-coupled system, this change would necessitate modifications
to our Main class:

``` java
class Main {
    public static void main(String[] args) {
        BankPayment bankPayment = new BankPayment();
        bankPayment.process(100.0);
        CryptoPayment cryptoPayment = new CryptoPayment();
        cryptoPayment.process(100.0);
    }
}
```

This might seem like a trivial change, but imagine if this was a massive
application. Multiple sections of our code would need updates to
accommodate this switch. Such a system is said to be tightly coupled,
which is unfavorable for maintainability and scalability.

------------------------------------------------------------------------

## How Interfaces Promote Loose Coupling

The solution is to insulate the Main class from direct dependencies. We
can achieve this by having our payment classes implement a
PaymentProcessor interface:

``` java
public interface PaymentProcessor {
    void process(double amount);
}

class BankPayment implements PaymentProcessor {
    @Override
    public void process(double amount) {
        System.out.println("Processed bank payment of: " + amount);
    }
}

class CryptoPayment implements PaymentProcessor {
    @Override
    public void process(double amount) {
        System.out.println("Processed crypto payment of: " + amount);
    }
}
```

Now the Main class can seamlessly transition between different payment
systems. It remains virtually unchanged because we only need to update
the initialization:

``` java
class Main {
    private static PaymentProcessor paymentProcessor = new BankPayment();

    public static void main(String[] args) {
        paymentProcessor.process(100.0);
    }
}
```

### Transition

``` java
class Main {
    private static PaymentProcessor paymentProcessor = new CryptoPayment();

    public static void main(String[] args) {
        paymentProcessor.process(100.0);
    }
}
```

Thanks to the interface, the Main class remains decoupled from the
actual payment logic. It simply relies on the contract that any payment
processor class will have a process method.

------------------------------------------------------------------------

## Why Not Abstract Classes?

A valid question at this juncture would be: *"Why not use abstract
classes instead?"* After all, abstract classes can also declare abstract
methods that child classes must implement.

The crux lies in the intended purpose:

-   **Interfaces**: They establish a contract, ensuring that certain
    behaviors (methods) exist in implementing classes. They promote
    polymorphism and loose coupling.
-   **Abstract Classes**: Beyond just method contracts, they can also
    offer a shared state (fields) and can provide concrete methods. They
    are about inheritance and sharing common features across subclasses.

For our payment processing scenario, our primary concern isn't sharing
common states or methods but ensuring consistent behavior across
different payment methods. Hence, interfaces are the more apt choice.

------------------------------------------------------------------------

## Conclusion

Interfaces, by promoting a separation of concerns and ensuring classes
adhere to specific behaviors without dictating how those behaviors are
achieved, are a powerful tool in ensuring loose coupling in our
applications. This, in turn, results in software that's easier to
maintain, scale, and adapt to ever-evolving requirements.