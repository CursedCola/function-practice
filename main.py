from add_fruits import add_fruits
from divide_fruits import divide_fruits
from subtract_fruits import subtract_fruits
from displayfruit import displayFruit
# functions printing and returning
# print something in a function, its only for displaying
# some data, you are doing nothing with the data

# when you return in a function, you are going to use it
# in another part of your program

apples = int(input("how many apples?: "))
oranges = int(input("how many oranges?: "))


# Golden rule: Whenever you return items, you must put returned value inside of
# a variable

# add fruit
fruitAdded = add_fruits(apples,oranges)
print(fruitAdded)
# subtract fruits
fruitSubtracted = subtract_fruits(apples,oranges)
print(fruitSubtracted)
# divide fruit
fruitDivided = divide_fruits(apples,oranges)
print(fruitDivided)
# display the added fruits, subtract fruits, and divid fruits

x,y,z = fruitAdded, fruitSubtracted, fruitDivided

displayed_fruits = displayFruit(x,y,z)
print(displayed_fruits)
display_fruit(fruit)