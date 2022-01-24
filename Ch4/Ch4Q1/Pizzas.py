''' 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store
    these pizza names in a list, and then use a for loop to print the name of
    each pizza.
•	Modify your for loop to print a sentence using the name of the pizza 
    instead of printing just the name of the pizza. For each pizza you should 
    have one line of output containing a simple statement like I like pepperoni 
    pizza.
•	Add a line at the end of your program, outside the for loop, that states 
    how much you like pizza. The output should consist of three or more lines 
    about the kinds of pizza you like and then an additional sentence, such as 
    I really love pizza! '''

pizzas = ["chicken pizza", "pigeon pizza", "veg pizza"]

for pizza in pizzas:
    print(f"I like {pizza}")
    
print("\nI like pizzas a lot. I eat them yearly. I like various other types" +
" of pizzas like cat pizza, doggo pizza.\nI really like pizzas")