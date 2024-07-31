#List comprehension
#couple ways to transform a string to a list and viceversa
'''
    syntax: [i for i in iterable if expression]
'''
#1st Way
word = 'Python'
listed_word = list(word)
print('Written as a string:',word)
print('Written in list comprehension:',listed_word)

#2nd Way (list comprehension)
word = 'Course'
listed_word = [i for i in word]
print('Written as a string:', word)
print('Written in list comprehension:',listed_word)

#To generate a list of numbers:
numbers_list = [i for i in range(11)]
print('List comprehension generated list:',numbers_list)
#During iteration, you can also do mathematical operations:
numbers_list = [i * i for i in range(11)]
print('List comprehension generated list with mathematical operators:',numbers_list)
#List of tuples:
numbers_list = [(i, i * i) for i in range(11)]
print('List comprehension generated list of tuples:',numbers_list)

#Combined with 'if' expression:
even_numbers = [i for i in range(11) if i % 2 == 0] #To generate even numbers from 0 to 11
print('Even numbers generated as a list comprehension:', even_numbers)

list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
combined_list = [item for i in list_of_lists for item in i]
print('Combined list:', combined_list)
'''
List comprehension as normal code for proper understanding:
    combined_list = list()
    list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
    for i in list_of_lists:
        for j in i:
            combined_list.append(j)
    print(combined_list)
'''

#Lambda functions:
#definition: lambda parameters, parameters,...: expression
#returns the result, not 'return' command needed
square = lambda x : x ** 2
print('Lambda function:',square(2))

multiple_variables = lambda x, y, z: x ** 2 + y - z
print('Lambda functions, multiple variables:', multiple_variables(1,2,3))

def lambda_power(x):
    return lambda n : x ** n
number = lambda_power(2)(3) #first parameter: function, second parameter: lambda
print('Lambda into another function:', number)




