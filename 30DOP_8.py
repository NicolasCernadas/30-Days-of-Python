new_dict = {
    'name':'Nicolas',
    'surname': 'Cernadas',
    'year': 2,
    'student': True,
    'family': {
        'mother': 'Roxana',
        'brother': 'Bruno',
        'step-father': 'Tomas'
    },
    'pronouns': ['he', 'him', 'his']
    }
#also we can create like this:
new_2dict = dict(name='Nicolas', surname='Cernadas',year=2, address=dict(street='Cosme Argerich', number=1572)) #and so on

print('First way:',new_dict) #<= more visual
print('Second way:', new_2dict)

#Accesing a dictionary
name = new_dict['name'] #if we search for a key that does not exist, this will raise an error
print(f'His name is \'{name}\'')
new_dict['name'] = 'Jorge'
#if we use .get instead, a none existing value returns 'none'
school = new_dict.get('school')
print(school)
#Accesing a dictionary in a dictionary
family = new_dict.get('family')
print(family)
mother = family.get('mother')
print(mother)

#Adding items
new_dict['school'] = 'San Miguel Arcangel'
print(new_dict)
#also
new_dict['pronouns'].append('they') #Adding an item to the list inside the dictionary
print(new_dict)

#checking existence
if 'family' in new_dict:
    print(new_dict['family'])
else:
    print('He or she does not have a family')

#deleting items
new_dict.pop('name') #removes specified key and value
new_dict.popitem() #removes last key and value
del new_dict['surname'] #removes specified key and value
print(f'School, name and surname removed: {new_dict} \n')

#dictionary to a list of tuples
tuple_list = print('listed items:', new_dict.items(),'\n') #this creates a list of tuples with the dictionary values (for what use?)

#clearing and deleting
new_2dict.clear()
del new_2dict

#copying and listing keys
new_2dict = new_dict.copy()
print('copied dictionary:', new_2dict, '\n')
keys = new_2dict.keys() #gets keys as a list of items
print('keys:', keys, '\n')
values = new_2dict.values() #gets values as a list of items
print('values:', values, '\n')
