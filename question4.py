#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

favorite_foods = ['Pizza', 'Sushi', 'Burger', 'Pasta', 'Salad']
favorite_foods.append('Tacos')
favorite_foods.append('Ice Cream')
favorite_foods.remove('Salad')


print("Updated list of favorite foods:", favorite_foods)

#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
numbers = [2, 5, 8, 10, 3, 6]

first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)
total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}")
