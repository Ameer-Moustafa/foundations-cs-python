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

def profileGenerator():
    ID = int(input('Enter your ID:'))
    NAME = input('Enter your Name:').replace("  ", " ")
    DOB = input('Enter your date of birth (DD-MM-YYYY or DD/MM/YYYY format):').replace("  ", " ")
    ADDRESS = input('Enter your address:').replace("  ", " ")
    
    print(f'Your profile: ID: {"0" + str(ID)}, name: {NAME.upper().strip()}, DOB: {DOB[0:2] + "/" + DOB[3:5] + "/" + DOB[6:10]}, Address: {ADDRESS.strip().lower()}')
    
#profileGenerator()

##############
# Question 3 #
##############


def digiter():
    digits = input('Input a number: ')
    print(f'{digits} has {len(digits)} digits')

#digiter()

##############
# Question 4 #
##############

def gradeConverter():
    numeric_grade = int(input("What is your numeric grade? "))
    letter_grade = ""
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
        

#gradeConverter()


##############
# Question 5 #
##############

def patterner():
    number = int(input("Enter a number to see something cool: "))
    astrix = "*"
    for i in range(1, number + 1):
        print(astrix * i)
    for i in range(number - 1, -1, -1):
        print(astrix * i)

#patterner()

##############
# Question 6 #
##############

def evenFinder():
    number1 = int(input('Enter the first number in your range: '))
    number2 = int(input('Enter the second number in your range: '))
    while(number2 < number1):
        number2 = int(input('Your second number cannot be smaller than your first number, input a new second number: '))
    
    for i in range(number1, number2 + 1):
        if(i % 2 == 0):
            print(i)
    
#evenFinder()