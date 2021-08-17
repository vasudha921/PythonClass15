import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go



df= pd.read_csv("data.csv")
data= df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean



def showfig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df],["Math_score"], show_hist= False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = random_set_of_mean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print("mean of sampling distribution:- ", mean)

setup()


    

def stddev():
    stdlist = []
    for i in range(0,1000):
        setofmeans = random_set_of_mean(100)
        stdlist.append(setofmeans)
    stddev = statistics.stdev(stdlist)
    print("standard deviation of sampling distribution:- ", stddev)

stddev()




    