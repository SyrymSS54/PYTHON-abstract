alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("the alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0,'y_position':25,'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))            