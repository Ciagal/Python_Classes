#!/usr/bin/env python3

import numpy as np

def main():
    A = np.random.randint(0, 101, (128, 128))
    B = np.random.randint(0, 101, (128, 128))

    C = A + B

    print(A[:2, :5])   
    print(B[:2, :5])
    print(C[:2, :5])
    
if __name__ == '__main__':
    main()