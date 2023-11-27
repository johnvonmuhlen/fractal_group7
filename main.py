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
generate_tree_button = Button(sidebar, text="Start Generating New Tree", command=lambda: generate_tree(canvas, 400, 520, -90, 300, 10, 0.5, generate_tree_button, root))
generate_tree_button.pack(pady=20)

root.mainloop()
