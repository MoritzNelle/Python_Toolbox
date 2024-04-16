'''
READ ME: 
- This module contains the script to read data and create an animated plot as well as the function update to plot the data in an animated fashion
- It imports pandas, matplotlib.pyplot, and matplotlib.animation.

DESCRIPTION:
- This script reads UAV data from a text file, extracts relevant data columns, and creates an animated plot. 
- The plot consists of two subplots: one showing the UAV's trajectory over time, and the other showing sensor data over time.
- The plots are created by the update function, which is called for each value-pair in the data to create the animation

PARAMETERS:
- The script does not take any parameters. It reads data from a file named 'UAV_data.txt'.
- The update function takes a single parameter, 'frame', which represents the current value-pair that is added in the animation.

LIMITATIONS:
- The script assumes that the data file is in the same directory and is named 'UAV_data.txt'.
- The data file must contain columns named 't', 'NO2_conc', 'x_coord', and 'y_coord' in the correct order.
- The script does not handle missing or malformed data.
- The animation may be slow or choppy for large data sets.

STRUCTURES:
- The script uses pandas to read and manipulate data.
- It uses matplotlib to create plots and animations.
- The update function 
    - uses slicing to select data up to the current frame number.
    - uses the clear method to clear the subplots before each frame.
    - uses the plot method to plot the data, and the set_title, set_xlabel, and set_ylabel methods to set the titles and labels of the subplots.
    - uses the set_xlim and set_ylim methods to set the limits of the subplots.

OUTPUTS:
- The script does not return any values. It displays an animated plot using matplotlib's show function.
- It does not use any print statements.
'''


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Read the data
data = pd.read_csv('UAV_data.txt', delimiter = '\t')

# Extract the lists
time = data['t']
concentration = data['NO2_conc']
x_coords = data['x_coord']
y_coords = data['y_coord']

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Define the update function for the animation
def update(frame):
    # Clear the subplots
    ax1.clear()
    ax2.clear()
    
    # Plot the trajectory on the left subplot
    ax1.plot(x_coords[:frame], y_coords[:frame], color='lightgrey')
    cmin = min(concentration)
    cmax = max(concentration)
    ax1.scatter(x_coords[:frame], y_coords[:frame], c = concentration[:frame], s = 300, cmap = 'coolwarm', vmin = cmin, vmax = cmax)
    ax1.set_title('UAV Trajectory')
    ax1.set_xlabel('x-coordinate')
    ax1.set_ylabel('y-coordinate')

    # Plot the sensor data on the right subplot
    ax2.plot(time[:frame], concentration[:frame], color='red')
    ax2.set_title('Sensor Data Over Time')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('NO2 Concentration')

    # Set the limits of the subplots
    ax1.set_xlim(min(x_coords), max(x_coords))
    ax1.set_ylim(min(y_coords), max(y_coords))
    ax2.set_xlim(min(time), max(time))
    ax2.set_ylim(min(concentration), max(concentration))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(time), interval=200)

# Display the animation
plt.tight_layout()
plt.show()
