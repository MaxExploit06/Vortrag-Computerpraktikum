import tkinter as tk
from PIL import Image, ImageTk
import random


def coin_toss():
    return "K" if random.randint(0,1) else "Z"


#Config
GRID_SIZE = 10          #kann geändert werden
PADDING = 2

HEADS_COLOR = "#2d7d31"
TAILS_COLOR = "#c22323"
WINDOW_COLOR = "#212121"


#Data
flips = [
    coin_toss() for i in range(GRID_SIZE * GRID_SIZE)
]


#Main Window
root = tk.Tk()

root.title("Coin Flips")
root.geometry("1280x720")
root.minsize(400, 400)

root.configure(bg=WINDOW_COLOR)

heads_original = Image.open("heads.png")
tails_original = Image.open("tails.png")

tk_heads = None
tk_tails = None


#Main Frame
grid_frame = tk.Frame(root, bg=WINDOW_COLOR)

grid_frame.pack(fill="both", expand=True, padx=10, pady=10)


#Grid Config
for row in range(GRID_SIZE):
    grid_frame.rowconfigure(row, weight=1)

for column in range(GRID_SIZE):
    grid_frame.columnconfigure(column, weight=1)


#Config list of lables
labels = []

for i in range(GRID_SIZE*GRID_SIZE):

    #Convert list index into row and column
    row = i // GRID_SIZE
    column = i % GRID_SIZE

    result = flips[i]

    if result == "K":
        background = HEADS_COLOR
    else:
        background = TAILS_COLOR

    label = tk.Label(
        grid_frame,
        bg=background,
        bd=0
    )

    label.grid(
        row=row,
        column=column,
        sticky="nsew",
        padx=PADDING,
        pady=PADDING
    )

    labels.append(label)


#Calculate and resize images
def redraw(event=None):

    global tk_heads, tk_tails

    width = grid_frame.winfo_width()
    height = grid_frame.winfo_height()

    if width <= 1 or height <= 1:
        return

    #current cell size
    cell_width = width // GRID_SIZE
    cell_height = height // GRID_SIZE

    image_size = min(cell_width, cell_height)
    image_size -= 2 * PADDING

    image_size = max(5, image_size)

    # Resize images
    resized_heads = heads_original.resize(
        (image_size, image_size)
    )

    resized_tails = tails_original.resize(
        (image_size, image_size)
    )

    tk_heads = ImageTk.PhotoImage(resized_heads)
    tk_tails = ImageTk.PhotoImage(resized_tails)

    #Update every cell
    for i in range(GRID_SIZE*GRID_SIZE):

        result = flips[i]
        label = labels[i]

        if result == "K":
            label.configure(image=tk_heads)
        else:
            label.configure(image=tk_tails)


#When resized, calculate image size again
grid_frame.bind("<Configure>", redraw)


#Mainloop of GUI
root.mainloop()