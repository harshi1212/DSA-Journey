# Phase 2 - Object-Oriented Programming (Complete Master Guide)

**Foundation for writing production-level code. Essential for interviews.**

---

## Table of Contents
1. [OOP Fundamentals](#oop-fundamentals)
2. [Classes and Objects](#classes-and-objects)
3. [Encapsulation](#encapsulation)
4. [Inheritance](#inheritance)
5. [Polymorphism](#polymorphism)
6. [Abstraction](#abstraction)
7. [SOLID Principles](#solid-principles)
8. [Design Patterns](#design-patterns)
9. [Worked Examples (40+)](#worked-examples)
10. [Interview Preparation](#interview-preparation)

---

# OOP FUNDAMENTALS

## What is Object-Oriented Programming?

**Definition:** Object-Oriented Programming is a paradigm that organizes code around objects and classes, encapsulating data and behavior together.

**Core Pillars:**
1. Encapsulation - Bundle data and methods
2. Inheritance - Reuse code through hierarchy
3. Polymorphism - Use objects interchangeably
4. Abstraction - Hide implementation details

---

## Class vs Object

**Class:** Blueprint for creating objects

```python
class Dog:
    """Blueprint for dog objects"""
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"
```

**Object:** Instance created from a class

```python
# Create objects from Dog blueprint
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Objects are independent
print(dog1.bark())  # "Buddy says woof!"
print(dog2.bark())  # "Max says woof!"
```

---

# CLASSES AND OBJECTS

## Class Definition

```python
class BankAccount:
    # Class variable (shared by all instances)
    interest_rate = 0.02
    
    # Constructor - called when object created
    def __init__(self, owner, balance=0):
        self.owner = owner          # Instance variable
        self.balance = balance      # Instance variable
        self.transactions = []      # Instance variable
    
    # Instance method
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    # Instance method
    def withdraw(self, amount):
        """Remove money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -${amount}")
            return True
        return False
    
    # Special method (magic method)
    def __str__(self):
        """String representation"""
        return f"Account({self.owner}, ${self.balance})"
    
    @classmethod
    def create_savings(cls, owner):
        """Class method - called on class, not instance"""
        return cls(owner, balance=100)  # Start with $100
    
    @staticmethod
    def calculate_fee(balance):
        """Static method - doesn't need self or cls"""
        return balance * 0.01  # 1% fee

# Usage:
account = BankAccount("Alice", 1000)
account.deposit(500)          # $1500
account.withdraw(200)         # $1300

savings = BankAccount.create_savings("Bob")  # $100

fee = BankAccount.calculate_fee(1000)  # $10
```

---

## Object Lifecycle

```python
class Thing:
    def __init__(self):
        print("1. Object created (initialization)")
    
    def __enter__(self):
        print("2. Object entering context (with statement)")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("3. Object exiting context")
    
    def __del__(self):
        print("4. Object deleted (garbage collected)")

# Usage with context manager:
with Thing() as t:
    print("Object in use")

# Output:
# 1. Object created (initialization)
# 2. Object entering context (with statement)
# Object in use
# 3. Object exiting context
# 4. Object deleted (garbage collected)
```

---

# ENCAPSULATION

## Encapsulation Principle

**Definition:** Bundle data and methods together, hiding internal details from outside world.

**Why Encapsulation Matters:**
```
Bad: Public attributes can be modified from anywhere
Good: Private attributes, public methods control access
```

---

## Access Modifiers

```python
class SecureAccount:
    def __init__(self, balance):
        self.public_data = 100          # Public (accessible)
        self._protected_data = 200      # Protected (by convention)
        self.__private_data = 300       # Private (name mangled)
    
    def get_balance(self):
        """Public method to access private data"""
        return self.__private_data
    
    def deposit(self, amount):
        """Public method to modify private data safely"""
        if amount > 0:
            self.__private_data += amount
            return True
        return False

account = SecureAccount(1000)

# Public access - OK
print(account.public_data)  # 100

# Protected access - technically possible but discouraged
print(account._protected_data)  # 200

# Private access - name mangled
print(account._SecureAccount__private_data)  # 300
account.deposit(500)
print(account.get_balance())  # 800
```

---

## Properties (Getters/Setters)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private
    
    @property
    def radius(self):
        """Getter - called when accessing circle.radius"""
        print("Getting radius")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter - called when assigning circle.radius = value"""
        if value > 0:
            print(f"Setting radius to {value}")
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
    
    @property
    def area(self):
        """Computed property - calculated on access"""
        import math
        return math.pi * self._radius ** 2

# Usage:
circle = Circle(5)
print(circle.radius)      # Calls getter: 5
print(circle.area)        # Calls getter (computed): 78.54

circle.radius = 10        # Calls setter
print(circle.radius)      # Calls getter: 10

circle.radius = -5        # Raises ValueError
```

---

# INHERITANCE

## Inheritance Principle

**Definition:** A class inherits properties and methods from a parent class, enabling code reuse and creating class hierarchies.

**Mathematical Definition:**
```
If class B inherits from class A:
B ⊇ A (B includes all of A)
Methods(B) ⊇ Methods(A)
Attributes(B) ⊇ Attributes(A)
```

---

## Single Inheritance

```python
class Animal:
    """Parent class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    """Child class - inherits from Animal"""
    def speak(self):
        """Override parent method"""
        return f"{self.name} barks!"
    
    def fetch(self):
        """New method specific to Dog"""
        return f"{self.name} fetches the ball"

# Usage:
dog = Dog("Buddy")
print(dog.speak())   # Overridden method: "Buddy barks!"
print(dog.fetch())   # New method: "Buddy fetches the ball"
```

---

## Multi-level Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def is_warm_blooded(self):
        return True

class Dog(Mammal):
    def bark(self):
        return f"{self.name} barks!"

# Hierarchy: Animal → Mammal → Dog
dog = Dog("Max")
print(dog.is_warm_blooded())  # From Mammal: True
print(dog.bark())              # From Dog: "Max barks!"
```

---

## Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "Flying..."

class Swimmable:
    def swim(self):
        return "Swimming..."

class Duck(Flyable, Swimmable):
    """Inherits from both Flyable and Swimmable"""
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())     # From Flyable: "Flying..."
print(duck.swim())    # From Swimmable: "Swimming..."
print(duck.quack())   # From Duck: "Quack!"
```

---

## Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# MRO: D → B → C → A
print(D.mro())
# [D, B, C, A, object]

d = D()
print(d.method())  # "B" (from B, first in MRO)
```

---

## super() Function

```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's __init__
        self.age = age
    
    def greet(self):
        parent_greeting = super().greet()  # Call parent's method
        return f"{parent_greeting} and I'm {self.age}"

child = Child("Alice", 10)
print(child.greet())
# "Hello, I'm Alice and I'm 10"
```

---

# POLYMORPHISM

## Polymorphism Principle

**Definition:** Objects of different classes can be treated through the same interface, with each class providing its own implementation.

**Mathematical Principle:**
```
Many forms: poly (many) + morph (form)
Same interface, different implementations
```

---

## Method Overriding

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

# Polymorphism in action:
shapes = [
    Rectangle(5, 4),
    Circle(3)
]

for shape in shapes:
    print(f"Area: {shape.area()}")
    # Each calls its own area() implementation!

# Output:
# Area: 20
# Area: 28.274...
```

---

## Duck Typing

```python
"""If it walks like a duck and quacks like a duck, it's a duck!"""

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

def make_speak(animal):
    """Works with any object that has a speak() method"""
    print(animal.speak())

make_speak(Dog())    # Works: "Woof!"
make_speak(Cat())    # Works: "Meow!"
make_speak(Robot())  # Works: "Beep boop!"
# No inheritance needed!
```

---

# ABSTRACTION

## Abstraction Principle

**Definition:** Hide complex implementation details and show only essential features through a simplified interface.

---

## Abstract Base Classes

```python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    """Abstract base class - can't be instantiated"""
    
    @abstractmethod
    def connect(self):
        """Subclasses must implement"""
        pass
    
    @abstractmethod
    def query(self, sql):
        """Subclasses must implement"""
        pass
    
    def execute(self):
        """Concrete method - inherited by subclasses"""
        self.connect()
        return self.query("SELECT * FROM users")

class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to MySQL"
    
    def query(self, sql):
        return f"MySQL: {sql}"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def query(self, sql):
        return f"PostgreSQL: {sql}"

# Usage:
# db = DatabaseConnection()  # ERROR! Can't instantiate abstract class

mysql = MySQLConnection()
print(mysql.execute())

postgresql = PostgreSQLConnection()
print(postgresql.execute())
```

---

# SOLID PRINCIPLES

## Single Responsibility Principle (SRP)

**Rule:** A class should have only one reason to change.

```python
# Bad: Class has multiple responsibilities
class User:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        """Database responsibility"""
        pass
    
    def send_email(self):
        """Email responsibility"""
        pass
    
    def generate_report(self):
        """Reporting responsibility"""
        pass

# Good: Each class has one responsibility
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, user):
        pass

class ReportGenerator:
    def generate(self, user):
        pass
```

---

## Open/Closed Principle (OCP)

**Rule:** Classes should be open for extension, closed for modification.

```python
# Bad: Must modify Reporter to add new format
class Reporter:
    def generate_report(self, format):
        if format == "csv":
            return "csv report"
        elif format == "json":
            return "json report"
        elif format == "xml":  # Need to modify class!
            return "xml report"

# Good: Extend without modifying
class Report:
    def generate(self):
        raise NotImplementedError

class CSVReport(Report):
    def generate(self):
        return "csv report"

class JSONReport(Report):
    def generate(self):
        return "json report"

class XMLReport(Report):  # New class, no modification!
    def generate(self):
        return "xml report"
```

---

## Liskov Substitution Principle (LSP)

**Rule:** Subclasses should be substitutable for their parent classes.

```python
# Bad: Square breaks Rectangle contract
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_width(self, w):
        self.width = w
        self.height = w  # Wrong! Breaks Rectangle

# Good: Don't force inheritance where it doesn't fit
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Square is separate, not subclass of Rectangle
class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
```

---

## Interface Segregation Principle (ISP)

**Rule:** Clients shouldn't depend on interfaces they don't use.

```python
# Bad: Worker interface too broad
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        return "Working"
    
    def eat(self):
        raise NotImplementedError("Robot can't eat!")

# Good: Segregate interfaces
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Working"
    
    def eat(self):
        return "Eating"

class Robot(Workable):
    def work(self):
        return "Working"
    # Robot doesn't implement Eatable
```

---

## Dependency Inversion Principle (DIP)

**Rule:** Depend on abstractions, not concrete implementations.

```python
# Bad: High-level depends on low-level
class PaymentProcessor:
    def __init__(self):
        self.payment_gateway = StripeGateway()  # Concrete class
    
    def process(self, amount):
        self.payment_gateway.charge(amount)

# Good: Both depend on abstraction
class PaymentGateway:
    def charge(self, amount):
        raise NotImplementedError

class StripeGateway(PaymentGateway):
    def charge(self, amount):
        return f"Charged ${amount} via Stripe"

class PayPalGateway(PaymentGateway):
    def charge(self, amount):
        return f"Charged ${amount} via PayPal"

class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway  # Abstract class
    
    def process(self, amount):
        self.gateway.charge(amount)

# Usage:
stripe_processor = PaymentProcessor(StripeGateway())
paypal_processor = PaymentProcessor(PayPalGateway())
```

---

# DESIGN PATTERNS

## Singleton Pattern

**Use:** Ensure only one instance of a class exists

```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def query(self, sql):
        return f"Executing: {sql}"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True - same instance!
```

---

## Factory Pattern

**Use:** Create objects without specifying exact classes

```python
class Animal:
    pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError(f"Unknown animal: {animal_type}")

# Usage:
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")
```

---

## Observer Pattern

**Use:** Notify multiple objects of state changes

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer:
    def update(self, event):
        raise NotImplementedError

class EmailNotifier(Observer):
    def update(self, event):
        print(f"Email sent: {event}")

class SMSNotifier(Observer):
    def update(self, event):
        print(f"SMS sent: {event}")

# Usage:
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())
subject.notify("User registered")
# Output:
# Email sent: User registered
# SMS sent: User registered
```

---

# WORKED EXAMPLES

## Example 1: Bank Account System

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transaction_history.append(f"Withdraw: -${amount}")
    
    def get_balance(self):
        return self._balance
    
    def get_history(self):
        return self._transaction_history

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._transaction_history.append(f"Interest: +${interest}")

# Usage:
account = SavingsAccount("Alice", 1000)
account.deposit(500)
account.withdraw(100)
account.apply_interest()
print(account.get_balance())    # 1386
print(account.get_history())
```

---

# INTERVIEW PREPARATION

## OOP Interview Questions

**Q1: Explain the four pillars of OOP**
```
A: Encapsulation - bundle data and methods
   Inheritance - reuse code through hierarchy
   Polymorphism - use objects interchangeably
   Abstraction - hide implementation details
```

**Q2: What's the difference between inheritance and composition?**
```
A: Inheritance (IS-A): Dog IS-A Animal
   Composition (HAS-A): Car HAS-A Engine
   
   Use inheritance for "is-a" relationships
   Use composition for "has-a" relationships
   
   Composition is often more flexible
```

**Q3: Explain polymorphism with an example**
```
A: Same interface, different implementations
   
   Example: eat() method
   - Dog.eat() → "eating dog food"
   - Cat.eat() → "eating cat food"
   - Human.eat() → "eating human food"
   
   Same method name, different behavior!
```

---

**Master OOP. It's 25% of system design interviews.** 🎯

