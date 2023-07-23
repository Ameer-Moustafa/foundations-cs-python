from datetime import datetime, date
import os

# Helper Functions

def clear(): # A function to clear the screen regardless of windows or Linux  # O(1)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def getName(): # Get initial user name and store it in a global variable # O(1)
    global name
    name = input("Hello there, enter your name to get started: ")

# A function to create matrices
def createMatrix(): # O(n^2) N being the number of inputs
    matrix = []
    num_rows = eval(input("Enter the number of rows for your matrix: "))
    num_col = eval(input("Enter the number of columns for your matrix: "))
    print()
    for row in range(num_rows):
        matrix.append([])
        for col in range(num_col):
                element = input(f"\033[0;32m Enter element {col} in row {row} to be added to the matrix: ")
                matrix[row].append(element)
    return matrix

def createDictionary(): # A function to help with creating dictionaries # O(N) N being how many key-value pairs the user inputs
    dict = {}
    pairs = eval(input("How many value-pairs do you want in your dictionary: "))

    for value in range(pairs):
        key = input("\033[0;32m Input your key: ")
        value = input("\033[0;31m Input your value: ")
        print()
        dict[key] = value
    return dict

# A function to check if a string is a palindrome or not.
def stringChecker(s): # O(n) N being how many times the function is called again.
    if len(s) == 0:
        return True
    else:
        if(s[0] == s[-1]):
            return stringChecker(s[1:-1])
        else:
            return False


def merge(left, right): # A function to handle the merging part of the merge sort algorithm
    merged_array = []
    index_left = 0
    index_right = 0
    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            merged_array.append(left[index_left])
            index_left += 1
        else:
            merged_array.append(right[index_right])
            index_right += 1
    merged_array += left[index_left:]
    merged_array += right[index_right:]
    return merged_array


def mergeSort(list): # A function to handle splitting the arrays   # O(N * LogN)
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])
    return merge(left, right)


def displayMenu(): # Main Menu function # O(1)
    clear()
    print("""\033[1;31m
    
░█████╗░░██████╗░██████╗██╗░██████╗░███╗░░██╗███╗░░░███╗███████╗███╗░░██╗████████╗  ██████╗░
██╔══██╗██╔════╝██╔════╝██║██╔════╝░████╗░██║████╗░████║██╔════╝████╗░██║╚══██╔══╝  ╚════██╗
███████║╚█████╗░╚█████╗░██║██║░░██╗░██╔██╗██║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░  ░█████╔╝
██╔══██║░╚═══██╗░╚═══██╗██║██║░░╚██╗██║╚████║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░  ░╚═══██╗
██║░░██║██████╔╝██████╔╝██║╚██████╔╝██║░╚███║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░  ██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░╚═════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░
""")
    print(f"""\033[0;32m           Welcome {name}""")
    print(f"""\033[0;32m           Today is {date.today().strftime("%B %d, %Y")} and it is currently {datetime.today().strftime("%H:%M %p")}\n""")
    print("           [+] Author: Ameer Moustafa")
    print("           [+] Mail: Ameer.Moustafa1@gmail.com")
    print("           [+] Github: https://github.com/Ameer-Moustafa\n")
    print("\033[1;31m   --------------------------------Main Menu--------------------------------\n")
    print("""                   [1] Add Matrices             [2] Check Rotation
                                
                   [3] Invert Dictionary        [4] Convert Matrix to Dictionary 

                   [5] Check Palindrome         [6] Search for an Element

                   [7] Exit\n""")
    selection = eval(input("            Enter the corresponding number to make your selection (0-7): "))
    if(selection == 1):
        addMatrices()
    elif(selection == 2):
        checkRotation()
    elif(selection == 3):
        invertDictionary()
    elif(selection == 4):
        convertMatrix()
    elif(selection == 5):
        checkPalindrome()
    elif(selection == 6):
        searchElement()

        



# Main functions

