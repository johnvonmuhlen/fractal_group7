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

#function to zoom in or out
def handle_zoom(event): 
    #check if right or left click
    if event.num == 1:
        #zoom in
        ratio_zoom = 1.1
    else:
        #zoom out
        ratio_zoom = 0.9
        
    #zoom method
    canvas.scale(ALL, event.x, event.y, ratio_zoom, ratio_zoom)

#create an object that lets us access zoom events by associating their number to zoom in or out
#we do this because the the canvas.bind method returns an object as well so we wanted to be able to handle all the zooming in the same function
class ZoomEvent:
    def __init__(self, num):
        self.num = num
        self.x = 250
        self.y = 250
    
#handle user click on zoom buttons
def segmented_button_callback(value):
    #if + button clicked, pass an object with num=1 so the handle_zoom function can recognize if its zoom in or out
    if value == '+':
        handle_zoom(ZoomEvent(1))
    #if the other is clicked, pass three(1 = left click, 3 = right click essentially)
    else:
        handle_zoom(ZoomEvent(3))
    #reset buttons so it can be clicked multiple times
    segemented_button.set(None)
        
#sidebar
sidebar = Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=4)
sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

#default tree values passed to generate tree
starting_tree_values = {'x1': 400,
                        'y1': 570,
                        'angle': -90,
                        'length':200,
                        }

#function that triggers when user moves sliders
def start_tree_generation(event=None):
    #clear the canvas
    canvas.delete(ALL)
    
    #call main function here
    generate_tree(canvas, starting_tree_values['x1'], starting_tree_values['y1'], starting_tree_values['angle'], starting_tree_values['length'], root, {'scale':scale_slider.get(), 'randomization':randomization_slider.get(),'season':selected_season.get(), 'depth': round(depth_slider.get())})

#intro label
intro_label = CTkLabel(sidebar, text='Welcome!', text_color='black', font=('Arial', 13))
intro_label.pack()

sub_intro_label = CTkLabel(sidebar, text='Start Moving Sliders To Generate Tree', text_color='black', font=('Arial', 11)).pack()

#zoom in commands for clicking
canvas.bind('<Button-1>', handle_zoom)
canvas.bind(f'<Button-{2 if platform.system() == "Darwin" else 3}>', handle_zoom)

#Depth slider Label
depth_label = CTkLabel(sidebar, text='Choose tree depth', text_color='black')
depth_label.pack()

#Slider to choose depth
depth_slider = CTkSlider(sidebar, from_=2, to=12, orientation='horizontal', command=start_tree_generation)
depth_slider.set(2)
depth_slider.pack()

#scale Slider Label
scale_slider_label = CTkLabel(sidebar, text='Choose tree size', text_color='black')
scale_slider_label.pack()

#Slider to choose scale
scale_slider = CTkSlider(sidebar, from_=40, to=100, orientation='horizontal', command=start_tree_generation)
scale_slider.set(40)
scale_slider.pack()

#randomization Slider Label
randomization_slider_label = CTkLabel(sidebar, text='Randomize Tree', text_color='black')
randomization_slider_label.pack()

#Slider to choose randomization
randomization_slider = CTkSlider(sidebar, from_=11, to=100, orientation='horizontal', command=start_tree_generation)
randomization_slider.set(11)
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
message_label = CTkLabel(sidebar, text="", text_color='black')
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
