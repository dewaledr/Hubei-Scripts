def palidrome(str):
    str = str.replace(' ','') #This will replace all spaces with no space
                              # Fixes issues with strings that have spaces +
                              # without using regular expression to do it.
    # Will return True if str == str[::-1]
    print(f"{str} - {str[::-1]}")
    return str == str[::-1]

# Check it out
print(palidrome('nurses run'))
print(palidrome('abcba'))
print(palidrome('rhetoric'))