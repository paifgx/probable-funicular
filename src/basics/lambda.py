from functools import reduce

# List<Integer> zahlen = IntStream.range(0, 10).boxed().collect(Collectors.toList());
# List<Integer> geradeZahlen = zahlen.stream()
#     .filter(x -> x % 2 == 0)
#     .collect(Collectors.toList());
# System.out.println(geradeZahlen);

zahlen = range(0, 10)
gerade_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))
print(gerade_zahlen)

# ------------------------------------------------------------

# List<Integer> zahlen = Arrays.asList(1, 2, 3, 4);
# int produkt = zahlen.stream()
#     .reduce(1, (a, b) -> a * b);
# System.out.println(produkt);

zahlen = [1, 2, 3, 4]
produkt = reduce(lambda a, b: a * b, zahlen, 1)
print(produkt)

# ------------------------------------------------------------

operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y if y != 0 else None
}

print(operations['add'](10, 5))
print(operations['div'](10, 0))

# ------------------------------------------------------------

safe_divide = lambda x, y: x / y if y != 0 else None
print(safe_divide(10, 0))

# ------------------------------------------------------------

alt_safe_divide = lambda x, y: x / y if y != 0 else 'Division durch Null'
print(alt_safe_divide(10, 0))

# ------------------------------------------------------------

command = input("> ")
while command != "quit":
    print("You entered:", command)
    command = input("> ")

while (command := input("> ")) != "quit":
    print("You entered:", command)   

# ------------------------------------------------------------

[(lambda y: [y, x/y])(x+1) for x in range(5)]

[[y := x+1, x/y] for x in range(5)]