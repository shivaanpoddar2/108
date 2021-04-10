import plotly.figure_factory as pff
import pandas as pd
import csv
a=pd.read_csv('data.csv')
fig = pff.create_distplot([a["Weight(Pounds)"].tolist()], ["Weight"], show_hist=True)

fig.show()
