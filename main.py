country = input("type country\n") # Add country name
visits = int(input("how many visits?\n")) # Number of visits
list_of_cities = eval(input('list cities visited in the format ["city name", "city 2 name"]\n')) # create list from formatted string

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
# Do NOT change the code above 👆

def add_new_country(country, visits, list_of_cities):
  travel_log.append({
    "country":country,
    "visits":visits,
    "cities":list_of_cities
  })

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")