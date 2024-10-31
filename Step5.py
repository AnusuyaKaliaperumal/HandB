import json
from typing import List, Dict, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def transform_price_per_weight(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    updated_bikes = []
    
    for entry in data:
        new_entry = entry.copy()
        weight = entry.get("weight_kg")
        price = entry.get("price_gbp")
        
        if weight is not None and weight > 0:
            new_entry["price_per_weight"] = price / weight if price is not None else None
        else:
            new_entry["price_per_weight"] = None
        
        updated_bikes.append(new_entry)
    
    return updated_bikes

def write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
    with open(output_file, "w") as file:
        json.dump(data, file, indent=2)

def main() -> None:
    input_file = "./cleaned_data.json"
    output_file = "./transformed_bicycles.json"

    try:
        with open(input_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        logging.error(f"The file {input_file} was not found.")
        return
    except json.JSONDecodeError:
        logging.error(f"The file {input_file} is not a valid JSON.")
        return

    transformed_bicycles = transform_price_per_weight(data)
    write_data_to_file(transformed_bicycles, output_file)
    logging.info("Transformed bicycles have been written to %s", output_file)

if __name__ == "__main__":
    main()
