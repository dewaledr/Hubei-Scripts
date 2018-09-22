
# #1 Version without Input Error checking
''' 
print()
response = int(input("Please Enter a number: "))

outsideVal = 1
while outsideVal <= response:
    insideVal = 1
    while insideVal <= response:
        print(f"{insideVal*outsideVal:4}", end='')
        insideVal += 1
    print()
    outsideVal += 1 
'''
# #2 Version with Input Error checking
''' while True:
    try:
        response = int(input("Please Enter a number: "))
    except:
        continue
    else:
        outsideVal = 1
        while outsideVal <= response:
            insideVal = 1
            while insideVal <= response:
                print(f"{insideVal*outsideVal:4}", end='')
                insideVal += 1
            print()
            outsideVal += 1
        break  '''

# #3 Version with Input Error checking and input arguments from command line...
import sys
import os

def genMUX(num): 
    """
    DOCSTRING:  This Function produces a square multiplication Table, taking input from command line
    Input:      int
    Output:     Square multiplication table of input argument
    """
    print()
    outsideVal = 1
    while outsideVal <= num:
        insideVal = 1
        while insideVal <= num:
            print(f"{insideVal*outsideVal:4}", end='')
            insideVal += 1
        print()
        outsideVal += 1 
    print("Exiting program...")


if __name__ == '__main__':
    os.system("clear")
    # Terminate the program if input arg is not an integer
    print(f"Number of arguments = {len(sys.argv)}")
    while True:
        try:
            if len(sys.argv) == 2:    # If there was argv[1]. argv[0] is name of pgm
                inputArg = int(sys.argv[1])
            else:
                print("Incorrect number of argument supplied. Please try again...")
                break
        except:
            #if len(sys.argv) == 2:    # If there was argv[1]. argv[0] is name of pgm
            print(f"Input argument was: {sys.argv[1]}")
            print("..............")
            print("\tPlease try again. Ensure that the input argument is an integer...")
            print("..............")
            #else:
            #    print("No input argument supplied. Please try again...")
            #    break
        else:
            # Success... Correct int arg supplied during pgm instantiation
            #if type(sys.argv[1]) == int:
            print(f"Generating {sys.argv[1]} x {sys.argv[1]} TABLE...")
            genMUX(inputArg)
        break

    
