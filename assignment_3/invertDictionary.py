# dict = {"1":"x", "2":"y", "3":"x", "4":"m"}

def flip_dict(dict):
    flipped_dict = {}
    for key, value in dict.items():
        if value in flipped_dict:
            # If the value already exists in the flipped dictionary,
            # convert the corresponding key to a list and append the new key.
            if isinstance(flipped_dict[value], list):
                flipped_dict[value].append(key)
            else:
                flipped_dict[value] = [flipped_dict[value], key]
        else:
            # If the value is not yet present in the flipped dictionary,
            # simply add the key-value pair.
            flipped_dict[value] = key
    return flipped_dict

# Test the function
flipped_dict = flip_dict(dict)
print(flipped_dict)



print(dict)