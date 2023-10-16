from datetime import datetime
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Caesar="Николай II", Start='1896-05-14', Finish='1917-03-09'),
    dict(Caesar="Александр III", Start='1883-05-15', Finish='1894-10-20'),
    dict(Caesar="Александр II", Start='1856-08-26', Finish='1881-03-01'),
    dict(Caesar="Николай I", Start='1826-08-22', Finish='1855-02-18'),
    dict(Caesar="Александр I", Start='1801-09-15', Finish='1825-12-01'),
])

dates = [datetime.strptime(d, "%Y-%m-%d") for d in df["Start"]]
Color = ['gray']*len(df)
Level = ['Периоды правления']*len(df)
df['Level'] = Level
df['Color'] = Color
df['Start'] = [datetime.strptime(d, "%Y-%m-%d") for d in df["Start"]]
df['Finish'] = [datetime.strptime(d, "%Y-%m-%d") for d in df["Finish"]]

fig = px.timeline(df, 
    x_start="Start", 
    x_end="Finish", 
    y="Level", 
    color="Color", 
    text="Caesar", 
    hover_name=df['Caesar']+'\n'+[datetime.strftime(d,'%d %b %Y') for d in df['Start']])
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()
