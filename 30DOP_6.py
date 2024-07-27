new_tuple = ('banana', 'melon', 'watermelon','pineapple', 'apple')
#indexed item
first_item = new_tuple[0]
print(type(first_item), '=>', first_item)

#slicing tuples
sub_touple = new_tuple[1:3] #includes first parameter, omits second
print(sub_touple)
sub_touple = new_tuple[-3:-1] #tuple(-5, -4, -3, -2, -1)
print(sub_touple)

#converting a tuple to a list and vice versa
new_list = list(new_tuple)
print(type(new_list), '=>', new_list)
second_tuple = tuple(new_list)
print(type(second_tuple), '=>', second_tuple)

#checking existence
if 'melon' in new_tuple:
    print(f'Found at new_tuple[{new_tuple.index('melon')}]!')
else:
    print('Not found :(')

#joining tuples
third_tuple = new_tuple + second_tuple
print(third_tuple)

#deletig the tuple
del third_tuple
print(third_tuple) #<= this will return an error: "name third_tuple" is not defined