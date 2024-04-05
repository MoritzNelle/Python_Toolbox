'''
# READ ME SECTION

# DESCRIPTION
- This python program uses the Haversine formula to calculate the great-circle distance between two points - that is, the shortest distance over the Earth's surface - giving an "as-the-crow-flies" distance between the points (ignoring any elevations or obstacles). The Haversine formula accounts for the Earth's curvature to calculate the shortest distance between two points on the surface of a sphere.

# PARAMETERS
The 'distance' function takes the following parameters:
- 'signLat1', 'degLat1', 'minLat1': The sign (1 for N/-1 for S), degrees, and minutes of the latitude for the first location.
- 'signLon1', 'degLon1', 'minLon1': The sign (1 for E/-1 for W), degrees, and minutes of the longitude for the first location.
- 'signLat2', 'degLat2', 'minLat2': The sign (1 for N/-1 for S), degrees, and minutes of the latitude for the second location.
- 'signLon2', 'degLon2', 'minLon2': The sign (1 for E/-1 for W), degrees, and minutes of the longitude for the second location.

# NEW FUNCTIONS
- 'errorExit': Handles errors and exits the program.
- 'firstFourNumbers': Finds and returns the first four numbers in a string.
- 'input2haversine': Processes the input strings and returns a list for the haversine formula.

# LIMITATIONS
- The program does not account for the elevation of the locations.
- The program does not account for the Earth's oblateness.
- The program does not check the user input for valid latitude and longitude values.

# STRUCTURES
The program consists of six main functions:
- 'convert_to_radians': Converts degrees and minutes to radians.
- 'haversine': Calculates the haversine distance between two points in radians.
- 'distance': Converts latitudes and longitudes to radians and calculates the distance between the two points in kilometers.
- 'errorExit': Handles errors and exits the program.
- 'firstFourNumbers': Finds and returns the first four numbers in a string.
- 'input2haversine': Processes the input strings and returns a list for the haversine formula.
-- Note, that the user only interacts with the 'input2haversine' function. The other functions are helper functions and are not called directly by the user.

# OUTPUT
The program prints the calculated distances between the pairs of locations. The distances are in kilometers.
'''

import math                                                         # Import the math module

def convert_to_radians(sign, degrees, minutes):                     
    return (sign * (degrees + minutes/60))*(3.14159265359/180)      # Convert degrees and minutes to radians by multiplying by pi/180 (=2pi/360). Note, that also the math.radians() function could be used here.
     
def haversine(lat1, lon1, lat2, lon2):                              # Define a function to calculate the haversine distance
    dLat = lat2 - lat1                                              # Calculate the difference in latitude between the two points
    dLon = lon2 - lon1                                              # Calculate the difference in longitude between the two points
    a2 = math.sin(dLat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2)**2  # Calculate a^2 using the haversine formula from reader
    radDist = 2 * math.atan2(a2**.5, (1-a2)**.5)                    # Calculate the haversine distance in radians, note that: b^2 = 1 - a^2
    return radDist

def distance(signLat1, signLon1, degLat1, minLat1, degLon1, minLon1, signLat2, signLon2,  degLat2, minLat2, degLon2, minLon2):  # Define a function to calculate the distance between two points
    lat1 = convert_to_radians(signLat1, degLat1, minLat1)           # Convert latitude 1 to radians
    lon1 = convert_to_radians(signLon1, degLon1, minLon1)           # Convert longitude 1 to radians
    lat2 = convert_to_radians(signLat2, degLat2, minLat2)           # Convert latitude 2 to radians
    lon2 = convert_to_radians(signLon2, degLon2, minLon2)           # Convert longitude 2 to radians
    return haversine(lat1, lon1, lat2, lon2) * 6371                 # Calculate the distance in kilometers

# Function to handle errors and exit the program
def errorExit(ErrorCode):
    print ("!!!An ERROR occurred!!!\nProgram exited with error code", ErrorCode)
    exit()

# Function to find and return the first four numbers in a string
def firstFourNumbers(string):
    numbers = []
    num = ''
    for char in string:                     # Iterate over each character in the string
        if char.isdigit():                  # If the character is a digit, add it to the current number
            num += char
        elif num:                           # If the character is not a digit and there is a current number, add the current number to the list of numbers
            numbers.append(int(num))
            num = ''
        if len(numbers) == 4:               # Stop when we have found four numbers
            break
    if num and len(numbers) < 4:            # If there is a current number when we stop, add it to the list of numbers
        numbers.append(int(num))
    return numbers[:4]                      # Return the first four numbers found

# Function to process the input strings and return a list for the haversine formula
def input2haversine(stringA, stringB):
    finalString = [0]*12                    # Initialize a list with 12 zeros
    if stringA.find('N') != -1:             # Check for 'N' or 'S' in stringA and set the corresponding value in finalString
        finalString[0] = 1
    elif stringA.find('S') != -1:
        finalString[0] = -1
    else:
        errorExit(1)
    if stringA.find('E') != -1:             # Check for 'E' or 'W' in stringA and set the corresponding value in finalString
        finalString[1] = 1
    elif stringA.find('W') != -1:
        finalString[1] = -1
    else:
        errorExit(3)
    finalString[2], finalString[3], finalString[4], finalString[5] = firstFourNumbers(stringA)    # Find the first four numbers in stringA and set them in finalString

    # Repeat the above steps for stringB
    if stringB.find('N') != -1:
        finalString[6] = 1
    elif stringB.find('S') != -1:
        finalString[6] = -1
    else:
        errorExit(1)
    if stringB.find('E') != -1:
        finalString[7] = 1
    elif stringB.find('W') != -1:
        finalString[7] = -1
    else:
        errorExit(4)
    finalString[8], finalString[9], finalString[10], finalString[11] = firstFourNumbers(stringB)
    
    return finalString                      # Return the final list

if __name__ == "__main__":
    # Get the input strings from the user
    inputStringA = input("\nEnter the latitude and longitude of the first location (e.g. 52 0' N; 52° N ,...): \n")
    inputStringB = input("Enter the latitude and longitude of the second location (e.g. 23 0' E; 23° E ,...): \n")
    print(distance(*input2haversine(inputStringA, inputStringB)), " km\n") # Calculate and print the distance between the two locations


    '''
    # Testing the program by calculating the distances between Amsterdam, Montreal, and Auckland and just print them to the console
    distance1 = distance(1, 52, 22, 1, 4, 32, 1, 45, 30, -1, 73, 35)    # Amsterdam to Montreal
    distance2 = distance(1, 45, 30, -1, 73, 35, -1, 36, 52, 1, 174, 45) # Montreal to Auckland
    distance3 = distance(-1, 36, 52, 1, 174, 45, 1, 52, 22, 1, 4, 32)   # Auckland to Amsterdam

    print("The distance from Amsterdam to Montreal is {:.4f} km.".format(distance1))    # Print the distances with 4 decimal places to the console
    print("The distance from Montreal to Auckland is {:.4f} km.".format(distance2))     # "
    print("The distance from Auckland to Amsterdam is {:.4f} km.".format(distance3))    # "
    '''