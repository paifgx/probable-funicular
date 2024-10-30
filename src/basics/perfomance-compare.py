from timeit import timeit
from my_package import modul_a as np

np.test()

# List Comprehension
lc_time = timeit('[x**2 for x in range(1000)]', number=10000)

# Traditionelle Schleife
loop_time = timeit('''
result = []
for x in range(1000):
    result.append(x**2)
''', number=10000)

print(f"List Comprehension Zeit: {lc_time}")
print(f"Schleifenzeit: {loop_time}")

# result = [f(x) if condition else g(x) for x in iterable if another_condition]

# gen = (x**2 for x in range(1000000))

def import_module(modulname, alias=None):
    try:
        if alias:
            modul = __import__(modulname)
            globals()[alias] = modul
            return modul
        else:
            return __import__(modulname)
    except ImportError as e:
        print(f"Fehler beim Importieren des Moduls '{modulname}': {e}")
        return None

numpy_module = import_module('numpy')
if numpy_module:
    print("numpy importiert")
else:
    print("numpy konnte nicht importiert werden")