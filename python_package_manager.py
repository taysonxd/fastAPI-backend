

import numpy

# print(numpy.version.version)

numpy_array = numpy.array([ 10, 22, 36, 41, 52, 66, 71, 73 ])
print(type(numpy_array))
print(numpy_array * 2)

# import pandas

import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics
print(arithmetics.sum_two_values(1, 4))
