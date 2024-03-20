'''
Cylinder Testing

READ ME:
This module contains the following functions:
- `area_cylinder(r, h)`
- `volume_cylinder(r, h)`

DESCRIPTION:
This module contains two functions that calculate the area and volume of a cylinder respectively. The area and volume are calculated using the formulas for the area and volume of a cylinder. The results are printed to the console.

PARAMETERS:
- `r`: The radius of the base of the cylinder. It should be a positive float.
- `h`: The height of the cylinder. It should be a positive float.

LIMITATIONS:
- The functions do not check if the radius and height are positive. If negative values are passed, the functions will return negative results, which do not make sense in the context of a physical cylinder.
- The functions do not check if the radius and height are numbers. If non-numeric values are passed, the functions will raise a TypeError.

STRUCTURES:
- The module uses a while-loop to continuously prompt the user for the radius and height of a cylinder until the user types 'exit'.
- The module uses if-statements to check if the user has typed 'exit' and to break the loop if so.
- The module uses the function `input` to get the radius and height from the user.

OUTPUT:
The module prints the area of the base and the volume of the cylinder to the console. It uses print-statements to do this because the purpose of the module is to display the results to the user. The functions themselves do not have return statements; they only calculate the area and volume and print the results.
'''


def area_cylinder(r):                                   # Define the functions to calculate the area and volume of a cylinder
    return 3.14159 * r * r

def volume_cylinder(r, h):
    return area_cylinder(r) * h

print("\nTest of the functions area_cylinder and volume_cylinder\nType 'exit' for the radius or height to end the test\n")

while True:                                             # Loops until the user types 'exit'
    r = input('Radius of the cylinder [cm]:     ')      # not converted to float yet, because we need to check if the user typed 'exit' (string)
    if r == 'exit':                                     # Check if the user typed 'exit'
        print("Test ended")
        break                                           # We are not encuraged to use break, but it is the most efficient way to end the loop
    r = float(r)                                        # Convert the user's input to a float after checking if the user typed 'exit'
    
    h = input('Height of the cylinder [cm]:     ')
    if h == 'exit':
        print("Test ended\n")
        break
    h = float(h)

    print('The area of the base is [cm^2]: ', area_cylinder(r))
    print('The volume is [cm^3]:           ', volume_cylinder(r, h), '\n')