from sklearn import preprocessing
import pickle
from sklearn import metrics

with open("df.pickle",'r') as f:
    df = pickle.load(f)


le = preprocessing.LabelEncoder()
le.fit(df['genres'])

list(le.classes_)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline




text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

import numpy as np
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( df['synopsis'], le.transform(df['genres']), test_size=0.33, random_state=42)

text_clf.fit(X_train, y_train)


def show_top10(classifier, categories):
    for i, category in enumerate(categories):
        top10 = np.argsort(classifier.coef_[i])[-10:]
        print("%s: %s" % (category, " ".join(le.transform(top10))))

pred = text_clf.predict(X_test)
# metrics.f1_score(y_test, pred, average='macro')

# show_top10(text_clf, df['synopsis'])

import pickle
with open("labels.pickle",'wb') as f:
    pickle.dump(le, f)

with open("model.pickle",'wb') as f:
    pickle.dump(text_clf, f)
