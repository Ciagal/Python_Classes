#!/usr/bin/env python3

import numpy as np

def main():
    
    #generation
    A = np.random.randint(0, 10, (8, 8))
    B = np.random.randint(0, 10, (8, 8))

    #multiplying using numpy
    C = np.matmul(A, B)

    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)
    print("\nMatrix A * B =\n", C)
    
if __name__ == '__main__':
    main()