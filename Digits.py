# Outputs the digits in the list as one number.
def get_number(input_list):
    numbers_remaining  = len(input_list)
    total = 0
    for number in input_list:
        total = total + (number * numbers_remaining)
        numbers_remaining = numbers_remaining - 1
    return total

