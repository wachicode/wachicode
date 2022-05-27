import sys
import os


class Pet(object):  # class for pet details
    def __init__(self, petID, species, gender, name, price):  # constructor
        # data members
        self.petID = petID
        self.species = species
        self.gender = gender
        self.name = name
        self.price = price

    # method to display pet details
    def getDetails(self):
        print(
            "\n pet [" + self.petID + "] : name: " + self.name + " - " + self.species + " - " + self.gender + " -- [ " + self.price + " ]")


class PetInfo(Pet):  # inheritance
    def __init__(self, petID, species, gender, name, price, breed, age):
        self.breed = breed
        self.age = age
        Pet.__init__(self, petID, species, gender, name, price)

    def getCost(self):
        print(
            "\n -- price: [ " + self.price + " ]" + "\n NAME: " + self.name + "\n BREED: " + self.breed + "\n GENDER: " + self.gender + "\n AGE: " + self.age)


# creating object of a class
pet1 = PetInfo('001', 'dog', 'male', 'tomas', 'Php1000', 'askal', '2-years & 3-months')
pet2 = PetInfo('002', 'dog', 'male', 'mochi', 'Php1000', 'askal', '1-year & 8-months')
pet3 = PetInfo('003', 'cat', 'male', 'kofi', 'Php700', 'puspin', '9-months')
pet4 = PetInfo('004', 'cat', 'female', 'fury', 'Php350', 'puspin', '4-months')


class Shelter(object):
    def __init__(self, shelterID, name):
        self.shelterID = shelterID
        self.name = name

    def getShelter(self):
        print("\n -> " + self.name + " [ " + self.shelterID + " ] ")


class Details(Shelter):
    def __init__(self, shelterID, name, contact, location):
        self.contact = contact
        self.location = location
        Shelter.__init__(self, shelterID, name)

    def getDetails(self):
        print(" LOCATION: " + self.location +
              "\n CONTACT: " + self.contact)


s1 = Details('CV09PES02', 'Bamtori Animal Shelter', '09913200103', 'Poblacion, Mabini, Batangas')
s2 = Details('BC02VON05', 'Rage Animal Shelter', '09902200511', 'Mabini, Batangas')


def clear():  # clear the console
    command = 'cls'
    if os.name != 'nt':
        command = 'clear'
    os.system(command)
    return 0


def main(): # menu()
    menu()


def display(): # display title
    print("\n       || Tubatu's Pet Adoption ||")


def menu(): # register & log in
    display()
    choice = input("""
    1: REGISTER 
    2: LOGIN (if already have an account)

    choice: """)
    clear()

    if choice == '1':
        register()
    elif choice == '2':
        login1()
    else:
        print("\n X: Please Try Again!")
        menu()


fname = []
lname = []
contact = []
houseno = []
brgy = []
town = []
city = []
email = []
uname = []
pword = []


def register(): # use append() for the list of items
    display()
    print("\n---> REGISTER\n")
    fname.append(input(' first name: '))
    lname.append(input(' last name: '))
    contact.append(input(' contact number: '))
    uname.append(input(' username: '))
    pword.append(input(' password: '))
    clear()
    print("\n-- you can now log in your account")
    login1()


def login1(): # if the user already have registered
    display()
    print("\n---> LOG IN\n")
    username = input(' username: ')
    password = input(' password: ')
    clear()
    if username in uname and password in pword:
        homepage()
    else:
        print("\n X: Incorrect! Please Try Again!")
        login2()


def login2(): # if the user choose to log in but not registered
    display()
    print("\n---> LOG IN\n")
    username = input(' username: ')
    password = input(' password: ')
    clear()
    if username in uname and password in pword:
        homepage()
    else:
        print("\n X: Account Not Found! Please Register!")
        register()


def homepage(): # homepage of the program
    display()
    print("\n---> HOMEPAGE")
    choice = input("""
    1: VIEW PET DETAILS
    2: VIEW ACCOUNT PROFILE
    3: LOG OUT

  	choice: """)
    clear()

    if choice == '1':
        viewpet()
    elif choice == '2':
        viewacc()
    elif choice == '3':
        logout()
    else:
        print("\n X: Please Try Again!")
        homepage()


