# Phase 2 - Object Oriented Programming (OOP)

## What is it?

OOP is a way to organize code using "objects" — things that have properties and can do actions.

Think of it like real-world objects:
- **A Car** is an object with properties (color, speed, fuel) and actions (accelerate, brake)
- **A Student** is an object with properties (name, age, grade) and actions (study, take_exam)
- **A BankAccount** is an object with properties (balance, holder) and actions (deposit, withdraw)

Why organize code this way? Instead of scattered variables and functions, group related data and operations together.

---

## Why does it matter?

**Real-world reasons:**
1. **Code reuse** - Write once, create many objects from it
2. **Real-world modeling** - Code mirrors actual things (student, product, employee)
3. **Large projects** - Organize millions of lines of code into manageable pieces
4. **Interview questions** - "Design a system" requires OOP thinking
5. **DSA with objects** - Trees, graphs, linked lists all use classes

---

## How to think about it

A class is like a BLUEPRINT, objects are built from that blueprint.

```
CLASS (Blueprint):          OBJECT (Actual Thing):
┌─────────────────┐        ┌─────────────────┐
│ Student         │        │ student1        │
│ ─────────────── │   →    │ ─────────────── │
│ name            │        │ name: "Harshi"  │
│ age             │        │ age: 16         │
│ grade           │        │ grade: "A"      │
│ ─────────────── │        │ ─────────────── │
│ study()         │        │ study()         │
│ take_exam()     │        │ take_exam()     │
└─────────────────┘        └─────────────────┘
```

---

## Python Implementation

### Classes and Objects

```python
# Define a class (blueprint)
# Why: Create a reusable template for objects
class Student:
    # __init__ is the constructor (creates new object)
    # Why: Set up initial properties when object is created
    def __init__(self, name, age):
        # "self" represents the object itself
        # Why: Each object needs its own data
        self.name = name  # Property: name
        self.age = age    # Property: age
        self.grade = "A"  # Default property
    
    # Methods are functions inside a class
    # Why: Actions the object can perform
    def study(self, hours):
        # self.age refers to THIS object's age
        print(f"{self.name} studied for {hours} hours")
    
    def take_exam(self):
        print(f"{self.name} is taking the exam...")
        return self.grade

# Create objects (instances) from the class
# Why: Each student is a separate object with own data
student1 = Student("Harshi", 16)
student2 = Student("Alice", 17)

# Access properties
# Why: Get object's data
print(f"Student 1: {student1.name}, Age: {student1.age}")
print(f"Student 2: {student2.name}, Age: {student2.age}")

# Call methods
# Why: Make the object do something
student1.study(2)
student2.study(3)

exam_result = student1.take_exam()
print(f"Grade: {exam_result}")
```

### Inheritance

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (inherits from Animal)
# Why: Reuse parent code, add specific behavior
class Dog(Animal):
    def speak(self):
        # Override parent method
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Both inherit from Animal but speak differently
dog.speak()  # Buddy barks: Woof!
cat.speak()  # Whiskers meows: Meow!
```

---

## Common Mistakes Beginners Make

1. **Forgetting `self` parameter in methods**
   - ❌ Wrong: `def study(hours):`
   - ✅ Right: `def study(self, hours):`

2. **Using class name instead of self inside class**
   - ❌ Wrong: `Student.name = name`
   - ✅ Right: `self.name = name`

3. **Not calling `__init__` through constructor**
   - ❌ Wrong: `student = Student()` without arguments when __init__ needs them
   - ✅ Right: `student = Student("Harshi", 16)`

4. **Modifying object that doesn't exist**
   - ❌ Wrong: `student.hobby = "coding"` if not initialized in __init__
   - ✅ Right: Initialize in __init__ or create carefully

5. **Confusing class variables with instance variables**
   - ❌ Wrong: Sharing data accidentally between objects
   - ✅ Right: Use `self.` for instance-specific data

6. **Not understanding inheritance order**
   - ❌ Wrong: Child class doesn't have parent's properties
   - ✅ Right: Child inherits all parent's properties and methods

---

## How to know I understand this

Checklist:
- [ ] I can explain class, object, and inheritance without notes
- [ ] I can write a class with __init__ and 3 methods in 10 minutes
- [ ] I can create objects and call their methods
- [ ] I understand what "self" means
- [ ] I can create a child class that inherits from parent
- [ ] I can solve an easy LeetCode OOP problem

---

## Practice Problems

- Easy: [Design a Parking System — LeetCode #1603](https://leetcode.com/problems/design-parking-system/)
- Easy: [Design an Ordered Stream — LeetCode #1656](https://leetcode.com/problems/design-an-ordered-stream/)
- Medium: [Design Authentication Manager — LeetCode #1797](https://leetcode.com/problems/design-authentication-manager/)
