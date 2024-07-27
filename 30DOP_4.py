#Capitalize first string letter

name = 'nicolas'
frase = 'This\tis\ta\tnew\tfrase'
print(name.capitalize())
#Counts how many times an argument appears
print(name.count('a', 0, 3)) #2nd argument is where to begin, last is where to finish. No arguments mean full string search
print(name.endswith('s'))  #boolean value
print(frase.expandtabs(15)) #changes tab characters with spaces (8 spaces if not specified)
print(name.find('n')) #returns index of the argument (first appearance)
print(name.rfind('p')) #returns index of the argument (last appearence. returns -1 if not found)
string = 'This is an example an'
sub_string = 'an'
print(string.index(sub_string)) #returns the first index of the substring in the string. returns error if not found
print(string.rindex(sub_string)) #returns the highest index of the substring in the string. returns error if not found
print(string.isalnum()) #checks if the whole string is alphanumerical (in this case, spaces are not, so returns false)
string = 'thisisanotherexample'
print(string.isalpha()) #checks if the whole string is alphabet characters (try changing 'string' to thisisanotherexample1, it will return false)
string = '123'
print(string.isdecimal()) #checks if the whole string is decimal (DOES NOT WORK WITH LITERAL INTEGERS string = 123 wont work)
string = '30'
print(string.isdigit()) #idem previous, but checks also for another unicode characters
print(string.isnumeric()) # same previous, accepts more digits
string = '30my_name'
print(string.isidentifier()) #checks if the string is a valid variable name (False in this case because it begins with a number)
print(string.islower()) #checks if whole string is in lowercase
print(string.isupper()) #idem upper
string_list = ['Jorge', 'Rodrigo', 'Matias']
whole_list = ' '.join(string_list) #'parameter'.join(list to concatenate) turns a list to a whole string variable
print(whole_list)
string_2 = 'what is what this what'
print(string_2.strip('what')) #removes all given characters from THE BEGINNIG AND ENDING of the string, does not work with things in the middle
print(string_2.replace('what', 'replaced')) #replaces one word for another
print(string_2.split()) #splits into a whole list (arguments such as split(',') are permitted)
string_2 = 'now this is a title'
print(string_2.title())
string_2 = 'This IS MUTant'
print(string_2.swapcase())
print(string_2.startswith('This')) #boolean return