#Bicycle Inventory Project
##Overview
The Bicycle Inventory Data Processing project aims to assess and manipulate bicycle inventory data stored in a JSON format. It focuses on various data engineering tasks to ensure the integrity and usability of the dataset, which includes attributes like model IDs, prices, weights, and stock availability of bicycles.
##Project Details
###Input->>>bike_data.json

### 1. Data Cleanup
Write a function or method that removes or quarantines rows that don't adhere to the expected data structure of constraints. Make practical assumptions regarding data structure and constraints. This function or method should always be called before other data manipulation functions to ensure validity of data.
  Python Script:Step1.py
  Input File:bike_data.json
  Output File:cleaned_data.json

###2. Filter according to requirements
Write a function method that filters the bicycles based on a specific requirement. Your function should return the full list of columns and rows which match the requirements.
The requirements are as follows - 
- Type of bike must be **Mountain Bike**
- Price must be less than or equal to **1000**
- There must be available stock for the bike
   Python Script:Step2.py
   Input File: cleaned_data.jon
   Output File:filtered_bikes.json
### 3. Count per Brand
Write a function or method that counts the number of each brand. Your function should return a data structure with **brand** as keys and the count of that brand as values.
   Python Script:Step2.py
   Input File: cleaned_data.jon
   Output File:brand-counts.json


    
