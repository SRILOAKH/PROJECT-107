import csv
import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig=px.scatter(mean,x="student_id",y="level",color="attempt",size_max=60)
fig.show()