import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
data =  df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math score plotting"], show_hist=False)
fig.show()
populationmean = statistics.mean(data)
populationstdev = statistics.stdev(data)
print(populationmean)
print(populationstdev)