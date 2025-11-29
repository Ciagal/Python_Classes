#!/usr/bin/env python3
import math

def roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return "No solutions in R"

    delta_sqr = math.sqrt(delta)
    x_1 = ((-b) + delta_sqr) / (2 * a)
    x_2 = ((-b) - delta_sqr) / (2 * a)

    return [x_1, x_2]

def main():
    temp_input = input("Provide elements a, b and c: ").strip()
    elements = temp_input.split()

    if len(elements) != 3:
        print("Invalid input. Please provide a, b, and c.")
        return
    
    a, b, c = map(float, elements)
    print(roots(a, b, c))

if __name__ == '__main__':
    main()