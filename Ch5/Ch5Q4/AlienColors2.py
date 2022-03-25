# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
# write an if-else chain.
# •	 If the alien’s color is green, print a statement that the player just earned 
# 5 points for shooting the alien.
# •	 If the alien’s color isn’t green, print a statement that the player just earned 
# 10 points.
# •	 Write one version of this program that runs the if block and another that 
# runs the else block.

color = ""
validColors = ["green", "yellow", "red"]

print("An alien was just shot down")
while(True):
    color = input("Color of alien: ")
    if(color.lower() in validColors):
        break
    
    print("\nPlease enter green , yellow or red")

if(color.lower() == validColors[0]):
    print("\nPlayer score: +5")
else:
    print("\nPlayer score: +10")