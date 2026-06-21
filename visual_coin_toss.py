import tkinter as tk
from PIL import Image, ImageTk
import random


def coin_toss():
    return "K" if random.randint(0, 1) else "Z"


#Constants

GRID_SIZE = 10

CELL_SIZE = 80

PAD_X = 80      #Between cells
PAD_Y = 10

MARGIN_X = 80       #From edges
MARGIN_Y = 90

HEADER_HEIGHT = 60

HEADS_COLOR = "#2d7d31"
TAILS_COLOR = "#c22323"
WINDOW_COLOR = "#E0D0EC"

WINDOW_W = 1680
WINDOW_H = 1000


#Coin flips
flips = [coin_toss() for _ in range(GRID_SIZE * GRID_SIZE)]


#Main window
root = tk.Tk()
root.title("Coin Flips")
root.geometry(f"{WINDOW_W}x{WINDOW_H}")
root.resizable(False, False)


#Main frame/canvas
canvas = tk.Canvas(
    root,
    width=WINDOW_W,
    height=WINDOW_H,
    bg=WINDOW_COLOR,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)


#Arrows for direction
try:
    bg_img = ImageTk.PhotoImage(
        Image.open("background.png")
    )
    canvas.create_image(0, 0, image=bg_img, anchor="nw")
except:
    bg_img = None


#Header with extra info
canvas.create_rectangle(
    0,
    0,
    WINDOW_W,
    HEADER_HEIGHT,
    fill="#2a2a2a",
    outline=""
)

#Calculating stats
heads = 0
tails = 0
for i in flips:
    if (i == "K"):
        heads += 1
    else:
        tails += 1

amount = (10 * heads) - (10 * tails)
abs_amount = abs(amount)

canvas.create_text(
    WINDOW_W // 2,
    HEADER_HEIGHT // 2,
    text= f"Würfe: {GRID_SIZE * GRID_SIZE}\t\t\t\tKopf: {heads}\t\t\t\tZahl: {tails}\t\t\t\tGewinn: {amount}"
        if amount >= 0 else f"Würfe: {GRID_SIZE * GRID_SIZE}\t\t\t\tKopf: {heads}\t\t\t\tZahl: {tails}\t\t\t\tVerlust: {abs_amount}",
    fill="white",
    font=("Arial", 14)
)


#Coin images config
heads_img = ImageTk.PhotoImage(
    Image.open("heads.png").resize((CELL_SIZE, CELL_SIZE))
)

tails_img = ImageTk.PhotoImage(
    Image.open("tails.png").resize((CELL_SIZE, CELL_SIZE))
)


#Grid config
for i in range(GRID_SIZE * GRID_SIZE):

    row = i // GRID_SIZE
    col = i % GRID_SIZE

    x = MARGIN_X + col * (CELL_SIZE + PAD_X)
    y = MARGIN_Y + row * (CELL_SIZE + PAD_Y)

    result = flips[i]

    if result == "K":
        bg = HEADS_COLOR
        img = heads_img
    else:
        bg = TAILS_COLOR
        img = tails_img

    #Cell background
    canvas.create_rectangle(
        x,
        y,
        x + CELL_SIZE,
        y + CELL_SIZE,
        fill=bg,
        outline=""
    )

    #Coin image
    canvas.create_image(
        x + CELL_SIZE // 2,
        y + CELL_SIZE // 2,
        image=img
    )


#Main loop for GUI
root.mainloop()