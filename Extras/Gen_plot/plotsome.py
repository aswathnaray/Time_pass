import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
from plotly import tools, offline

import Extras.Gen_plot.headerfind as hf


def plotly_plot(x_p, y1_p, y2_p):
    trace1 = go.Scatter(
        x=x_p,
        y=y1_p
    )
    trace2 = go.Scatter(
        x=x_p,
        y=y2_p
    )

    fig = tools.make_subplots(rows=2, cols=1)

    fig.append_trace(trace2, 1, 1)
    fig.append_trace(trace1, 2, 1)

    fig['layout'].update(height=600, width=600, title='Stacked subplots')
    py.iplot(fig, filename='stacked-subplots')

    fig = go.Figure(data=datap, layout=layout)
    offline.plot(fig, filename=('plots/' + str(ipf_plotly.replace('.csv', '.html'))))

    # plot_url = plotly.plotly.plot(fig, filename='multiple-axes-multiple')

file_source = input('Enter file path: ')
head_row = hf.head(file_source)
print(head_row)

if '.csv' in str(file_source):
    file_data = pd.read_csv(file_source, header=head_row)
elif '.xls' in str(file_source):
    file_data = pd.read_excel(file_source, sheetname=head_row[1], header=head_row[0])
else:
    print("!Warning: Only excel and CSV files are allowed")

print(file_data.head())
