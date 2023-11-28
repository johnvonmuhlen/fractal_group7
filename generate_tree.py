import random
import math
from tkinter import *

def generate_tree(canvas, x1, y1, angle, length, depth, scale, button, root, user_selections, width=7):
    if depth == 0:
        button.config(text="Clear Tree", state='normal')
        return
    
    if button['text'] == 'Clear Tree':
         canvas.delete('all')
         button.config(text="Start Generating New Tree", state='normal')
         return
    
    button.config(text="Generating Tree...", state='disabled')
    
    x2 = x1 + length * math.cos(math.radians(angle)) * scale
    y2 = y1 + length * math.sin(math.radians(angle)) * scale

    canvas.create_line(x1, y1, x2, y2, width = width, smooth=True)
    
    new_width = width * 0.8 
    
    canvas.after(300, generate_tree, canvas, x2, y2, angle - random.randint(10, user_selections['randomization']), length * (user_selections['scale'] * 0.01), depth - 1, scale, button, root, user_selections,new_width)
    canvas.after(300, generate_tree, canvas, x2, y2, angle + random.randint(10, user_selections['randomization']), length * (user_selections['scale'] * 0.01), depth - 1, scale, button, root, user_selections,new_width)