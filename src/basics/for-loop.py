matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()

print("-----------------")

for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number, end=' ')
print()