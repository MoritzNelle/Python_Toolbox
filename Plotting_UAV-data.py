'''
READ ME:
- This module contains the following functions:
    - pandas.read_csv
    - matplotlib.pyplot.subplots
    - matplotlib.pyplot.tight_layout
    - matplotlib.pyplot.show
- The module imports pandas and matplotlib.pyplot

DESCRIPTION:
- This script reads UAV data from a text file, extracts relevant data columns, and plots the UAV trajectory and sensor data over time.
- The data is read using pandas' read_csv function. The relevant data columns are extracted into separate lists.
- Two plots are created using matplotlib: one for the UAV trajectory and one for the sensor data over time.
- The plots are displayed using matplotlib's show function.

PARAMETERS:
- 'UAV_data.txt': a text file containing the UAV data. The data is tab-delimited.
- The data file should contain the following columns: 't', 'NO2_conc', 'x_coord', 'y_coord'.

LIMITATIONS:
- The script assumes that the data file is in the same directory as the script. If the data file is in a different location, the script will fail.
- The script assumes that the data file is correctly formatted and contains the required columns. If the data file is incorrectly formatted or missing columns, the script will fail.
- The script does not handle missing or NaN values in the data.

STRUCTURES:
- The script uses pandas' read_csv function to read the data file.
- The data columns are extracted into separate lists using pandas' DataFrame indexing.
- Two subplots are created using matplotlib's subplots function.
- The data is plotted using matplotlib's plot function.
- The plots are displayed using matplotlib's show function.

OUTPUT:
- The script outputs two plots: one for the UAV trajectory and one for the sensor data over time.
- The plots are displayed in a new window.
'''



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Read the data
data = pd.read_csv('UAV_data.txt', delimiter='\t')

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
    ax1.plot(x_coords[:frame], y_coords[:frame], color='blue')
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