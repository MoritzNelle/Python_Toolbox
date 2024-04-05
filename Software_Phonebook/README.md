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