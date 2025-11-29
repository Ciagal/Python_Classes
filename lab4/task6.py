#!/usr/bin/env python3

import numpy as np

def main():

    # generation
    A = np.random.randint(0, 10, (8, 8))

    # computing det using numpy
    det_A = np.linalg.det(A)

    print("Matrix A:\n", A)
    print("\nDeterminant of Matrix A:", det_A)

if __name__ == '__main__':
    main()