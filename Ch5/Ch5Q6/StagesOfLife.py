# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
# stage of life. Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is 
# a baby.
# •	 If the person is at least 2 years old but less than 4, print a message that 
# the person is a toddler.
# •	 If the person is at least 4 years old but less than 13, print a message that 
# the person is a kid.
# •	 If the person is at least 13 years old but less than 20, print a message that 
# the person is a teenager.
# •	 If the person is at least 20 years old but less than 65, print a message that 
# the person is an adult.
# •	 If the person is age 65 or older, print a message that the person is an 
# elder.

print("Program to let you know who you are")
while(True):
    age = input("Enter your age: ")
    try:
        age = int(age)
    except TypeError as e:
        print(f"\nError: {e}\nPlease enter a valid positive integer")
        continue
    except ValueError as e:
        print(f"\nError: {e}\nPlease enter a valid positive integer")
        continue
    
    if(age >= 0):
        break
    else:
        print("\nEnter a positive integer")

if(age < 2):
    print("\nYou are a baby")
elif(age >= 2 and age < 4):
    print("\nYou are a toddler")
elif(age >= 4 and age < 13):
    print("\nYou are a kid")
elif(age >= 13 and age < 20):
    print("\nYou are a teenager")
elif(age >= 20 and age < 65):
    print("\nYou are an adult")
else:
    print("\nYou are an elder")