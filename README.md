# Bicycle Inventory Data Processing

## Objective

This project processes bicycle inventory data contained in the `bicycle_inventory.json` file. The goal is to perform various operations on the dataset using appropriate data structures while ensuring data integrity.

## Data

The dataset is a list of data objects representing bicycle store inventory items. Below is an example of the data structure:

```json
[
  {"model_id": 1, "model_name": "Trailblazer 3000", "brand": "CycloX", "type": "Road Bike", "price_gbp": 936, "weight_kg": 13.5, "in_stock": true},
  {"model_id": 2, "model_name": "Speedster Pro", "brand": "RoadFlex", "type": "Road Bike", "price_gbp": null, "weight_kg": 7.8, "in_stock": false},
  {"model_id": 3, "model_name": "Hybrid Elite", "brand": "UrbanRide", "type": "Hybrid Bike", "price_gbp": 585, "weight_kg": null, "in_stock": null},
  {"model_id": 4, "model_name": "Climber 500", "brand": "HillMaster", "type": "Mountain Bike", "price_gbp": 1053, "weight_kg": 14.0, "in_stock": true},
  {"model_id": 5, "model_name": "City Cruiser", "brand": "UrbanRide", "type": "Hybrid Bike", "price_gbp": 468, "weight_kg": 11.5, "in_stock": true},
  {"model_id": null, "model_name": "Sprint King", "brand": "SpeedRacer", "type": "Road Bike", "price_gbp": 2496, "weight_kg": 8.0, "in_stock": false},
  {"model_id": 7, "model_name": "All-Terrain", "brand": "CycloX", "type": "Mountain Bike", "price_gbp": 858, "weight_kg": 16.0, "in_stock": true},
  {"model_id": 8, "model_name": "Roadster", "brand": "SpeedRacer", "type": "Road Bike", "price_gbp": null, "weight_kg": 10.2, "in_stock": true},
  {"model_id": 9, "model_name": null, "brand": "HillMaster", "type": "Mountain Bike", "price_gbp": 720, "weight_kg": 10.0, "in_stock": true},
  {"model_id": 10, "model_name": "Urban Comet", "brand": "CityRide", "type": "Hybrid Bike", "price_gbp": 720, "weight_kg": 11.0, "in_stock": true},
  {"model_id": 11, "model_name": "Speed Racer X", "brand": "RoadFlex", "type": "Road Bike", "price_gbp": 1499, "weight_kg": 7.5, "in_stock": false},
  {"model_id": 12, "model_name": "Trail Master 500", "brand": "CycloX", "type": "Mountain Bike", "price_gbp": 980, "weight_kg": 14.0, "in_stock": true}
]
Data Constraints
Each entry in the dataset should adhere to the following constraints:

The following fields should be populated:
model_id
price_gbp
weight_kg
in_stock
model_id must be unique across the dataset.
Tasks
1. Data Cleanup
Implement a function or method that removes or quarantines entries that don't adhere to the expected data structure and constraints. This function should be called before performing other data manipulations to ensure the validity of the dataset.

Example Script
python
Copy code
import json
import logging
import os
from typing import List, Dict

logging.basicConfig(level=logging.INFO)

def clean_bike_data(data: List[Dict]) -> List[Dict]:
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
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info("Cleaned data has been successfully written to %s", file_path)
    except IOError as e:
        logging.error(f"Failed to write data to {file_path}: {e}")
        raise

def main():
    input_file = "./bike_data.json"
    output_file = "./cleaned_data.json"

    try:
        data = read_data_from_file(input_file)
        cleaned_data = clean_bike_data(data)
        write_data_to_file(cleaned_data, output_file)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
