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


##Summary of the Python Scripts

Step1.py
### 	Main Data Flow:
•	The script reads bike data from a JSON file (bike_data.json).
•	It processes this data to remove duplicates and entries missing essential fields (model_id, price_gbp, weight_kg, and in_stock).
•	The cleaned data is then saved to another JSON file (cleaned_data.json).
### 	Key Functions:
•	clean_bike_data(data): Goes through each entry in the data list and checks for required fields. It removes any bikes missing these fields 
•	or with duplicate model_ids, adding only unique and valid entries to a final list.
•	read_data_from_file(file_path): Reads JSON data from a specified file path. If the file doesn’t exist, it logs an error and raises a FileNotFoundError. If JSON decoding fails, it logs that too.
•	write_data_to_file(data, file_path): Writes the cleaned data to the specified JSON file with proper formatting. If an I/O error occurs, it logs and raises the error.
### 	Logging and Error Handling:
•	The script uses logging to track progress and catch errors. This includes successful reads/writes and specific issues like missing files or JSON format errors.
### 	Execution:
•	The main function coordinates these steps, defining the input and output file paths and managing the cleaning pipeline. It ensures errors are logged if anything goes wrong, making debugging straightforward.


    
