'''
READ ME:
- This module contains the following functions: `help`, `export`, `closest_to`, `coordinates`, `lookup`, `enter`, `remove`, `alreadyEntered`, `entryCheck`, `sugestName`, `listAll`, `distance`, `main`.
- This module imports the `shelve` and `Haversine_Formula` modules.

DESCRIPTION:
- This is a phonebook application that allows users to add, remove, lookup, and list all contacts. It also calculates the distance between two contacts and finds the contact closest to a given contact.

PARAMETERS:
- Most functions take 'name' as a parameter, which is a string representing the name of a contact.
- The `enter` function also takes 'number' and 'city' as parameters, which are the phone number and city of the contact, respectively.
- The `distance` function takes 'contact1' and 'contact2' as parameters, which are the names of two contacts.

LIMITATIONS:
- The application assumes that the name of each contact is unique.
- The application does not validate the format of the phone number.
- The application only works with cities that are listed in the 'worldcities.txt' file.
- The application does not handle errors that may occur when opening or closing the 'phonebook' or 'worldcities.txt' files.

STRUCTURES:
- The application uses a while-loop in the `main` function to continuously accept user input until the user decides to quit.
- The application uses if-elif-else constructs to determine which function to call based on the user's input.
- The application uses for-loops in the `closest_to`, `coordinates`, `sugestName`, and `listAll` functions to iterate over the contacts in the phonebook.

OUTPUTS:
- The application uses print-statements to display information to the user, such as the list of contacts, the details of a contact, and the distance between two contacts.
- The application uses a return-statement in the `coordinates` function to return the coordinates of a city.
'''

import shelve
import Haversine_Formula


phonebook = shelve.open("phonebook")


def help():
    print("Overview of available commands:\n- `add/enter`:     Add a new contact to the phonebook.\n- `lookup/search`: Look up a contact by name.\n- `remove/delete`: Remove a contact from the phonebook.\n- `list all`:      List all contacts in the phonebook.\n- `distance`:      Calculate the distance between two contacts.\n- `closest`:       Find the contact closest to a given contact.\n- `quit/exit`:     Exit the phonebook application.\n- `help`:          Display this help message.")


def export():
    return


def closest_to(name):
    min_distance = 1000000000
    for key in phonebook:
        if name != key and distance(name, key) < min_distance:
            min_distance = distance(name, key)
            closest_contact = key
    print(f"The closest contact to {name} is {closest_contact} with a distance of {min_distance} km.")


def coordinates(city):
    city_file = open("worldcities.txt", "r")
    for line in city_file:
        data = line.split(",")
        if city == data[0]:
            return (float(data[1]), float(data[2]))
    return False
    city_file.close()


def lookup(name):
    print(f"Phonenumber: {phonebook[name][0]}")
    print(f"City:        {phonebook[name][1]}", end=" ")
    print(coordinates(phonebook[name][1]))


def enter(name, number, city):
    phonebook[name] = (number, city)
    print(f"Contact added.")


def remove(name):
    print(f"Contact '{name}' with phonenumber {phonebook[name]} has been removed from the phonebook.")
    del phonebook[name]


def alreadyEntered(name):
    if name in phonebook:
        print(f"The contact '{name}' does already exists with the phonenumber '{phonebook[name]}', do you what to override?")
        userInput = input("[Y]es/[N]o: ")
        if userInput == 'Y':
            result = True
        elif userInput == 'N':
            print("Contact not overwritten. Input canceled.")
            result = False
        else:
            raise ValueError("Invalid input. Please enter 'Y' or 'N'.")
    else:
        result = True
    
    return result


def entryCheck(name):
    if name not in phonebook:
        sugestName(name)
        print(f"The contact '{name}' could not been found.")
        print(f"Did you mean:\n{sugestName(name)}")
        result = False
    else:
        result = True
    return result


def sugestName(name):
    similarNames = []
    for key in phonebook.keys():
        if name.lower() in key.lower():
            similarNames.append(key)
        if len(similarNames) == 5:
            break
    if len(similarNames) == 0:
        return "No suggested entries."
    return '\n'.join(similarNames)


def listAll():
    for key, value in phonebook.items():
        print(f"{key}: {value}")


def distance(contact1, contact2):
    lat1, lon1 = coordinates(phonebook[contact1][1])
    lat2, lon2 = coordinates(phonebook[contact2][1])
    rad = (3.14159265359/180)
    distance = Haversine_Formula.haversine(lat1*rad, lon1*rad, lat2*rad, lon2*rad)*6371
    return distance


def main():
    while True:
        primary_input = input("> ").strip()

        if primary_input == "help":
            help()

        elif primary_input == "lookup" or primary_input == "search":
            name = input("Name: ")
            if entryCheck(name):
                lookup(name)

        elif primary_input == "enter" or primary_input == "add":
            name = input("Name: ")
            if alreadyEntered(name):
                number = input("Number: ")
                city = input("City: ")
                while not coordinates(city):
                    print("Invalid city name. Please reenter.")
                    city = input("City: ")
                enter(name, number, city)

        elif primary_input == "remove" or primary_input == "delete":
            name = input("Name to remove: ")
            if entryCheck(name):
                remove(name)

        elif primary_input == "quit" or primary_input == "exit":
            print("bye\n")
            phonebook.close()
            exit()

        elif primary_input == "list all":
            listAll()

        elif primary_input == "distance":
            contact1 = input("Name of contact 1: ")
            contact2 = input("Name of contact 2: ")
            if not entryCheck(contact1) or not entryCheck(contact2):
                print ("ERROR, one or both of the contacts could not be found.")
            print(f"The distance between {contact1} and {contact2} is {distance(contact1, contact2)} km.")
            
        
        elif primary_input == "closest":
            name = input("Name to search surroundings: ")
            if entryCheck(name):
                closest_to(name)

        else:
            print("ERROR, comand not recognized. Showing Help instead:")
            help()

        print("")

main()