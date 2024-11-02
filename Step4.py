import json
from typing import List, Dict, Any

def sort_bicycles(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sorts bicycle data by price (ascending), and then by weight if prices are equal."""
    sorted_bikes = sorted(
        data,
        key=lambda x: (
            x.get("price_gbp") if x.get("price_gbp") is not None else float('inf'), 
            x.get("weight_kg") if x.get("weight_kg") is not None else float('inf')
        )
    )
    
    sorted_output = [
        {"model_id": entry["model_id"], "price_gbp": entry["price_gbp"], "weight_kg": entry["weight_kg"]}
        for entry in sorted_bikes
    ]
    
    return sorted_output

def write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
    """Writes sorted bicycle data to a specified output file in JSON format."""
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

def main() -> None:
    """Main function to read bicycle data, sort it by price and weight, and write the result."""
    input_file = "./cleaned_data.json"
    output_file = "./sorted_bicycles.json"

    try:
        with open(input_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not a valid JSON.")
        return

    sorted_bicycles = sort_bicycles(data)
    write_data_to_file(sorted_bicycles, output_file)
    print("Sorted bicycles have been written to sorted_bicycles.json")

if __name__ == "__main__":
    main()
