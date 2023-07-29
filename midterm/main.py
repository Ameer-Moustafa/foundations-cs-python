###########
# Imports #
###########

#Importing Python's built in OS method to read from files and create a clear function for tidiness purposes.
import os

# Importing Regex to isolate integers from strings for sorting purposes

import re

#######################
# Main Data Structure #
#######################

# My programs main data structure, I've chosen a 2D array. This will be built by our importTickets function

ticket_structure = []

####################
# Helper Functions #
####################


# A simple function to clear the screen, for OCD purposes
def clear():
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')


#############################
# Merge sort implementation #
#############################

# I have chosen merge sort as my algorithm of choice because O(NlogN) is faster than O(N^2) when N is over 100 according to my research. Since the number of tickets could very well go over 100. I have chosen Merge sort.

# Research Reference
# https://stackoverflow.com/questions/23329234/which-is-better-on-log-n-or-on2
# Video showed me a cleaner implementation, learned it before but decided to include it here regardless.
# https://www.youtube.com/watch?v=iR1CXiC7OQc


def merge(left, right):  # This function will handle the merging part of our merge sort implementation
  merged_array = []
  index_left = 0
  index_right = 0
  while index_left < len(left) and index_right < len(right):
    if left[index_left] < right[index_right]:
      merged_array.append(left[index_left])
      index_left += 1
    else:
      merged_array.append(right[index_right])
      index_right += 1
  merged_array += left[index_left:]
  merged_array += right[index_right:]
  return merged_array


def mergeSort(list):  # This function will handle the splitting of the arrays in our implementation
  if len(list) <= 1:
    return list
  mid = len(list) // 2
  left = mergeSort(list[:mid])
  right = mergeSort(list[mid:])
  return merge(left, right)

##################
# Menu functions #
##################


def displayMenu():  # Initial display function and log-in form.
  print("""
  
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝\n""")
  print("Welcome to ticketer, please login to continue\n")

  username = input("Enter your username: ")

  if username == "admin":
    attempts = 5
    password = input("Enter your password: ")

    while password != "admin123123":
      clear()
      print(f"Incorrect password, please try again. {attempts} remaining.")
      attempts -= 1
      password = input("Attempt entering your password again: ")

      if attempts == 0:
        clear()
        return print(
          "Allowed password attempts exceeded, Incident will be reported")
    displayAdmin()


