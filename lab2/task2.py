#!/usr/bin/env python3

import os 
def main():  
    # List to store all  
    # directories 
    L = []
  
    # Traversing through Test 
    for root, dirs, files in os.walk('/Users/ciagal/desktop'): 
  
    # Adding the empty directory to 
    # list 
        L.append((root, dirs, files)) 

    print("List of all sub-directories and files:") 
    for i in L:
        print(i)
if __name__ == '__main__':
    main()