import pandas
def getDataFrame(csvSource):
    return pandas.read_csv(csvSource)
# def writeToCSV()
def makeCSV(dataframe):
    dataframe.to_csv(r'data/twitter_data.csv', index = False)
