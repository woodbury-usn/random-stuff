import countries
import foods
import animals
import random

def get_idx(arr):
    rand_int = random.randint(0, len(arr)-1)
    return rand_int


country = countries.get_country(get_idx(countries.countries))
food = foods.get_food(get_idx(foods.foods))
animal = animals.get_animal(get_idx(animals.animals))
print('You are going to ' + country + ', and you are gettin a ' + food + ' to give to your ' +  animal)








