import json
import logging
import os
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)

def clean_bike_data(data: List[Dict]) -> List[Dict]:
    """
    Cleans and filters the bike data.
    
    Parameters:
        data (List[Dict]): Raw bike data entries.
    
    Returns:
        List[Dict]: Cleaned bike data with unique model IDs.
    """
    unique_model_ids = set()
    final_data = []

    for entry in data:
        # Ensure required fields are present
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
    """Reads bike data from a JSON file."""
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
    """Writes cleaned bike data to a JSON file."""
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info("Cleaned data has been successfully written to %s", file_path)
    except IOError as e:
        logging.error(f"Failed to write data to {file_path}: {e}")
        raise

def main():
    # File paths
    input_file = "./bike_data.json"
    output_file = "./cleaned_data.json"


    # Read the data from the input file
    try:
        data = read_data_from_file(input_file)
        # Clean the data
        cleaned_data = clean_bike_data(data)
        # Write the cleaned data to the output file
        write_data_to_file(cleaned_data, output_file)
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        logging.error("An error occurred: %s", e)

# Entry point for the script
if __name__ == "__main__":
    main()
