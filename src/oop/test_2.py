from src.oop.VIPCustomer import VIPCustomer

vip_customer = VIPCustomer("Alice", "Health", 1000, 3)
print(vip_customer)

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __len__(self) -> int:
        return 10

point1 = Point(1, 2)
point2 = Point(3, 4)

print(len(point1))

# - **`__eq__`**: Gleichheit `==`
# - **`__ne__`**: Ungleichheit `!=`
# - **`__lt__`**: Kleiner `<`
# - **`__gt__`**: Größer `>`
# - **`__le__`**: Kleiner oder gleich `<=`
# - **`__ge__`**: Größer oder gleich `>=`

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, item, quantity):
        self.items[item] = quantity

cart = ShoppingCart()
cart["apple"] = 3
cart["banana"] = 2

print(cart)