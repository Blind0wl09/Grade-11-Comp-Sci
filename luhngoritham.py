# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

import csv, os, time, textwrap, random, pygame  # import modules

# Define the color escape codes
red = '\033[31m'         # Red text color
purple = '\033[35m'      # Purple text color
bright_green = '\033[92m'  # Bright green text color
underline = '\033[4m'     # Underline text color
reset = '\033[0m'        # Reset color (to default)

pygame.mixer.init()

# Load and play the MP3 file
def music_play():
    pygame.mixer.music.load("fnaf pizz theme.mp3")  # Make sure the file name matches
    pygame.mixer.music.play(-1, 0.0)  # 

def music_stop():
    pygame.mixer.music.stop()

# Generate random RGB values for text color
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)

# Create random text color escape sequence
TEXT_COLOR = f"\x1b[38;2;{R};{G};{B}m"  # Random text color (RGB)
BG_COLOR = f"\x1b[48;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m"  # Random background color

# Customer ID initialization
customer_id = 0

def type(text):  # function to animate text with delay parameter
    for char in text: 
        print(char, end='', flush=True) 
        time.sleep(0.009) 
    print()

def new_line():
    print("\n")

def clear_screen(): #clear screen function
    os.system('cls' if os.name == 'nt' else 'clear') 

music_stop()
clear_screen()
type(f"{red}Warning! Background music is present in this program!{reset}")
time.sleep(1.5)
clear_screen()
while True:
    type("Would you like to mute the background music? (yes/no)")
    mute = input("> ")
    
    if mute == "yes" or mute == "Yes":
        music_stop()
        break
    elif mute == "no" or mute == "No":
        music_play()
        break
    else:
        clear_screen()
        type(f"{red}Invalid input. Please enter 'yes' or 'no'.{reset}")
        time.sleep(1)
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
    type(menu_text.strip()) #animate menu

    new_line()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - enterCustomerInfo- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def enterCustomerInfo(customer_id): #function to receive customer's info
    clear_screen()
    print(f"{TEXT_COLOR}USER{reset} {customer_id + 1}")
    type("Input your first name")                           #ASKS FOR FIRST NAMES
    user_fname = input("> ")
    while user_fname== "":
        clear_screen()
        print(f"{red}Please enter a valid first name{reset}")
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

    while True:
        clear_screen()
        type("Please enter your postal code")               #ASKS FOR POSTAL CODE
        while True:
            user_postal = input("> ")
            try:
                if not user_postal:                     # Check for empty input
                    print(f"{red}Please enter a valid postal code{reset}")
                    continue
                if validatePostalCode(user_postal):      # Validate the postal code
                    type(f"{bright_green}Postal code is valid! Proceeding...{reset}")
                    time.sleep(0.75)
                    break
            except FileNotFoundError:
                continue
        break
        

    clear_screen()
    type("Please input your credit card number")            #ASKS FOR CREDIT CARD
    
    while True:
        user_credit = input("> ")
        clear_screen()
        if not user_credit:
            print(f"{red}Please enter a valid credit card number{reset}")
            continue
        if validateCreditCard(user_credit):
            type(f"{bright_green}Credit card is valid! Proceeding...{reset}")
            time.sleep(0.75)
            break
    clear_screen()
    print(f"First name: {purple}{user_fname}{reset}\nLast name: {purple}{user_lname}{reset}\nCity: {purple}{user_city}{reset}\nPostal code: {purple}{user_postal}{reset}\nCredit card: {purple}{user_credit}{reset}")
    type("Is this the correct info?(yes/no)")
    user_confirmation = input("> ")
    if user_confirmation == "Yes" or user_confirmation == "yes":
        print("Info confirmed!")
        customer_id += 1
        customer_information = [customer_id, user_fname, user_lname, user_city, user_postal, user_credit]
        filename = "data.csv"
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter='|')  
            csvwriter.writerow(customer_information)
        return customer_information, customer_id
    else:
        return None
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validatePostalCode - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def read_postalcode(user_postal):
    try:
        with open('postal_codes.csv', 'r', encoding= 'iso-8859-1', newline='') as file:
            reader = csv.reader(file, delimiter='|')  # Use '|' as delimiter
            for row in reader:
                if row and row[0] == user_postal:
                    return True
        return False
    except FileNotFoundError:
        print(f"{red}Postal code database file not found{reset}")
        return False

def validatePostalCode(user_postal):
    if not user_postal:
        clear_screen()
        print(f"{red}Postal code cannot be empty{reset}")
        return False
    
    if read_postalcode(user_postal):
        return True
    else:
        clear_screen()
        print(f"{red}Invalid postal code. Please ensure it's a valid postal code in the database.{reset}")
        return False
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validateCreditCard - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def luhn_algorithm_check(user_credit): #credit card number checker with luhn algorithm
    total_sum = 0 
    reverse_credit = user_credit[::-1] 
    for i in range(len(reverse_credit)): 
        digit = int(reverse_credit[i])
        if i % 2 == 1: 
            digit *= 2 
            if digit > 9: 
                digit -= 9 
        total_sum += digit 
    return total_sum % 10 == 0 

def validateCreditCard(user_credit):
    if len(user_credit) ==  16 and luhn_algorithm_check(user_credit): 
        return True 
    else: 
        clear_screen()
        print(f"{red}Invalid credit card{reset}")
        return False
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - generateCustomerDataFile - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def generateCustomerDataFile():
    clear_screen()
    print("Please enter the user number you wish to view (Input 'return' to exit).")
    generate_search_user = input("> ")

    if generate_search_user == 'return':
        printMenu()
        return

    filename = "data.csv"      # CSV file only opens through EXCEL and won't work. 
    found = False

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Skip empty rows or rows with insufficient columns
            if not row or len(row) < 1:
                continue
            
            # If the user number matches, print their data
            if row[0] == generate_search_user:  # Assuming the user number is in the first column
                clear_screen()
                print(f"User: {purple}{row[0]}{reset}")
                print(f"First name: {purple}{row[1]}{reset}")
                print(f"Last name: {purple}{row[2]}{reset}")
                print(f"City: {purple}{row[3]}{reset}")
                print(f"Postal code: {purple}{row[4]}{reset}")
                print(f"Credit card: {purple}{row[5]}{reset}")
                found = True
                input("> ")
                break
    
    if not found:
        print(f"User with number {generate_search_user} not found.")
        time.sleep(1)

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
    userInput = input("> ");        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        customer_data,customer_id = enterCustomerInfo(customer_id)
        print("Customer info", customer_data)

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

#Exits once the user types 
if userInput == exitCondition:
    clear_screen()
    type("Program Terminated")
    time.sleep(1)
    music_stop()
    clear_screen()
    file =  "data.csv"
    with open(file, 'w'):   #writes nothing and deletes all information when closed
        pass
