with open('assignment.txt', 'w') as file:
    file.write('this is my first paragraph.\n')
    file.write('this is my second paragraph.\n')
    print("file")

with open('assignment.txt', 'r') as file:
    data = file.read()
    print(data)