# 5-2. More Conditional Tests: You don’t have to limit the number of tests you 
# create to ten. If you want to try more comparisons, write more tests and add 
# them to conditional_tests.py. Have at least one True and one False result for 
# each of the following:
# •	 Tests for equality and inequality with strings
# •	 Tests using the lower() method
# •	 Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to
# •	 Tests using the and keyword and the or keyword
# •	 Test whether an item is in a list
# •	 Test whether an item is not in a list

bird = "flying rat"
print("Is bird == 'pigeon'? I predict False")
print(bird == "pigeon")

print("\nIs bird == 'Flying Rat'.lower()? I predict True")
print(bird == "Flying Rat".lower())

num = 4
print("\nIs num == 4? I predict True")
print(num == 4)

print("\nIs num <= 4? I predict True")
print(num <= 4)

print("\nIs num > 4? I predict False")
print(num > 4)

print("\nIs num != 4? I predict False")
print(num != 4)

print("\nIs num <= 5 and num >= -5? I predict True")
print(num <= 5 and num >= -5)

print("\nIs num > 6 or num < -6? I predict False")
print(num > 6 or num < -6)

randomList = ["pigeon", "cat", "doggo", "rat", "fat dino", "crazy jay"]
print("\nIs cat in randomList? I predict True")
print(f"{'cat' in randomList}")

print("\nIs cow not in randomList? I predict True")
print(f"{'cow' not in randomList}")