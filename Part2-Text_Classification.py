# Darren Coughlan - 13305471
# Part 2

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


# ============================================ 1 -- Save articles and categories in lists

articles = []
num_articles = 1408

for n in range(0,num_articles):
    article = open("Article_text_files\\"+str(n)+"_article.txt", "r", encoding="utf8")
    text = article.read()
    articles.append(text)

for x in articles:
    x.lower()

f = open("Categories\\Categories.txt", encoding="utf8")
text = f.read()
categories = text.strip().split()

print(len(categories))
# ============================================= 2 -- Vectorisation and pre-processing
def lemma_tokenizer(text):
    # use the standard scikit-learn tokenizer first
    tokenizer = CountVectorizer().build_tokenizer()
    tokens = tokenizer(text)
    # Then use the NLTK to perform lemmatisation on each token
    lemma_tokens = []
    lemmatizer = WordNetLemmatizer()
    for token in tokens:
        lemma_tokens.append(lemmatizer.lemmatize(token))
    return lemma_tokens


vectorizer = CountVectorizer(tokenizer=lemma_tokenizer,stop_words="english", min_df=5)
data_counts = vectorizer.fit_transform(articles)
# Term frequency weighting
tfidf_transformer = TfidfTransformer()
data_tfidf = tfidf_transformer.fit_transform(data_counts)

data_train, data_test, target_train, target_test = train_test_split(data_tfidf, categories, test_size=0.2)
# ============================================= 3 -- Naive Bayes

model_NB = MultinomialNB()
model_NB.fit(data_train, target_train)
predicted_NB = model_NB.predict(data_test)

acc_NB = accuracy_score(target_test, predicted_NB)
print("Accuracy Score NB: ", acc_NB)

# ============================================= 4 -- KNN

model_KNN = KNeighborsClassifier()
model_KNN.fit(data_train, target_train)
predicted_KNN = model_KNN.predict(data_test)

acc_KNN = accuracy_score(target_test, predicted_KNN)
print("Accuracy Score KNN: ", acc_KNN)

# ============================================= 5 -- SVC

model_SVC = SVC(kernel='linear')
model_SVC.fit(data_train, target_train)
predicted_SVC = model_SVC.predict(data_test)

acc_SVC = accuracy_score(target_test, predicted_SVC)
print("Accuracy Score SVC: ", acc_SVC)


