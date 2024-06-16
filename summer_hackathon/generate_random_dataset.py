import json
import random

# Sample car data in English
sample_data_english = {
    "Vehicle Condition": "second-hand",
    "Category": "SportsCar",
    "First Registration": "11/2017",
    "Transmission": "Automatic transmission",
    "Fuel": "Diesel",
    "Mileage": 150144,
    "Power": "140 kW (190 HP)",
    "Engine Capacity": "1995 cc",
    "Number of Seats": 5,
    "Number of Doors": "Four or five",
    "Technical Inspection": "03/2025",
    "Color": "Metallic Blue",
    "Vehicle Status": "second-hand",
    "Vehicle Category": "Sports Car / Coupe",
    "Drive Type": "Internal combustion engine",
    "Parking Sensors": "Front, Rear",
    "Interior Design": "Alcantara, Black"
}


# Generating random data based on the sample in English
def generate_random_data_english(sample):
    new_data = sample.copy()

    # Modify some fields to generate new entries
    new_data["First Registration"] = f"{random.randint(1, 12)}/20{random.randint(15, 22)}"
    new_data["Mileage"] = random.randint(50000, 200000)
    new_data["Technical Inspection"] = f"{random.randint(1, 12)}/20{random.randint(23, 29)}"
    new_data["Power"] = f"{random.randint(100, 400)} HP"
    new_data["Engine Capacity"] = f"{random.randint(1600, 3000)} cc"
    new_data["Price"] = f"${random.randint(15000, 50000)}"  # Adding random price

    return new_data


random_data_english = [generate_random_data_english(sample_data_english) for _ in range(100)]

# Save the generated data to a JSON file
english_file_path = 'Random_Car_Data_English.json'
with open(english_file_path, 'w') as file:
    json.dump(random_data_english, file, indent=4)

