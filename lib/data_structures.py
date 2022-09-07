spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

def get_names(spicy_foods):
    solution = list()
    for spicy_food in spicy_foods: 
        solution.append(spicy_food['name'])
    return solution

def get_spiciest_foods(spicy_foods):
    solution = list()
    for spicy_food in spicy_foods: 
        if spicy_food['heat_level'] > 5:
            solution.append(spicy_food)
    return solution

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = spicy_food['heat_level']
        peppers = '🌶' * heat_level
        name = spicy_food['name']
        cuisine = spicy_food['cuisine']
        message =  f'{name} ({cuisine}) | Heat Level: {peppers}'
        print(message)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        spicy_food_cuisine = spicy_food['cuisine']
        spicy_food_name = spicy_food['name']
        spicy_food_heat_level = spicy_food['heat_level']
        if spicy_food_cuisine == cuisine: 
            solution = {"name": spicy_food_name, "cuisine": spicy_food_cuisine,"heat_level": spicy_food_heat_level}
            return solution

def print_spiciest_foods(spicy_foods):
    spicy_enough = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_enough)

def get_average_heat_level(spicy_foods):
    solution = 0
    length = len(spicy_foods)
    for spicy_food in spicy_foods:
        solution += spicy_food['heat_level']
    return solution/length
