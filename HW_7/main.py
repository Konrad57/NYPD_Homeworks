import time
from data_processor import generate_large_data, matrix_multiply


def main():
    start_time = time.time()

    # Generate large data matrices
    print("Generating data...")
    matrix_a = generate_large_data(10000)  # Adjust size as needed for profiling
    matrix_b = generate_large_data(10000)

    # Perform matrix multiplication
    print("Multiplying matrices...")
    result = matrix_multiply(matrix_a, matrix_b)

    # Measure the time taken and print it
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
