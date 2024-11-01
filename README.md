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
