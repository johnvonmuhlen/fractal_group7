import random

#default tree values passed to generate tree
starting_tree_values = {'x1': 400,
                        'y1': 650,
                        'angle': -90,
                        'length':200,
                        }

#Create Radio Buttons
seasons = ['Summer', 'Autumn', 'Winter', 'Spring', 'None']

#values passed when crazy tree is created
random_tree_values = { 'scale':70,
                        'randomization':random.randint(100, 150),
                        'season':random.choice(seasons),
                        'depth': 10
                        }
