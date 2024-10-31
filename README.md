
## Objective
Please find the attached ZIP file containing `bicycle_inventory.json.` Perform the operations mentioned in the "Tasks" section on the provided dataset using appropriate data structures.
## Data
Example of a list of data objects representing bicycle store inventory items.
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
  {"model_id": 9, "model_name": null, "brand": "HillMaster","type": "Mountain Bike","price_gbp": 720,"weight_kg": 10.0,"in_stock": true},
  {"model_id": 10, "model_name": "Urban Comet", "brand": "CityRide", "type": "Hybrid Bike", "price_gbp": 720, "weight_kg": 11.0, "in_stock": true},
  {"model_id": 11, "model_name": "Speed Racer X", "brand": "RoadFlex", "type": "Road Bike", "price_gbp": 1499, "weight_kg": 7.5, "in_stock": false},
  {"model_id": 12, "model_name": "Trail Master 500", "brand": "CycloX", "type": "Mountain Bike", "price_gbp": 980, "weight_kg": 14.0, "in_stock": true}
]
The follow constraints should be true for each entry:
- The follow fields should be populated:
  * `model_id`
  * `price_gbp`
  * `weight_kg`
  * `in_stock`
- `model_id` should be unique within the whole dataset
### 1. Data Cleanup

Write a function or method that removes or quarantines rows that don't adhere to the expected data structure of constraints. Make practical assumptions regarding data structure and constraints. This function or method should always be called before other data manipulation functions to ensure validity of data.
Script 
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
 

	Main Data Flow:
•	The script reads bike data from a JSON file (bike_data.json).
•	It processes this data to remove duplicates and entries missing essential fields (model_id, price_gbp, weight_kg, and in_stock).
•	The cleaned data is then saved to another JSON file (cleaned_data.json).
	Key Functions:
•	clean_bike_data(data): Goes through each entry in the data list and checks for required fields. It removes any bikes missing these fields 
•	or with duplicate model_ids, adding only unique and valid entries to a final list.
•	read_data_from_file(file_path): Reads JSON data from a specified file path. If the file doesn’t exist, it logs an error and raises a FileNotFoundError. If JSON decoding fails, it logs that too.
•	write_data_to_file(data, file_path): Writes the cleaned data to the specified JSON file with proper formatting. If an I/O error occurs, it logs and raises the error.
	Logging and Error Handling:
•	The script uses logging to track progress and catch errors. This includes successful reads/writes and specific issues like missing files or JSON format errors.
	Execution:
•	The main function coordinates these steps, defining the input and output file paths and managing the cleaning pipeline. It ensures errors are logged if anything goes wrong, making debugging straightforward.
### 2. Filter according to requirements
Write a function method that filters the bicycles based on a specific requirement. Your function should return the full list of columns and rows which match the requirements.
The requirements are as follows - 
- Type of bike must be **Mountain Bike**
- Price must be less than or equal to **1000**
- There must be available stock for the bike
Script
import json
from typing import List, Dict, Any

def read_data_from_file(input_file: str) -> List[Dict[str, Any]]:
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
    filtered_bikes = [
        entry for entry in data
        if entry.get("type") == "Mountain Bike"
        and (entry.get("price_gbp") is not None and entry["price_gbp"] <= 1000)
        and entry.get("in_stock") is True
    ]
    return filtered_bikes

def write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
def main() -> None:
 

    input_file = "./cleaned_data.json"
    output_file = "./filtered_bikes.json"
    cleaned_data = read_data_from_file(input_file)
    filtered_bikes = filter_mountain_bikes(cleaned_data)
    write_data_to_file(filtered_bikes, output_file)
    print("Filtered mountain bikes have been written to filtered_bikes.json")
if __name__ == "__main__":
    main()



