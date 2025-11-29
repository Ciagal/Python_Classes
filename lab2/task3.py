#!/usr/bin/env python3

from PIL import Image
import sys
import os

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir(directory):
        print(f"Error: directory '{directory}' does not exist.")
        return
    
    jpg_counter = 0
    
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            jpg_counter += 1
    
    if (jpg_counter == 0):
        print("\nThere's no JPG files.")
        return
    
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            prefix = filename.split(".jpg")[0]
            im = Image.open(filename)
            im.save(prefix+'.png')
        else:
            continue
if __name__ == '__main__':
    main()
