import json
import logging
import os
from typing import List, Dict

logging.basicConfig(level=logging.INFO)

def clean_bike_data(data: List[Dict]) -> List[Dict]:
    """Cleans and filters bike data, ensuring unique model IDs and required fields."""
    unique_model_ids = set()
    final_data = []
    for entry in data:
        if (
            entry.get("model_id") is not None
            and entry.get("price_gbp") is not None
            and entry.get("weight_kg") is not None
            and entry.get("in_stock") is not None
            and entry["model_id"] not in unique_model_ids
        ):
            unique_model_ids.add(entry["model_id"])
            final_data.append(entry)
    return final_data

def read_data_from_file(file_path: str) -> List[Dict]:
    """Reads JSON data from the specified file path."""
    if not os.path.exists(file_path):
        logging.error(f"The file {file_path} does not exist.")
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, "r") as f:
        try:
            data = json.load(f)
            logging.info("Data successfully read from %s", file_path)
            return data
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from {file_path}: {e}")
            raise

def write_data_to_file(data: List[Dict], file_path: str):
    """Writes JSON data to the specified file path."""
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info("Cleaned data has been successfully written to %s", file_path)
    except IOError as e:
        logging.error(f"Failed to write data to {file_path}: {e}")
        raise

def main():
    """Main function to read, clean, and write bike data."""
    input_file = "./bike_data.json"
    output_file = "./cleaned_data.json"
    try:
        data = read_data_from_file(input_file)
        cleaned_data = clean_bike_data(data)
        write_data_to_file(cleaned_data, output_file)
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
