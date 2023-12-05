from tkinter import *
from generate_tree import generate_tree
from customtkinter import *
import random
import platform

# startup tkinter canvas
root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack(fill=BOTH, expand=True, side='right')
#window title
root.title("Group 7 Tree Fractal")

#zoom in/out functions for clicking
def zoom_in_click(event):
   if generate_tree_button.cget('text') != 'Generating Tree...' or generate_tree_button.cget('text') == 'Clear Tree':
        canvas.scale(ALL, event.x, event.y, 1.1, 1.1)
        
def zoom_out_click(event):
   if generate_tree_button.cget('text') != 'Generating Tree...' or generate_tree_button.cget('text') == 'Clear Tree':
    canvas.scale(ALL, event.x, event.y, 0.9, 0.9)

#zoom in out functions for buttons
def zoom_in():
    if generate_tree_button.cget('text') != 'Generating Tree...' or generate_tree_button.cget('text') == 'Clear Tree':
        canvas.scale(ALL, 250, 250, 1.1, 1.1)
    
def zoom_out():
    if generate_tree_button.cget('text') != 'Generating Tree...' or generate_tree_button.cget('text') == 'Clear Tree':
        canvas.scale(ALL, 250, 250, 0.9, 0.9)

#handle user click on zoom buttons
def segmented_button_callback(value):
    if value == '+':
        zoom_in()
    else:
        zoom_out()
        
    segemented_button.set(None)
        
#sidebar
sidebar = Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=4)
sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

#default tree values passed to generate tree
starting_tree_values = {'x1': 400,
                        'y1': 570,
                        'angle': -90,
                        'length':300,
                        }

#Button to generate trees                                                                                        
generate_tree_button = CTkButton(sidebar, text="Start Generating New Tree", command=lambda: generate_tree(canvas, starting_tree_values['x1'], starting_tree_values['y1'], starting_tree_values['angle'], starting_tree_values['length'], generate_tree_button, root, {'scale':scale_slider.get(), 'randomization':randomization_slider.get(),'season':selected_season.get(), 'depth': round(depth_slider.get() / 10)}))
generate_tree_button.pack(pady=20)

#zoom in commands for clicking
canvas.bind('<Button-1>', zoom_in_click)
canvas.bind(f'<Button-{2 if platform.system() == "Darwin" else 3}>', zoom_out_click)

#Depth slider Label
depth_label = CTkLabel(sidebar, text='Choose tree depth', text_color='black')
depth_label.pack()
CTkLabel(sidebar, text='(Choices bigger than default can make the program laggy)', text_color='black', font=('Arial', 9)).pack()

#Slider to choose depth
depth_slider = CTkSlider(sidebar, from_=20, to=150, orientation='horizontal')
depth_slider.set(100)
depth_slider.pack()

#scale Slider Label
scale_slider_label = CTkLabel(sidebar, text='Choose tree size', text_color='black')
scale_slider_label.pack()

#Slider to choose scale
scale_slider = CTkSlider(sidebar, from_=40, to=100, orientation='horizontal')
scale_slider.set(70)
scale_slider.pack()

#randomization Slider Label
randomization_slider_label = CTkLabel(sidebar, text='Randomize Tree', text_color='black')
randomization_slider_label.pack()

#Slider to choose randomization
randomization_slider = CTkSlider(sidebar, from_=11, to=100, orientation='horizontal')
randomization_slider.set(45)
randomization_slider.pack()

#Seasons Label
seasons_label = CTkLabel(sidebar, text='Select Season', text_color='black')
seasons_label.pack(pady=5)

#Create Radio Buttons
seasons = ['Summer', 'Autumn', 'Winter', 'Spring', 'None']

#make the default selected season None
selected_season = StringVar(value='None')

#array to store radiobuttons so we then we can access them to perform methods on them
radio_buttons = []

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
randomize_settings_button.pack(pady=10)  

# Create a label to display the season message
message_label = CTkLabel(root, text="")
message_label.pack()

#reset sliders to default
def reset_to_default():
    depth_slider.set(100)
    scale_slider.set(70)
    randomization_slider.set(45)
    radio_buttons[4].select()

#reset everyhting to default button
reset_to_default_button = CTkButton(sidebar, text='Reset to Default', command=lambda:reset_to_default())
reset_to_default_button.pack()

#label for zooming in buttons
zoom_buttons_label = CTkLabel(sidebar, text="Zoom In/Out", text_color='black')
zoom_buttons_label.pack(pady=10)

#buttons to zoom in and out
segemented_button_var = StringVar(value="Value 1")
segemented_button = CTkSegmentedButton(sidebar, values=["+", "-"], command=segmented_button_callback, variable=segemented_button_var)
segemented_button.pack()

# Bind arrow key events to the xview_scroll and yview_scroll methods of the canvas
canvas.bind("<Left>", lambda event: canvas.xview_scroll(-1, "units"))
canvas.bind("<Right>", lambda event: canvas.xview_scroll( 1, "units"))
canvas.bind("<Up>",   lambda event: canvas.yview_scroll(-1, "units"))
canvas.bind("<Down>", lambda event: canvas.yview_scroll( 1, "units"))

# Give focus to the canvas so the arrows can trigger
canvas.focus_set()

root.mainloop()
