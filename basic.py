def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage
nums = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(nums))  # Output: [2, 4, 6]