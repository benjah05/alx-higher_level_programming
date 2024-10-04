#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

# Test with valid integer radius
print("Testing with radius = 5:")
circle1 = MagicClass(5)
print(f"Area: {circle1.area()}")
print(f"Circumference: {circle1.circumference()}")

# Test with valid float radius
print("\nTesting with radius = 3.5:")
circle2 = MagicClass(3.5)
print(f"Area: {circle2.area()}")
print(f"Circumference: {circle2.circumference()}")

# Test with invalid radius (string)
try:
    print("\nTesting with radius = 'a string':")
    circle3 = MagicClass("a string")
except TypeError as e:
    print(e)
