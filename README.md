# Bicycle Inventory Project
## Overview
The Bicycle Inventory Data Processing project aims to assess and manipulate bicycle inventory data stored in a JSON format. It focuses on various data engineering tasks to ensure the integrity and usability of the dataset, which includes attributes like model IDs, prices, weights, and stock availability of bicycles.
## Project Details
### Input->>>bike_data.json

The below ection gives details about the Python script, input and output file names for each given challenges 

### 1. Data Cleanup
Write a function or method that removes or quarantines rows that don't adhere to the expected data structure of constraints. Make practical assumptions regarding data structure and constraints. This function or method should always be called before other data manipulation functions to ensure validity of data.
  #### Python Script:Step1.py
  #### Input File:bike_data.json
  #### Output File:cleaned_data.json

### 2. Filter according to requirements
Write a function method that filters the bicycles based on a specific requirement. Your function should return the full list of columns and rows which match the requirements.
The requirements are as follows - 
- Type of bike must be **Mountain Bike**
- Price must be less than or equal to **1000**
- There must be available stock for the bike
   #### Python Script:Step2.py
   #### Input File: cleaned_data.jon
   #### Output File:filtered_bikes.json
### 3. Count per Brand
Write a function or method that counts the number of each brand. Your function should return a data structure with **brand** as keys and the count of that brand as values.
   #### Python Script:Step3.py
   #### Input File: cleaned_data.jon
   #### Output File:brand-counts.json

### 4. Sort bicycles by price followed by weight
Write a function or method that sorts the list of records by **price_gbp** and then by **weight_kg** in ascending order. Your function should return a data structure containing **model_id**, **price_gbp** and **weight_kg** as keys, along with their corresponding values
   #### Python Script:Step4.py
   #### Input File: cleaned_data.jon
   #### Output File:sorted_bicycles.json

### 5. Transform - price/weight
Write a function or method that adds a new column called `price_per_weight` to each bicycle record. This column should represent the price of the bicycle divided by its weight. Your function should return updated list of records including the new `price_per_weight` column.

   #### Python Script:Step4.py
   #### Input File: cleaned_data.jon
   #### Output File:transformed_bicycles.json


## Summary of the Python Scripts

### Step1.py
#### 	Main Data Flow:
•	The script reads bike data from a JSON file (bike_data.json).
•	It processes this data to remove duplicates and entries missing essential fields (model_id, price_gbp, weight_kg, and in_stock).
•	The cleaned data is then saved to another JSON file (cleaned_data.json).
#### 	Key Functions:
•	clean_bike_data(data): Goes through each entry in the data list and checks for required fields. It removes any bikes missing these fields 
•	or with duplicate model_ids, adding only unique and valid entries to a final list.
•	read_data_from_file(file_path): Reads JSON data from a specified file path. If the file doesn’t exist, it logs an error and raises a FileNotFoundError. If JSON decoding fails, it logs that too.
•	write_data_to_file(data, file_path): Writes the cleaned data to the specified JSON file with proper formatting. If an I/O error occurs, it logs and raises the error.
#### 	Logging and Error Handling:
•	The script uses logging to track progress and catch errors. This includes successful reads/writes and specific issues like missing files or JSON format errors.
#### 	Execution:
•	The main function coordinates these steps, defining the input and output file paths and managing the cleaning pipeline. It ensures errors are logged if anything goes wrong, making debugging straightforward.

### Step2.py
The script is designed to read a JSON file containing bicycle inventory data, filter the data for specific criteria related to mountain bikes, and then write the filtered results to a new JSON file. It consists of the following key functions:

####read_data_from_file(input_file: str) -> List[Dict[str, Any]]:
This function takes a file path as input and attempts to read data from the specified JSON file.
It uses the json library to load the data into a Python list of dictionaries.
If the file is not found or if the content is not valid JSON, it handles the exceptions and returns an empty list.

#### filter_mountain_bikes(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
This function filters the input data to extract only those entries that represent mountain bikes.
It checks three conditions for each bike:
The bike's type must be "Mountain Bike."
The price must be less than or equal to £1000.
The bike must be in stock (i.e., in_stock is True).
It returns a list of dictionaries representing the filtered mountain bikes.

#### write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
This function writes the provided data (a list of dictionaries) to a specified JSON file.
The data is formatted with an indentation of 4 spaces for readability.

#### main() -> None:
This is the main function of the script that orchestrates the execution.
It specifies the input and output file paths.
It reads the cleaned data from cleaned_data.json, filters the mountain bikes using the filter_mountain_bikes function, and writes the filtered data to filtered_bikes.json.
Finally, it prints a confirmation message indicating that the filtering operation has been completed.

