"""Test program for the Unit Conversion Microservice."""
import requests

response = requests.get(
    "http://localhost:5003/convert",
    params={
        "value": 225,
        "from_unit": "pounds",
        "to_unit": "kilograms",
    },
)

conversion_data = response.json()

print(conversion_data["original_value"], conversion_data["original_unit"], "=")
print(conversion_data["converted_value"], conversion_data["converted_unit"])