# spannungen = [5.0, 3.3, 12.0, -1.0, 9.9]

# index = 0
# while index < len(spannungen):
#     if spannungen[index] < 0:
#         print("Fehler: negative Spannung")
#         break
    
#     print("Spannung: ", spannungen[index])
#     index += 1

my_input = input("Gib eine Zahl ein: ")

while not my_input.isdigit():
    print("Fehler: keine Zahl")
    my_input = input("Gib eine Zahl ein: ")

print("Eingabe: ", int(my_input) + 1)