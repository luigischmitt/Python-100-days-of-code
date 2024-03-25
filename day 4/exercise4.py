line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure? (e.g. A1 for row 1 and column A)

y = str(position[0]) 
x = int(position[1]) - 1

if y == "A":
    y = 0
    map[x][y] = "X"
elif y == "B":
    y = 1
    map[x][y] = "X"
elif y == "C":
    y = 2
    map[x][y] = "X"

print(f"{line1}\n{line2}\n{line3}")