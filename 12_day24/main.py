path = r"C:\Users\Gumo\Desktop\Git\Class\Udemy\12_day24\my_file.txt"

# with open(path) as file:
#     contents = file.read()
#     print(contents)


with open(path, "a+") as file:
    file.write("meow")
