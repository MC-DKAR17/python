import random

# starting with values of zero for counting heads and tails
heads = 0

tails = 0

# now, this for loop goes through a random number 20 times. If the value of the random is 0, then its heads. If it's 1, then thats tails.

# effectively, we have a working coin flip, which is totally not rigged.
print("Flipping a coin 20 times: ")
for i in range(20):
    random_num = random.randint(0,1)
    if random_num == 0:
        print("H", end=" ")
        heads += 1
    else:
        print("T", end=" ")
        tails += 1

# this will print the final results, while also keeping the data clean
print("")
print(f"Heads: {heads}")
print(f"Tails: {tails}")
