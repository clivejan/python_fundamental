# importing an entire module
#import pizza

#pizza.make_pizza(16, 'sock')
#pizza.make_pizza(12, 'sock', 'booger', 'rock')

# importing specific functions
#from pizza import make_pizza

#make_pizza(16, 'sock')
#make_pizza(12, 'sock', 'booger', 'rock')

# using as to give a function an alias
from pizza import make_pizza as mp

mp(16, 'sock')
mp(12, 'sock', 'booger', 'rock')
