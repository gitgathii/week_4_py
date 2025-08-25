#loops
fruits=['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"i love {fruit}!")
#range 
for number in range(1,6):
    print(f"number:{number}")
#while loops
count=1
while count <=8:
    print(f"count:{count}")
    count +=1
#loop controls:break and continue
for number in range(1, 10):
    if number == 10:#breaking the loop at 10
        print('breaking the loop at 10')
        break#breaking the loop at 10
    elif number % 2 == 0:# find the number is even or not
        print(f"skipping {number} because its even")
        continue
    print(f"processing number: {number}")
# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"outer loop: {i}, inner loop:{j} ")

for i in range(1, 5):
    for j in range(1, 6):
        print(f"outer loop: {i}, inner loop:{j} ")
#list comprehension
square=[x**2 for x in range(5)]
print(square)
even_number=[x**2 for x in range(10) if x % 2==0]
print(even_number)
#nested comprehension
matrix=[[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
#transforming data
names=["Alice", "bob", "charlie"]
uppercased_names=[name.upper()for name in names]
print(uppercased_names)
#filtering data
number=[10,15,20,25,30]
divisible_by_5=[num for num in number if num %5==0]
print(divisible_by_5)
#flattening a list
nested_list=[[1,2],[3,4], [5,6]]
flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)

#functions
def greet(name):
    '''greet a person by their name.'''
    return f"hello {name}!"
print(greet("Alice"))
#positional Arguments
def add(a, b ):
    return a+b
print(add(5, 10))
#default arguments
def multiply(a, b=2):
    return a * b
print(multiply(5))
print(multiply(5, 2))
#default arguments
def greet(name="guest"):
    return f"hello {name}!"
print(greet())
print(greet("Alice"))
#keyword arguments
def introduce(name, age):
    return f"my name is {name}, and i'm {age} years old."
print(introduce(name='Owen', age=21))  
#returning values 
def square(number):
    return number**2
result=square(4)
print(result)
#lambda functions
add=lambda x,y: x+y
print(add(5, 10))
#using maps
numbers=[1, 2, 3, 4, 5]
squares=list(map(lambda x: x**2, numbers))
print(squares)
#recursive
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(6))
