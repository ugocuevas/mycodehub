import json

filename = 'names.json'
with open(filename) as f:
    names = json.load(f)
    
print(f"Welcome back {names}!")

