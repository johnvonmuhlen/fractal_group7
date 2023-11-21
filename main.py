from tkinter import *
import random
import math
#hello its me
#functions to update the tree thorugh user input not wokring
#TODO: fix user input

def draw_tree(canvas, x1, y1, angle, length, depth, scale):
 if depth == 0:
   return

 x2 = x1 + length * math.cos(math.radians(angle)) * scale
 y2 = y1 + length * math.sin(math.radians(angle)) * scale

 canvas.create_line(x1, y1, x2, y2, width=3, smooth=True)

 canvas.after(500, draw_tree, canvas, x2, y2, angle - random.randint(10, 45), length * 0.7, depth - 1, scale)
 canvas.after(500, draw_tree, canvas, x2, y2, angle + random.randint(10, 45), length * 0.7, depth - 1, scale)

def update_scale(scale):
 scale_factor = float(scale) / 100
 canvas.delete("all")
 draw_tree(canvas, 400, 600, -90, 300, 10, scale_factor)

def update_tree(event):
 value = int(entry.get())
 canvas.delete("all")
 draw_tree(canvas, 400, 600, -90, 300, value, 1)

root = Tk()
canvas = Canvas(root, width=800, height=600)
canvas.pack()
root.title("Group 7 Tree Fractal")

scale = Scale(root, from_=50, to=200, orient='horizontal')
scale.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Draw Tree", command=update_tree)
button.pack()

update_scale(scale.get())

root.mainloop()
