# initializing a user input variable to take how many triangles they would like to compute the area of
triangle_count = int(input("How many triangles would you like to compute?: "))

# empty array to put the calculated areas into
storage = []

# this for loop basically starts off with print out what triangle it is currently trying to calculate the area for.
# then, once it does that, it takes the calculated area of the triangle and puts it into the empty array.
# once it does that, it tells you the area of that triangle, and it starts the process over again.
for i in range(triangle_count):
    print(f"Triangle {i + 1}: ")
    triangle_base = int(input("Enter base: "))
    triangle_height = int(input("Enter a height: "))
    triangle_area = 0.5 * triangle_base * triangle_height
    storage.append(triangle_area)
    print(f"Area: {triangle_area}")

# this will print out the final value of all the sums inside of the array filled with the calculated areas of the triangles.
print(f"Total area of triangles: {sum(storage)}")