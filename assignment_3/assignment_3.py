from datetime import datetime, date
import os

def getName():
    global name
    name = input("Hello there, enter your name to get started: ")

def displayMenu():
    os.system('clear')
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
        
            
            

def addMatrices():
    os.system('clear')
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

    print(f"\033[1;31m The sum of the two matrices is {matrix3}\n")
    choice = str(input("\033[1;31m Enter Y to add another matrix or any button to return to the main menu: "))
    if(choice == "y" or choice == "Y"):
        addMatrices()
    else:
        displayMenu()









def main():
    getName()
    displayMenu()
    

main()