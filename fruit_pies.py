


""""
Determin the price of a specific pie
Each type of fruit pie has a different price
"""

"""
obtain user input
provide display options to user
crate a dictionary with the types of fruits and prices
display results to user
"""

def main():
    print("Enter the name of the type of fruit pie you want ", end="")
    fruit_pie_name = input("(apple, orange, pear, or razzberry): ")
    print("The cost of the pie is", fruit_pie_cost(fruit_pie_name), "dollars.")

def fruit_pie_cost(fruit_pie_name):
    pie_prices = {"apple": 15, "orange": 12, "pear": 13, "razzberry": 16}
    return pie_prices[fruit_pie_name]

main()