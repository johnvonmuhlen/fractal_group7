from tkinter import *
from generate_tree import generate_tree

import random

root = Tk()
canvas = Canvas(root,width=800, height=600)
canvas.pack(fill=BOTH, expand=True, side='right')
root.title("Group 7 Tree Fractal")

def zoom_in(event):
   canvas.scale(ALL, event.x, event.y, 1.1, 1.1)

def zoom_out(event):
   canvas.scale(ALL, event.x, event.y, 0.9, 0.9)

# sidebar
sidebar = Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=4)
sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

#Button to generate trees
generate_tree_button = Button(sidebar, text="Start Generating New Tree", command=lambda: generate_tree(canvas, 400, 520, -90, 300, 10, 0.5, generate_tree_button, root, {'scale':slider.get(),
                                                                                                                                                                         'randomization':slider_2.get(),
                                                                                                                                                    'season':selected_season.get()}))
generate_tree_button.pack(pady=20)


#if generate_tree_button['text'] != 'Generating Tree...' or generate_tree_button['text'] != 'Clear Tree':
canvas.bind('<Button-1>', zoom_in)
canvas.bind('<Button-3>', zoom_out)

#Slider Label
slider_label = Label(sidebar, text='Choose tree scale')
slider_label.pack()

#Slider to make tree larger/shorter
slider = Scale(sidebar, from_=0, to=100, orient='horizontal')
slider.set(70)
slider.pack()

#Slider Label
slider_label = Label(sidebar, text='Randomize Tree')
slider_label.pack()

#Slider to make tree larger/shorter
slider_2 = Scale(sidebar, from_=0, to=100, orient='horizontal')
slider_2.set(45)
slider_2.pack()

#Seasons Label
seasons_label = Label(sidebar, text='Select Season')
seasons_label.pack()

seasons = ['Summer', 'Autumn', 'Winter', 'Spring', 'None']

selected_season = StringVar(value='None')

for season in seasons:
    radio = Radiobutton(sidebar, text=season, value=season, variable=selected_season)
    radio.pack()

random_tree_button = Button(sidebar, text="Create Crazy Tree", command=lambda: generate_tree(canvas, 400, 520, -90, 300, 10, 0.5, random_tree_button, root, {'scale':slider.get(),
                                                                                                                                                  'randomization':random.randint(100, 150),
                                                                                                                                                    'season':selected_season.get()}))
random_tree_button.pack()  

root.mainloop()
