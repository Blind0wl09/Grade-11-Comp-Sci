# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

import csv, os, time, textwrap, random, pygame  # import modules

#Ansi escape codes
red = '\033[31m'         # Red text color
purple = '\033[35m'      # Purple text color
bright_green = '\033[92m'  # Bright green text color
underline = '\033[4m'     # Underline text color
reset = '\033[0m'        # Reset color (to default)

pygame.mixer.init()


def music_play():
    pygame.mixer.music.load("fnaf pizz theme.mp3") 
    pygame.mixer.music.play(-1, 0.0)  

def music_stop():
    pygame.mixer.music.stop()

R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)

TEXT_COLOR = f"\x1b[38;2;{R};{G};{B}m"  


customer_id = 0

def type(text): 
    for char in text: 
        print(char, end='', flush=True) 
        time.sleep(0.009) 
    print()

def new_line():
    print("\n")

def clear_screen(): 
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
    filename = "data.csv"
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')  
            for row in reader:
                pass
            customer_id =  int(row[0]) + 1
    except:
            customer_id = 1
            
    print(f"{TEXT_COLOR}USER {reset}{customer_id}")
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
                if not user_postal:                    
                    print(f"{red}Please enter a valid postal code{reset}")
                    continue
                if validatePostalCode(user_postal): 
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
    while True: 
        while user_confirmation != "Yes" or"yes" or "No" or "no":
            type(f"{red}INVALID{reset}")
            user_confirmation = input("> ")
            if user_confirmation == "Yes" or "yes":
                print("Info confirmed!")
                customer_information = [customer_id, user_fname, user_lname, user_city, user_postal, user_credit]
                filename = "data.csv"
                with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter='|')  
                    csvwriter.writerow(customer_information)
                return customer_information, customer_id
            elif user_confirmation == "No" or "no":
                return None
            
        

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - validatePostalCode - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def read_postalcode(user_postal):
    try:
        with open('postal_codes.csv', 'r', encoding= 'iso-8859-1', newline='') as file:
            reader = csv.reader(file, delimiter='|') 
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
    
    found = False
    filename = "data.csv"
    
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')  
            for row in reader:
                if not row or len(row) < 6:
                    continue
                
                print(f"Comparing: {row[0]} with {generate_search_user}")
                
                if str(row[0]).strip() == str(generate_search_user).strip():
                    clear_screen()
                    print(f"User: {purple}{row[0]}{reset}")
                    print(f"First name: {purple}{row[1]}{reset}")
                    print(f"Last name: {purple}{row[2]}{reset}")
                    print(f"City: {purple}{row[3]}{reset}")
                    print(f"Postal code: {purple}{row[4]}{reset}")
                    print(f"Credit card: {purple}{row[5]}{reset}")
                    found = True
                    print("Is this the right user? (yes/no)")
                    user_confirmation = input("> ")
                    if user_confirmation == "yes":
                        break
                    else:
                        continue
        
        if not found:
            print(f"User with number {generate_search_user} not found.")
            time.sleep(1)
    
    except FileNotFoundError:
        print(f"{red}Data file not found{reset}")
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
        try:
            customer_data,customer_id = enterCustomerInfo(customer_id)
            print("Customer info", customer_data)
        except:
            pass

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
