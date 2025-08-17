my_list=[1,2,3,4,5,6]
print(my_list[1:4])
print(my_list[2:])
print(my_list[:])
print(my_list[-3])
print("before append:", my_list)
my_list.append(7)
print("after append:", my_list)

prime_numbers=[2,3,5]
even_numbers=[4,6,8]
prime_numbers.extend(even_numbers)
print("after extend:",prime_numbers)

languages=['Python','Java','JavaScript','Ruby','C++']
languages[2]='C'
print(languages)

languages=['Python','Java','JavaScript','Ruby','C++']
del languages[1]
print(languages)
languages.remove('C++')
print(languages)

languages=['python','java','javascript','ruby','c++']
for lang in languages:
    print(lang)

numbers=[num for num in range(1,6)]
print(numbers)

numbers=[num*num for num in range(1,6)]
print(numbers)
#tuples
var=('owen gathii')
print(type(var))
#dictionaries
capital_city={'Kenya':'Nairobi', 'Uganda':'Kampala', 'Tanzania':'Dodoma'}
print(capital_city)
capital_city['Ethopia']='addis ababa'
print(capital_city)
del capital_city['Tanzania']
print(capital_city)
print(capital_city['Kenya'])
squares={1:1, 2:4, 3:9, 4:16, 5:25 , 7:49, 9:81}
print(1 in squares)
print(6 in squares)
print(16 in squares)
print(2 in squares )
for i in squares:
    print(i, squares[i])
for keys in squares:
    print(squares[keys])
#keys 
students_id={112,113,114,115,116}
print('Student IDs:', students_id)
vowel_letters={'a', 'e', 'i', 'o', 'u'}
print('Vowels:', vowel_letters)
numbers={1, 2, 3, 4, 5, 6}
numbers.add(7)
print('num;', numbers)
#string
name='owen gathii'
print(name)
name='owen gathii'
print(name[1])
name='oswald'
print(name[1:4])
message='''never gonna give up
never gonna let you down
'''
print(message)
str_1='hello, world'
str_2='i love python'
str_3='hello, world'
print(str_1==str_3)
print(str_1==str_2)
greet='hello'
for letter in greet:
    print(letter)
name='melanie'
print(len(name))
