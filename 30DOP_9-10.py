# === IF ===

a = 3
#regular way
print('\nFirst way:')
if a > 0:
    print('\'a\' is a positive number')
elif a < 0:
    print('\'a\' is a negative number')
else:
    print('\'a\' is zero')

#short handed
print('\nSecond way:')
print('\'a\' is a positive number') if a > 0 else print('\'a\' is a negative number')

#nested
print('\nNested way:')
if a > 0:
    if a % 2 == 0:
        print('\'a\' is positive and even')
    else:
        print('\'a\' is positive')
elif a == 0:
    print('\'a\' is zero')
else:
    print('\'a\' is a negative number')

#better way for nested
print('\n\'and\' operator:')
if a > 0 and a % 2 == 0:
    print('\'a\' is positive and even')
elif a > 0:
    print('\'a\' is positive')
elif a == 0:
    print('\'a\' is zero')
else:
    print('\'a\' is zero')

#'or' operator
print('\'or\' operator')
user = 'Jorge'
level = 10
if user is 'Admin' or level >= 10:
    print('Access granted!')
else:
    print('You do not meet the requirements')

# === WHILE ===

count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print('Now the cycle finished, and this message is printed')

#break and continue iteration:
count = 1
while count < 10:
    print(count)
    count += 1
    if count == 3:
        print('Maximum reached!')
        break
else:
    print(f'Count reached: {count}')

count = 1
while count < 10:
    if count == 3:
        count += 1
        continue #omits printing number 3, it continues with the next cycle
    print(count)
    count += 1

#=== FOR ===
count = 0
new_list = ['a', 'b', 'c', 'd']
for i in new_list:
    print(f'List[{count}] item: {i}')
    count += 1

print('\n')
count = 0
word = '30 Days of Python'
for i in word:
    print(f'Word[{count}] item: {i}')

print(range(len(word))) #working from 0 to 17
for i in range(len(word)):
    if i == 3:
        print(word[i])
    else:
        pass

first_dict = {
    'name': 'Jorge',
    'surname': 'Sanazi'
}

dict_keys = []
for keys in first_dict:
    print(keys)
    dict_keys.append(keys)
print(f'All dict keys: {dict_keys}')

for key, value in first_dict.items():
    print(key, ':', value)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
    
