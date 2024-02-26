import os
from time import sleep

while True:
    to_open = input("Which file to open? ") 
    try:
        f = open(to_open)
        break
    except:
        print ("Bad input.")
    
text = "██"

#creates a whole frame as a string to avoid flickering
def create_frame(data):
    current_y = 0
    frame = ""
    for d in data:
        pixel_data = d.split(",")
        try:
            x, y, r, g, b = int(pixel_data[0]), int(pixel_data[1]), int(pixel_data[2]), int(pixel_data[3]), int(pixel_data[4])
        except:
            pass
        if y != current_y:
            frame += "\n"
        colored_text = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
        frame += colored_text

        current_y = y
    return frame



def player(data):
    while True:
        for pixel in pixels:
            print (create_frame(pixel), end='\r')
            sleep(0.03)


    
lines = f.readlines()
pixels = [x.strip().split("#") for x in lines]

player(pixels)