dict = {"1":"x", "2":"y", "3":"x", "4":"m"}
dict2 = {}

for key, value in dict.items():
    if(dict2.get(value)):
        print("We goofed")
    else:
        dict2[value] = key



print(dict2)