#### if __name__ == "__main__":
This line checks if the script is being run as the main module and, if so, calls the main() function to execute the defined operations.

### Step3.py

#### count_per_brand(data: List[Dict[str, Any]]) -> Dict[str, int]:
This function takes a list of dictionaries (representing bicycle data) as input and counts the occurrences of each brand.
It initializes an empty dictionary, brand_count, to store the brand names as keys and their respective counts as values.
The function iterates through each entry in the data, retrieves the brand, and increments its count in the brand_count dictionary.
It returns the dictionary containing the counts of bicycles for each brand.
#### write_data_to_file(data: Dict[str, int], output_file: str) -> None:
This function writes the provided brand count data (a dictionary) to a specified JSON file.
The data is formatted with an indentation of 4 spaces for improved readability.
#### main() -> None:
This is the main function that orchestrates the script's execution.
It specifies the paths for the input and output files.
The function attempts to read the cleaned data from cleaned_data.json. If the file is not found or contains invalid JSON, it handles the exceptions and prints an appropriate error message.
Once the data is successfully loaded, it calls the count_per_brand function to obtain the brand counts and then writes this data to brand_counts.json.
Finally, it prints a confirmation message indicating that the brand counts have been successfully written to the output file.
#### if __name__ == "__main__":
This line checks if the script is being run as the main module and, if so, calls the main() function to execute the defined operations.

### Step4.py

#### sort_bicycles(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
This function takes a list of dictionaries (representing bicycle data) as input and sorts it based on two criteria: price in GBP and weight in kilograms.
It uses Python's built-in sorted function with a custom sorting key defined by a lambda function:
The sorting first considers the price_gbp field. If this field is missing, it assigns a value of positive infinity to ensure those entries appear last.
The secondary sorting criterion is weight_kg, similarly handling missing values by assigning them positive infinity.
After sorting, it constructs a new list (sorted_output) that includes only the model_id, price_gbp, and weight_kg for each bicycle.
The function returns the list of sorted bicycles.

#### write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
This function writes the sorted bicycle data (a list of dictionaries) to a specified JSON file.
The output data is formatted with an indentation of 4 spaces for better readability.

#### main() -> None:
This is the main function that manages the script's execution.
It specifies the paths for the input and output files.
The function attempts to read the cleaned data from cleaned_data.json. If the file is not found or contains invalid JSON, it handles the exceptions and prints an appropriate error message.
Once the data is successfully loaded, it calls the sort_bicycles function to obtain the sorted list and then writes this data to sorted_bicycles.json.
Finally, it prints a confirmation message indicating that the sorted bicycles have been successfully written to the output file.

#### if __name__ == "__main__":
This line checks if the script is being run as the main module and, if so, calls the main() function to execute the defined operations.

### Step5.py

#### transform_price_per_weight(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
This function takes a list of dictionaries (representing bicycle data) as input.
It initializes an empty list updated_bikes to hold the transformed entries.
For each bicycle entry in the input data:
It creates a copy of the entry to avoid modifying the original data.
It retrieves the weight_kg and price_gbp for the bicycle.
If the weight is greater than zero, it calculates price_per_weight by dividing the price by the weight. If the price is missing, it assigns None.
If the weight is not valid (i.e., zero or missing), it sets price_per_weight to None.
The updated entry is appended to the updated_bikes list.
Finally, the function returns the list of transformed bicycles.

#### write_data_to_file(data: List[Dict[str, Any]], output_file: str) -> None:
This function writes the transformed bicycle data (a list of dictionaries) to a specified JSON file, formatting it with an indentation of 2 spaces for readability.

#### main() -> None:
This is the main function that coordinates the script's execution.
It defines the paths for the input and output files.
It attempts to read the cleaned data from cleaned_data.json. If the file is not found or contains invalid JSON, it logs an error message and exits the function.
If the data is successfully loaded, it calls the transform_price_per_weight function to calculate the price per weight for each bicycle.
The transformed data is then saved to transformed_bicycles.json.
Finally, it logs an informational message confirming the successful writing of the transformed data.

####if __name__ == "__main__":
This line checks if the script is being executed as the main module and calls the main() function to initiate the processing.

## Test Case Coverage
### Python Script--> Test1.py
### Test Cases Covered
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

## Containerization

### Script-->Dockerfile
The below objectives have been covered by using Docker and also attached the screenshot of the results in Linux Shell(Gitbash)
The project should work on common Linux distributions and/or OSX.
- If the project requires external platform dependencies, they should be available as a Docker container so the project can be easily tested.


## Best Practices Implemented

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

