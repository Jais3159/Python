def sum_of_even_numbers(numbers):
    if not numbers:
        return 0
    even_sum = 0
    for number in numbers:
        if isinstance(number,(int,float)):
            if number % 2 == 0:
                even_sum += number
        else:
            print(f"Warning: Ignoring Non-Numeric value: {numbers}")
    return even_sum
numbers2 = [16,13,24,53,67,80,70]
result2 = sum_of_even_numbers(numbers2)
print(f"Sum of even numbers in {numbers2} : {result2}")