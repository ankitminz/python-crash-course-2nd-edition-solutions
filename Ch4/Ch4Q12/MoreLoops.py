''' 4-12. More Loops: All versions of foods.py in this section have avoided 
    using for loops when printing to save space. Choose a version of foods.py, 
    and write two for loops to print each list of foods. '''

myFoods = ["pizza", "falafel", "carrot cake"]
friendFoods = myFoods[:]

myFoods.append("cannoli")
friendFoods.append("ice cream")
print("My favorite foods are")
for food in myFoods:
    print(food)

print("\nMy friend's favorite foods are")
for food in friendFoods:
    print(food)