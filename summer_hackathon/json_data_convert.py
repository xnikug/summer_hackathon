import csv
import json

def convert_csv_to_json(csv_filepath, json_filepath):
    # Columns to be retained in the JSON output
    retained_columns = [
        'manufacturer_name', 'model_name', 'transmission', 'color',
        'odometer_value', 'year_produced', 'engine_fuel', 'engine_has_gas',
        'engine_type', 'engine_capacity', 'body_type', 'has_warranty',
        'state', 'price_usd'
    ]

    # Initialize a list to store the processed data
    processed_data = []

    # Open the CSV file and read data
    with open(csv_filepath, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Filter out unwanted columns and keep only the retained columns
        for row in reader:
            filtered_row = {key: row[key] for key in retained_columns if key in row}
            processed_data.append(filtered_row)

    # Write the processed data to a JSON file
    with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
        json.dump(processed_data, jsonfile, ensure_ascii=False, indent=4)

# Example usage
csv_filepath = 'cars.csv'  # Path to your CSV file
json_filepath = 'cars.json'  # Desired JSON output file path
convert_csv_to_json(csv_filepath, json_filepath)
