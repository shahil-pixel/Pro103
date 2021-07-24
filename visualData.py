import pandas as pd
import plotly_express as px

df = pd.read_csv("covidData.csv")
fig = px.line(df,x = "date",y = "cases",color = "country")
fig.show()
