import random
import math
from tkinter import *

def generate_tree(canvas, x1, y1, angle, length, button, root, user_selections, width=7):
    #base case
    if user_selections['depth'] == 0:
        button.configure(text="Clear Tree", state='normal')
        return
    
    #user can clear the tree after its done generating
    if button.cget("text") == 'Clear Tree':
         canvas.delete('all')
         button.configure(text="Start Generating New Tree", state='normal')
         return
    
    #disable button while tree is generating
    button.configure(text="Generating Tree...", state='disabled')

    #math to draw tree
    x2 = x1 + length * math.cos(math.radians(angle)) * (user_selections['scale'] * 0.01)
    y2 = y1 + length * math.sin(math.radians(angle)) * (user_selections['scale'] * 0.01)
    
    #draws each line
    canvas.create_line(x1, y1, x2, y2, width=width, smooth=True)
    
    #make the branches progressively shorter
    new_width = width * 0.8
    
    #update depth
    new_user_selections = {
        'scale':user_selections['scale'],
        'randomization':user_selections['randomization'],
        'season':user_selections['season'],
        'depth':user_selections['depth'] - 1
    }
    
    #one branch for left and one for right
    canvas.after(300, generate_tree, canvas, x2, y2, angle - random.randint(10, user_selections['randomization']), length * (user_selections['scale'] * 0.01), button, root, new_user_selections, new_width)
    canvas.after(300, generate_tree, canvas, x2, y2, angle + random.randint(10, user_selections['randomization']), length * (user_selections['scale'] * 0.01), button, root, new_user_selections, new_width)