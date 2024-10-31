Overview
The Bicycle Inventory Data Processing project aims to assess and manipulate bicycle inventory data stored in a JSON format. It focuses on various data engineering tasks to ensure the integrity and usability of the dataset, which includes attributes like model IDs, prices, weights, and stock availability of bicycles.

Project Structure
The project is organized as follows:

bash
Copy code
bicycle_inventory/
│
├── data/
│   └── bicycle_inventory.json  # JSON file containing bicycle inventory data
│
├── src/
│   └── main.py                 # Main script to execute data processing tasks
│   └── data_processing.py       # Contains functions for data manipulation tasks
│
├── tests/
│   └── test_data_processing.py   # Unit tests for data processing functions
│
├── output/
│   └── cleaned_data.json         # Output file for cleaned data
│   └── filtered_data.json        # Output file for filtered bicycles
│   └── brand_count.json          # Output file for brand counts
│   └── sorted_data.json          # Output file for sorted bicycles
│   └── transformed_data.json     # Output file for transformed data with price per kg
│
└── README.md                     # Project documentation and usage instructions
Input
The main input for the project is the bicycle_inventory.json file, which contains an array of objects representing bicycle inventory items. Each object includes the following fields:

model_id: Unique identifier for the bicycle model
model_name: Name of the bicycle model
brand: Brand of the bicycle
type: Type of bicycle (e.g., Road Bike, Mountain Bike, Hybrid Bike)
price_gbp: Price in GBP
weight_kg: Weight in kilograms
in_stock: Availability status (true or false)
Steps
The data processing involves the following key steps:

Data Cleanup:

Validate the dataset to remove or quarantine entries that do not meet specified constraints, such as missing required fields.
Filtering:

Filter the dataset based on specific requirements such as bicycle type (Mountain Bike), price (≤ £1000), and stock availability.
Counting by Brand:

Count the number of bicycles available for each brand and create a summary.
Sorting:

Sort the bicycles by price and then by weight in ascending order.
Transformation:

Add a new column price_per_kg to each bicycle record, representing the price of the bicycle divided by its weight.
