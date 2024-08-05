#Regular Expression
import re #RegEx module
'''
re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''
#'Match' ('Search' works the same)
txt = 'I love programming in Python, i love programming'
match = re.match('I love programming', txt, re.I) # (match string, where from, case ignore), return None if not match is found
if match is None:
    print('No matches found!')
else:
    print('Match found:', match)
#The span is the starting and ending point of the match, we could get it like this:
span = match.span()
print('Span as a tuple:', span)
#And then slice the first string to the match:
start, end = span
sliced_text = txt[start:end]
print('Sliced text:',sliced_text)

#'Findall'
txt = 'As you previously could see, none of them was as good as me. Not to be honest, but even though, as good. but even'
match = re.findall('As', txt, re.I) #returns all coincidences in a list
print(match)

#'Sub'
sub_string = re.sub('As', 'Or', txt, re.I) #replaces first coincidence
print(sub_string)

#'Split'
txt = '''Hello there.
I am new here.
What about you?
Im glad we met'''

splitted_text = re.split('\n', txt)
print('Splitted text as a list:',splitted_text)

#RegEx patterns
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/images/regex.png all RexEx patterns
#Expample
word = r'apple' #we are declaring just lowercase, this is our pattern
txt = 'I love apples. Apples are good'
match = re.findall(word, txt)
print('Match found:',match)
'''We might want to find all cases where the word 'apple' appears, whether it has 'A' or 'a', we can keep on adding the 're.I' argument to insensitive cases, or might aswell do this: word = r'[Aa]pple' '''
word = r'[Aa]pple'
txt = 'I love apples. Apples are good'
match = re.findall(word, txt)
print('Match found:',match)

#Another examples
word = r'[Aa]pple|[Ll]ove'
txt = 'I love apples. Apples are good. Love is also good'
match = re.findall(word, txt)
print('Match found:',match)

word = r'\d'
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match) #list of single numbers, hardly useful

word = r'\d+'
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match) #much better, list of whole numbers

word = r'[a].' #every time 'a' appears, followed by its next character, except new line
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match)

word = r'[a]*'
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match) #Full list of singular characters of the string

word = r'[a].*' #combined
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match)

word = r'e-?mail' #'?' means that '-' is optional
word2 = r'dress-?code'
txt = 'What was your email again?'
txt2 = 'Would you write it as dress-code or dresscode?'
match = re.findall(word, txt)
match2 = re.findall(word2, txt2)
print('Match found:',match)
print('Match found:',match2)

word = r'\d{4}' #'{}'  means a lenght. could take more than 1 parameter: {1, 4} would bring numbers of 1 to 4 digits
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match)

word = r'^[Ii]' #starts with (weird)
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match)

word = r'[^A-Za-z .]+' #negation, not letter from A - Z, from a - z, nor spaces or dots (+ is to make whole numbers and not singles)
txt = 'I was born in August the 28th of 2001. 28 Times i have seen you!. 2012 Was a hard year'
match = re.findall(word, txt)
print('Match found:',match)



