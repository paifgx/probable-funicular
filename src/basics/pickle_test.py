# pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)

import pickle as pkl
import shelve

# ---------------------------------------------------------

# cities = ["Paris", "Berlin", "London"]
# file = open("cities.pkl", "wb")
# pkl.dump(cities, file)
# file.close()

# ---------------------------------------------------------

# file = open("cities.pkl", "rb")
# cities = pkl.load(file)
# print(cities)

# ---------------------------------------------------------

# file = open("data.pkl", "bw")
# programming_languages = ["Python", "Java", "C++"]
# python_dialect = ["CPython", "Jython", "IronPython"]

# pickle_object = (programming_languages, python_dialect)
# pkl.dump(pickle_object, file)

# file.close()

# ---------------------------------------------------------

# file = open("data.pkl", "br")
# (p_lang, p_dialect) = pkl.load(file)
# print(p_lang, p_dialect)

# ---------------------------------------------------------

# s = shelve.open("MyShelve")

# s["key1"] = {1: "Python", 2: "Java", 3: "C++"}
# s["key2"] = {1: "CPython", 2: "Jython", 3: "IronPython"}

# for key in s:
#     print(key, s[key])

# s.close()