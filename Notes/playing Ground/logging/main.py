import random
import logging

logging.basicConfig(level=logging.INFO)
# Define the function to generate a random list of numbers
def generate_random_list(n):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(1, 100))
    return random_list

# Define the function to filter out even numbers from the list
def filter_even_numbers(numbers):
    filtered_list = []
    for number in numbers:
        if number % 2 == 0:
            filtered_list.append(number)
    return filtered_list

# Define the function to calculate the average of a list of numbers
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

# Define the function to print out the statistics of the list
def print_statistics(numbers):
    filtered_numbers = filter_even_numbers(numbers)
    average = calculate_average(filtered_numbers)
    logging.info(f"Original List: {numbers}" )
    print("Filtered List (even numbers only): ", filtered_numbers)
    print("Average of filtered list: ", average)

# Generate a random list of numbers and print out the statistics
numbers = generate_random_list(10)
print_statistics(numbers)
