import plotly.graph_objects as go
from datetime import datetime

open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
hight_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]

dates =[datetime(year=2013, month=10, day=10),
        datetime(year=2013, month=11, day=10),
        datetime(year=2013, month=12, day=10),
        datetime(year=2014, month=1, day=10),
        datetime(year=2014, month=2, day=10)]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_data, high=hight_data,
                                     low=low_data, close=close_data)])
fig.show()