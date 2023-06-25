import sys
import os
from PIL import Image

# grab first and second argument
try:
    old_jpg_folder = sys.argv[1]
    new_png_folder = sys.argv[2]

    # check if new/ exists, if not create it
    if not os.path.exists(new_png_folder):
        os.mkdir(new_png_folder)

    # loop through Pokedex
    if os.path.exists(old_jpg_folder):
        for file in os.listdir(old_jpg_folder):
            #check if its jpg
            if not file.endswith(".jpg"):
                continue
            # convert images to png
            img = Image.open("./"+old_jpg_folder+"/"+file)
            clean_name = os.path.splitext(file)[0]
            #  save to the new folder
            img.save("./"+new_png_folder+"/"+clean_name+".png", "png")
except IndexError:
    print("Please provide the folder name")



