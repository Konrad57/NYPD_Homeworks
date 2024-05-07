import os
import csv
import random


def create_folder_structure(root_folder):
    """
    Create folder structure with subfolders and a 'Solutions.csv' file in each subfolder.

    Args:
        root_folder (str): Root folder where the folder structure will be created.
    """
    # List of weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Create folders for each weekday
    for weekday in weekdays:
        weekday_folder = os.path.join(root_folder, weekday)
        os.makedirs(weekday_folder, exist_ok=True)

        # Create morning and evening subfolders
        for time_of_day in ['morning', 'evening']:
            time_folder = os.path.join(weekday_folder, time_of_day)
            os.makedirs(time_folder, exist_ok=True)

            # Create 'Solutions.csv' file in each subfolder
            with open(os.path.join(time_folder, 'Solutions.csv'), 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(["Model", "Output value", "Time of computation"])
                model = random.choice(['A', 'B', 'C'])
                output_value = random.randint(0, 1000)
                time_of_computation = f"{random.randint(0, 1000)}s"
                csvwriter.writerow([model, output_value, time_of_computation])


def sum_time_of_computation(root_folder, model='A'):
    """
    Calculate the sum of "Time of computation" for the given model.

    Args:
        root_folder (str): Root folder where the folder structure is created.
        model (str): Model name for which the sum of "Time of computation" is to be calculated.

    Returns:
        total_time (int): Sum of "Time of computation" for the given model.
    """
    total_time = 0

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file == 'Solutions.csv':
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    next(csvreader)  # Skip header
                    for row in csvreader:
                        if row[0].strip() == model:
                            total_time += int(row[2].strip()[:-1])  # Remove 's' and convert to int
    return total_time


# Part A
root_folder = os.path.join(os.getcwd(), "Weekdays")
create_folder_structure(root_folder)

# Part B
total_time_model_A = sum_time_of_computation(root_folder)
print("Total time of computation for model A:", total_time_model_A, "s")
