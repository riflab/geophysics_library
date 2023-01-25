import longmantides
from datetime import datetime

print ("\n\nRun Full 7 Day model")
model = longmantides.TideModel()  # Make a model object
model.increment = 60*10  # Run every 10 minutes
model.latitude = -7.13221  # Station Latitude
model.longitude = 107.41902  # Station Longitude
model.altitude = 1500.  # Station Altitude [meters]
model.start_time = datetime(2020, 6, 12, 6, 47, 0)
model.duration = 1  # Model run duration [days]
model.run_model()  # Do the run
model.write('output.txt')  # Save results to text file
model.plot()  # Make a quick-dirty-plot
# print
