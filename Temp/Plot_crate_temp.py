import pandas as pd
import plotly
import plotly.graph_objs as go

def plotly_plot(px, py, plotly_data1, pd1name, plotly_data2, pd2name, plotly_data3, pd3name, setname, ipf_plotly):

    trace1 = go.Scatter(
        x=plotly_data1[px],
        y=plotly_data1[py],
        name=pd1name
    )
    trace2 = go.Scatter(
        x=plotly_data2[px],
        y=plotly_data2[py],
        name=pd2name,
    )
    trace3 = go.Scatter(
        x=plotly_data3[px],
        y=plotly_data3[py],
        name=pd3name,
    )


    datap = [trace1, trace2, trace3]
    layout = go.Layout(
        title=setname,
        width=1920,
        height=1080,
        font=dict(size=18),
        xaxis=dict(
            domain=[0.2, 0.9],
            title=px
        ),
        yaxis=dict(
            title=py,
        )
    )

    fig = go.Figure(data=datap, layout=layout)
    plotly.offline.plot(fig, filename=(str(ipf_plotly.replace('.xlsx', '_')) + str(setname.replace('/', '_')) + '.html'))



xc_varname = 'Charge Capacity (mAh)'
xd_varname = 'Discharge Capacity (mAh)'
y_varname = 'Voltage (mV)'

set1 = 'C/25 Charging'
set2 = 'C/25 Disharging'
set3 = '1C Charging'
set4 = '1C Discharging'


data1name = 'T = 5C'
data2name = 'T = 25C'
data3name = 'T = 45C'


file = "C:/Users/BADRINAR/Documents/Plots/Temp/SPICY_Pouch.xlsx"


t05c25 = pd.read_excel(file, sheetname='T05_C25')
print('Reading file ...')
t25c25 = pd.read_excel(file, sheetname='T25_C25')
print('Reading file ...')
t45c25 = pd.read_excel(file, sheetname='T45_C25')
print('Reading file ...')

plotly_plot(xc_varname, y_varname, t05c25, data1name, t25c25, data2name, t45c25, data3name, set1, file)

t05d25 = pd.read_excel(file, sheetname='T05_D25')
print('Reading file ...')
t25d25 = pd.read_excel(file, sheetname='T25_D25')
print('Reading file ...')
t45d25 = pd.read_excel(file, sheetname='T45_D25')
print('Reading file ...')

plotly_plot(xd_varname, y_varname, t05d25, data1name, t25d25, data2name, t45d25, data3name, set2, file)

t051c = pd.read_excel(file, sheetname='T05_1C')
print('Reading file ...')
t251c = pd.read_excel(file, sheetname='T25_1C')
print('Reading file ...')
t451c = pd.read_excel(file, sheetname='T45_1C')
print('Reading file ...')

plotly_plot(xc_varname, y_varname, t051c, data1name, t251c, data2name, t451c, data3name, set3, file)

t051d = pd.read_excel(file, sheetname='T05_1D')
print('Reading file ...')
t251d = pd.read_excel(file, sheetname='T25_1D')
print('Reading file ...')
t451d = pd.read_excel(file, sheetname='T45_1D')
print('Reading last file ...')

plotly_plot(xd_varname, y_varname, t051d, data1name, t251d, data2name, t451d, data3name, set4, file)

