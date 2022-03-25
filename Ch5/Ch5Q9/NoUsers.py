# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
# not empty.
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct 
# message is printed.

usernames = []

while(True):
    temp = input("Enter name: ").lower()
    if(temp == "" or temp == None):
        break
    else:
        usernames.append(temp)

print()
if(len(usernames) != 0):
    for name in usernames:
        if(name == "admin"):
            print(f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again")
else:
    print("Bruh! no users\nWe need to find some users")