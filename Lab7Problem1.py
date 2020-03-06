from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
#score with bigram is 0.765, only a very slight decrease from before
#score with stop words = english is 0.807, a little bit of an increase from the original
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
#print(tfidf_Vect.vocabulary_)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = clf.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print(score)
#score before changes is 0.774

#svc = SVC()
#svc.fit(X_train_tfidf, twenty_train.target)
#Y_pred = svc.predict(X_test_tfidf)
#acc_svc = round(svc.score(X_train_tfidf, twenty_train.target) * 100, 2)
#print("svm accuracy is:", acc_svc)
#score after svm is 99.78, but it took a lot longer