# Admin display menu
def displayAdmin():
  clear()
  print("""
  
████████╗██╗░█████╗░██╗░░██╗███████╗████████╗███████╗██████╗░
╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
  print("""Welcome Administrator:\n
            [1] Display Statistics
            [2] Book a Ticket
            [3] Display all tickets
            [4] Change Ticket's priority
            [5] Disable Ticket
            [6] Run Events
            [7] Exit\n""")

  choice = int(input("Please select a number to continue: "))
  if choice == 1:
    getStatistics()
  elif choice == 2:
    bookTicketAdmin()
  elif choice == 3:
    pass
  elif choice == 4:
    changePriority()


# User display Menu
def displayUser(username):
  print("""
  
████████╗██╗░█████╗░██╗░░██╗███████╗████████╗███████╗██████╗░
╚══██╔══╝██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
  print(f"""Welcome {username}, Please select a function:\n
              [1] Book a Ticket
              [2] Exit""")


#########################
# Main program functions#
#########################

# A function to import our data and build our data structure.


def importTickets():
  with open('data.txt', 'r') as data:
    for line in data:
      # Remove spaces from a line and split every line into an array
      line_array = line.replace(' ', '').split(',')
      # Remove "\n" from the end of every array returned and convert our priority string into an integer
      line_array[-1] = int(line_array[-1].strip())
      ticket_structure.append(line_array)


# Resources used for this function:
# https://realpython.com/read-write-files-python/ - To learn how to read and write files as well as iterate through.


# Function to display the event ID with the highest number of tickets

def getStatistics():
  clear()
  print(f"""

░██████╗████████╗░█████╗░████████╗██╗░██████╗████████╗██╗░█████╗░░██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝╚══██╔══╝██║██╔══██╗██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░██║╚█████╗░░░░██║░░░██║██║░░╚═╝╚█████╗░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░╚═══██╗░░░██║░░░██║██║░░██╗░╚═══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░██║██████╔╝░░░██║░░░██║╚█████╔╝██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═════╝░
        \n""")
  event_list = []
  for row in range(len(ticket_structure)):
    event_list.append(ticket_structure[row][1])
    most_popular_event = max(event_list)
  print(
    f"Event number {most_popular_event[len(most_popular_event) - 1]} is the event with the highest ticket sales\n"
  )
  choice = input(
    "Please enter Y to check statistics again or any other key to return to the main menu: "
  )
  if choice == "y" or choice == "Y":
    getStatistics()
  else:
    displayAdmin()


# Resources for this function:
# I used the below link, to learn about the max() function, which I used to return the most repeated value in the array
# https://bobbyhadz.com/blog/python-find-most-common-element-in-list


# A function allowing the admin to book tickets
def bookTicketAdmin():
  clear()
  print(f"""

██████╗░░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
██████╦╝██║░░██║██║░░██║█████═╝░██║██╔██╗██║██║░░██╗░
██╔══██╗██║░░██║██║░░██║██╔═██╗░██║██║╚████║██║░░╚██╗
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
        \n""")
  ticket_list = []
  for row in range(len(ticket_structure)):
    numbers = re.findall('[0-9]+', ticket_structure[row][0])
    for number in numbers:
      ticket_list.append(int(number))
  ticket_list = mergeSort(ticket_list)
  ticket_id = ticket_list[len(ticket_list) - 1]

  print("Please fill out the below prompts to book a new ticket to the system:\n")
  username = str(input("Please enter a username to append: "))
  print()
  eventID = str(input("Please enter an eventID in the following format (ex: ev001, ev002): "))
  print()
  eventDate = str(input("Please enter the event date in the following format (ex: 2023-08-03): ")).replace('-','')
  print()
  priority = int(input("Enter the ticket holder's priority in the following format (ex: 0): "))
  print()

  ticket = [f"tick{ticket_id + 1}", eventID, username, eventDate, priority]

  print(f"""
        ######################
        # Your current Ticket#
        ######################
        
        Ticket ID: {ticket_id + 1}        
        EventID: {eventID}
        Username: {username}      
        EventDate: {eventDate}
        Priority: {priority}
        """)

  choice1 = input(str("Press Y to book your ticket or any other key to discard it and return to the main menu: "))
  if(choice1 == "Y" or choice1 == "y"):
    ticket_structure.append(ticket)
    print()
    print("Your ticket has been added to the system\n")
    choice2 = str(input("Press Y to add another ticket or any other key to return to the main menu: "))
    if(choice2 == "Y" or choice2 == "y"):
      clear()
      bookTicketAdmin()
    else:
      displayAdmin()
  else:
    displayAdmin()

# Resources used for this function
# I knew about regex before, but used this to figure out how to do what I needed to do
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html

def showTickets(): # TO-DO, choice 3
  pass

def changePriority():
  clear()
  print(f"""

██████╗░██████╗░██╗░█████╗░██████╗░██╗████████╗██╗░░░██╗
██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗░██╔╝
██████╔╝██████╔╝██║██║░░██║██████╔╝██║░░░██║░░░░╚████╔╝░
██╔═══╝░██╔══██╗██║██║░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░
██║░░░░░██║░░██║██║╚█████╔╝██║░░██║██║░░░██║░░░░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
        \n""")
  ticket_id = str(input("Enter your ticket ID with the following order (ex: tick1, tick11): "))
  priority = int(input("Enter your tickets priority number: (ex: 0): "))
  for row in range(len(ticket_structure)):
    if ticket_structure[row][0] == ticket_id and ticket_structure[row][4] == priority:
      new_priority = int(input("Your ticket has been found, please enter a new priority number: "))
      ticket_structure[row][4] = new_priority
      print("Ticket priority has been changed \n")
      print()
      choice = input("Press Y to change another ticket's priority or any other key to return to the main menu: ")
      if(choice == "Y" or choice == "y"):
        changePriority()
      else:
        displayAdmin()
    else:
      ticket_flag = False

  if not ticket_flag:
    choice = input("Your ticket has not been found, press Y to search for another ticket or any key to return to the main menu: ")
    if(choice == "Y" or choice == "y"):
      changePriority()
    else:
      displayAdmin()


    


def main():
  importTickets()
  displayMenu()


main()
