import pandas as pd
import plotly.express as px
import plotly.data as pldata

df = pldata.wind()
df['strength'] = df['strength'].astype(str).str.replace(r'[^\d\.]', '', regex=True).astype(float)

print("First 5 rows")
df.head()
print("Last 5 rows")
df.tail()

fig = px.scatter(
    df,
    x='frequency',
    y='strength',
    color='direction',  
    title='Wind Data: Strength vs. Frequency',
    labels={'frequency': 'Frequency', 'strength': 'Strength'},
    hover_data=['direction'])
fig.write_html("wind_scatter.html", auto_open=True)