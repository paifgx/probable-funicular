# [ Ausdruck for Element in Iterable if Bedingung ]

test = [ x**2 for x in range(10) if x % 2 == 0 ]
print(test)

# ------------------------------------------------------------

zahlen = [x for x in range(10)]
print(zahlen)

# ------------------------------------------------------------

woerter = ['Hallo', 'Welt', 'Python', 'Programmierung']
lengths = [len(wort) for wort in woerter]
print(lengths)

# ------------------------------------------------------------

matrix = [[i * j for j in range(5)] for i in range(3)]
print(matrix)

# ------------------------------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primzahlen = [x for x in range(100) if is_prime(x)]
print(primzahlen)

# ------------------------------------------------------------

quadrate_dict = {x: x**2 for x in range(5)}
print(quadrate_dict)

# ------------------------------------------------------------

unique_values = {x % 3 for x in range(10)}
print(unique_values)