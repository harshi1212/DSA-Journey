"""
TOPIC: Classes and Objects
Difficulty: Beginner

Classes are blueprints for objects.
An object is a "thing" with properties and methods.
"""

print("=== CLASSES AND OBJECTS ===\n")

# Define a class (blueprint)
# Why: Create a template for objects
class Car:
    # Constructor (__init__) - runs when you create an object
    # Why: Set up the object's initial state
    def __init__(self, brand, color):
        # self = the specific object being created
        # Why: Each car has its own brand and color
        self.brand = brand
        self.color = color
        self.speed = 0  # All new cars start at speed 0
    
    # Method (function inside class)
    # Why: Cars can do things (accelerate, brake)
    def accelerate(self, amount):
        # "self.speed" = THIS car's speed
        self.speed = self.speed + amount
        print(f"{self.color} {self.brand} accelerated to {self.speed} mph")
    
    def brake(self, amount):
        self.speed = max(0, self.speed - amount)  # Don't go below 0
        print(f"{self.color} {self.brand} braked to {self.speed} mph")
    
    def show_info(self):
        print(f"Car: {self.color} {self.brand} @ {self.speed} mph")

# Create objects (instances) from the class
# Why: Each object is independent with own data
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Access properties
# Why: See object's current state
print(f"Car 1: {car1.brand}, Color: {car1.color}")
print(f"Car 2: {car2.brand}, Color: {car2.color}")

# Call methods
# Why: Make object do something
car1.accelerate(50)
car1.show_info()

car2.accelerate(60)
car2.show_info()

car1.brake(20)
car1.show_info()

print("\n" + "="*50 + "\n")

# Another example: Student class
# Why: Group student data and operations together
class Student:
    def __init__(self, name, grade):
        # Constructor sets up the student
        self.name = name
        self.grade = grade
        self.score = 0  # Starts with 0 points
    
    def add_score(self, points):
        # Add points to student's total
        self.score = self.score + points
        print(f"{self.name} gained {points} points")
    
    def show_status(self):
        # Show student's current status
        print(f"{self.name}: {self.score} points (Grade: {self.grade})")

# Create students
harshi = Student("Harshi", "A")
alice = Student("Alice", "B")

# Each student tracks their own score
harshi.add_score(50)
alice.add_score(30)

harshi.add_score(25)  # Harshi gets more points
alice.add_score(40)

print("\nStudent Status:")
harshi.show_status()
alice.show_status()

# Key insight: harshi and alice have same structure
# but completely independent data!
print(f"\nHarshi score: {harshi.score}")
print(f"Alice score: {alice.score}")
