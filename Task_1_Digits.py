# Program to convert a list of number to a string of digits.

# Intuition:
# The digits program below, takes a list of numbers and converts it into a single number. This is done by 
# multiplying each number by 10 to the power of the number of digits remaining in the list. This works because
# the first number in the list is the most significant digit, and the last number in the list is the least significant
# digit. For example, the number 1234 can be represented as 1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0. This is the same
# as 1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1. This is the same as 1000 + 200 + 30 + 4. This is the same as 1234.
# Due to this reason, we can multiply each number by 10 to the power of the number of digits remaining in the list.

# Example: [3, 4, 1] -> 341:
# If we have the list [3, 4, 1], we can multiply 3 by 10 to the power of 2, because there are 2 digits remaining
# in the list. This gives us 3 * 10^2, which is 300. We can then add this to the total. We then subtract 1 from the number of
# digits remaining in the list, because we have one less digit remaining. We then repeat this process for the next number in the
# list, which is 4. We multiply 4 by 10 to the power of 1, because there is 1 digit remaining in the list. This gives us 4 * 10^1,
# which is 40. We can then add this to the total. We then subtract 1 from the number of digits remaining in the list, because we have
# one less digit remaining. We then repeat this process for the next number in the list, which is 1. We multiply 1 by 10 to the power of 0,
# because there are 0 digits remaining in the list. This gives us 1 * 10^0, which is 1. We can then add this to the total. We then subtract
# 1 from the number of digits remaining in the list, because we have one less digit remaining. We now have no digits remaining in the list,
# so we can return the total, which is 341.

def digits(input_list):
    # We first create a variable to store the total. This will be returned at the end of the function.
    total = 0
    # We then create a variable to store the number of digits remaining in the list. This will be used to calculate the power
    # of 10 to multiply each number by.
    numbers_remaining = len(input_list) - 1
    # We then loop through each number in the list and multiply it by 10 to the power of the number of digits remaining in the list.
    for number in input_list:
        # We then add the result of the multiplication to the total.
        total = total + number * 10 ** (numbers_remaining)
        # We then subtract 1 from the number of digits remaining in the list, because we have one less digit remaining.
        numbers_remaining = numbers_remaining - 1
    # After the loop, we now have our final number, so we can return it.
    return total

# We can now test the function with some sample data.
print(digits([1, 2, 3, 4])) # Should return 1234
print(digits([9, 1, 0, 6, 9, 7, 2])) # Should return 9106972
print(digits([0, 1, 5, 2, 0])) # Should return 1520
print(digits([1, 3, 4])) # Should return 134
print(digits([2, 4, 5, 3, 7, 8])) # Should return 245378
print(digits([4, 0, 3, 5, 6])) # Should return 40356
print(digits([0, 4, 3, 2])) # Should return 432


