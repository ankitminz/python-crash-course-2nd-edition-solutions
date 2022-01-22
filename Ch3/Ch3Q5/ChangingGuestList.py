'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	Start with your program from Exercise 3-4. Add a print() call at the end 
    of your program stating the name of the guest who can’t make it.
•	Modify your list, replacing the name of the guest who can’t make it with 
    the name of the new person you are inviting.
•	Print a second set of invitation messages, one for each person who is still 
    in your list.
'''

guests = ["Tom", "Jerry", "Pegion", "Doggo"]
oldGuest = guests.pop()
newGuest = "Snail"
guests.append(newGuest)
print(f"{oldGuest} won't be able to join us in dinner.\nSo I'm inviting {guests[-1]} to the dinner")
print()
for guest in guests:
    print(f"Hello {guest}, please come to dinner tonight")