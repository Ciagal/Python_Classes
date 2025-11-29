#!/usr/bin/env python3

import getpass

def main():
    print("==Setup==\n")
    print ("Setup your code: ")
    code = getpass.getpass()
    print("Confirm your code:")
    retype = getpass.getpass()
    
    while retype != code:
        
        print("\nTry again.")
        print("\n==Setup==\n")
        print ("Setup your code: ")
        code = getpass.getpass()
        print("Confirm your code:")
        retype = getpass.getpass()
    
    print("\n==Verify==")
    print("\nProvide your code: ")
    
    attempt = getpass.getpass()
    
    if attempt == retype:
        print("\nUnlocked.")
    else:
        print("\nAborted.")

if __name__ == '__main__':
    main()
