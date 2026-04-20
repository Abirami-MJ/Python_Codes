#NLP CODES


### Tokenization ###
#it is a process of splitting a text into a chunk of pieces 
import nltk
from nltk.tokenize import word_tokenize
#nltk.download("punkt")
nltk.download("punkt_tab")
text="Hello everyone! how are you"
tokens=word_tokenize(text)
print(tokens)


### Stop words ###
### it is used to remove common words in a setence like the, is, a etc 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
text= " NLP is the subfield of AI which helps to perform task in related to text "
words= word_tokenize(text)
stop_words=set(stopwords.words("english"))
filtered_words=[word for word in words if word.lower() not in stop_words]
print("original:", text)
print("filtered:"," ".join(filtered_words))


### stemming ###
# It is used to remove a part of word like Playing -> play.
from nltk. stem import PorterStemmer
stemmer= PorterStemmer()
words=["playing", "walking","Dancing", "jogging"]
stemmed_words=[stemmer.stem(word) for word in words]
print("Stemmed words:",stemmed_words)


### Lemmatization ###

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import  wordnet
nltk.download("wordnet")
lemmatizer=WordNetLemmatizer()
words=["playing","played", "walking","Dancing", "jogging","running"]
lemmatized_words=[lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]
print("lemmatized_words:", lemmatized_words)

### POS Tagging ###
import nltk
from nltk. tokenize import word_tokenize
from nltk import pos_tag
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
sentence=" the quick brown fox jumps over the lazy dog."
tokens=word_tokenize(sentence)
tagged=pos_tag(tokens)
print(tagged)


### Syntax and parsing 
exp="5+3*3"
result=eval(exp)
print(result)

### lowercasing
text="EXCELLENT"
lowercase_text=text.lower()
print(lowercase_text)

###Removal of spl character
# to rem punction , spl charc like @#$!%^^ etc
import re
def remove(text):
    return re.sub(r'[^A-Za-z0-9\s]', "",text)
i="Hello All #@!@@#$%"
c=remove(i)
print(c)

### Remove punctuation
import string
def remove_punctuation(text):
return text.translate(str.maketrans('', '', string.punctuation))
# Example usage
text = "Lets make this NLP more intersting."
clean_text = remove_punctuation(text)
print(clean_text)


###Bag of words
from sklearn.feature_extraction.text import CountVectorizer
# Sample documents
documents = [
"I love NLP ",
"NLP is used to perform a task with text",
"I love learning NLP"
]
# Create the Bag of Words model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
# Get feature names and transformed data
feature_names = vectorizer.get_feature_names_out()
print("Feature Names:", feature_names)
print("Bag of Words Model:\n", X.toarray())


### N - gram
def n_grams(text, n):
words = text.split()
return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
# Example usage
text = "The world is too big"
n = 2
print(n_grams(text, n))
