##############
# Question 1 #
##############

# A)
print(10*(90+2)-5);

# B)
print(10*90+2-5);

# C)
print(10*90+(2-5));

# D)
print(10.0*(90+2)-5);

# E)
print(120/(20+40)-(6-2)/4);

# F)
print(5.0/2);

# G)
print(5/2);

# H)
print(5.0/2.0);

# I)
print(5/2.0);

# J)
print(678%3*(8-(9/4)))

##############
# Question 2 #
##############

# Below is a function that takes user input, stores it in variables and prints a new profile for the user.

def profileGenerator():
    ID = int(input('Enter your ID:')) # Saves the user's ID into a variable

    NAME = input('Enter your Name:').replace("  ", " ") # Saves the user's name into a variable

    DOB = input('Enter your date of birth (DD-MM-YYYY or DD/MM/YYYY format):') # Saves the user's date of birth into a variable

    while(len(DOB) < 10 or len(DOB) > 10): # A loop that asks the user for a new input if they don't input their date of birth correctly
        DOB = input('Please input your date of birth with the proper format (ex: 03/05/1995 or 03-05-1995): ')

    ADDRESS = input('Enter your address:').replace("  ", " ") # Saves the user's address into a variable

    print(f'Your profile: ID: {"0" + str(ID)}, name: {NAME.upper().strip()}, DOB: {DOB[0:2] + "/" + DOB[3:5] + "/" + DOB[6:10]}, Address: {ADDRESS.strip().lower()}')
    # Code above prints all the inputed variables into a profile.
    
profileGenerator()

##############
# Question 3 #
##############

# Below is a function that asks the user for a number and returns how many digits the number has

def digiter():

    digits = input('Input a number: ') # asks the user for a number and saves it into a variable
    print(f'{digits} has {len(digits)} digits') # Returns how many digits are in said number

digiter()

##############
# Question 4 #
##############

# Below is a function that asks the user for a numeric grade and returns a letter grade

def gradeConverter():
    numeric_grade = int(input("What is your numeric grade? ")) # Saves numeric grade into a variable
    letter_grade = "" # initial letter grade variable

    # Below code converts the numeric grade into a letter grade then prints it
    if numeric_grade >= 90:
        if numeric_grade >= 97:
            letter_grade = "A+"
        elif numeric_grade >= 93:
            letter_grade = "A"
        else:
            letter_grade = "A-"

    if numeric_grade >= 80:
        if numeric_grade >= 87:
            letter_grade = "B+"
        elif numeric_grade >= 83:
            letter_grade = "B"
        else:
            letter_grade = "B-"

    if numeric_grade >= 70:
        if numeric_grade >= 77:
            letter_grade = "C+"
        elif numeric_grade >= 73:
            letter_grade = "C"
        else:
            letter_grade = "C-"

    if numeric_grade <= 69:
        if numeric_grade >= 67:
            letter_grade = "D+"
        elif numeric_grade >= 65:
            letter_grade = "D"
        else:
            letter_grade = "D-"

    print(f'{numeric_grade} is equivelant to {letter_grade}')
        

gradeConverter()


##############
# Question 5 #
##############

# Below is a function that prints an astrix pattern based on the number a user inputs.

def patterner():
    number = int(input("Enter a number to see something cool: ")) # Saves the number into a variable
    astrix = "*" # The initial "*" variable that is going to be used to print the pattern

    # Below code loops through using the number and prints "*" accordingly
    for i in range(1, number + 1):
        print(astrix * i)

    # Does the same thing as the above loop but iterates in reverse
    for i in range(number - 1, -1, -1):
        print(astrix * i)

patterner()

##############
# Question 6 #
##############

# Below is a function that takes a range of two numbers and returns the even numbers between them.

def evenFinder():
    number1 = int(input('Enter the first number in your range: ')) # Saves the first number into a variable
    number2 = int(input('Enter the second number in your range: ')) # Saves the second number into a variable

    while(number2 < number1): #A loop that asks the user to re-input the second number if it is smaller than the first one
        number2 = int(input('Your second number cannot be smaller than your first number, input a new second number: '))
    
    # A loop that prints any number that returns 0 when divided by two AKA an even number.
    for i in range(number1, number2 + 1):
        if(i % 2 == 0):
            print(i)
    
evenFinder()