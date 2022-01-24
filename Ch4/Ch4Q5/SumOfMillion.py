''' 4-5. Summing a Million: Make a list of the numbers from one to one
million, and then use min() and max() to make sure your list actually
starts at one and ends at one million. Also, use the sum() function to
see how quickly Python can add a million numbers. '''

oneMillion = list(range(1, 1_000_001))

print(f"Minimum value = {min(oneMillion)}")
print(f"Maximum value = {max(oneMillion)}")
print(f"Sum of million numbers = {sum(oneMillion)}")