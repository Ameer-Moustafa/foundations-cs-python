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

# print(reverseConcatinate("hello", 2))


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

# print(rearrangeString("Wake Up Neo"))


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
    
# print(checkCharacter(string1, string2))

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

# getHighestValue(num_list)

##### Bonus #####

def getLowestValue(l):
    index = 0
    sorted_list = sorted(l, reverse=True)
    for i in range(len(l)):
        if(l[i] == sorted_list[len(sorted_list) - 1]):
            index = i
    print(f'The lowest value in the list is {sorted_list[len(sorted_list) - 1]} and it is at index {index}')

# getLowestValue(num_list)


##############
# Question 5 #
##############

