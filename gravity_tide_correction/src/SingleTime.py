import longmantides
from datetime import datetime

def cal(lat, lon, alt, time):

	model = longmantides.TideModel()  # Make a model object
	
	gm, gs, g = model.solve_longman(lat, lon, alt, time)
	print (g)  # Lunar, Solar, and Total

if __name__ == '__main__':

	lat = -7.1747218  # Station Latitude
	lon = 107.3926086 # Station Longitude
	alt = 2088  # Station Altitude [meters]

	time = datetime(2020, 6, 13, 8, 54, 8)  # When we want the tide

	cal(lat, lon, alt, time)