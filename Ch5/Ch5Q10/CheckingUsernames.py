# 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.
# •	 Make a list of five or more usernames called current_users.
# •	 Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
# •	 Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
# •	 Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
# current_users containing the lowercase versions of all existing users.

currentUsers = ["ankit", "punkit", "sunkit", "aniket"]
newUsers = []

while(True):
    temp = input("Enter username: ").lower()
    if(temp == "" or temp == None):
        break
    else:
        newUsers.append(temp)

print()
if(len(newUsers) != 0):
    for name in newUsers:
        if(name in currentUsers):
            print(f"Username '{name}' already exist\n" + 
            "Please enter a new username\n")
        else:
            print(f"Username '{name}' is available\n")
else:
    print("Bruh! no users\nWe need some new users")