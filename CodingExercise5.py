# Create a dictionary named car with the following keys: make, model, year, and color. Assign appropriate values to each key.
#     "make": "Toyota",
#     "model": "Camry",
#     "year": 2020,
#     "color": "Blue"
# Print the value associated with the model key.
# Add a new key called owner and assign it the name "Rahul".
# Print the entire dictionary.

carDetails ={"make":"Toyota","model":"Camry","year":2020,"color":"Blue"}
print(f"Car model:",carDetails["model"])
carDetails["owner"]="Rahul"
print(f"Updated Car dictionary:",carDetails)