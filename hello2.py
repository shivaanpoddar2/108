import plotly.figure_factory as pff
import pandas as pd
import csv
a=pd.read_csv('data2.csv')
fig = pff.create_distplot([a["Marks(Percentage)"].tolist()], ["Marks"], show_hist=True)

fig.show()
