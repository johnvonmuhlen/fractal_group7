from tkinter import *
from generate_tree import generate_tree

root = Tk()
canvas = Canvas(root,width=800, height=600)
canvas.pack(fill=BOTH, expand=True, side='right')
root.title("Group 7 Tree Fractal")

# sidebar
sidebar = Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=4)
sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

#Button to generate trees
generate_tree_button = Button(sidebar, text="Start Generating New Tree", command=lambda: generate_tree(canvas, 400, 520, -90, 300, 10, 0.5, generate_tree_button, root, {'scale':slider.get(),
                                                                                                                                                                         'randomization':slider_2.get(),
                                                                                                                                                                         'season':selected_season.get()}))
generate_tree_button.pack(pady=20)

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

root.mainloop()
