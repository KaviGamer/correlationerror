import plotly.express as px
import pandas as pd

df = pd.read_csv("coffee.csv")
figure = px.scatter(df,x="Coffee in ml",y="sleep in hours")
figure.show()