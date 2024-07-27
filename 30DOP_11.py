#No parameters:
'''
    FUNCTIONS RECIBE ARGUMENTS, THEY WORK WITH PARAMETERS
    def function(PARAMETERS):
        code
        code
        return code
    
    function(ARGUMENTS)
'''
def no_parameters():
    first_number = int(input('Please, enter a number: '))
    second_number = int(input('Now enter another: '))
    added_numbers = first_number + second_number
    print(f'When we add {first_number} to {second_number}, we get: {added_numbers}')
    return added_numbers

# result = no_parameters()  #<= This way, we are assigning the value of the function's return to a variable
# print(result)

#Single parameter:
def greetings(name):
    message = (f'Hello, {name}. We are glad to have you back!')
    print(message)

greetings('Jorge') #<= When the function is called, the arguments (1 in this case) are passed

def square_numbers(n):
    square = n*n
    return square #<= this variable dies within the function, so we can actually have another called the same

number = 5
square = square_numbers(number)
print(square)

#Multiple parameters:
def year_of_birth(actual, born):
    age = actual - born
    print(f'You have {age} years old')
    #No return value, not necessary

this_year = 2024
birthday_year = 2001
year_of_birth(this_year, birthday_year)

#Arguments can be given as 'key = value' items, so the order does not matter:
def order_not_matters(number1, number2):
    divided = number1 / number2
    print(f'{number1}/{number2} = {int(divided)}')

order_not_matters(number2 = 2, number1 = 0) #if order mattered, this would be 2/0!

#Returning a Boolean
def counting(numbers):
    i = 0
    for index in numbers:
        if index == 0:
            print(f'\'0\' Found at index[{i}]!')
            return True #Finishes the function if condition is met
        i += 1
    return False

listed_numbers = [1, 2, 3, 4, 0]
listed_cero = counting(listed_numbers)
if listed_cero != True:
    print('\'0\' Could not be found!')

#Returning a list
def listing(listed, quant):
    for i in range(quant):
        if i % 2 == 0:
            listed.append(i)
    return listed

new_list = []
listing(new_list, 10)
print(new_list)

#While we give functions different kind of arguments, we can decide wether or not we want to have a 'default' value for
#a singular parameter, if no argument is given for the parameter, the 'default' will be used
def enterprise(worker, admin = False):
    print(f'Welcome back, {worker['name']}')
    if worker['rol'] == 'Admin':
        admin = True
    if admin == True:
        answer = 'Acces granted'
    else:
        answer = 'Acces denied'
    print(answer)

personal_info = {
    'ID' : 1480,
    'name' : 'Nicolas',
    'surname' : 'Cernadas', 
    'rol' : 'Employee'
}
enterprise(personal_info)

#Arbitrary number of arguments:
def total_added(*args):
    #(*args) is a tuple made of the arguments given
    total = 0
    for i in args:
        total += i
    return total

added_numbers = total_added(1,2,3,4,5,6,7,8,9,10)
print(added_numbers)

