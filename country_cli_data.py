import argparse
import json
import requests

API_URL = "https://www.travel-advisory.info/api"

def pull_country_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get("data", {})
    else:
        print("Failed to fetch data from the API.")
        return {}

def data_to_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def data_from_json():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def search_country(country_code, data):
    country_name = data.get(country_code, {}).get("name", "Unknown")
    return country_name

def main():
    parser = argparse.ArgumentParser(description="Country CLI")
    parser.add_argument("--countryCodes", nargs="+", help="List of country codes to find the details")

    args = parser.parse_args()
    country_codes = args.countryCodes

    if not country_codes:
        print("Please Enter Minimum One Country Code to proceed further")
        return

    data = data_from_json()

    if not data:
        print("Fetching data from the API...")
        data = pull_country_data()
        data_to_json(data)
        print("Data saved to data.json.")

    for country_code in country_codes:
        country_name = search_country(country_code, data)
        print(f"{country_code}: {country_name}")

if __name__ == "__main__":
    main()
