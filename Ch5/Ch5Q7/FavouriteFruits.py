# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas!

favoriteFruits = []
print("Program for favorite fruits")
i = 0
while(True):
    temp = input("Enter fruit: ").lower()
    if(temp != "" or None):
        favoriteFruits.append(temp)
    else:
        break

fruits = []
if("apple" in favoriteFruits):
    fruits.append("apple")

if("mango" in favoriteFruits):
    fruits.append("mango")

if("banana" in favoriteFruits):
    fruits.append("banana")

print()
for fruit in fruits:
    print(f"You really like {fruit}!")