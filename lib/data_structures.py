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
    },
]

def get_names(spicy_foods):
    food_names = []
    for item in spicy_foods:
        food_names.append(item["name"])
    return food_names
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    chosen_cuisine_foods = {}
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            chosen_cuisine_foods.update(food)
    return chosen_cuisine_foods

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    pass

def get_average_heat_level(spicy_foods):
    total_spice_num = 0
    num_foods = len(spicy_foods)
    for food in spicy_foods:
        total_spice_num += food["heat_level"]
    average_heat_level = total_spice_num / num_foods
    return average_heat_level
    pass

def create_spicy_food(spicy_foods, spicy_food):
    combined_spicy_foods = spicy_foods
    combined_spicy_foods.append(spicy_food)
    return combined_spicy_foods
    pass
