# data_processor.py
import numpy as np


def generate_large_data(size):
    """
    Generates a large matrix of random floats.
    """
    return np.random.rand(size, size)


def matrix_multiply(matrix_a, matrix_b):
    """
    Multiplies two matrices.
    """
    return np.dot(matrix_a, matrix_b)
