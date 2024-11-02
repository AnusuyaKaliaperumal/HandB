import json
from typing import List, Dict, Any

def read_data_from_file(input_file: str) -> List[Dict[str, Any]]:
    """Reads JSON data from the specified input file."""
    try:
        with open(input_file, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not a valid JSON.")
        return []

def filter_mountain_bikes(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filters data to include only mountain bikes under £1000 and in stock."""
    filtered_bikes = [
        entry for entry in data
        if entry.get("type") == "Mountain Bike"
        and (entry.get("price_gbp") is not None and entry["price_gbp"] <= 1000)
        and entry.get("in_stock") is True
    ]
    return filtered_bikes

def write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
    """Writes filtered data to the specified output file in JSON format."""
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

def main() -> None:
    """Main function to read, filter, and write mountain bike data."""
    input_file = "./cleaned_data.json"
    output_file = "./filtered_bikes.json"
    cleaned_data = read_data_from_file(input_file)
    filtered_bikes = filter_mountain_bikes(cleaned_data)
    write_data_to_file(filtered_bikes, output_file)
    print("Filtered mountain bikes have been written to filtered_bikes.json")

if __name__ == "__main__":
    main()
