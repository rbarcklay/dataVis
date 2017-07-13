import pandas
import matplotlib.pyplot as plt
from datetime import datetime



data = pandas.read_csv("weather_year.csv")

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
data.index = data.date
data = data.drop(["date"], axis=1)

empty = data.apply(lambda col: pandas.isnull(col))


data.mean_temp.hist()
plt.ylabel('Mean Tempurature (F)')
plt.title('Histogram of Mean Tempuratures')

plt.show()

print("hello")

print(data.columns)