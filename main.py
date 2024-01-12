from tkinter import *
from customtkinter import *
import platform
from tktooltip import ToolTip
import webbrowser
from tkinter import Label



#our files
from generate_tree import generate_tree
from util import *
from static import starting_tree_values, seasons

# startup tkinter canvas
root = Tk()
canvas = Canvas(root, width=800, height=700)
canvas.pack(fill=BOTH, expand=True, side='right')
root.title("Group 7 Tree Fractal")

symmmetric_mode_switch = StringVar(value="on")
wind_mode_switch = StringVar(value="off")

#sidebar
sidebar = Frame(root, width=300, bg='white', height=500, relief='sunken', borderwidth=4)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# Function to allow clickable links 
def open_link(url):
    webbrowser.open_new_tab(url)


#function that triggers when user moves sliders
def start_tree_generation(event=None):
    #clear the canvas
    canvas.delete(ALL)
    
    #get the value of switches
    symmetric_mode = symmmetric_mode_switch.get()
    
    #call main function here
    generate_tree(canvas, starting_tree_values['x1'], starting_tree_values['y1'], starting_tree_values['angle'], starting_tree_values['length'], root, {'scale':scale_slider.get(), 'randomization': randomization_slider.get(),'season':selected_season.get(), 'depth': round(depth_slider.get() / 10)}, symmetric_mode)

#intro label
intro_label = CTkLabel(sidebar, text='Welcome!', text_color='black', font=('Arial', 13))
intro_label.pack()

#Creat new tree button
reset_to_default_button = CTkButton(sidebar, text='Grow a Tree!', command=lambda:reset_to_default(depth_slider, scale_slider, randomization_slider, start_tree_generation, radio_buttons))
reset_to_default_button.pack()
ToolTip(reset_to_default_button, msg="Press to grow a tree")

sub_intro_label = CTkLabel(sidebar, text='Use Arrow Keys To Move Around', text_color='black', font=('Arial', 11)).pack()

#zoom in commands for clicking
canvas.bind('<Button-1>', lambda event: handle_zoom(event, canvas, ALL))
canvas.bind(f'<Button-{2 if platform.system() == "Darwin" else 3}>', lambda event:handle_zoom(event, canvas, ALL))

#Depth slider Label
depth_label = CTkLabel(sidebar, text='Tree depth', text_color='black')
depth_label.pack()

#Slider to choose depth
depth_slider = CTkSlider(sidebar, from_=0, to=110, orientation='horizontal', command=start_tree_generation)
depth_slider.set(0)
depth_slider.pack()
ToolTip(depth_slider, msg="Slide to change the depth of the tree")

#scale Slider Label
scale_slider_label = CTkLabel(sidebar, text='Tree size', text_color='black')
scale_slider_label.pack()

#Slider to choose scale
scale_slider = CTkSlider(sidebar, from_=40, to=88, orientation='horizontal', command=start_tree_generation)
scale_slider.set(0)
scale_slider.pack()
ToolTip(scale_slider, msg="Slide to change the size of the tree")

#randomization Slider Label
randomization_slider_label = CTkLabel(sidebar, text='Split angel', text_color='black')
randomization_slider_label.pack()

#Slider to choose randomization
randomization_slider = CTkSlider(sidebar, from_=0, to=180, orientation='horizontal', command=start_tree_generation)
randomization_slider.set(0)
randomization_slider.pack()
ToolTip(randomization_slider, msg="Slide to change the angel")

#Seasons Label
seasons_label = CTkLabel(sidebar, text='Select Season', text_color='black')
seasons_label.pack()

#make the default selected season None
selected_season = StringVar()

#array to store radiobuttons so we then we can access them to perform methods on them
radio_buttons = []

#loop that creates all radio buttons
for i in range(len(seasons)):
    radio = CTkRadioButton(sidebar, text=seasons[i], value=seasons[i], variable=selected_season, text_color='black', command=lambda:handle_season_change(canvas, selected_season.get(), start_tree_generation))
    radio.pack(pady=5)
    radio_buttons.append(radio)

#Create Random Tree Button
randomize_settings_button = CTkButton(sidebar, text="Random", command=lambda:randomize_settings(depth_slider, scale_slider, randomization_slider, start_tree_generation, radio_buttons))
randomize_settings_button.pack(pady=10)
ToolTip(randomize_settings_button, msg="Click to randomize the sittings") 

#reset everyhting to default button
reset_to_default_button = CTkButton(sidebar, text='Reset', command=lambda:reset_to_default(depth_slider, scale_slider, randomization_slider, start_tree_generation, radio_buttons))
reset_to_default_button.pack()
ToolTip(reset_to_default_button, msg="Click to reset to default settings")

#swicth to turn on symmetric mode
symmetric_switch = CTkSwitch(sidebar, text="Symmetric Mode", variable=symmmetric_mode_switch, onvalue="on", offvalue="off", text_color='black')
symmetric_switch.pack(pady=10)

#label for zooming in buttons
zoom_buttons_label = CTkLabel(sidebar, text="Zoom In/Out", text_color='black')
zoom_buttons_label.pack(pady=10)

#buttons to zoom in and out
segmented_button_var = StringVar(value="Value 1")
segmented_button = CTkSegmentedButton(sidebar, values=["+", "-"], variable=segmented_button_var)
segmented_button.configure(command=lambda value: handle_zoom_buttons(value, segmented_button, canvas, ALL))
segmented_button.pack()

sub_intro_label = CTkLabel(sidebar, text='To learn more:', text_color='black', font=('Arial', 11)).pack()

#Adding a clickable link to the sidebar
link1 = Label(sidebar, text="Fractals ", fg="blue", cursor="hand1")
link1.pack()
link1.bind("<Button-1>", lambda e: open_link("https://brilliant.org/wiki/fractals/"))

link2 = Label(sidebar, text="Symmetric Binary Tree", fg="blue", cursor="hand1")
link2.pack()
link2.bind("<Button-1>", lambda e: open_link("https://larryriddle.agnesscott.org/ifs/pythagorean/symbinarytree.htm"))

link3 = Label(sidebar, text="Fractal canopy", fg="blue", cursor="hand1")
link3.pack()
link3.bind("<Button-1>", lambda e: open_link("https://en.wikipedia.org/wiki/Fractal_canopy"))



sub_intro_label = CTkLabel(sidebar, text='Beta version, work in progress!', text_color='black', font=('Arial', 11)).pack()
sub_intro_label = CTkLabel(sidebar, text='V. 1.0', text_color='black', font=('Arial', 11)).pack()
# Bind arrow key events to the xview_scroll and yview_scroll methods of the canvas
canvas.bind("<Left>", lambda event: canvas.xview_scroll(-1, "units"))
canvas.bind("<Right>", lambda event: canvas.xview_scroll( 1, "units"))
canvas.bind("<Up>",   lambda event: canvas.yview_scroll(-1, "units"))
canvas.bind("<Down>", lambda event: canvas.yview_scroll( 1, "units"))

# Give focus to the canvas so the arrows can trigger
canvas.focus_set()

root.mainloop()
