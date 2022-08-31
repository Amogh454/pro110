#Creator: Amogh P Kaushik
#DataSampling project of class 110

#importing libraries
import statistics
import pandas as pd
import random
import plotly.figure_factory as ff

#reading data using pandas
data = pd.read_csv("medium_data.csv");
#data to array
dataList = data["reading_time"].tolist();
#calculating mean and printing the same
population_mean = statistics.mean(dataList);
print("Population Mean:",population_mean);
#plotting on graph
fig = ff.create_distplot([dataList],["Reading Time"],show_hist=False);
fig.show();

#Code to find the mean of the 30 sample data. 
# In place of the counter pass the number of samples you want to take.
def random_mean(counter):
  dataSet = []
  for i in range(30,counter):
    randomIndex = random.randint(30,len(dataList))
    value = dataList[randomIndex];
    dataSet.append(value)
  sample_mean = statistics.mean(dataSet)
  return sample_mean 


#Repeating the data for 100 times
def setup():
  meanList = []
  for i in range(0,100):
    mean_set = random_mean(30);
    meanList.append(mean_set)
  sampling_mean = statistics.mean(meanList)
  print("Sampling Mean:",sampling_mean)
  showFig(meanList);

def showFig(mean_list):
  df = mean_list
  fig = ff.create_distplot([df],["Reading Time"],show_hist=False)
  fig.show()


setup();