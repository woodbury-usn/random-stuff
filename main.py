import countries
import foods
import random

def get_idx(arr):
    rand_int = random.randint(0, len(arr)-1)
    return rand_int


country = countries.get_country(get_idx(countries.countries))
food = foods.get_food(get_idx(foods.foods))
print('You are going to ' + country)
print('And you are getting a ' + food + ' to eat!')








