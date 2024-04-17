import turtle
from prettytable import PrettyTable

timmy =  turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")

my_screen = turtle.Screen()
my_screen.exitonclick()

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "Eletric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"

print(table)

# Just Examples