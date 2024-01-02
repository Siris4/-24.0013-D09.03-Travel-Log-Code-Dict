country = input("Enter country name: ") # Add country name
visits = int(input("Enter number of visits: ")) # Number of visits
cities_input = input("Enter list of cities (comma-separated): ") # Get cities as a string
list_of_cities = cities_input.split(', ') # Convert string to list

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
print(f"My favourite city was {travel_log[-1]['cities'][0]}.")
