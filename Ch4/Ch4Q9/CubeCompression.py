''' 4-9. Cube Comprehension: Use a list comprehension to generate a list 
of the first 10 cubes. '''

cubes = [num ** 3 for num in range(1, 11)]

for cube in cubes:
    print(cube)