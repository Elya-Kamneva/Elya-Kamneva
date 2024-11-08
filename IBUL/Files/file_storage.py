#сохранение данных итерации
import json
import os

def save_data(data, filename='init_data.json'):
    """Saves data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data saved to {filename}")

def load_data(filename='init_data.json'):
    """Loads data from a JSON file, creating the file if it does not exist."""
    # Check if the file exists
    if not os.path.exists(filename):
        # If file doesn't exist, create it with default empty data
        print(f"{filename} not found. Creating file with default data.")
        default_data = {
            "start_amount": 100,
            "start_number": 200
        }  # You can set your own default data here
        save_data(default_data, filename)
        return default_data

    # Load and return data if the file exists
    with open(filename, 'r') as file:
        data = json.load(file)
    print(f"Data loaded from {filename}")
    return data
