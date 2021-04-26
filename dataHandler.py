import random

import os
import pandas
def getDataFrame(csvSource):
    return pandas.read_csv(csvSource)

def makeCSV(dataframe, index):
    file_name = "data/twitter_data"+str(index)+".csv"
    dataframe.to_csv(file_name, index = False)
