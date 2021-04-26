from sklearn.metrics import precision_score, recall_score , f1_score , classification_report,precision_recall_fscore_support,accuracy_score

def train_model(classifier, feature_vector_train, label, feature_vector_valid,valid_y, epochs=1, show_report=True, print_pred=False):

    classifier.fit(feature_vector_train, label)
    
    # predict the labels on validation dataset
    predictions = classifier.predict(feature_vector_valid)

    if print_pred:
      print(predictions)
    if show_report:
      print(classification_report(valid_y,predictions))
    return accuracy_score(valid_y, predictions) , precision_recall_fscore_support(valid_y,predictions)


import dataHandler
dataFile = "data/feature_data.csv"
dataframe = dataHandler.getDataFrame(dataFile)

print(dataframe.shape)
data_folds = [
    dataframe.iloc[:4819,:],
    dataframe.iloc[4819:9638,:],
    dataframe.iloc[9638:14457,:],
    dataframe.iloc[14457:19276,:],
    dataframe.iloc[19276:,:]
]


from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn import decomposition, ensemble

model=ensemble.RandomForestClassifier(n_estimators=10000,criterion='gini',max_features=None)

features = ["name_contains_bot","screen_name_contains_bot","name_screen_levenshtein","followers_count","following_count","favorites_count","tweets_count","verified","description_contains_link","description_contains_bot","tweets_contains_link_count","tweets_contains_bot_count","retweet_count","tweet_levenstein1","tweet_levenstein2","tweet_levenstein3","tweet_levenstein4",]

train_features = data_folds[0][features]
train_label = data_folds[0]["is_bot"]

test_features = data_folds[4][features]
test_label = data_folds[4]["is_bot"]
accuracy , prfs = train_model(model, train_features, train_label, test_features,test_label,print_pred=False)
print(accuracy)