def viewpet(): # display pet details & shelter details from class methods
    display()
    print("\n---> PET FEED")
    petfeed()
    choice = input("\n view petID: ")
    clear()

    if choice == '001':
        display(), pet1.getDetails(), pet1.getCost(), s1.getShelter(), s1.getDetails(), confirm()
    elif choice == '002':
        display(), pet2.getDetails(), pet2.getCost(), s2.getShelter(), s2.getDetails(), confirm()
    elif choice == '003':
        display(), pet3.getDetails(), pet3.getCost(), s1.getShelter(), s1.getDetails(), confirm()
    elif choice == '004':
        display(), pet4.getDetails(), pet4.getCost(), s2.getShelter(), s2.getDetails(), confirm()
    else:
        print("\n X: Wrong petID! Please Try Again!")
        viewpet()


def petfeed(): # calling the public method of class
    pet1.getDetails()
    pet2.getDetails()
    pet3.getDetails()
    pet4.getDetails()


def confirm(): # asking the user if they are going to adopt the viewed pet
    display()
    choice = input("""
  [ are you going to adopt the pet? ]

  1: ADOPT
  2: BACK
  3: HOMEPAGE

  choice: """)
    clear()

    if choice == '1':
        adopt()
    elif choice == '2':
        viewpet()
    elif choice == '3':
        homepage()
    else:
        print("\n X: Please Try Again!")
        confirm()


def adopt(): # if adopt, user fill in and confirm the details for the adoption process
    display()
    print("\n---> ADOPTION PROCESS")
    print("\n [ please set an address for the delivery ]\n")
    houseno.append(input(' address | house/bldg no.: '))
    brgy.append(input(' address | sitio/barangay: '))
    town.append(input(' address| municipality: '))
    city.append(input(' address | city: '))
    email.append(input(' e-mail: '))
    print("\n [ please confirm details below ]\n")
    print("- name: ", fname, lname)
    print("- contact  number: ", contact)
    print("- address:", houseno, brgy, town, city)
    print("- e-mail: ", email)

    choice = input("""
  1: CONFIRM ADOPT
  2: BACK

  choice: """)
    clear()

    if choice == '1':
        deliver()
    elif choice == '2':
        confirm()
    else:
        print("\n X: Please Try Again!")
        adopt()


def deliver(): # if the user confirm adoption, message
    display()
    print("\n---> ADOPTION CONFIRMED <3")
    print("\n Thank you so much", fname, ", for adopting our pet!")
    print(" Our pet will be at your HOME soon, please take CARE of it!")
    print(" We will send an e-mail at", email, "for more details!")
    print("\n---> lots of furrlove from TUBATU PET ADOPTION! THANK YOU!")

    choice = input("""
  1: BACK HOMEPAGE
  2: CANCEL ADOPT
  3: LOG OUT

  choice: """)
    clear()

    if choice == '1':
        homepage()
    elif choice == '2':
        cancel()
    elif choice == '3':
        logout()
    else:
        print("\n X: Please Try Again!")
        deliver()


def cancel(): # if the user cancel the adoption, message
    display()
    print("\n---> ADOPTION CANCELED </3")
    print("\n Hello,", fname, "!")
    print(" We will process the cancellation of adoption!")
    print(" We will send an e-mail at", email, "for more details!")
    print("\n---> lots of furrlove from TUBATU PET ADOPTION! THANK YOU!")

    choice = input("""
  1: BACK HOMEPAGE
  2: LOG OUT

  choice: """)
    clear()

    if choice == '1':
        homepage()
    elif choice == '2':
        logout()
    else:
        print("\n X: Please Try Again!")
        cancel()


def viewacc(): # display account profile information from append()
    display()
    print("\n---> PROFILE")
    print("\n name: ", fname, lname)
    print(" contact:  ", contact)
    print(" username:", uname)
    print(" password: ", pword)

    choice = input("""
  1: BACK HOMEPAGE
  2: LOG OUT

  choice: """)
    clear()

    if choice == '1':
        homepage()
    elif choice == '2':
        logout()
    else:
        print("\n X: Please Try Again!")
        viewacc()


def logout(): # log out
    print("\n---> ACCOUNT LOGGED OUT")


main()