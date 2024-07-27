#
fruits = ['orange', 'apple', 'lemon']
print(f'Fruits: {fruits}')
print(f'Amount of fruits in the list: {len(fruits)}')
last_fruit = len(fruits)-1
last_fruit = fruits[last_fruit]
print(f'The last fruit is the {last_fruit}')
first_fruit, second_fruit, *rest_fruits = fruits
print(first_fruit)
print(second_fruit)
print(rest_fruits) #If there were more fruits in the list, they would all be saved here as a new list
numbers = [1,2,3,4,5,6,7,8,9,10]
one, two, three, *four_to_nine, ten = numbers
print(one)
print(two)
print(three)
print(four_to_nine) #its weird, but its not because of the name, Python understands you want to save everything from the 3rd index to the 9th because the tenth is saved somewhere else
print(ten)
sliced_numbers = numbers[4:5] # [ start (not included) : end (included) : step ] \\returns a list
print(sliced_numbers)
backwards_numbers = numbers[::-1]
print(backwards_numbers)
if 'banana' in fruits: #'in' operator yo check membership
    print('It is!')
else:
    print('Its not')
fruits.append('banana') #Adds an item at the end of the list
print(fruits)
fruits.insert(1, 'mango') #Adds an item at an specific index in a list (other items are shifted)
print(fruits)
fruits.remove('banana') #Removes an specific item
print(fruits)
fruits.pop(0) #Removes an specifi index item
print(fruits)
del fruits[1:2] #idem as pop, but also works within a range of items (includes the first, excludes the second)
print(fruits)   #also a whole list if we type del list_name
fruits.clear() #Clears the list
print(fruits) 

#If we have 2 lists and want to copy one to another, we can do the following:
list1 = [1, 2]
list2 = []
list2 = list1 #Now changes made to list2 will also affect list1, like:
list2[0] = 0
print(list1, list2)
#If we do not want that to happen, we can use '.copy()', like this:
list2 = list1.copy()
list2[0] = 1
print(list1, list2)

#We can concatenate them:
list3 = list1 + list2
list3[0] = 3 #changes made to this list wont alter the other ones
print(list3)
list3.clear()
list3.extend(list1) 
print(list3)
list3.extend(list2)
print(list3)

#Count an amount of times an item appears in a list:
print(f'\'2\' appears: {list3.count(2)} times.')

#Find an item by its index (first time it appears):
print(f'\'1\' Appears for the first time at \"{list3.index(1)}\" index')

#Reverse order
list3.reverse()
print(list3)

#Order and copy the list to another list, without modifying the original list
ordered_copied_list = sorted(list3)
print(f'This is the ordered copied list: {ordered_copied_list}')
print(f'This is the original list: {list3}')

#Sort it:
list3.sort()
print(f'Sorted list: {list3}')
list3.sort(reverse=True) #sorted backwards
print(f'Sorted backwards: {list3}')

print(f'Maximum number in list3: \'{max(list3)}\'')
print(f'Minimum number in list3: \'{min(list3)}\'')
