'''
3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
    call to the end of your program informing people that you found a bigger 
    dinner table.
	Use insert() to add one new guest to the beginning of your list.
	Use insert() to add one new guest to the middle of your list.
	Use append() to add one new guest to the end of your list.
	Print a new set of invitation messages, one for each person in your list.
'''

guests = ["Tom", "Jerry", "Pegion", "Doggo"]
oldGuest = guests.pop()
newGuest = "Snail"
guests.append(newGuest)
print(f"{oldGuest} won't be able to join us in dinner.\nSo I'm inviting {guests[-1]} to the dinner")
print()
for guest in guests:
    print(f"Hello {guest}, please come to dinner tonight")  

print("\nHorray! I found a big ass table. Now we can invite more people")
guests.insert(0, "Cat")
guests.insert(len(guests) // 2, "Fat Dino")
guests.append("Dani")
for guest in guests:
    print(f"Hi {guest}, please come to dinner tonight")