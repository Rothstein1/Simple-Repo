# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:33:20 2022

@author: jacob
"""

name = "Eric"
age = 74

#################
## Str.format()##
#################
"Hello, {}. You are {}.".format(name,age)

#can reference variables by their index
"Hello, {1}. You are {0}.".format(age, name)

# str.format() with dictionaries 
person = {"name": "eric", "age" : 74}

"Hello, {x}. You are {y}".format(x = person["name"], y = person["age"])

# ** trick with dictionaries
"Hello, {name}. You are {age}.".format(**person)

#################
## f-strings##
#################
#f-strings are a better alternative to str.format()

#can use either a lower class letter, 
name = "Eric"
age = 74
f"Hello {name}. You are {age}!"

#or an upper case letter 
name = "Eric"
age = 74
F"Hello {name}. You are {age}!"

#This works
y= f"{2*7}"


#f-strings with self-defined functions
def to_lower(i):
    return i.lower()

name = "Eric Sasha"
f"{to_lower(name)} is funny"

#f-strings with built in functions
f"{name.lower()} is funny"

##Multi-line f-strings

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"

message = f"Hi {name}." f" Is it true you are a {profession}." f" Or is your real name {affiliation}"
message

## Is the same as the below (Can use open and close parenthesis in beginning and end of message to write over multiple lines ):
message2 = (
    f"Hi {name}."
    f" Is it true you are a {profession}." 
    f" Or is your real name {affiliation}"
    )
message2

## Can also do the below (Can use backslash at the end of each line to write over mutliple lines)
message3 = f"Hi {name}." \
    f" Is it true you are a {profession}."  \
    f" Or is your real name {affiliation}"
message3


##But you can't use the triple quotes:
message4 = f""""Hi {name}.
    Is it true you are a {profession}.
    Or is your real name {affiliation}.
    """
message4

#Can use any type of quotations:
f"{name}"
#or
f'{name}'
#or
f"""{name}"""
#or
f'''{name}'''

#Only rule is that you can't use the same type of quotation mark outside the f-string and inside the expression
# If that is needed then you can escape with a \
f"The \"Comedian\" is {name}, aged {age}"

# When using dictionaires. If we use single quotes for the keys of the dict, then use double quotes for the f-strings:
comedian = {'name': 'Eric Idle', 'age': 74}
f"The Comedian is {comedian['name']},  aged {comedian['age']}"

# Braces
# Using one brace will lead to no braces in output
f"{name}"
# Using three braces will lead to single brace in output
f"{{{name}}}"

name = "Eric Idle"
f"{name}"

