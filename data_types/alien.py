alien_0 = {'color': 'green', 'points': 5}

# accessing values in a dictionary
print(alien_0['color'])

new_points = alien_0['points']
print(f"You earned {new_points} points.")

# adding new key-value pairs
print(f"Original:\t{alien_0}")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"Added:\t\t{alien_0}")
