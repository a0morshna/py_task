## Task #1

Make a function to translate from Arabic numerals to Roman numerals.

Input: 75.

Output: LXXV.

> Do not forget about checking the entered data, that is, suddenly someone will try to enter letters or something else.

## Solution

I choose solution in which we divided the number by its largest base value.

Update:
1. Use `dict` data structure.
2. Check input with `assert` construction.

### For example
> Input number = **75**.
> 
> 90 > **75** > 50, so the largest value will be 50.
> 
> Divide **75** / 50. Quotient = 1. Remainder = **25**. The corresponding symbol **L** will be repeated once.
> 
> Divide **25** / 10. Quotient = 2. Remainder = **5**. The corresponding symbol **X** will be repeated twice.
> 
> Divide **5** / 5. Quotient = 1. Remainder = **0**. The corresponding symbol **V** will be repeated once.
> 
> The output = **LXXV**.

## Library
We can also use small helper library to convert arabic to roman numerals.

More about library [here](https://pypi.org/project/roman/).

### Instalation
> pip install roman