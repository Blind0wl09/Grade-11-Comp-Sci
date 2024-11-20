import csv, os, sys, random, time, textwrap
# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor

underline = '\033[4m'
reset = '\033[0m'

def type(text):  # function to animate text with delay parameter
    for char in text: #for loops  through each character in the text
        print(char, end='', flush=True) #flush prints out the character immediately
        time.sleep(0.002)  # delays the print of each letter by the assigned delay value
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PRINT MENU - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def printMenu():
    clear_screen()
    menu_text = textwrap.dedent(f"""
    {underline}Customer and Sales System{reset}
                                
    1. Enter Customer Information
    2. Generate Customer data file
    3. Report on total Sales (Not done in this part)
    4. Check for fraud in sales data (Not done in this part)
    9. Quit
    Enter menu option (1-9)
    """)
    type(menu_text)
    
    userInput = print('> ', end='')
    return userInput
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - enterCustomerInfo- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def enterCustomerInfo():
    clear_screen()
    type("Input your first name")                           #AASSES FOR FIRST NAMES
    user_fname = input("> ")
    while user_fname== "":
        clear_screen()
        print("Please enter a valid first name")
        type("Input your first name")                  
        user_fname = input("> ")
    else:
        pass

    clear_screen()
    type("Input your last name")                            #ASKS FOR LAST NAME
    user_lname = input("> ")
    while user_lname == "":
        clear_screen()
        print("Please enter a valid last name")
        type("Input your last name")               
        user_lname = input("> ")
    else:
        pass

    clear_screen()
    type("Please enter the city you reside in")             #ASKS FOR CITY
    user_city = input("> ")
    while user_city == "":
        clear_screen()
        print("Please enter a valid city")
        type("Please enter the city you reside in") 
        user_city = input("> ")
    else:
        pass

    clear_screen()
    type("Please enter your postal code")                   #ASKS FOR POSTAL CODE
    while True:
        user_postal = input("> ")
        if not user_postal:  # Check for empty input
            clear_screen()
            print("Please enter a valid postal code")
            continue
        if validatePostalCode(user_postal):  # Validate the postal code
            type("Postal code is valid! Proceeding...")
            break
        
            
        

    clear_screen()
    type("Please input your credit card number")            #ASKS FOR CREDIT CARD
    user_credit = int(input("> "))
    while user_credit == "":
        print("Please enter a valid credit card number")
    else:
        pass
    clear_screen()
    return user_fname, user_lname, user_city, user_postal, user_credit

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This functi may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validatePostalCode - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def read_postalcode(user_postal):

    with open('postal_codes.csv', mode='r', encoding='ISO-8859-1', newline='') as file:     #Reads list of postal codes
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            print(row)
            if row[0] == user_postal:
                return True
                    
        return False  


def validatePostalCode(user_postal):
    if len(user_postal) == 3 and read_postalcode(user_postal): #Checks if user given postal is in proper format
        return True
    else:
        print("Invalid postal code")
        return False
    
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validateCreditCard - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def validateCreditCard():
    '''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - generateCustomerDataFile - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def generateCustomerDataFile():
    pass    # Remove this pass statement and add your own code below

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        customer_data = enterCustomerInfo()
        print("Customer info", customer_data)

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")