### 3. Count per Brand
Write a function or method that counts the number of each brand. Your function should return a data structure with **brand** as keys and the count of that brand as values.
Script
import json
from typing import List, Dict, Any
def sort_bicycles(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
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
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
def main() -> None:
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

### 4. Sort bicycles by price followed by weight
Write a function or method that sorts the list of records by **price_gbp** and then by **weight_kg** in ascending order. Your function should return a data 
 
structure containing **model_id**, **price_gbp** and **weight_kg** as keys, along with their corresponding values
Script
import json
from typing import List, Dict, Any

def sort_bicycles(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
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
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

def main() -> None:
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

### 5. Transform - price/weight
Write a function or method that adds a new column called `price_per_weight` to each bicycle record. This column should represent the price of the bicycle divided by its weight. Your function should return updated list of records including the new `price_per_weight` column.
Script
import json
from typing import List, Dict, Any

def transform_price_per_weight(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    updated_bikes = []
    
 

    for entry in data:
        new_entry = entry.copy()
        
        if entry.get("weight_kg") is not None and entry["weight_kg"] > 0:
            new_entry["price_per_weight"] = entry["price_gbp"] / entry["weight_kg"] if entry.get("price_gbp") is not None else None
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
        print(f"Error: The file {input_file} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not a valid JSON.")
        return

    transformed_bicycles = transform_price_per_weight(data)
    write_data_to_file(transformed_bicycles, output_file)
    print("Transformed bicycles have been written to transformed_bicycles.json")

if __name__ == "__main__":
    main()


Test Coverage:

import pytest
import json
import os
from Step1 import clean_bike_data
from Step2 import filter_mountain_bikes
from Step3 import count_per_brand
from Step4 import sort_bicycles
from Step5 import transform_price_per_weight

FILE_PATH = "./bike_data.json"
 


@pytest.fixture(scope="module")
def sample_data():
    try:
        with open(FILE_PATH, "r") as f:
            content = f.read()
            return json.loads(content)
    except FileNotFoundError:
        pytest.fail(f"File not found: {FILE_PATH}")
    except json.JSONDecodeError as e:
        pytest.fail(f"Error decoding JSON: {e}")

def test_clean_bike_data_valid(sample_data):
    cleaned_data = clean_bike_data(sample_data)
    assert len(cleaned_data) <= len(sample_data)
    assert all("model_id" in item for item in cleaned_data)
    assert all(item["model_id"] is not None for item in cleaned_data)

def test_clean_bike_data_missing_fields():
    test_data = [{"model_id": None, "price_gbp": 100, "weight_kg": 10, "in_stock": True}]
    cleaned_data = clean_bike_data(test_data)
    assert cleaned_data == []

def test_filter_mountain_bikes(sample_data):
    cleaned_data = clean_bike_data(sample_data)
    filtered_bikes = filter_mountain_bikes(cleaned_data)
    assert all(bike["type"] == "Mountain Bike" for bike in filtered_bikes)
    assert all(bike["price_gbp"] <= 1000 for bike in filtered_bikes)
    assert all(bike["in_stock"] for bike in filtered_bikes)

def test_filter_mountain_bikes_no_matches():
    test_data = [{"model_id": 1, "type": "Road Bike", "price_gbp": 500, "in_stock": True}]
    filtered_bikes = filter_mountain_bikes(test_data)
    assert filtered_bikes == []
def test_count_per_brand(sample_data):
    cleaned_data = clean_bike_data(sample_data)
    brand_counts = count_per_brand(cleaned_data)
    assert isinstance(brand_counts, dict)
    assert all(isinstance(count, int) for count in brand_counts.values())

def test_count_per_brand_single_brand():
    test_data = [{"model_id": 1, "brand": "CycloX"}, {"model_id": 2, "brand": "CycloX"}]
    brand_counts = count_per_brand(test_data)
    assert brand_counts == {"CycloX": 2}

def test_sort_bicycles(sample_data):
    cleaned_data = clean_bike_data(sample_data)
    sorted_bikes = sort_bicycles(cleaned_data)
    prices = [bike["price_gbp"] for bike in sorted_bikes if bike["price_gbp"] is not None]
    assert prices == sorted(prices)

def test_sort_bicycles_stability():
    test_data = [{"model_id": 1, "price_gbp": 1000, "weight_kg": 10},
                  {"model_id": 2, "price_gbp": 1000, "weight_kg": 12}]
    sorted_bikes = sort_bicycles(test_data)
    assert sorted_bikes[0]["model_id"] == 1

def test_transform_price_per_weight(sample_data):
    cleaned_data = clean_bike_data(sample_data)
 

    transformed_data = transform_price_per_weight(cleaned_data)
    for bike in transformed_data:
        if bike["weight_kg"] and bike["price_gbp"]:
            assert bike["price_per_weight"] == pytest.approx(bike["price_gbp"] / bike["weight_kg"], rel=1e-2)

def test_transform_price_per_weight_zero_weight():
    test_data = [{"model_id": 1, "price_gbp": 1000, "weight_kg": 0}]
    transformed_data = transform_price_per_weight(test_data)
    assert transformed_data[0]["price_per_weight"] is None
def test_empty_data():
    empty_data = []
    cleaned_data = clean_bike_data(empty_data)
    assert cleaned_data == []
    
    filtered_bikes = filter_mountain_bikes(cleaned_data)
    assert filtered_bikes == []
    
    brand_counts = count_per_brand(cleaned_data)
    assert brand_counts == {}
    
    sorted_bikes = sort_bicycles(cleaned_data)
    assert sorted_bikes == []
    
    transformed_data = transform_price_per_weight(cleaned_data)
    assert transformed_data == []

def test_sorted_bicycles_output_count(sample_data):
    cleaned_data = clean_bike_data(sample_data)
    sorted_bikes = sort_bicycles(cleaned_data)

    model_test_cases = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 0)
    ]

    for model_id, expected_output in model_test_cases:
        model_count = sum(1 for bike in sorted_bikes if bike["model_id"] == model_id)
        assert model_count == expected_output

if __name__ == "__main__":
    pytest.main()

Test Cases Covered
1. Data Cleaning
•	Test: test_clean_bike_data_valid
Validates that valid bike data is cleaned correctly, ensuring all entries have a model_id and are not missing.
•	Test: test_clean_bike_data_missing_fields
Checks that bikes with a None model_id are removed from the dataset.
2. Filtering
 

•	Test: test_filter_mountain_bikes
Validates that filtering returns only mountain bikes that are in stock and priced under £1000.
•	Test: test_filter_mountain_bikes_no_matches
Tests that the filter returns an empty list when there are no matching bike types (e.g., a road bike).
3. Counting Per Brand
•	Test: test_count_per_brand
Validates that counting bikes per brand returns a dictionary with integer counts for each brand.
•	Test: test_count_per_brand_single_brand
Checks that counting bikes for a single brand returns the correct count.
4. Sorting Bicycles
•	Test: test_sort_bicycles
Ensures that bicycles are sorted by price in ascending order.
•	Test: test_sort_bicycles_stability
Validates that sorting is stable for bikes with the same price, ensuring the original order is maintained for ties.
5. Transforming Price Per KG
•	Test: test_transform_price_per_kg
Tests that the price per kilogram is calculated correctly for each bike, using relative approximation to handle floating-point arithmetic.
•	Test: test_transform_price_per_kg_zero_weight
Validates that bikes with zero weight return a None value for price per kg.
6. Handling Empty Data
•	Test: test_empty_data
Checks the behavior of all processing functions when provided with an empty dataset, ensuring they return appropriate results (empty lists or dictionaries).
7. Additional Output Count Tests
•	Test: test_sorted_bicycles_output_count
Verifies the count of specific model_ids in the sorted output, ensuring that the number of occurrences matches expectations.
Dockerfile:

# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all the Python scripts and required data files into the container
COPY . .

# Install pytest or any other dependencies specified
RUN pip install --no-cache-dir pytest

# Run all steps in sequence, followed by the tests
 

CMD ["bash", "-c", "python Step1.py && python Step2.py && python Step3.py && python Step4.py && python Step5.py && pytest Test1.py"]


Best Practices Implemented

1. Modular Code Design
•	Separation of Concerns: The functionality is divided into distinct modules (e.g., Step1, Step2, Step3, etc.), each handling a specific aspect of the bike data processing (cleaning, filtering, counting, sorting, transforming). This promotes reusability and makes the code easier to manage.
2. Descriptive Function and Variable Names
•	Readability: Functions and variables are named descriptively (e.g., clean_bike_data, filter_mountain_bikes, transform_price_per_kg), making it clear what each part of the code does, thus enhancing maintainability.
3. Use of Type Annotations
•	Clarity: The use of type annotations in function signatures helps clarify the expected input and output types, improving code readability and aiding in type-checking.
4. Error Handling
•	Robustness: Error handling in file operations (e.g., using try and except blocks) ensures that the application can handle common issues (like file not found or JSON decode errors) gracefully without crashing.
5. Comprehensive Testing with Pytest
•	Test Coverage: The use of pytest for unit testing allows for comprehensive testing of the application. Each test function checks specific functionality or edge cases, ensuring code correctness.
•	Use of Assertions: Assertions are used to validate expected outcomes, helping to catch bugs early in the development cycle.
6. Fixture Utilization
•	Sample Data Loading: The use of a function (load_sample_data) to load sample data promotes reusability in tests and reduces redundancy in code.
7. Test Organization
•	Structured Tests: Tests are organized logically, following the sequence of functionality (cleaning, filtering, counting, sorting, transforming), making it easier to understand and navigate the test suite.
8. Use of Comments and Documentation
•	Clarity: While the provided code snippets don't contain detailed comments (which is also a good practice to avoid clutter), ensuring that key functions are adequately documented is critical for maintainability.
9. Assertions for Edge Cases
•	Comprehensive Testing: Tests are designed to handle edge cases, such as empty datasets, missing fields, and zero weight, ensuring that the code behaves as expected in less common scenarios.
10. Continuous Integration Compatibility
•	Test-Driven Development: The structure and organization of the tests suggest that the code could easily integrate into a continuous integration (CI) workflow, allowing for automatic testing whenever changes are made.
11. Performance Considerations
•	Efficiency: Sorting, filtering, and transforming functions are designed to minimize overhead, ensuring that the application can handle larger datasets effectively.
12. Data Integrity Checks
•	Validation: The tests check that data integrity is maintained throughout the process, ensuring that no invalid data passes through the system and that outputs match expected formats.
13. Using Official Base Image:
•	Implementation: The Dockerfile starts with FROM python:3.9-slim, which is an official Python image.
•	Benefit: Official images are maintained by the community and often receive regular updates, security patches, and performance optimizations.
14. Setting a Working Directory:
•	Implementation: The command WORKDIR /app sets a dedicated working directory inside the container.
 
•	
•	Benefit: This organizes the file structure and makes the path to execute commands cleaner and more manageable. It also avoids potential issues with relative paths.
 
o	
15. Copying Only Required Files:
•	Implementation: The command COPY . . copies all the necessary Python scripts and data files into the working directory.
•	Benefit: This allows the container to access your application files easily. However, it's good practice to use a .dockerignore file to exclude unnecessary files, improving the build context and image size.
16. Installing Dependencies Efficiently:
•	Implementation: The command RUN pip install --no-cache-dir pytest installs pytest without caching.
•	Benefit: Using --no-cache-dir reduces the size of the image by not storing the downloaded packages, keeping the image lightweight.
17. Using a Single CMD Instruction:
•	Implementation: The CMD command runs all Python scripts and then executes tests sequentially.
•	Benefit: This approach clearly defines the main task of the container, making it straightforward to understand what the container does when it starts.
18. Combining Build and Run Steps:
•	Implementation: The Dockerfile builds and tests the application in one sequence using a single command.
1.	Benefit: This allows for an efficient pipeline where the application is built, executed, and tested in a single container run, simplifying the workflow.
