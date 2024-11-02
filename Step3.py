import json
from typing import List, Dict, Any

def count_per_brand(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Counts the occurrences of each brand in the provided data."""
    brand_count = {}
    for entry in data:
        brand = entry.get("brand")
        if brand:
            brand_count[brand] = brand_count.get(brand, 0) + 1
    return brand_count

def write_data_to_file(data: Dict[str, int], output_file: str) -> None:
    """Writes the brand count data to a specified output file in JSON format."""
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

def main() -> None:
    """Main function to read data, count brand occurrences, and write the result."""
    input_file = "./cleaned_data.json"
    output_file = "./brand_counts.json"

    try:
        with open(input_file, "r") as file:
            cleaned_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not a valid JSON.")
        return

    brand_counts = count_per_brand(cleaned_data)
    write_data_to_file(brand_counts, output_file)
    print("Brand counts have been written to brand_counts.json")

if __name__ == "__main__":
    main()
