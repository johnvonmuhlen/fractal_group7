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

<<<<<<< Updated upstream
#Slider to make tree larger/shorter
slider = Scale(sidebar, from_=0, to=100, orient='horizontal')
slider.set(70)
slider.pack()
=======
#Slider to choose depth
depth_slider = CTkSlider(sidebar, from_=20, to=150, orientation='horizontal')
depth_slider.set(80)
depth_slider.pack()
>>>>>>> Stashed changes

#Slider Label
slider_label = Label(sidebar, text='Randomize Tree')
slider_label.pack()

<<<<<<< Updated upstream
#Slider to make tree larger/shorter
slider_2 = Scale(sidebar, from_=0, to=100, orient='horizontal')
slider_2.set(45)
slider_2.pack()
=======
#Slider to choose scale
scale_slider = CTkSlider(sidebar, from_=40, to=100, orientation='horizontal')
scale_slider.set(60)
scale_slider.pack()

#randomization Slider Label
randomization_slider_label = CTkLabel(sidebar, text='Randomize Tree', text_color='black')
randomization_slider_label.pack()

#Slider to choose randomization
randomization_slider = CTkSlider(sidebar, from_=11, to=100, orientation='horizontal')
randomization_slider.set(45)
randomization_slider.pack()
>>>>>>> Stashed changes

#Seasons Label
seasons_label = Label(sidebar, text='Select Season')
seasons_label.pack()

seasons = ['Summer', 'Autumn', 'Winter', 'Spring', 'None']

selected_season = StringVar(value='None')

for season in seasons:
    radio = Radiobutton(sidebar, text=season, value=season, variable=selected_season)
    radio.pack()

<<<<<<< Updated upstream
random_tree_button = Button(sidebar, text="Create Crazy Tree", command=lambda: generate_tree(canvas, 400, 520, -90, 300, 10, 0.5, random_tree_button, root, {'scale':slider.get(),
                                                                                                                                                  'randomization':random.randint(100, 150),
                                                                                                                                                    'season':selected_season.get()}))
random_tree_button.pack()  
=======
#loop that creates all radio buttons
for i in range(len(seasons)):
    radio = CTkRadioButton(sidebar, text=seasons[i], value=seasons[i], variable=selected_season, text_color='black')
    radio.pack(pady=5)
    radio_buttons.append(radio)

#values passed when crazy tree is created
random_tree_values = { 'scale':70,
                        'randomization':random.randint(100, 150),
                        'season':random.choice(seasons),
                        'depth': 10
                        }

#function to randomize settings
def randomize_settings():
    depth_slider.set(random.randint(20, 100))
    scale_slider.set(random.randint(40, 100))
    randomization_slider.set(random.randint(11, 100))
    radio_buttons[random.randint(0, 4)].select()

#Create Random Tree Button
randomize_settings_button = CTkButton(sidebar, text="Randomize Settings", command=lambda:randomize_settings())
randomize_settings_button.pack(pady=20)  

# Create a label to display the season message
message_label = CTkLabel(root, text="")
message_label.pack()

def reset_to_default():
    depth_slider.set(80)
    scale_slider.set(60)
    randomization_slider.set(45)
    radio_buttons[4].select()

#reset everyhting to default button
reset_to_default_button = CTkButton(sidebar, text='Reset to Default', command=lambda:reset_to_default())
reset_to_default_button.pack()

CTkLabel(sidebar, text='Zoom In/Out: Right & Left Click', text_color='black', font=('Arial', 11)).pack()
>>>>>>> Stashed changes

root.mainloop()
