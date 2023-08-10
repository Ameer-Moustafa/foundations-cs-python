import os
from datastructures import singly_list, plaindrome_stack, plaindrome_queue

####################
# Helper functions #
####################

# A function that clears the screen

def clear():
  # If statement used to check if the system is windows or not
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')


##################
# Menu Functions #
##################

def displayMenu():
    clear()
    print(f"""
    
▄▀█ █▀ █▀ █ █▀▀ █▄░█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   █░█
█▀█ ▄█ ▄█ █ █▄█ █░▀█ █░▀░█ ██▄ █░▀█ ░█░   ▀▀█\n

    [1] Singly Linked List
    [2] Check if Palindrome
    [3] Priority Queue
    [4] Evaluate an Infinix Expression
    [5] Exit\n""")

    menu_selection = int(input("Input a number to decide what you want to do: "))

    if menu_selection == 1:
        linkedListMenu()
    elif menu_selection == 2:
        plaindromeCheckerMenu()



def linkedListMenu():
    clear()
    print(f"""
    
█░░ █ █▄░█ █▄▀ █▀▀ █▀▄   █░░ █ █▀ ▀█▀
█▄▄ █ █░▀█ █░█ ██▄ █▄▀   █▄▄ █ ▄█ ░█░\n
    [A] Add node
    [B] Display Nodes
    [C] Search for & Delete Node
    [D] Return to main Menu \n""")

    menu_selection = input("Enter one of the above letters: ").lower()

    if menu_selection == "a":
        addNode()
    elif menu_selection == "b":
        displayNodes()
    elif menu_selection == "c":
        deleteNode()
    elif menu_selection == "d":
        displayMenu()
    

################################
# Singly Linked list Functions #
###############################

def addNode():
    clear()
    print(f"""

█░░ █ █▄░█ █▄▀ █▀▀ █▀▄   █░░ █ █▀ ▀█▀
█▄▄ █ █░▀█ █░█ ██▄ █▄▀   █▄▄ █ ▄█ ░█░\n""")

    numerical_value = eval(input("Please enter a number to be added to the linked list: "))
    print()

    singly_list.add(numerical_value)

    print(f"{numerical_value} has been added to the linked list.\n")

    choice = input("Press Y to add another value to the linked list or any other button to return to the linked list menu: ").lower()

    if choice == "y":
        addNode()
    else:
        linkedListMenu()

def displayNodes():
    clear()
    print(f"""

█░░ █ █▄░█ █▄▀ █▀▀ █▀▄   █░░ █ █▀ ▀█▀
█▄▄ █ █░▀█ █░█ ██▄ █▄▀   █▄▄ █ ▄█ ░█░\n""")

    singly_list.display()
    print()

    choice = input("Press Y to display the linked list again or any other button to return to the linked list menu: ").lower()
    if choice == "y":
        displayNodes()
    else:
        linkedListMenu()

def deleteNode():
    clear()
    print(f"""

█░░ █ █▄░█ █▄▀ █▀▀ █▀▄   █░░ █ █▀ ▀█▀
█▄▄ █ █░▀█ █░█ ██▄ █▄▀   █▄▄ █ ▄█ ░█░\n""")

    choice = eval(input("Enter the number you wish for all instances to be removed from the linked list: "))
    print()
    singly_list.remove(choice)
    print()
    choice = input("Press Y to input another number to remove or any button to return to the linked list menu: ").lower()
    if choice == "y":
        deleteNode()
    else:
        linkedListMenu()

################################
# Palindrome Checker Functions #
################################

# A function that takes characters from a string input, enqueue them in a queue and a stack respectively. Then dequeue them and check if they are matching.
def checkPalindrome(string):
    for character in string:
        plaindrome_queue.enqueue(character)
        plaindrome_stack.push(character)
    
    while not plaindrome_queue.isEmpty():
        first_string = plaindrome_queue.dequeue()
        second_string = plaindrome_stack.pop()

        if first_string != second_string:
            return print(f"The string {string} is not a palindrome\n")
    return print(f"The string {string} is a palindrome.\n")

# Our main palindrome checker function which will display info to the user
def plaindromeCheckerMenu():
    clear()
    print("""
    
█▀█ ▄▀█ █░░ █ █▄░█ █▀▄ █▀█ █▀█ █▀▄▀█ █▀▀   █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
█▀▀ █▀█ █▄▄ █ █░▀█ █▄▀ █▀▄ █▄█ █░▀░█ ██▄   █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄\n""")

    string_input = input("Enter a string to perform the plaindrome check on: ")
    print()
    checkPalindrome(string_input)

    choice = input("Press Y to check for another string or any other button to return to the main menu: ").lower()
    if choice == "y":
        plaindromeCheckerMenu()
    else:
        displayMenu()

############################    
# Priority Queue Functions #
############################




########
# Main #
########

def main():
    username = input("Welcome, Please input a username to get started: ")
    clear()
    print(f"""
    
▄▀█ █▀ █▀ █ █▀▀ █▄░█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   █░█
█▀█ ▄█ ▄█ █ █▄█ █░▀█ █░▀░█ ██▄ █░▀█ ░█░   ▀▀█\n""")
    input(f"Welcome to Assignment 4 {username}, press ENTER to continue.....")
    clear()
    
    displayMenu()


main()