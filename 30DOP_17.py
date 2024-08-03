#Exception handling
#try:
#   block of code to run
#except:
#   block of code to run if things go wrong
try:
    name = input('Enter your name: ')
    age = input("Enter your age: ")
    year_born = 2024 - int(age)
    print('The year you were born is:', year_born)
except: #this one is the most common one
    print('Something went wrong')
#solution would be to convert age to an int

'''
for more specific purposes we migh want
    except TypeError:
        code if type error
    except ValueError:
        code if value error
    except ZeroDivisionError:
        code if zero division error
to shorten the code above, might aswell want to use
    except Exception as e:
        print(e)
'''

