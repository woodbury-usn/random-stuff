import countries
import random

rand_int = random.randint(0, len(countries.countries)-1)
country = countries.get_country(rand_int)
print('You are going to ' + country + '!!!')







