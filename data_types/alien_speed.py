alien_0 = {'x_position': 0, 'y_posotion': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move alien on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")
