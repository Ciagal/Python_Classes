#!/usr/bin/env python3

import os, os.path

def main():  
    count = 0

    dir_path = '/Users/ciagal/desktop/studia/sem7/python'

    for folder_element in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, folder_element)):
            count += 1
    print('file count: ', count)
if __name__ == '__main__':
    main()