# Best Identation for dictionaries.
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# Retriving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary.
empty_dictionary = {}

# Loop through a dictionary.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."

# Wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

# Nesting a list in a dictionary.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary.
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting a dictionary in a list.
travel_log = [
    {
      "country": "France", 
      "cities_visited": ["Paris", "Lille", "Dijon"], 
      "total_visits": 12
    },
    {
      "country": "Germany", 
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
      "total_visits": 5
    }
]
