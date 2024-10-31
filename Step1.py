import json

def clean_bike_data(data):
    """Cleans and filters the bike data."""
    # Filtering entries based on required fields
    filtered_data = [
        entry for entry in data
        if entry.get("model_id") is not None
        and entry.get("price_gbp") is not None
        and entry.get("weight_kg") is not None
        and entry.get("in_stock") is not None
    ]

    unique_model_ids = set()
    final_data = []

    # Ensure unique model IDs
    for entry in filtered_data:
        if entry["model_id"] not in unique_model_ids:
            unique_model_ids.add(entry["model_id"])
            final_data.append(entry)

    # Rename model_name for model_id 9
    for entry in final_data:
        if entry["model_id"] == 9:
            entry["model_name"] = "Summit Strider"

    return final_data

def read_data_from_file(file_path):
    """Reads bike data from a JSON file."""
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def write_data_to_file(data, file_path):
    """Writes cleaned bike data to a JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# File paths
input_file = "bike_data.json"  # Input JSON file with bike data
output_file = "cleaned_data.csv"  # Output JSON file for cleaned data

# Read the data from the input file
data = read_data_from_file(input_file)

# Clean the data
cleaned_data = clean_bike_data(data)

# Write the cleaned data to the output file
write_data_to_file(cleaned_data, output_file)

print("Cleaned data has been written to cleaned_data.json")
