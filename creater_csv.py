import csv
import random

def generate_random_values():
    current_value = 22.0
    values = []

    for _ in range(365):
        current_value += random.uniform(-1.5, 1.5)
        current_value = min(28.0, max(22.0, current_value))  # Ensure the value stays between 22 and 28
        values.append(round(current_value, 2))

    return values

def write_csv_file(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Day', 'RandomValue']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for day, value in enumerate(generate_random_values(), start=1):
            writer.writerow({'Day': day, 'RandomValue': value})

if __name__ == "__main__":
    file_name = "random_values.csv"
    write_csv_file(file_name)
    print(f"File '{file_name}' has been successfully generated.")
