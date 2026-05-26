"""
TOPIC: Inheritance
Difficulty: Beginner-Intermediate

Inheritance lets a child class get properties and methods from parent class.
Why: Avoid code duplication. Share common functionality.
"""

print("=== INHERITANCE ===\n")

# PARENT CLASS (base class)
# Why: Define common properties and methods
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} was created")
    
    def speak(self):
        # Generic speak method
        print(f"{self.name} makes a sound")
    
    def move(self):
        # All animals move
        print(f"{self.name} is moving")

# CHILD CLASS (derived class)
# Why: Inherit from Animal, but add specific behavior
class Dog(Animal):
    # No __init__ here, uses parent's __init__!
    # Why: Dogs have same creation process as Animals
    
    def speak(self):
        # Override parent method
        # Why: Dogs have specific sound
        print(f"{self.name} barks: Woof Woof!")
    
    def fetch(self):
        # New method Dog has (parent doesn't)
        # Why: Only dogs can fetch
        print(f"{self.name} fetched the ball!")

# ANOTHER CHILD CLASS
class Cat(Animal):
    def speak(self):
        # Override parent method
        print(f"{self.name} meows: Meow!")
    
    def scratch(self):
        # New method Cat has
        print(f"{self.name} scratched the furniture!")

# Create objects
# Why: Each animal type has common + unique behavior
dog = Dog("Buddy")
cat = Cat("Whiskers")
generic = Animal("Robo")

print("\n--- Behavior ---")
# All have move() from parent
dog.move()
cat.move()

# speak() is different for each
dog.speak()
cat.speak()
generic.speak()

# Unique methods
print()
dog.fetch()  # Only dogs can fetch
cat.scratch()  # Only cats can scratch

print("\n" + "="*50 + "\n")

# Another inheritance example
# Why: Show practical use in DSA

class Vehicle:
    """Parent class for all vehicles"""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    """Car inherits from Vehicle"""
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)  # Call parent's __init__
        self.doors = doors
    
    def info(self):
        return f"{super().info()} Car with {self.doors} doors"

class Motorcycle(Vehicle):
    """Motorcycle inherits from Vehicle"""
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
    
    def info(self):
        sidecar = "with" if self.has_sidecar else "without"
        return f"{super().info()} Motorcycle {sidecar} sidecar"

# Create vehicles
car = Car("Toyota", 2020, 4)
bike = Motorcycle("Harley", 2021, False)

print(f"Car: {car.info()}")
print(f"Bike: {bike.info()}")

# INHERITANCE PYRAMID
# Why: Visual understanding
print("\n" + "="*50)
print("INHERITANCE HIERARCHY")
print("="*50)
print("""
        Vehicle (Parent)
        /          \\
      Car       Motorcycle (Children)
""")
