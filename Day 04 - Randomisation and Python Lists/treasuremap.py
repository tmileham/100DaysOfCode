row1 = ["😄","😄","😄"]
row2 = ["😄","😄","😄"]
row3 = ["😄","😄","😄"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

treasure = "👑"

# Overcomplicated method...
# position = list(input("Where do you want to put the treasure :"))
# map[int(position[1])-1][int(position[0])-1] = treasure

position = input("Where would you like to place the treasure? ")

horizontal = int(position[0])-1
vertical = int(position[1])-1

map[vertical][horizontal] = treasure


print(f"{row1}\n{row2}\n{row3}")