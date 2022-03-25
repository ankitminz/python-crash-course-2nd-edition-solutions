# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed 
# for the appropriate color alien.

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
elif(color.lower() == validColors[1]):
    print("\nPlayer score: +10")
else:
    print("\nPlayer score: +15")