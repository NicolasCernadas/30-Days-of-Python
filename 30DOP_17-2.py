#Packing and Unpacking
#*list/tuple to unpack them
#**dict to unpack a dict

def sum_of_five(a,b,c,d,e):
    return a + b + c + d + e
lst = (1,2,3,4,5) #works both with tuples and lists

print('Result of the sum of the unpacked list:',sum_of_five(*lst)) #Otherwise this will raise an error, function takes 5 arguments but only received one

#weird, but also works like this:

ranged_list = range(2, 5)
print('Normal call with arguments:',list(ranged_list))
args = [7, 10]
ranged_unpacked_list = range(*args) #its taking the first element from the list and placing it range(x, -), the other one as the second argument
print('Argument passed as an unpacked list:',list(ranged_unpacked_list))

#Also works like this:
countries = ['Argentina', 'Finland', 'Norway', 'Croatia', 'France', 'Chile']
arg, fin, nor, *rest = countries
print(type(rest))
print(arg, fin, nor, rest) #we can either print it this way or *rest, to print it as an unpacked list

#unpacking dictionaries function
def dict_unpacker(name, country, age, school):
    if 'school' in school.lower():
        return (f'{name} lives in {country}, is {age} years old and wento to {school}')
    else:
        return (f'{name} lives in {country}, is {age} years old and wento to {school} School')

dct = {'name':'Nicolas', 'country':'Argentina', 'age':22, 'school':'San Miguel Arcangel School'}
print(dict_unpacker(**dct))

#Packing method to allow python functions to receive as many arguments as needed
def many_arguments(*args):
    for i in args:
        print('For each argument, i will print this one time')

many_arguments(2, 'a', True)

#Packing dictionaries:
def dict_packing(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

dict_packing(name='Jorge', religion='Christian', age=22, anything='Any value')

#Spreading:
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [*list_1, *list_2]
print('Spreaded list:',list_3)

list_1 = ['Matias', 'Carlos']
list_2 = ['Roberto', 'Jorge']
list_3 = [*list_1, *list_2]
print('Spreaded list:',list_3)

#Enumerate() function for the index of a list
# for index, i in enumerate(list/touple):
#   code to do
countries = ['Peru', 'Argentina', 'Ecuador']
for index, i in enumerate(countries):
    if i == 'Argentina':
        print(f'\'{i}\' found at index[{index}]')

#Combined lists:
students_list = ['name', 'surname', 'class', 'grade']
student_8989 = ['Carlos', 'Llamazares', '25A', '9th']
listed_student_8989 = dict()
for i, t in zip(student_8989, students_list):
    listed_student_8989[t] = i

print(listed_student_8989)
