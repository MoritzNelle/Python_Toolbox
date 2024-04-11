# For all, how are reeding this on GitHub, please note that this code is part of a university course... Don't question the logic, just accept it.

'''
READ ME:
- CityData class
- Imported modules: math

DESCRIPTION:
- The CityData class represents a city with its name and geographical coordinates (latitude and longitude).
- The latitude and longitude are stored as degrees, minutes, and direction (N/S for latitude, E/W for longitude).
- The class provides methods to set and get these attributes.

PARAMETERS:
- The constructor takes a single parameter, `name`, which is the name of the city.
- The `set_latitude` and `set_longitude` methods each take three parameters: `degrees` (an integer), `minutes` (an integer), and `direction` (a string, either 'N', 'S', 'E', or 'W').

LIMITATIONS:
- The class does not validate the input parameters. For example, it does not check if `degrees` and `minutes` are within valid ranges, or if `direction` is one of the allowed values.
- The class does not provide any methods to calculate distances or other geographical operations.

STRUCTURES:
- The class uses simple assignment statements to set the attributes in the `set_name`, `set_latitude`, and `set_longitude` methods.
- The `get_name` method uses a return statement to return the name of the city.

OUTPUTS:
- The `get_name` method returns the name of the city.
- The `set_name`, `set_latitude`, and `set_longitude` methods do not have any output. They modify the state of the CityData object.
'''


import math

class CityData:
    def __init__(self, name):       # Constructor
        self.name                   = name
        self.latitude_degrees       = None
        self.latitude_minutes       = None
        self.latitude_direction     = None
        self.longitude_degrees      = None
        self.longitude_minutes      = None
        self.longitude_direction    = None

    def set_name(self, name):
        self.name = name

    def set_latitude(self, degrees, minutes, direction):
        self.latitude_degrees = degrees
        self.latitude_minutes = minutes
        self.latitude_direction = direction

    def set_longitude(self, degrees, minutes, direction):
        self.longitude_degrees = degrees
        self.longitude_minutes = minutes
        self.longitude_direction = direction

    def get_name(self):
        return self.name
    
    def convert_to_radians(sign, degrees, minutes):                     
        return (sign * (degrees + minutes/60))*(3.14159265359/180)      # Convert degrees and minutes to radians by multiplying by pi/180 (=2pi/360). Note, that also the math.radians() function could be used here.
  
    def get_lat_lon_radians(self):
        sign = 1 if self.latitude_direction == 'N' else -1    # Convert 'N' or 'S' to 1 or -1
        radLat = CityData.convert_to_radians(sign, self.latitude_degrees, self.latitude_minutes)
        radLon = CityData.convert_to_radians(sign, self.longitude_degrees, self.longitude_minutes)
        return radLat, radLon

    def get_nested_tuple(self):
        nestedTuple = ((CityData.get_name(self)),
                       (self.latitude_degrees,  self.latitude_minutes,  self.latitude_direction ),
                       (self.longitude_degrees, self.longitude_minutes, self.longitude_direction))
        return nestedTuple
    
    def set_latitude_radians(self, radians):
        degrees = math.degrees(radians)
        minutes = (degrees - int(degrees)) * 60
        direction = 'N' if radians >= 0 else 'S'
        self.set_latitude(int(degrees), int(minutes), direction)
        return (int(degrees), int(minutes), direction)

    def set_longitude_radians(self, radians):
        degrees = math.degrees(radians)
        minutes = (degrees - int(degrees)) * 60
        direction = 'E' if radians >= 0 else 'W'
        self.set_longitude(int(degrees), int(minutes), direction)
        return (int(degrees), int(minutes), direction)



#===================================================================================================
#======================================= TEST CODE =================================================
#===================================================================================================

if __name__ == '__main__':
    
    city = CityData("New York")                                     # Create an instance of CityData
    print ("City name:\t\t", city.get_name()) # print the name of the city

    # Set latitude and longitude
    city.set_latitude(40, 45, "N")
    city.set_longitude(73, 58, "W")

    # Return the latitude and longitude
    print("Latitude:\t\t",  city.latitude_degrees,  city.latitude_minutes,  city.latitude_direction )
    print("Longitude:\t\t", city.longitude_degrees, city.longitude_minutes, city.longitude_direction)

    print("City name:\t\t", city.get_name())                        # Get the name of the city
    print("Latitude (radians):\t", city.get_lat_lon_radians())      # Get the latitude and longitude in radians
    print("Nested tuple:\t\t", city.get_nested_tuple())             # Get the nested tuple representation

    print("Latitude:\t\t",city.set_latitude_radians(0.7112216701877361))            # Set the latitude in radians
    print("Longitude:\t\t",city.set_longitude_radians(1.2915436464758034))          # Set the longitude in radians

    print()