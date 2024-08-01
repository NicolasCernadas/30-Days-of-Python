# High Order Functions
#functions as parameters of functions
#returning a function as a value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    return -(x)

def high_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = high_order_function('cube') #first we give the argument to work with
print('Functions as a return value of another function:',result(3)) #then the one the function 'cube' (in this case) will work with

#Closure
#A nested function is allowed to access the outer scope, like this:

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

number = add_ten()
print('\'Closure\', functions using parameters of the outer scope:',number(10))

#More examples

# =========================================== #

def greetings(name):
    return (f'Welcome, {name}. Is nice to have you back')

def upper_case(text):
    return text.upper()

def lower_case(text):
    return text.lower()

def options(func, text):
    message = func(text)
    return message

welcome = greetings('Jorge')
upper_welcome = options(upper_case, welcome)
print(upper_welcome)

# =========================================== #

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

division = divisor(2) # number to divide with
print('Division:',division(10)) # number to be divided

# =========================================== #
 
def principal_function(func):
    '''
    This function recibes another function as a parameter, it returns 'secondary function' as a parameter, so what we get
    from assigning it to a variable, is converting it to a function, so to be called, we must use brackets
    '''
    def secondary_function(name):
        print(f'Hello, {name}')
        func()
        #waiting_time = input('To leave, please press \'Enter\'')
        print('Goodbye')
    return secondary_function

def greetings():
    print('How are you?')

x = principal_function(greetings)
x('Nicolas') #this argument given, is going to be used by secondary function

# =========================================== #

#DECORATORS:

'''
    instead of this
    => x = f1(f)('hola')
    or
    => x = f1(f)
    => x('hola')
    we could use decorators.
    @functionname
    they do the exact same 2 lines from above, but simplify the code, so we get the following
    previous to the declaration of the function, we place the decorator to run
'''
    
def f1(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@f1
def f(a):
    print(a.upper())

f('hola')

# =========================================== #

def f1(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return val
    return wrapper

@f1
def f(a, b):
    return a + b

value = f(4,5)
print(value)

# =========================================== #

#MAP FUNCTION
# map(function, iterable)
#It iterates over a list, applying the function to the elements and generating a new object
lst = [1, 2, 3, 4, 5]
names = ['Jorge', 'Matias', 'Carlos']
def square(x):
    return x ** 2
def upper(name):
    return name.upper()

numbers_squared = list(map(square, lst)) #the function map has a class of its own, if we want to show it as a list, we can convert it (either to a list or a tuple, NOT a dict)
print(numbers_squared)

upper_names = tuple(map(upper, names))
print(upper_names)

int_to_str = list(map(str, lst))
print(int_to_str)

lambda_function = tuple(map(lambda x: x ** 2, lst))
print(lambda_function)

upper_names = list(map(lambda names : names.upper(), names))
print(upper_names)

# =========================================== #

#FILTER FUNCTION
#filter(function, iterable)
#return the true values of the function:

numbers = [1, 2, 3, 4, 5, 6, 7]
names = ['Jorge', 'Candelaria', 'Matias']

def even_numbers(value):
    if value % 2 == 0:
        return True
    return False

def large_names(name):
    if len(name) > 7:
        return True
    return False

filtered_names = list(filter(large_names, names))
print(filtered_names)

filtered_numbers = list(filter(even_numbers, numbers))
print(filtered_numbers) 

# =========================================== #

#REDUCE FUNCTION
#reduce(function, iterable)
#returns a single value, not a list
from functools import reduce

lst = [1, 2, 3, 4, 5]

def added_list(value1, value2):
    return value1 + value2

total = reduce(added_list, lst)
print(total)