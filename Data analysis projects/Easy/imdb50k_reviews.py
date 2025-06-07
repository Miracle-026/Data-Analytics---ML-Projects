#Aim: Sentiment Analysis
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from wordcloud import WordCloud
from sklearn.metrics import accuracy_score

#Step 1: Load the data
data = pd.read_csv("C:/Users/DEKATECH/Data analysis projects/Easy/imdb50k.csv")
#print(data.head())

#Step 2: Preprocess the data, remove duplicates, handle missing values and normalize text
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
def process(s):
    s = re.sub(r"[^\w\s]", '', s) #remove punctuation
    s = s.lower() #convert to lowercase
    return s
data['review'] = data['review'].apply(process)
#print(data['review'].head())

#Step 3: Analyze the data to understand trends, distributions and relationships
sns.countplot(x='sentiment', data=data)
plt.title("Sentiment Distribution")
#plt.show()

#Step 4: Convert text data to numerical format
vect = TfidfVectorizer(max_features=5000)
X = vect.fit_transform(data['review']).toarray()
y = data['sentiment'].map({'positive': 1, 'negative': 0}).values

#Step 5: Choose a model for sentiment classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()

#Step 6: Train the model and make predictions
model.fit(X_train, y_train)
preds = model.predict(X_test)

#Step 7: Assess the model's performance
#print(classification_report(y_test, preds))

#Step 8: Predict sentiments on new movie reviews
new_review = ["This movie was fantastic!", "I did not like this film."]
new_review_pro = [process(review) for review in new_review]
new_X = vect.transform(new_review_pro).toarray()
predictions = model.predict(new_X)
#print(predictions)

#Step 9: Visualize data to show findings
pos_reviews = ' '.join(data[data['sentiment']=='positive']['review'])
neg_reviews = ' '.join(data[data['sentiment']=='negative']['review'])
plt.figure(figsize=(10, 5))
plt.subplot(1,2,1)
plt.imshow(WordCloud().generate(pos_reviews))
plt.title('Positive Reviews')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(WordCloud().generate(neg_reviews))
plt.title('Negative Reviews')
plt.axis('off')
#plt.show()

acc_score = accuracy_score(preds, y_test)
print(acc_score)