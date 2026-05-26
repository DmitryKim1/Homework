def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

nums = [1, 2, 3, 4, 5, 6]

for x in even_numbers(nums):
    print(x)

    