# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# greet("Alice")
# greet("Bob", "Good morning")
# greet(name="Charlie", greeting="Good evening")

# def add(*args):
#     return sum(args)

# print(add(1, 2, 3))
# print(add(4, 5, 6, 7))


# def display_info(**kwargs):
#     print(kwargs.items())
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(name="Alice", age=25)

# def add(*args, test):
#     return sum(args)

# print(add(1, 2, 3, test=4))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))