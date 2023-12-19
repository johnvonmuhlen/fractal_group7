import random
import math
from tkinter import *

def add_flower(canvas, x, y):
    try:
        flower_img = PhotoImage(file="flower.png")  # Replace "flower.png" with your flower image file
        canvas.create_image(x, y, anchor="center", image=flower_img)
        canvas.image = flower_img  # Keep a reference to avoid garbage collection
    except FileNotFoundError:
        print("Error: Image file not found!")

def generate_tree(canvas, x1, y1, angle, length, user_selections, symmetric_mode, width=7):
    # base case
    if user_selections['depth'] == 0:
        return

    # math to draw tree
    x2 = x1 + length * math.cos(math.radians(angle)) * (user_selections['scale'] * 0.01)
    y2 = y1 + length * math.sin(math.radians(angle)) * (user_selections['scale'] * 0.01)

    # draws each line
    canvas.create_line(x1, y1, x2, y2, width=width, smooth=True)

    # add flower at the end of the branch
    add_flower(canvas, x2, y2)

    # make the branches progressively shorter
    new_width = width * 0.8

    # update depth
    new_user_selections = {
        'scale': user_selections['scale'],
        'randomization': user_selections['randomization'],
        'season': user_selections['season'],
        'depth': user_selections['depth'] - 1
    }

    # one branch for left and one for right
    generate_tree(canvas, x2, y2, (angle - random.uniform(10, user_selections['randomization']) if symmetric_mode == 'off' else angle - user_selections['randomization']), length * (user_selections['scale'] * 0.01), new_user_selections, symmetric_mode, new_width)
    generate_tree(canvas, x2, y2, (angle + random.uniform(10, user_selections['randomization']) if symmetric_mode == 'off' else angle + user_selections['randomization']), length * (user_selections['scale'] * 0.01), new_user_selections, symmetric_mode, new_width)
