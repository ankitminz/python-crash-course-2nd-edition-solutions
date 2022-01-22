'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
    arrive in time for the dinner, and you have space for only two guests.
	Start with your program from Exercise 3-6. Add a new line that prints a 
    message saying that you can invite only two people for dinner.
	Use pop() to remove guests from your list one at a time until only two 
    names remain in your list. Each time you pop a name from your list, print 
    a message to that person letting them know you’re sorry you can’t invite 
    them to dinner.
	Print a message to each of the two people still on your list, letting them 
    know they’re still invited.
	Use del to remove the last two names from your list, so you have an empty 
    list. Print your list to make sure you actually have an empty list at the end 
    of your program.
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

print("\nO Crap! The new dinner table is not going to arrive in time and there is space for only two guests")
while(len(guests) > 2):
    print(f"Sorry {guests.pop()}, I can't invite you to dinner. There is not enough space")

print()
for guest in guests:
    print(f"Hi {guest}, you are still invited to dinner tonight")

del guests[:]

print(f"\n{guests}")
    