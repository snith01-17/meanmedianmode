import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("SOCR-HeightWeight 3.csv")
heightList = df["Height(Inches)"].to_list()

mean = statistics.mean(heightList)
median = statistics.median(heightList)
mode = statistics.mode(heightList)

print("Mean of data is: {}".format(mean))
print("Median of data is: {}".format(median))
print("Mode of data is: {}".format(mode))
