TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
pwds = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
separator = 40 * '-'
user = input('username: ')
password = input('password: ')

if password == pwds.get(user):
    print(f"""{separator}
Welcome to the app, {user}.
We have 3 texts to be analyzed.
{separator}""")
else:
    print('Incorrect username or password, exiting...')
    quit()

text_nr = input('Enter a number between 1 and 3 to select: ')
if text_nr.isnumeric():
    if int(text_nr) not in range(1, 4):
        print('Incorrect number entered, exiting...')
        quit()
else:
    print('Entered value is not a number, exiting...')
    quit()

stripped_text = TEXTS[int(text_nr)-1].replace(',', '').replace('.', '').split()
title_count = 0
upper_count = 0
lower_count = 0
number_count = 0
number_sum = 0

for word in stripped_text:
    if word.islower() and word.isalpha():
        lower_count += 1
    if word.isupper() and word.isalpha():
        upper_count += 1
    if word.isnumeric():
        number_count += 1
        number_sum += int(word)
    if word.istitle() and word.isalpha():
       title_count += 1


print(f"""There are {len(stripped_text)} words in the selected text
There are {title_count} titlecase words.
There are {upper_count} uppercase words.
There are {lower_count} lowercase words.
There are {number_count} numeric strings.
The sum of all numbers {number_sum}""")

lengths = {}
for wrd in stripped_text:
    if len(wrd) not in lengths:
        lengths[len(wrd)] = 1
    else:
        lengths[len(wrd)] += 1

lengths = sorted(lengths.items())

print(f"""{separator}
LEN| OCCURENCES |NR.
{separator}""")
for i in lengths:
    print(str(i[0]) + '|' + '*'*i[1] + '|' + str(i[1]))
