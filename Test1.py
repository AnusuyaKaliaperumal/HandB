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
    """Loads sample data from a JSON file for testing."""
    try:
        with open(FILE_PATH, "r") as f:
            content = f.read()
            return json.loads(content)
    except FileNotFoundError:
        pytest.fail(f"File not found: {FILE_PATH}")
    except json.JSONDecodeError as e:
        pytest.fail(f"Error decoding JSON: {e}")

def test_clean_bike_data_valid(sample_data):
    """Tests cleaning of bike data to ensure valid entries are returned."""
    cleaned_data = clean_bike_data(sample_data)
    assert len(cleaned_data) <= len(sample_data)
    assert all("model_id" in item for item in cleaned_data)
    assert all(item["model_id"] is not None for item in cleaned_data)

def test_clean_bike_data_missing_fields():
    """Tests cleaning bike data with missing fields to ensure it returns an empty list."""
    test_data = [{"model_id": None, "price_gbp": 100, "weight_kg": 10, "in_stock": True}]
    cleaned_data = clean_bike_data(test_data)
    assert cleaned_data == []

def test_filter_mountain_bikes(sample_data):
    """Tests filtering of mountain bikes to ensure only valid entries are returned."""
    cleaned_data = clean_bike_data(sample_data)
    filtered_bikes = filter_mountain_bikes(cleaned_data)
    assert all(bike["type"] == "Mountain Bike" for bike in filtered_bikes)
    assert all(bike["price_gbp"] <= 1000 for bike in filtered_bikes)
    assert all(bike["in_stock"] for bike in filtered_bikes)

def test_filter_mountain_bikes_no_matches():
    """Tests filtering of mountain bikes with no matches to ensure an empty list is returned."""
    test_data = [{"model_id": 1, "type": "Road Bike", "price_gbp": 500, "in_stock": True}]
    filtered_bikes = filter_mountain_bikes(test_data)
    assert filtered_bikes == []

def test_count_per_brand(sample_data):
    """Tests counting of bikes per brand to ensure the result is a dictionary of counts."""
    cleaned_data = clean_bike_data(sample_data)
    brand_counts = count_per_brand(cleaned_data)
    assert isinstance(brand_counts, dict)
    assert all(isinstance(count, int) for count in brand_counts.values())

def test_count_per_brand_single_brand():
    """Tests counting of bikes for a single brand to ensure the count is correct."""
    test_data = [{"model_id": 1, "brand": "CycloX"}, {"model_id": 2, "brand": "CycloX"}]
    brand_counts = count_per_brand(test_data)
    assert brand_counts == {"CycloX": 2}

def test_sort_bicycles(sample_data):
    """Tests sorting of bicycles to ensure they are sorted by price and weight."""
    cleaned_data = clean_bike_data(sample_data)
    sorted_bikes = sort_bicycles(cleaned_data)
    prices = [bike["price_gbp"] for bike in sorted_bikes if bike["price_gbp"] is not None]
    assert prices == sorted(prices)

def test_sort_bicycles_stability():
    """Tests the stability of sorting bicycles with equal prices."""
    test_data = [{"model_id": 1, "price_gbp": 1000, "weight_kg": 10},
                  {"model_id": 2, "price_gbp": 1000, "weight_kg": 12}]
    sorted_bikes = sort_bicycles(test_data)
    assert sorted_bikes[0]["model_id"] == 1

def test_transform_price_per_weight(sample_data):
    """Tests the transformation of price per weight for bicycles."""
    cleaned_data = clean_bike_data(sample_data)
    transformed_data = transform_price_per_weight(cleaned_data)
    for bike in transformed_data:
        if bike["weight_kg"] and bike["price_gbp"]:
            assert bike["price_per_weight"] == pytest.approx(bike["price_gbp"] / bike["weight_kg"], rel=1e-2)

def test_transform_price_per_weight_zero_weight():
    """Tests the transformation of price per weight when weight is zero."""
    test_data = [{"model_id": 1, "price_gbp": 1000, "weight_kg": 0}]
    transformed_data = transform_price_per_weight(test_data)
    assert transformed_data[0]["price_per_weight"] is None

def test_empty_data():
    """Tests all functions with an empty dataset to ensure they handle it gracefully."""
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
    """Tests the count of model IDs in the sorted bicycles output to ensure correctness."""
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
