# AQI GUI is a program providing a Graphical User Interface for users to input values to be used to calculate and return AQI readings.

# Importing tk and ttk for GUI functionality and modern styling.

from tkinter import *
from tkinter import ttk

# Importing messagebox in order to create alerts for use in error handling.

from tkinter import messagebox

# Function for calculating AQI.
# User input is taken for each pollutant to be used in the calculation.
# AQI is calculated for ozone, sulfur dioxide and particles separately, with the final aqi result being the highest of the pollutant calculations.
# A button linked to this function enables users to run the function using the GUI.
# The AQI result displayed in the output for the function is rounded to two decimal places.
# While loops are utilised in order to validate user input to be positive integers.
# Messageboxes will appear and prompt users to input a positive integer upon enacting the function in the event that they have input extraneous characters.

def calculate_aqi(*args):
    while True:
        try:
            ozone_value = float(ozone.get())
            if ozone_value < 0: 
                raise(ValueError)
            break
        except ValueError:
            messagebox.showwarning(title = "Error", message = "Please enter a non-negative integer.")
        break    
    while True:
        try:
            sulfur_dioxide_value = float(sulfur_dioxide.get())
            if sulfur_dioxide_value < 0:
                raise(ValueError)
            break
        except ValueError:
            messagebox.showwarning(title = "Error", message = "Please enter a non-negative integer.")
        break
    while True:
        try:
            particles_value = float(particles.get())
            if particles_value < 0:
                raise(ValueError)
            break
        except ValueError:
                messagebox.showwarning(title = "Error", message = "Please enter a non-negative integer.")
        break 
    final_ozone = 100*(ozone_value/8)
    final_sulfur_dioxide = 100*(sulfur_dioxide_value/20)
    final_particles = 100*(particles_value/25)
    aqi_readings = [final_ozone, final_sulfur_dioxide, final_particles]
    aqi_result = max(aqi_readings)
    aqi_formatted = "{:.2f}".format(aqi_result)
    aqi.set(aqi_formatted)

# Creating a window for the AQI GUI program.

root = Tk()
root.title("AQI GUI")

# Setting a minimum size for resizing.

root.minsize(600, 115)

# Creating and positioning a frame to cover the window.

frame = ttk.Frame(root, padding = "3 3 12 12")
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))

# Resizing for main window.

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# Resizing for columns and rows.

for column in range (1, 5):
    frame.columnconfigure(column, weight = 1)

for row in range (1, 6):
    frame.rowconfigure(row, weight = 1)

# ozone represents the ozone reading input by the user.
# sulfur_dioxide represents the sulfur dioxide reading input by the user.
# particles represents the particles reading input by the user.
# aqi represents the final AQI reading calculated and formatted to display to two decimal places.

ozone = StringVar()
sulfur_dioxide = StringVar()
particles = StringVar()
aqi = StringVar()

# Creating and positioning widgets for each input field for the purposes of input and user information.

ozone_label = ttk.Label(frame, text = "Ozone:")
ozone_label.grid(column = 1, row = 1, sticky = E)

ozone_entry = ttk.Entry(frame, width = 10, textvariable = ozone)
ozone_entry.grid(column = 2, row = 1, columnspan = 2, sticky = (W, E))

ozone_details = ttk.Label(frame, text = "parts per hundred million")
ozone_details.grid(column = 4, row = 1, sticky = W)

sulfur_dioxide_label = ttk.Label(frame, text = "Sulfur dioxide:")
sulfur_dioxide_label.grid(column = 1, row = 2, sticky = E)

sulfur_dioxide_entry = ttk.Entry(frame, width = 10, textvariable = sulfur_dioxide)
sulfur_dioxide_entry.grid(column = 2, row = 2, columnspan = 2, sticky = (W, E))

sulfur_dioxide_details = ttk.Label(frame, text = "parts per hundred million")
sulfur_dioxide_details.grid(column = 4, row = 2, sticky = W)

particles_label = ttk.Label(frame, text = "Particles less than 2.5 micrometre diameter:")
particles_label.grid(column = 1, row = 3, sticky = E)

particles_entry = ttk.Entry(frame, width = 10, textvariable = particles)
particles_entry.grid(column = 2, row = 3, columnspan = 2, sticky = (W, E))

particles_details = ttk.Label(frame, text = "micrograms per cubic metre")
particles_details.grid(column = 4, row = 3, sticky = W)

# Creating and positioning a button enabling users to run the program to calculate the aqi.

aqi_button = ttk.Button(frame, text = "Calculate AQI", command = calculate_aqi)
aqi_button.grid(column = 2, row = 4, columnspan = 2, sticky = (W, E))

# Creating and positioning an output field displaying a heading and the output of the calculate aqi function.

aqi_label = ttk.Label(frame, text = "AQI: ")
aqi_label.grid(column = 2, row = 5, sticky = E)

aqi_result_label = ttk.Label(frame, textvariable = aqi)
aqi_result_label.grid(column = 3, row = 5, sticky = (W, E))

# Cursor initially focuses on the user input field for ozone.

ozone_entry.focus()

# Binding the return button on the keyboard to the calculate_aqi function for convenience.

root.bind("<Return>", calculate_aqi)

# Run program to allow AQI to be calculated and returned based on user input.

root.mainloop()
