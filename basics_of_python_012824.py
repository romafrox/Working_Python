# -*- coding: utf-8 -*-
"""Basics of Python_012824.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lJXWgjNUaKE9QhsAQPkGC9aTO-SZhlkC
"""



"""# Python Basics for Astronomy"""

# My first code in Python
print("Hello World!")

"""### 1. Comments"""

# Selected the text below and pressed command + /
# Hello
# my
# name
# is
# astro

"""**Above**: Command + Forward Slash [ / ] -> inserts a hashtag before any selected words
**Below**: Triple " " " lets you leave comments in between " " "

This is my first line of comment
This is my second line of comment

### 2. Variables and Constants
"""

# variables
x = 4
y = 5
print(x+x+y+x+y)
# cosntants; are
X = 4
Y = 5

"""### 3. Basic Data Types (Strings, Integers, and Floats)"""

# Create variables to store the information about a planet in our Solar System
planet_name = "Venus"
planet_name
planet1_name = ''' Planet Name: - Venus
This is the second planet in our Solar System '''
# You can use either triple ' or " to write multiple lines of comments/strings
planet_age = '4.6 Billion Years'
planet_index = 1  # In Python, index starts from 0. Hence, Venus is on Index 1 after Mercury on Index 0.

# Displaying the data values for the data types
print(planet_name)
print(planet_age)
print(planet_index)

# Checking the types of variables by using type() command
print(type(planet_name))
print(type(planet_age))
print(type(planet_index))

z = 3.2
print(type(z))

"""### 4. F-strings"""

# Understanding the power of f'strings
name_planet = "Saturn"
moons_planet = 150
print(f'Planet {name_planet} has {moons_planet} Moons')

# String concatenation
str_1 = "Earth is the only planet with life."
str_2 = "Maybe not! :D:"
print(str_1 + " " + str_2) # this is one way to join the two strings BUT there's another way...
print(f'{str_1} {str_2}') # this way incorporates the f'string and is simpler than above.

"""### 5. User Inputs"""

# Use input() to take user inputs
user_name = input("Enter your name: ") #input() doesn't fully work if you don't assign it to a variable (e.g. user_name); Also it's best if you assign some sort of string to inform what type of input is requested '''

# Displaying the variable and its type given by the user
print(user_name)
print(type(user_name))

# Ask user to input their fave number
user_favenumber = input("Enter your fave number: ")

# Display the variable and its type given by the user
print(user_favenumber)
print(type(user_favenumber))

"""### 6. Data Type Conversion"""

# Commands to convert --> str(input), int(input), float(input)

# Convert a string data into integer and float
  #print(type(user_favenumber)) -> Useless?
str_to_int = int(user_favenumber)
print(str_to_int)
print(type(str_to_int))

# string numbers with decimals ('4.5) can't be converted straight into integers, they must be converted into floats then integers
  # example:
  #wrong: str_to_int1 = int('3.9')
  #correct: str_to_int1 = int(float('3.9'))

str_to_int1 = int(float('3.9'))
print(str_to_int1)
print(type(str_to_int1))

str_to_float = float(user_favenumber) # as above states, user_favenumber was a str, now it's becoming a float (4.0)
print(str_to_float)
print(type(str_to_float))

# Get user input of two different integers and add them together
n1 = int(input('Give any integer number: '))
n2 = int(input('Give one more integer: '))
print(f'The sum of {n1} and {n2} is {n1+n2}')

"""### 7. Control Flow (Loops, For Loops & More)
  * For Loop and While Loop
  * Condition Statements
"""

# range (start, end, skip) ---> Star is inclusive and end is exclusive. I.e. start includes that number, but end doesn't.
range(1,11)

for n in range(10):
  print (n)

#for index in [0,1,2,3,4]:
  #print(index)'''

# While Loop

ct = 0

# The following below wouldn't work because the conditions aren't fully expressed. One's fave CO will infinitely be asked.
# while condition:
#   obj = input(f'Enter your fave Celestial Object {ct+1}: ')

print('---Type "quit" or "stop" to exit!')
while True:
  obj = input(f'Enter your fave Celestial Object {ct+1}: ')
  ct += 1
  if obj.lower == 'quit' or obj.lower == 'stop': #.lower function automatically converts the variable into lowercase. vice versa goes for .upper
    break

"""### 8. Functions!!!"""

# Much like in mathematics, Python allows one to assign a value in order to achieve something else. e.g., f(x) = 3x^2 + 2x + 3 ; x = 4

# Creating a function to greet astronomy fans without any input arguments or conditions
def greet():
  print('Hey Astrophiles!')

# Call the above function
greet()

# Define a function to greet a person whose name will given as an input
#WRONG: greet(input('Your name: ')) # don't want to over
def greet_person(name):
  print(f'Hey {name}, I hope you are enjoying this session and learning a lot of things in Python!')

#Call the above function
greet_person('Roman')

# Positional Arguments
def greeting(name, msg):
  print(f'Hey {name}, {msg}')

# ONE MUST ALWAYS ABIDE BY THE POSTIION OF THE ARGUMENTS IN THE FUNCTION. DON'T SWAP THEM UNLESS YOU LABEL THEM AS SUCH
  # CORRECT: greeting(msg= you're so sexy. ;), name= Milo) --> *** This is an example of a keyword argument ***
  # WRONG: greeting(you're so sexy. ;), Milo) --> This doesn't work because name must come first. Unless you label them as above. ^^^

# Call the above function
greeting('Milo', "you're so sexy. ;)")

# Positional argument
greeting('Milo', "you're so sexy. ;)")
# Keyword argument
greeting(msg = "You're so sexy. ;)", name = "Milo")
### IMPORTANT ---> They output the same thing, but their setup is different. PAY ATTENTION TO THIS.

# Default argument
def greeting_with_default_args(name, msg='welcome, you little bitch!'):
  print(f'Hey {name}, {msg}')

greeting_with_default_args('Roman')

## IMPORTANT: Always write positional arguments BEFORE keyword arguments. Post. Non-default argument follows default argument
  ## WRONG: greeting_with_default_args(msg= "What's up?", 'Mikey')
  ## CORRECT: greeting_with_default_args('Mikey', msg= "What's up?")

# Create a function that will either add, subtract, multiply or divide two numbers
def basic_calc(n1, n2, operation):
  """
  Creates a basic calculator tht takes n1 and n2 in the same order and performs either of:
    - add
    - subtract
    - multiply
    - divide

    Parameters -
    n1 - first number
    n2 - second number
    operations - any of the operations mentioned above for basic_calc

    Return -
    The output of the operations done on n1 and n2
  """
  if operation.lower() == 'add':
    return n1+n2
  elif operation.lower() == 'subtract':
    return n1-n2
  elif operation.lower() == 'multiply':
    return n1*n2
  elif operation.lower() == 'divide':
    return n1/n2
  else:
    print(f'Operation input can only be: add, subtract, multiply or divide. You gave {operation}. Please try again.')

addition = basic_calc(2, 3, 'add')
print(addition)

multiply = basic_calc(3,3,'multiply')
print(multiply)