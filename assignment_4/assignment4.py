import os
from datastructures import singly_list, plaindrome_stack, plaindrome_queue, Student, student_queue

####################
# Helper functions #
####################

# A function that clears the screen
# O(1)
def clear():
  # If statement used to check if the system is windows or not
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')


##################
# Menu Functions #
##################
# Our main menu function
# O(1)
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
    elif menu_selection == 3:
        displayStudents()


# The main menu for our linkedList selection
# O(1)
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
# O(N) N represents the amount of nodes already existing in our linked list
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


# A function for adding a node to our linked list
# O(N) N representing the amount of nodes in our linked list to display.
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

# A function to delete all instances of a node from our linked list
# O(N) N representing the amount of nodes in our linked list.
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
# O(N) N represents the amount of characters in our string
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
# O(N) N represents the amount of characters in our string
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

# A menu to handle adding and interviewing students
# O(1)
def displayStudents():
    clear()
    print(f"""

█▀ ▀█▀ █░█ █▀▄ █▀▀ █▄░█ ▀█▀   █▀▄▀█ █▀▀ █▄░█ █░█
▄█ ░█░ █▄█ █▄▀ ██▄ █░▀█ ░█░   █░▀░█ ██▄ █░▀█ █▄█\n
          [A] Add Student
          [B] Interview Student
          [C] Return to the main menu\n""")

    choice = input("Pick a menu option to continue: ").lower()

    if choice == "a":
        addStudent()
    elif choice == "b":
        interviewStudent()
    else:
        displayMenu()




# A function to add a student to the priority queue
# O(N) N represents the amount of students already in our priority Queue.
def addStudent():
    clear()
    print("""

▄▀█ █▀▄ █▀▄   █▀ ▀█▀ █░█ █▀▄ █▀▀ █▄░█ ▀█▀
█▀█ █▄▀ █▄▀   ▄█ ░█░ █▄█ █▄▀ ██▄ █░▀█ ░█░\n""")
    

    student_name = input("Enter the student's name: ")
    print()
    student_midterm = eval(input("Enter the student's mid-term grade: "))
    print()
    student_final = eval(input("Enter the student's final grade: "))
    print()
    student_attitude = input("Enter the student's attitude represented by True for a good attitude and False for a bad one: ").lower()
    print()

    while student_attitude != "true" and student_attitude != "false":
        print(student_attitude)
        student_attitude = input("Please try again, use either True or False to represent the student's attitude: ").lower()

    
    if student_attitude == "true":
        student_attitude = True
    elif student_attitude == "false":
        student_attitude = False
    
    student = Student(student_name, student_midterm, student_final, student_attitude)

    student_queue.enqueue(student)

    print(f"Student {student.getName()} has been added to the queue for interview\n")

    choice = input("Press Y to add another student or any other button to return to the student menu: ").lower()

    if choice == "y":
        addStudent()
    else:
        displayStudents()

# A function that will dequeue an student for interviewing
# O(1)
def interviewStudent():
    clear()
    student = student_queue.dequeue()

    print(f"""

█▀▀ █▀█ █▄░█ █▀▄ █░█ █▀▀ ▀█▀   █ █▄░█ ▀█▀ █▀▀ █▀█ █░█ █ █▀▀ █░█░█
█▄▄ █▄█ █░▀█ █▄▀ █▄█ █▄▄ ░█░   █ █░▀█ ░█░ ██▄ █▀▄ ▀▄▀ █ ██▄ ▀▄▀▄▀\n
          
          # Student {student.getName()} will now be processed #
          
          # Name: {student.getName()}
          # Mid-term Grade: {student.getMidtermGrade()}
          # Final Grade: {student.getFinalGrade()}\n""")
    
    choice = input("student has been interviewed, press Y to interview the next student or any other button to return to the student menu: ").lower()

    if choice == "y":
        interviewStudent()
    else:
        displayStudents()







########
# Main #
########
# O(1)
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