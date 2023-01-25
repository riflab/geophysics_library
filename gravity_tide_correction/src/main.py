import SingleTime
from datetime import datetime

data = 'data.txt'

with open(data,'r') as f:
	for line in f:
		read = line.split('\n')[0].split()

		time = datetime(int(read[3]), int(read[4]), int(read[5]), int(read[6]), int(read[7]), int(read[8]))
		# print(read)
		SingleTime.cal(float(read[0]), float(read[1]), float(read[2]), time)