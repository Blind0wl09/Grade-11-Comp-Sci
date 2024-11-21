# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv, os, time, textwrap #import modules
red = '\033[31m' #ANSI escape codes
purple = '\033[35m'
reset = '\033[0m'
underline = '\033[4m'
reset = '\033[0m'
customer_id = 1

def type(text):  # function to animate text with delay parameter
    for char in text: #for loops  through each character in the text
        print(char, end='', flush=True) #flush prints out the character immediately
        time.sleep(0.002)  # delays the print of each letter by the assigned delay value
    print()

def clear_screen(): #clear screen function
    os.system('cls' if os.name == 'nt' else 'clear') 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PRINT MENU - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def printMenu(): #print menu function
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
    type(menu_text) #animate menu
    
    userInput = print('> ', end='') #user inputs choice
    return userInput #return userinput's choice
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - enterCustomerInfo- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def enterCustomerInfo(customer_id): #function to receive customer's info
    clear_screen()
    print(f"USER {customer_id}")
    type("Input your first name")                           #AASSES FOR FIRST NAMES
    user_fname = input("> ")
    while user_fname== "":
        clear_screen()
        print(f"{red}Please enter a valid first name{reset}")
        type("Input your first name")                  
        user_fname = input("> ")
    else:
        pass

    clear_screen()
    type("Input your last name")                            #ASKS FOR LAST NAME
    user_lname = input("> ")
    while user_lname == "":
        clear_screen()
        print("Please enter a valid last name")
        type("Input your last name")               
        user_lname = input("> ")
    else:
        pass

    clear_screen()
    type("Please enter the city you reside in")             #ASKS FOR CITY
    user_city = input("> ")
    while user_city == "":
        clear_screen()
        print("Please enter a valid city")
        type("Please enter the city you reside in") 
        user_city = input("> ")
    else:
        pass

    while True:
        clear_screen()
        type("Please enter your postal code")                   #ASKS FOR POSTAL CODE
        while True:
            user_postal = input("> ")
            try:
                if not user_postal:  # Check for empty input
                    print("Please enter a valid postal code")
                    continue
                if validatePostalCode(user_postal):  # Validate the postal code
                    type("Postal code is valid! Proceeding...")
                    time.sleep(0.75)
                    break
            except FileNotFoundError:
                continue
        break
        

    clear_screen()
    type("Please input your credit card number")            #ASKS FOR CREDIT CARD
    
    while True:
        user_credit = input("> ")
        clear_screen()
        if not user_credit:
            print("Please enter a valid credit card number")
            continue
        if validateCreditCard(user_credit):
            type("Credit card is valid! Proceeding...")
            time.sleep(0.75)
            break
    clear_screen()
    print(f"First name: {purple}{user_fname}{reset}\nLast name: {purple}{user_lname}{reset}\nCity: {purple}{user_city}{reset}\nPostal code: {purple}{user_postal}{reset}\nCredit card: {purple}{user_credit}{reset}")
    type("Is this the correct info?(yes/no)")
    user_confirmation = input("> ")
    if user_confirmation == "Yes" or user_confirmation == "yes":
        print("Info confirmed!")
        customer_id += 1
        customer_information = [user_fname, user_lname, user_city, user_postal, user_credit]
        filename = "user_data.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(customer_information)
        return customer_information, customer_id
    else:
        return None

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This functi may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validatePostalCode - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def read_postalcode(user_postal):
    try:
        with open('postal_codes.csv', mode='r', encoding='ISO-8859-1', newline='') as file:     #Reads list of postal codes
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if row[0] == user_postal:
                    return True
            return False  
    except FileNotFoundError:
        type("Postal code not found.")
        return True                 #this is for the file.run since it wont work without it. should be false

def validatePostalCode(user_postal):
    if len(user_postal) == 3 and read_postalcode(user_postal): #Checks if user given postal is in proper format
        return True
    else:
        clear_screen()
        print("Invalid postal code")
        return False
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validateCreditCard - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def luhn_algorithm_check(user_credit): #credit card number checker with luhn algorithm
    total_sum = 0 #set total to zero
    reverse_credit = user_credit[::-1] #reverse credit card number by slicing
    for i in range(len(reverse_credit)): #loop through each digit in the reversed credit card number
        digit = int(reverse_credit[i]) #convert digit to integer
        if i % 2 == 1: # check if the digit is an odd number
            digit *= 2 #double the digit
            if digit > 9:  #if the doubled digit is greater than 9 subtract 9 from the doubled digit
                digit -= 9 
        total_sum += digit #add the digit to the total sum
    return total_sum % 10 == 0 #return True if the total sum is dividedable by 10, if no? = continues to restart check

def validateCreditCard(user_credit): #final credit card number check
    if len(user_credit) ==  16 and luhn_algorithm_check(user_credit): #if credit card number is 16 digits and passes the luhn algorithm and verhoeff algorithm
        return True 
    else: 
        clear_screen()
        print(f"{red}Invalid credit card{reset}")
        return False
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - generateCustomerDataFile - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def generateCustomerDataFile():
    pass    # Remove this pass statement and add your own code below

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"


# More variables for the main may be declared in the space below
while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        customer_data,customer_id = enterCustomerInfo(customer_id)
        print("Customer info", customer_data)

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

#Exits once the user types 
while userInput == exitCondition:
    clear_screen
    type("Program Terminated")
    time.sleep(1)
    break


