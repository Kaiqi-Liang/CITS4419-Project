import random
lat = -31.97747
lng = 115.81629
def generate_coord(coord: float):
	return '{0:.6f}'.format(coord + random.randint(-99, 99)/10000000)
for _ in range(150):
	print(f'{generate_coord(lat)},{generate_coord(lng)}')