def addMatrices(): # A function to add matrices # O(N^2) N representing the number of inputs
    clear()
    print(f"""

░█████╗░██████╗░██████╗░  ███╗░░░███╗░█████╗░████████╗██████╗░██╗░█████╗░███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗  ████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝██╔════╝
███████║██║░░██║██║░░██║  ██╔████╔██║███████║░░░██║░░░██████╔╝██║██║░░╚═╝█████╗░░╚█████╗░
██╔══██║██║░░██║██║░░██║  ██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██╗██║██║░░██╗██╔══╝░░░╚═══██╗
██║░░██║██████╔╝██████╔╝  ██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║██║╚█████╔╝███████╗██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░╚══════╝╚═════╝░
\n""")

    matrix1 = []
    matrix2 = []
    matrix3 = []
    
    num_rows = eval(input("Enter number of rows: "))
    num_col = eval(input("Enter number of cols: "))
    print()

    for row in range(num_rows):
        matrix1.append([])
        matrix2.append([])
        matrix3.append([])
        for col in range(num_col):
            element = eval(input(f"\033[0;32m    Enter element {col} in row {row} in the FIRST matrix: "))
            matrix1[row].append(element)
            element2 = eval(input(f"\033[0;33m    Enter element {col} in row {row} in the SECOND matrix: "))
            print()
            matrix2[row].append(element2)
            matrix3[row].append(matrix1[row][col] + matrix2[row][col])

    print(f"\033[0;32m The sum of the two matrices is {matrix3}\n")
    choice = str(input("\033[1;31m Enter Y to add another matrix or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        addMatrices()
    else:
        displayMenu()


def invertDictionary(): # A function to invert a dictionary # O(n) N being the input size from our createDictionary() function.
    clear()
    print("""
    
██╗███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗
██║████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝
██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░
██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░
██║██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

██████╗░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░█████╗░██████╗░██╗░░░██╗
██╔══██╗██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝
██║░░██║██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║███████║██████╔╝░╚████╔╝░
██║░░██║██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║██╔══██║██╔══██╗░░╚██╔╝░░
██████╔╝██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██║░░██║██║░░██║░░░██║░░░
╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░\n""")

    dict = createDictionary()
    flipped_dict = {}
    for key, value in dict.items():
        if value in flipped_dict:
            if isinstance(flipped_dict[value], list):
                flipped_dict[value].append(key)
            else:
                flipped_dict[value] = [flipped_dict[value], key]
        else:
            flipped_dict[value] = key
    print(f"Your original dictionary is {dict} and your inverted dictionary is {flipped_dict}\n")
    choice = str(input("\033[1;31m Enter Y to invert another dictionary or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        invertDictionary()
    else:
        displayMenu()

    
def checkRotation(): # A function to check if a matrice is a rotation of another matrice #O(N^2) N being the number of inputs from our create matrix function
    clear()
    print(f"""
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░  ██████╔╝██║░░██║░░░██║░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░  ██╔══██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗  ██║░░██║╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
\n""")
    matrix1 = createMatrix()
    input("First matrix created, press Enter to continue....\n")
    matrix2 = createMatrix()
    input("Second matrix created, press Enter to continue....\n")
    matrix3 = []
    matrix4 = []
    
    for row in range(len(matrix1)):
        for col in range(len(matrix1[row])):
            matrix3.append(matrix1[row][col])

    
    for col in range(len(matrix2[0])):
        for row in range(len(matrix2)):
            matrix4.append(matrix2[row][col])

    if(matrix3 == matrix4):
        print(f"""
        #####################################################################
        #The first and second matrices provided are rotations of each other.#
        #####################################################################\n""")
    else:
        print(f"""
        #########################################################################
        #The first and second matrices provided are NOT rotations of each other.#
        #########################################################################\n""")
    
    choice = str(input("\033[1;31m Enter Y to check the rotation of another pair or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        checkRotation()
    else:
        displayMenu()



def convertMatrix(): # A function that convers a matrix to a dictionary # O(N^2) Due to our CreateMatrix function
    clear()
    print(f"""
    
░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗  ████████╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝  ╚══██╔══╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░  ░░░██║░░░██║░░██║
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░  ░░░██║░░░██║░░██║
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░  ░░░██║░░░╚█████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░

██████╗░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░█████╗░██████╗░██╗░░░██╗
██╔══██╗██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝
██║░░██║██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║███████║██████╔╝░╚████╔╝░
██║░░██║██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║██╔══██║██╔══██╗░░╚██╔╝░░
██████╔╝██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██║░░██║██║░░██║░░░██║░░░
╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░""")
    print("Please make sure the elements inside your matrix rows follow the following convention: [First Name, Last Name, ID, Job Title, Company]")
    matrix = createMatrix()
    dict = {}

    for row in range(len(matrix)):
        key = matrix[row].pop(2)
        dict.setdefault(key,matrix[row])
    
    print()
    print("Your dictionary is below:\n")
    print(dict)
    print()
    choice = str(input("\033[1;31m Enter Y to convert another matrix or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        convertMatrix()
    else:
        displayMenu()


def checkPalindrome(): # O(n) N being the amount of times our recursive function stringChecker is called
    clear()
    print(f"""
    
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝

██████╗░░█████╗░██╗░░░░░██╗███╗░░██╗██████╗░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔══██╗██║░░░░░██║████╗░██║██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝
██████╔╝███████║██║░░░░░██║██╔██╗██║██║░░██║██████╔╝██║░░██║██╔████╔██║█████╗░░
██╔═══╝░██╔══██║██║░░░░░██║██║╚████║██║░░██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══╝░░
██║░░░░░██║░░██║███████╗██║██║░╚███║██████╔╝██║░░██║╚█████╔╝██║░╚═╝░██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝\n""")

    string = str(input("Input a string to perform the check on: "))
    print()
    result = stringChecker(string)
    if(result):
        print(f"{string} is a Palindrome\n")
    else:
        print(f"{string} is NOT a Palindrome\n")
    
    choice = str(input("\033[1;31m Enter Y to check another string or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        checkPalindrome()
    else:
        displayMenu()


def searchElement(): # O(N*LogN) Due to our mergeSort algorithm
    print(f"""
    
░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗  ███████╗██╗░░░░░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║  ██╔════╝██║░░░░░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║  █████╗░░██║░░░░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║  ██╔══╝░░██║░░░░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ███████╗███████╗███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░\n""")
    elements = input("Enter the elements for your list, seperated by a space: ").split()
    value = input("Now enter a value to search for within your list: ")
    sorted_list = mergeSort(elements)
    for i in range(len(sorted_list)):
        if sorted_list[i] == value:
            return print(f"{value} has been found at index {i}")
    return print(f"{value} has not been found")
    choice = str(input("\033[1;31m Enter Y to search for another element or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        searchElement()
    else:
        displayMenu()











# Main program loop # O(N^2) is the worst case senario for our program

def main():
    getName()
    displayMenu()
    

main()