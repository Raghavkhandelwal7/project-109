import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
reading_time=df["reading_time"].tolist()
population_mean=statistics.mean(reading_time)

def randomSetofMean(counter):
    dataset=[]

    for i in range(0,counter):
        randomIndex=random.randint(0,len(reading_time)-1)
        value=reading_time[randomIndex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def show_fig(population_mean):
    df=population_mean
    fig=ff.create_distplot([df], ["reading time"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range (0,100):
        setOfMeans=randomSetofMean(30)
        mean_list.append(setOfMeans)

    show_fig(mean_list)

setup()