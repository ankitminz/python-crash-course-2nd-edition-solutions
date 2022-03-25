# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
# describing each test and your prediction for the results of each test. Your code 
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line 
# evaluates to True or False.
# •	 Create at least ten tests. Have at least five tests evaluate to True and 
# another five tests evaluate to False.


car = "subaru"
print("Is car == 'subaru'? I predict True")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False")
print(car == "audi")

print("\nIs car == 'Subaru'? I predict False")
print(car == "Subaru")

print("\nIs car == 'SUBARU'? I predict False")
print(car == "SUBARU")

print("\nIs car == car? I predict True")
print(car == car)

anotherCar = "SuBaRu"
print("\nIs car == anotherCar? I predict False")
print(car == anotherCar)

print("\nIs car == anotherCar.lower()? I predict True")
print(car == anotherCar.lower())

print("\nIs car == 'sUbaru'? I predict False")
print(car == "sUbaru")

print("\nIs car == 'sUbaru'.lower()? I predict True")
print(car == "sUbaru".lower())

print("\nIs car == 'SUBARU'.lower()? I predict True")
print(car == "SUBARU".lower())

print("\nIs car == 'subarU'.lower()? I predict True")
print(car == "subarU".lower())