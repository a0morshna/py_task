# function to convert arabic numbers to roman
def convert_nums(input_number):

    # write all numbers what we need in dictionary
    arabic_to_roman_nums = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
                            40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    # write here our result
    result = ""

    # arabic_to_roman_nums.keys - return keys in dictionary
    for keys in arabic_to_roman_nums.keys():
        # divide by largest value
        dividing = input_number // keys

        # find out the remainder and add
        # the value of the right operand to the left
        # and assign the sum in the left operand
        result += arabic_to_roman_nums[keys] * dividing

        # subtract right operand from the left
        # and assign the result to the left operand
        input_number -= keys * dividing

    return result


def check_input(input_number):
    # if input_number is equal to zero
    assert input_number != 0, 'ValueError, please, try another one. Argument must be between 1 to 9999.'

    # if input_number is equal to 9999
    assert input_number != 9999, 'ValueError, please, try another one. Argument must be between 1 to 9999.'

    # if input_number wrong type
    assert isinstance(input_number, int), 'TypeError! Its not a number, try again.'

    # if input_number out of scope
    assert 0 < input_number < 9999, 'ValueError, please, try another one. Argument must be between 1 to 9999.'


# the main function
if __name__ == '__main__':
    input_number = int(input("Arabic Number: "))

    # call function to check our input
    check_input(input_number)

    # call converter function
    converter = convert_nums(input_number)
    print("Roman Number: ", converter)
