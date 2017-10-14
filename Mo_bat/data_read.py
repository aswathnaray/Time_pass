import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go


def plotly_plot(plotly_data, ipf_plotly):

    plotly.tools.set_credentials_file(username='aswathnaray', api_key='h2svlZVIPbNfdygtRK0E')

    trace1 = go.Scatter(
        x=plotly_data.index,
        y=plotly_data['Voltage'],
        name='Voltage (mV)'
    )
    trace2 = go.Scatter(
        x=plotly_data.index,
        y=plotly_data['Level'],
        name='State of Charge (%)',
        yaxis='y2',
        line=dict(dash='dot', color='#32cd32')
    )
    trace3 = go.Scatter(
        x=plotly_data.index,
        y=plotly_data['Temperature'],
        name='Temperature (C)',
        yaxis='y3',
        line=dict(dash='dot', width=0.5, color='#d62728')
    )

    datap = [trace1, trace2, trace3]
    layout = go.Layout(
        title='Battery log output',
        width=1920,
        height=1080,
        font=dict(size=18),
        xaxis=dict(
            domain=[0.2, 0.9]
        ),
        yaxis=dict(
            title='Voltage (mV)',
            titlefont=dict(
                color='#1f77b4'
            ),
            tickfont=dict(
                color='#1f77b4'
            )
        ),
        yaxis2=dict(
            title='State of charge (%)',
            titlefont=dict(
                color='#ff7f0e'
            ),
            tickfont=dict(
                color='#ff7f0e'
            ),
            anchor='free',
            overlaying='y',
            side='left',
            position=0.15
        ),
        yaxis3=dict(
            title='Temperature (C)',
            titlefont=dict(
                color='#d62728'
            ),
            tickfont=dict(
                color='#d62728'
            ),
            anchor='x',
            overlaying='y',
            side='right'
        )
    )

    fig = go.Figure(data=datap, layout=layout)
    plotly.offline.plot(fig, filename=('plots/' + str(ipf_plotly.replace('.csv', '.html'))))

    # plot_url = plotly.plotly.plot(fig, filename='multiple-axes-multiple')


def mpl_plot(mpl_data):

    fig, ax1 = plt.subplots()
    ax1.plot(mpl_data.index, mpl_data['Level'], 'g-.')
    ax1.set_ylabel('State of Charge (%)', color='g')
    ax1.set_ylim(0, 105)
    ax1.tick_params('y', colors='g')

    ax2 = ax1.twinx()

    ax2.plot(mpl_data.index, mpl_data['Voltage'], 'b-')
    ax2.set_ylabel('Voltage (mV)', color='b')
    ax2.set_ylim(3300, 4400)
    ax2.tick_params('y', colors='b')

    ax3 = ax1.twinx()

    ax3.plot(mpl_data.index, mpl_data['Temperature'], 'r:')
    ax3.set_ylabel('Temperature (C)', color='r')
    ax3.set_ylim(15, 45)
    ax3.tick_params('y', colors='r')

    # plt.plot(data.index, data['Temperature'], 'r:')

    fig.tight_layout()
    plt.grid()
    plt.show()

file_name = '2017-10-12.csv'
data = pd.read_csv('csv_files/'+str(file_name))
data.set_index(pd.to_datetime(data['Datetime']), inplace=True)
plotly_plot(data, file_name)