# function to convert arabic numbers to roman
def convert_nums(n):

    # write all numbers what we need in array
    arabic_nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_nums = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    # quantity of our steps is 12 cause 12 numbers in array
    quantity = 12

    # do function while n become a zero
    while n != 0:

        # divide by largest value
        dividing = n // arabic_nums[quantity]

        # find out the remainder
        n %= arabic_nums[quantity]

        while dividing:
            print(roman_nums[quantity], end='')

            # subtract right operand from the left
            # and assign the result to the left operand
            dividing -= 1

        quantity -= 1


# the main function
if __name__ == '__main__':

    n = int(input("Arabic Number: "))

    # write an exception
    try:
        # if input wrong type
        if not type(n) is int:
            raise TypeError

        # if n out of scope
        if not 0 < n < 9999:
            raise ValueError

        # if n is equal to zero
        if n == 0:
            raise ValueError

        # if n equal to 9999
        if n == 9999:
            raise ValueError

    # if an exception with this error occur
    except TypeError:
        print("TypeError! It's not a number, try again.")

    except ValueError:
        print("ValueError, please, try another one. Argument must be between 1 to 9999.")

    # if everything is fine execute the convert_nums function
    else:
        print("Roman Number: ", end="")
        convert_nums(n)
