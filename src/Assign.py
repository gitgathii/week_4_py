#assignment
my_list=[10,20,30,40]
print(my_list)
my_list.append(15)
print(my_list)
my_list.extend([50,60,70])
print(my_list)
for _ in range(3):
    my_list.pop()
    print(my_list)
my_list.sort()
print("ascending order:", my_list)