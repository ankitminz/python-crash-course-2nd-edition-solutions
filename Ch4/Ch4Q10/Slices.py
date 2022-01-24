''' 4-10. Slices: Using one of the programs you wrote in this chapter, 
    add several lines to the end of the program that do the following:
•	 Print the message The first three items in the list are:. Then use 
    a slice to print the first three items from that program’s list.
•	 Print the message Three items from the middle of the list are:. 
    Use a slice to print three items from the middle of the list.
•	 Print the message The last three items in the list are:. Use a 
    slice to print the last three items in the list. '''

oneMillion = list(range(1, 1_000_001))

print(f"Minimum value = {min(oneMillion)}")
print(f"Maximum value = {max(oneMillion)}")
print(f"Sum of million numbers = {sum(oneMillion)}")
print(f"First three elements are")
for num in oneMillion[:3]:
    print(num)

print(f"\nThree elements from middle are")
for num in oneMillion[len(oneMillion)//2:(len(oneMillion)//2)+3]:
    print(num)

print(f"\nLast three elements are")
for num in oneMillion[-3:]:
    print(num)
