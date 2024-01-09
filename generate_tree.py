import random
import math
from tkinter import *

def generate_tree(canvas, x1, y1, angle, length, root, user_selections, symmetric_mode, width=7):
    
    #set color of leaves
    leaves_color = ''
    
    if user_selections['season'] == 'Autumn':
        leaves_color = '#892D11'
    elif user_selections['season'] == 'Summer':
        leaves_color = 'green'
    elif user_selections['season'] == 'Spring':
        leaves_color = '#be2596'
    elif user_selections['season'] == 'Winter':
        leaves_color = 'white'
    elif user_selections['season'] == 'None':
        leaves_color  = ''
    
    #base case
    if user_selections['depth'] == 0:
        # Draw leaves at the end of branches
        leaf_size = random.randint(1,7)  # Define the size of the leaf
        canvas.create_oval(x1 - leaf_size, y1 - leaf_size, x1 + leaf_size, y1 + leaf_size, fill=leaves_color, outline='')
        return
    
    #math to draw tree
    x2 = x1 + length * math.cos(math.radians(angle)) * (user_selections['scale'] * 0.01)
    y2 = y1 + length * math.sin(math.radians(angle)) * (user_selections['scale'] * 0.01)
    
    #draws each line
    canvas.create_line(x1, y1, x2, y2, width=width, smooth=True, fill='#3B1104')
    
    #make the branches progressively shorter
    new_width = width * 0.8
    
    #update depth
    new_user_selections = {
        'scale':user_selections['scale'],
        'randomization':user_selections['randomization'],
        'season':user_selections['season'],
        'depth':user_selections['depth'] - 1
    }
    
    generate_tree(canvas, x2, y2, (angle - random.uniform(10, user_selections['randomization']) if symmetric_mode == 'off' else angle - user_selections['randomization']), length * (user_selections['scale'] * 0.01), root, new_user_selections, symmetric_mode, new_width)
    generate_tree(canvas, x2, y2, (angle + random.uniform(10, user_selections['randomization']) if symmetric_mode == 'off' else angle + user_selections['randomization']), length * (user_selections['scale'] * 0.01), root, new_user_selections, symmetric_mode, new_width)
   