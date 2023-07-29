###########
# Imports #
###########

#Importing Python's built in OS method to read from files and create a clear function for tidiness purposes.
import os

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
  os.system('clear')


# Merge sort implementation

# I have chosen merge sort as my algorithm of choice because O(NlogN) is faster than O(N^2) when N is over 100 according to my research. Since the number of tickets could very well go over 100. I have chosen Merge sort.

# Research Reference
# https://stackoverflow.com/questions/23329234/which-is-better-on-log-n-or-on2
# Video showed me a cleaner implementation, learned it before but decided to include it here regardless.
# https://www.youtube.com/watch?v=iR1CXiC7OQc


def merge(
  left, right
):  # This function will handle the merging part of our merge sort implementation
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


def mergeSort(
  list
):  # This function will handle the splitting of the arrays in our implementation
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
      # Split every line into an array
      line_array = line.split(',')
      # Remove "\n" from the end of every array returned and convert our priority string into an integer
      line_array[-1] = int(line_array[-1].strip())
      ticket_structure.append(line_array)


# Resources used for this function:
# https://realpython.com/read-write-files-python/ - To learn how to read and write files as well as iterate through.

# Function to display the event ID with the highest number of tickets


def getStatistics():
  clear()
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
  ticket_list = []
  for row in range(len(ticket_structure)):
    ticket_list.append(ticket_structure[row][0])


def main():
  importTickets()
  # displayMenu()
  bookTicketAdmin()


main()
