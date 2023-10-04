
list_of_numbers = list(range(1, 6))
list_of_numbers.pop()
print("The length of the existing list is:", len(list_of_numbers))
replacement_number = int(input("Please enter an integer number to replace the middle number in the list: "))
list_of_numbers.insert(len(list_of_numbers) // 2, replacement_number)
print("The updated list is:", list_of_numbers)
