#!/usr/bin/env python3

import datetime

def main():
    temp_input = input("What is your name first name, last name and year of brith?\n").strip()

    parts = temp_input.split()

    if len(parts) != 3:
        print("Invalid input. Please provide first name, last name, and year of birth.")
        return
    
    first, last, year_str = parts
    
    try:
        year = int(year_str)
    except ValueError:
        print("Invalid year of birth. Please enter a integer number.")
        return

    current_year = datetime.datetime.now().year


    if year > current_year:
        print("Invalid year of birth. Please enter a valid year.")
        return

    age = current_year - year

    print(f"Hello I'm {first} {last} and I've got {age} years old")

if __name__ == '__main__':
    main()