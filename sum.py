def sum_even_and_odd_numbers(start, end):
    sum_even = 0
    sum_odd = 0

    for number in range(start, end + 1):
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number

    return sum_even, sum_odd

start_range = 1
end_range = 10
even_sum, odd_sum = sum_even_and_odd_numbers(start_range, end_range)
print(f"Sum of even numbers from {start_range} to {end_range}: {even_sum}")
print(f"Sum of odd numbers from {start_range} to {end_range}: {odd_sum}")