# file_object_in = open('src/basics/test.txt', 'r')
# file_object_out = open('src/basics/test_copy.txt', 'w')

# i = 1
# for line in file_object_in:
#     print(line.rstrip())
#     file_object_out.write(str(i) + ': ' + line)
#     i += 1

# file_object_in.close()
# file_object_out.close()

# Zur Ergänzung einer Datei wird der Modus 'a' (append) verwendet
# with open('src/basics/example.txt', 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('Hello, Python!\n')
#     file.write('Hello, File!\n')

# lorem = open('src/basics/lorem.txt').readlines()
lorem = open('src/basics/lorem.txt').read()
print(type(lorem))