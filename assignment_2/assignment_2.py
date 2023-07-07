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

#print(reverseConcatinate("hello", 2))


##############
# Question 2 #
##############

string = "Hello World"
capitalized = ""
lower_case = ""
for i in range(len(string)):
    if(string[i].upper() == string[i]):
        capitalized += string[i]
    else:
        lower_case += string[i]

print(capitalized + lower_case)