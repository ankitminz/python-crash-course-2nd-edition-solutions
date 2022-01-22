''' 3-10. Every Function: Think of something you could store in a list. For example, 
    you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items 
    and then uses each function introduced in this chapter at least once. '''

languages = ["C#", "Python", "C++", "Kotlin", "Rust", "Javascript"]

print(f"Original list\n{languages}")
languages.append("mlog")
print(f"\nList after appending stuff\n{languages}")
languages.insert(len(languages) // 2, "Java")
print(f"\nList after inserting stuff\n{languages}")
del languages[0]
print(f"\nList after removing stuff with del\n{languages}")
print(f"\nList after popping {languages.pop()}\n{languages}")
languages.remove("Rust")
print(f"\nList after removing stuff by value\n{languages}")