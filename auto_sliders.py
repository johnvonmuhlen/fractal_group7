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