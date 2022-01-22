name = input("Enter your name\n")
name = "\n\t" + name + "\n\t"
print(f"{name} original\n")
print(f"{name.lstrip()} using lstrip\n")
print(f"{name.rstrip()} using rstrip\n")
print(f"{name.strip()} using strip")