#!/usr/bin/env python3


def dot_product(vec1,vec2):
    #yeah, hardcoding, but task provided 4-element vector
    return (vec1[0] * vec2 [0]) + (vec1[1] * vec2 [1]) + (vec1[2] * vec2 [2]) + (vec1[3] * vec2 [3])

def main():
    vec1 = [1, 2, 12, 4]
    vec2 = [2, 4, 2, 8] 

    print(dot_product(vec1,vec2))

if __name__ == '__main__':
    main()