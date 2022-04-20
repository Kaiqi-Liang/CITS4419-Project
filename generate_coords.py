import random
lat = -31.977710
lng = 115.816484
def generate_coord(coord: float):
	return '{0:.6f}'.format(coord + random.randint(-99, 99)/10000000)
for _ in range(150):
	print(f'{generate_coord(lat)},{generate_coord(lng)}')