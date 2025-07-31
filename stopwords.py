import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('spanish')
print(lista_stopwords)