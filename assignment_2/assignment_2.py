##############
# Question 1 #
##############

def reverseConcatinate(s, i):
    if(i == 0):
        return ""
    else:
        reversed_string = ""
        for j in range(len(s) - 1, -1, -1):
            reversed_string += s[j]
        return reversed_string * i

# print(reverseConcatinate("hello", 10)) O(n) Compplexity is dependant on how many times we have to iterate through and multiply the string.


##############
# Question 2 #
##############

def rearrangeString(string):
    upper_case = ""
    lower_case = ""
    for i in range(len(string)):
        if(string[i].isupper() and string[i] != " "):
            upper_case += string[i]
        elif(string[i] != " "):
            lower_case += string[i]
    return upper_case + lower_case

# print(rearrangeString("Wake Up Neo")) O(n), N will increase in complexity when the length of the string grows.


##############
# Question 3 #
##############

string1 = "abcde"
string2 = "edacb"

def checkCharacter(s1, s2):
    checked_string_1 = ""
    checked_string_2 = ""
    for i in range(len(s1)):
        checked_string_1+= s1[i]
        for j in range(len(s2)):
            if(s1[i] == s2[j]):
                checked_string_2 += s2[j]
    if(checked_string_1 == checked_string_2):
        return True
    else:
        return False
    
# print(checkCharacter(string1, string2)) O(N^2) This is quadratic since the inner for-loop is dependant on the outer for loop

##############
# Question 4 #
##############

num_list = [5, 8, 9, 43, 10, 15, 2]

def getHighestValue(l):
    index = 0
    sorted_list = sorted(l)
    for i in range(len(l)):
        if(l[i] == sorted_list[len(sorted_list) - 1]):
            index = i
    print(f'The Highest value in the list is {sorted_list[len(sorted_list) - 1]} and it is at index {index}')

# getHighestValue(num_list) O(n), The time complexity of the algorithm will grow depending on the size of the list that needs to be sorted.

##### Bonus #####

def getLowestValue(l):
    index = 0
    sorted_list = sorted(l, reverse=True)
    for i in range(len(l)):
        if(l[i] == sorted_list[len(sorted_list) - 1]):
            index = i
    print(f'The lowest value in the list is {sorted_list[len(sorted_list) - 1]} and it is at index {index}')

# getLowestValue(num_list) # O(n), The time complexity of the algorithm will grow depending on the size of the list that needs to be sorted.


##############
# Question 5 #
##############

number = 6812

def returnSum(n):
    if n // 10 == 0:
        return n
    return n % 10 + returnSum(n // 10)

# print(returnSum(number)) O(n) The complexity of the algorithm will grow depending on how many times the function is called.

##############
# Question 6 #
##############

string = "Hellloooo worlddddd"

def cleanString(s):
    if len(s) < 2:
        return s
    elif(s[0] == s[1]):
        return cleanString(s[1:])
    else:
        return s[0] + cleanString(s[1:])
    
        

# print(cleanString(string)) # O(n), N being the length of the string.

