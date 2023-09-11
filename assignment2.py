def split_and_sort(nums):
    nums = set(nums) # <<< FIX for Assignment 2
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."
    # check if 0 is in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."
    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]
    # remove duplicates and sort
    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)
    return odd_nums, even_nums

nums = [8, 3, 5, 8, 18, 17, 9, 7, 5, 3, 10, 6, 5, 4, 2, 8]
odd_nums, even_nums = split_and_sort(nums)
print("Odd numbers:", odd_nums)
print("Even numbers:", even_nums)
