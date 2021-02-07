from bs4 import BeautifulSoup
import sqlite3
# TODO: Parse mask price

# TODO: Send email alerts to users

# TODO: Database for daily checker
CONNECTION = sqlite3.connect('emp.sqlite3')
cur = CONNECTION.cursor()
cur.execute('DROP TABLE IF EXISTS Employees')
cur.execute('CREATE TABLE Employees(LastName TEXT, FirstName TEXT, CloseContact TEXT, Symptoms TEXT, COVIDTest TEXT)')
def employeeCheckIn():
    print("EMPLOYEE CHECK-IN")
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    print("Have you been in close contact with someone experiencing COVID symptoms or that has tested positive for COVID? Enter '1' for 'YES' or '2' for 'NO'.")
    while True:
        closeContact = input("Please enter the following number (1 or 2) indicating the scenario that applies to you: ")
        if closeContact == "1":
            closeContact = "YES"
            break;
        elif closeContact == "2":
            closeContact = "NO"
            break;
        else:
            print("Sorry, that is not a valid input. Please enter either '1' or '2'.")
            continue
    print("Have you recently experienced symptoms of COVID including, but not limited to coughing, fever or chills, and shortness of breath? Enter '1' for 'YES' or '2' for 'NO'.")
    while True:
        covidSymptoms = input("Please enter the following number (1 or 2) indicating the scenario that applies to you: ")
        if covidSymptoms == "1":
            covidSymptoms = "YES"
            break;
        elif covidSymptoms == "2":
            covidSymptoms = "NO"
            break;
        else:
            print("Sorry, that is not a valid input. Please enter either '1' or '2'.")
            continue
    print("Have you recently tested positive for COVID? Enter '1' for 'YES' or '2' for 'NO'.")
    while True:
        covidTest = input("Please enter the following number (1 or 2) indicating the scenario that applies to you: ")
        if covidTest == "1":
            covidTest = "YES"
            break;
        elif covidTest == "2":
            covidTest = "NO"
            break;
        else:
            print("Sorry, that is not a valid input. Please enter either '1' or '2'.")
            continue
        cur.execute("INSERT INTO Employees(LastName, FirstName, CloseContact, Symptoms, COVIDTest) VALUES (?, ?, ?, ?, ?)", (lName, fName, closeContact, covidSymptoms, covidTest))  
def employeeLookUp():
    
def showMenu():
    selection = ""
    while selection != "3":
        print("\n" + ('*' * 25) + "MENU" + ('*' * 25))
        print("1 - Employee check-in")
        print("2 - Search for employees that may introduce a risk for COVID")
        print("3 - Quit")
        selection = input("Please enter a menu number: ")
        if selection == "1":
            employeeCheckIn()
        elif selection == "2":
            employeeLookUp()
        elif selection == "3":
            break;
        else:
            print("That is not a valid option.")
showMenu()
# TODO: Vaccine status of employees

# TODO: Scrape for general COVID data in the country
