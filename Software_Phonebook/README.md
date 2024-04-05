# Phonebook Software

This software is a simple, command-line based phonebook application. It allows you to add, remove, lookup, and list all contacts. Additionally, it can calculate the distance between two contacts and find the contact closest to a given contact.

## How it Works

The software uses a Python module called `shelve` to store and retrieve contact information. The contact's name is used as the key, and a dictionary containing the contact's phone number and city is stored as the value.

The software also uses a module called `Haversine_Formula` to calculate the distance between two contacts. This calculation is based on the coordinates of the cities where the contacts are located.

## How to Interact

Interaction with the software is done through a command-line interface. After starting the software, you will be prompted to enter a command. The following commands are available:

- `add` or `enter`: Add a new contact to the phonebook. You will be prompted to enter the contact's name, phone number, and city.
- `lookup` or `search`: Look up a contact by name. You will be prompted to enter the name of the contact.
- `remove` or `delete`: Remove a contact from the phonebook. You will be prompted to enter the name of the contact.
- `list all`: List all contacts in the phonebook.
- `distance`: Calculate the distance between two contacts. You will be prompted to enter the names of the two contacts.
- `closest`: Find the contact closest to a given contact. You will be prompted to enter the name of the contact.
- `quit` or `exit`: Exit the phonebook application.
- `help`: Display a help message with an overview of the available commands.

## Limitations

- The software assumes that the name of each contact is unique.
- The software does not validate the format of the phone number.
- The software only works with cities that are listed in the 'worldcities.txt' file.
- The software does not handle errors that may occur when opening or closing the 'phonebook' or 'worldcities.txt' files.

## Getting Started

1. Click on the green `Code` button on the top right of the repository page.

2. In the dropdown, click `Download ZIP`.

3. Once the ZIP file is downloaded, extract it to the working directory of your IDE (VS Code, PyCharm, ...).

4. Execute the `Phonebook.py` from your IDE and interface the Software with the terminal.

## How It Works in the Background

The phonebook application is implemented in Python and uses a module called `shelve` to persistently store contact information. 

When you add a contact using the `enter` function, the application stores the contact's name, phone number, and city in a shelve database. The name of the contact is used as the key, and the phone number and city are stored as a tuple that is the value associated with the key.

The `lookup` function retrieves a contact's information from the shelve database using the contact's name as the key.

The `remove` function deletes a contact's information from the shelve database using the contact's name as the key.

The `listAll` function iterates over all the keys in the shelve database and retrieves the associated values to display all contacts in the phonebook.

The `distance` function calculates the distance between two contacts. It retrieves the city of each contact from the shelve database, then uses the `coordinates` function to get the coordinates of each city. The coordinates are then passed to the `Haversine_Formula` module to calculate the distance between the two cities.

The `closest_to` function finds the contact closest to a given contact. It calculates the distance between the given contact and all other contacts in the phonebook, then returns the contact with the smallest distance.

The `main` function is the entry point of the application. It uses a while-loop to continuously accept user input and uses if-elif-else constructs to determine which function to call based on the user's input. The loop continues until the user decides to quit by entering the `quit` or `exit` command.