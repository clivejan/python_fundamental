import random

# generate a random number between 1 to 6
print(random.randint(1, 6))

# retruns a randomly chosen element from a list or tuple
flavours = ['booger', 'sock', 'rock']
print(f"You got a {random.choice(flavours)} sandwich.")
