import tkinter as tk
import random
from time import sleep
from tqdm import tqdm
import sys

#   Possible values
possibleValues = ["E9", "1C", "55", "BD"]

#   Randomized sequence
#   HARDCODED TO BE LENGTH OF 3
sequence = [possibleValues[random.randint(0, 3)], possibleValues[random.randint(0, 3)], possibleValues[random.randint(0, 3)]]

#   Instantiate buffer and "alternate" variable
buffer = []
alternate = 0

#   Button press function
def button_pressed(row, col, value):
    #   Increment alternate global var to decide if row or column to enable.
    global alternate
    alternate = alternate + 1
    
    #   Append value to buffer
    buffer.append(value)
    
    #   Print current buffer
    #   The sys.stdout with flush allows the text to overwrite itself in the terminal.
    sys.stdout.write(f"\rCURRENT BUFFER: {buffer}")
    sys.stdout.flush()
    
    #   Once buffer length matches sequence length,
    if len(buffer) >= len(sequence):
        print("\n\n========================================")
        #   Fake loading bar. I have no idea how this one works, this was ChatGPT lol
        for _ in tqdm(range(100), desc="LOADING", ascii=" █", ncols=75):
                sleep(0.025)  # Adjust speed
        #   Decide win or loss
        if buffer == sequence:
            print("\nHACKING COMPLETE")
            exit()
        else:
            print("\nERROR: INCORRECT SEQUENCE")
            exit()
    
    #   Disable all buttons first
    for r in range(5):
        for c in range(5):
            buttons[r][c]["state"] = "disabled"

    #   Alternate row and column buttons to be enabled
    if alternate % 2 == 0:
        for i in range(5):
            buttons[i][col]["state"] = "normal"  # Enable same column
    else:
        for i in range(5):
            buttons[row][i]["state"] = "normal"  # Enable same row

#   Create main window and set some basic aspects
root = tk.Tk()
root.geometry("640x360")
root.title("CODE MATRIX")

#   Configure grid to be resizable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)     # Make rows expand
    root.grid_columnconfigure(i, weight=1)  # Make columns expand

#   Create a 5x5 grid of buttons
buttons = []
#   For each row,
for r in range(5):
    #   Instantiate row buttons per row
    row_buttons = []
    #   For each column,
    for c in range(5):
        randomNumber = random.randint(0, 3)
        '''   
            Create a button in root, with the text as a random value from possibleValues list. command = lambda to capture the r, c, and random value
            at the time of the instantiation of the button, rather at the end of the program. Attach a button_pressed() function with button press.
        '''
        btn = tk.Button(root, text=possibleValues[randomNumber], command=lambda r=r, c=c , value=possibleValues[randomNumber]: button_pressed(r, c, value))
        #   Places the button in the grid, with a 5 pixel space between buttons. NSEW allows buttons to stretch when resized.
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="NSEW")
        #   Append the button to the row button list
        row_buttons.append(btn)
    #   When finished with row_button list, append the list to buttons list.
    buttons.append(row_buttons)

#   Begin of root program and initial title
print("SEQUENCE REQUIRED TO UPLOAD:", sequence, "\n")
root.mainloop()
