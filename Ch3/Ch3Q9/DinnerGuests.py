''' 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
    through 3-7 (page 42), use len() to print a message indicating the number 
    of people you are inviting to dinner. '''

guests = ["Tom", "Jerry", "Pegion", "Doggo"]

for guest in guests:
    print(f"Hello {guest}. I would like to invite you to dinner tonight at my home.")

print(f"\nI am inviting {len(guests)} guests for dinner")