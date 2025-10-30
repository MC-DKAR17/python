# this is a very unconventional way of doing this task, but I just love lists

# so first, we import the math function so that we can multiply all the elements in the list for later

# the only reason I have this here is because in Python, there is no multiplication variant of the sum() command, so... you have to import this
import math


# asking the user for what number they wish to turn into a factorial
user_input = int(input("Enter a number: "))

# empty array
total = []

# setting count to be the user's number
count = user_input

# formula for factorials: n! = n * (n-1)...

# in this program however...

# formula becomes: user_input! = [count, count-1, count-2, count-3... until 0]

# this loop continues forever, until count reaches 0
while True:
    if count == 0:
        break
    else:
        # add the current amount of count, then subtract by 1
        total.append(count)
        count -= 1


# here is where the prod method is used, which is the multiplication equivalent of the sum() method.
print(f"{user_input}! = {math.prod(total)}")