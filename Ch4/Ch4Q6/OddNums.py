''' 4-6. Odd Numbers: Use the third argument of the range() function to
make a list of the odd numbers from 1 to 20. Use a for loop to print each
number. '''

oddNums = [num for num in range(1, 20, 2)]

for num in oddNums:
    print(num)