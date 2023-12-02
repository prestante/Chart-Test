import pandas as pd
import plotly.express as px

#df = pd.read_csv(r'C:\PS\logs\CTC-02 2023-11-30 11-44-50.csv')
df = pd.read_csv(r'C:\PS\logs\18MB 2023-11-23 10-16-38.csv')
fig = px.line(df, x='Time', y=['services(952)CPU'], title='Title of your graph')
fig.show()
