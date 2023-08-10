
# A node class that will be reused for a lot of our data structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A singly linked list class 
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("Linked list is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
    
    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            self.size += 1

    def remove(self, value):
        if self.isEmpty():
            print("The list is empty, there is nothing to remove")
        current = self.head
        previous = current
        while current.next != None:
            previous = current
            current = current.next
            if self.head.data == value:
                self.head = self.head.next
                size -= 1
            elif current.data == value:
                previous.next = current.next
                size -= 1
        return print(f"All instances of the number {value} have been removed!")

# A Queue data structure
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("Linked list is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
    
    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("The list is empty, there is nothing to remove")
        elif self.size == 1:
            value = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return value
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

# A stack data structure

class Stack:
    def __init__(self):
        self.head = None
        self.size = 1
    
    def isEmpty(self):
        return self.head == None
    
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            print("The stack is empty, there is nothing to remove")
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

    def peek(self):
        if self.isEmpty():
            print("The stack is empty, Nothing to see here")
        else:
            print(self.head.data)

# The constructor for our Student object

class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
    
    def getName(self):
        return self.name
    
    def getMidtermGrade(self):
        return self.midterm_grade
    
    def getFinalGrade(self):
        return self.final_grade
    
    def getAttitude(self):
        return self.good_attitude

# The priority queue data structure that we're going to use to process students

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("The Queue is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data.getName())
                current = current.next
    
    def enqueue(self, data):

        node = Node(data)

        # if list is empty, just add a node
        if self.isEmpty():
            self.head = node
            self.size += 1
        
        # Check to see if there is only one node in our priority queue
        elif self.size == 1:
            # If only student in queue has false attitude and student to be added has True attitude, put good attitude at head
            if not self.head.data.getAttitude() and node.data.getAttitude():
                node.next = self.head
                self.head = node
                self.size += 1

            # Check if only student in queue and student do be added both have a good attitude
            elif self.head.data.getAttitude() and node.data.getAttitude():
                # Add the student with the highest final grade to the top
                if self.head.data.getFinalGrade() >= node.data.getFinalGrade():
                    self.head.next = node
                    self.size += 1
                else:
                    node.next = self.head
                    self.head = node
                    self.size += 1
            # If both students have a bad attitude, just add the new student to the end of the queue
            else:
                self.head.next = node
                self.size += 1
        # Rest of logic to add when queue has 2 elements. Everything above works, don't touch it
        else:
            current = self.head
            previous = current


            




        


            
            
            

                



batoul = Student('Batoul', 60, 70, True)

ali = Student('Ali', 100, 100, False)

omar = Student('omar', 100, 100, False)

mazen = Student('Mazen', 70, 75, True)

faisal = Student('Faisal', 30, 80, True)



test_prio = PriorityQueue()
test_prio.enqueue(ali)
test_prio.enqueue(omar)


test_prio.display()







# The singly linked list that we're going to be using for the first question
singly_list = LinkedList()

# The stack and queue we're going to be using for our plaindrome problem
plaindrome_stack = Stack()
plaindrome_queue = Queue()
