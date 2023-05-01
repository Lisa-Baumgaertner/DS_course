def count_letter(some_str):
    
    if isinstance(some_str, str) == True:
        
        letter_dict = {} # create the dict
        # get rid of whitespaces in entered string, we do not want to add them to the dict
        some_str = some_str.replace(" ", "")
        # also remove all special characters from the string + remove integers
        # I do this by calling my own function
        some_str = remove_specials(some_str)
        # make all letters lowercase 
        some_str = some_str.lower()
        # now iterate over all chars in the input string
        for char in some_str:
            # check if char is already a key in dictionairy
            if char in letter_dict:
                # get value associated with key
                temp_value = letter_dict.get(char)
                temp_value = temp_value + 1 # update the value, because one more occurence
                # update the dict
                letter_dict[char] = temp_value
            else:
                # add char as key to dict
                letter_dict[char] = 1
        
        return letter_dict
    
    else:
        return 'TypeError: input is not a string'
    
    

def remove_specials(in_str):
    special_list = [',', '.', '?', '!', '"', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_string = ""
    for c in in_str:
        if c in special_list:
            c = c.replace(c, '')
            new_string += c
        else:
            new_string += c
    return new_string

#print(remove_specials('Hello!?.,')) # input to test if remove_specials works
print(count_letter("I am a boy, and you?"))
#print(count_letter(234)) # input to test that function will throw error with non-string input
