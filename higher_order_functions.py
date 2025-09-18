
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, fn_sum):
    return fn_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

# Closures 

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(1)(5))

# Built-in Higher Order Functions

numbers = [ 2, 4, 10, 16, 25, 50, 6, 5, 12, 33, 8, 44, 11, 12 ]

def multiply_numbers(number):
    return number * 2

numbers_multiplied = list(map(multiply_numbers, numbers))
print(numbers_multiplied)
numbers_multiplied = list(map(lambda number: number * 2, numbers))
print(numbers_multiplied)

#  filter

def filter_greater_than_ten(number):
    return number > 10        

numbers_filtered = list(filter(filter_greater_than_ten, numbers))
print(numbers_filtered)

numbers_filtered = list(filter(lambda number: number > 10, numbers))
print(numbers_filtered)

# Reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))
