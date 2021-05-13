from sklearn.metrics import precision_score, recall_score , f1_score , classification_report,precision_recall_fscore_support,accuracy_score
import pandas
import pickle
import random

def train_model(classifier, feature_vector_train, label, feature_vector_valid,valid_y, epochs=1, show_report=True, print_pred=False):

    classifier.fit(feature_vector_train, label)

    # predict the labels on validation dataset
    predictions = classifier.predict(feature_vector_valid)

    if print_pred:
      print(predictions)
    if show_report:
      print(classification_report(valid_y,predictions))
    

    filename = 'finalized_model' + str(random.randint(0,100000)) + ".sav"
    pickle.dump(model, open(filename, 'wb'))

    return accuracy_score(valid_y, predictions) , precision_recall_fscore_support(valid_y,predictions)
def test_model(classifier, feature_vector_valid, valid_y, epochs=1, show_report=True, print_pred=False):
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
data_folds = [#pre shuffled
    dataframe.iloc[:4819,:],
    dataframe.iloc[4819:9638,:],
    dataframe.iloc[9638:14457,:],
    dataframe.iloc[14457:19276,:],
]
test_set = dataframe.iloc[19276:,:]#test set



from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn import decomposition, ensemble
features_with_class = ["name_contains_bot","screen_name_contains_bot","name_screen_levenshtein","followers_count","following_count","favorites_count","tweets_count","verified","description_contains_link","description_contains_bot","tweets_contains_link_count","tweets_contains_bot_count","retweet_count","tweet_levenstein1","tweet_levenstein2","tweet_levenstein3","tweet_levenstein4","is_bot"]
features = ["name_contains_bot","screen_name_contains_bot","name_screen_levenshtein","followers_count","following_count","favorites_count","tweets_count","verified","description_contains_link","description_contains_bot","tweets_contains_link_count","tweets_contains_bot_count","retweet_count","tweet_levenstein1","tweet_levenstein2","tweet_levenstein3","tweet_levenstein4"]


model_random_forest =ensemble.RandomForestClassifier(n_estimators=10000,criterion='gini',max_features=None)
model_ada_boost = ensemble.AdaBoostClassifier(n_estimators=10000)
model_hist_grad_boost = ensemble.BaggingClassifier(n_estimators=10000)

model = ensemble.VotingClassifier(estimators=[('rf', model_random_forest), ('ada', model_ada_boost), ('hgb', model_hist_grad_boost)], voting='hard')

# for i in range(0, len(data_folds)): #K folds
#     sum_folds = pandas.DataFrame()
#     for j in range(0, len(data_folds)):
#         if i!=j:
#             sum_folds = sum_folds.append(data_folds[j])
#     train_features = sum_folds[features]
#     train_label = sum_folds["is_bot"]

#     test_features = data_folds[i][features]
#     test_label = data_folds[i]["is_bot"]
#     accuracy , prfs = train_model(model, train_features, train_label, test_features,test_label,print_pred=False)
#     print(accuracy)

filename = "finalized_model55956.sav"
loaded_model = pickle.load(open(filename, 'rb'))

training_set = dataframe.iloc[:19276,:]

train_features = training_set[features]
train_label = training_set["is_bot"]

test_features = test_set[features]
test_label = test_set["is_bot"]
# accuracy , prfs = train_model(model, train_features, train_label, test_features,test_label,print_pred=False)
accuracy , prfs = test_model(loaded_model, test_features,test_label,print_pred=False)
print(accuracy)