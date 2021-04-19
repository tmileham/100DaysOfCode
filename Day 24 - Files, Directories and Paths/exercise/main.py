# Manual open and close file

# file = open("Day 24 - Files, Directories and Paths/exercise/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#######

# Reading File
# with open("Day 24 - Files, Directories and Paths/exercise/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing to File - (Overwriting / Creating)
with open(
    "Day 24 - Files, Directories and Paths/exercise/new_file2.txt", mode="w"
) as file:
    file.write("New File")


# Writing to File - Append
with open(
    "Day 24 - Files, Directories and Paths/exercise/my_file.txt", mode="a"
) as file:
    file.write("\nAppend")
