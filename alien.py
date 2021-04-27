#alien_0 = {'color' : 'green', 'points' : 5}
#print(alien_0)
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)
#new_points = alien_0['points']
#print(f"You just earned {new_points} points!")

#alien_0 = {'color': 'green'}
#print(f"The alien is {alien_0['color']}!")

#alien_0['color'] = 'yellow'
#print(f"The alien is now {alien_0['color']}!")

aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'medium'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10


for alien in aliens[:5]:
	print(alien)
print(...)

print(f"Total number of aliens created {len(aliens)}!")