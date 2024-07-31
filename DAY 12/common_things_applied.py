import common_things
print(common_things.gen_fullname('Nicolas', 'Cernadas'))
#We are calling the function inside the module we brought with the 'import' command, this brings all within the file

from common_things import gen_fullname
print(gen_fullname('Nicolas', 'Cernadas'))
#This way, we are bringing only the 'gen_fullname' function

from common_things import adding_numbers as ad, saying_hi as hi
print('The result is:', ad(2, 3))
hi('Jorge') #print() included in function
#As we are bringing only 2 functions from the module, is not necessary to call day_12.function

