import random

#function to reset sliders to adjust recursively
def handle_sliders(slider, target_value, generate_tree, step=1, delay=25):
    current_value = slider.get()
    
    #base case
    if current_value == target_value:
        return
    
    #if current value is smaller than target value, increase it by 1 step
    if current_value < target_value:
        new_value = round(current_value + step)
     #else decrease it
    else:
        new_value = round(current_value - step)
        
    #set slider to new value
    slider.set(new_value)
    
    #call the generate tree function so the tree is updated in real time
    generate_tree()
    
    #call the function again after a delay
    slider.after(delay, handle_sliders, slider, target_value, generate_tree, step, delay)
    
#function to zoom in or out
def handle_zoom(event, canvas, ALL): 
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
def handle_zoom_buttons(value, segmented_button, canvas, ALL):
    #if + button clicked, pass an object with num=1 so the handle_zoom function can recognize if its zoom in or out
    if value == '+':
        handle_zoom(ZoomEvent(1), canvas, ALL)
    #if the other is clicked, pass three(1 = left click, 3 = right click essentially)
    else:
        handle_zoom(ZoomEvent(3), canvas, ALL)
    #reset buttons so it can be clicked multiple times
    segmented_button.set(None)
    
#function to randomize sliders
def randomize_settings(depth_slider, scale_slider, randomization_slider, start_tree_generation, radio_buttons):
    handle_sliders(depth_slider, random.randint(20, 120), start_tree_generation)
    handle_sliders(scale_slider, random.randint(40, 100), start_tree_generation)
    handle_sliders(randomization_slider, random.randint(11, 100), start_tree_generation)
    radio_buttons[random.randint(0, 4)].select()
        
#reset sliders to default
def reset_to_default(depth_slider, scale_slider, randomization_slider, start_tree_generation, radio_buttons):
    handle_sliders(depth_slider, 80, start_tree_generation)
    handle_sliders(scale_slider, 70, start_tree_generation)
    handle_sliders(randomization_slider, 45, start_tree_generation)
    radio_buttons[4].select()