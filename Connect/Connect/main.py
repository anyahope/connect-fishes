
#always set screen first before importing game library and working on game design
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50}, {50}' #positioning of screen

import random
import pgzrun

#set length and height of screen
WIDTH = 1000 
HEIGHT = 600

current_fish = 0  #marks index / (position in list) of fish being clicked
line_coordinates = []
number_of_fishes = 15

character_list = [] #store characters inside this list
characters_images = ["fish1", "fish2", "fish3", "fish4", "shark1", "shark2", "starfish1", "starfish2", "turtle1", "turtle2"]
for i in range(number_of_fishes):
    image = random.choice(characters_images)
    character = Actor(image)
    x = random.randint(20, 950)
    y = random.randint(10, 550)
    character.pos = (x, y)
    character_list.append(character)

############################################################################

def draw():
    screen.clear()
    screen.blit('background2', (0, 0))

    count = 1

    for character in character_list: #fetch each thing in list one by one
        character.draw() #draw image --> Actor cannot be 'printed' on window
        screen.draw.text(str(count), (character.pos[0], character.pos[1] + 35), color = 'black')
        count = count + 1
    
    for i in line_coordinates:
        #i is not an individual value, but a list with two tuples. each tuple has two values x and y. 
        #first tuple is starting of line, second tuple is ending of the line.
        print(i) 
        screen.draw.line(i[0], i[1], (0, 0, 0))

###########################################################################

def on_mouse_down(pos): #POS is point mouse is clicked 
    global current_fish, line_coordinates
    if current_fish < number_of_fishes:
        if character_list[current_fish].collidepoint(pos):
            if current_fish > 0:
                line_coordinates.append([character_list[current_fish -1].pos, character_list[current_fish].pos])
            current_fish = current_fish + 1
            #print(line_coordinates)
        else:
            line_coordinates = []
            current_fish = 0






pgzrun.go()
