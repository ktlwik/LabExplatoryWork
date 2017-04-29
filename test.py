import os
from gensim.models import Word2Vec
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

PATH = "resources/abstract/1992/"

tokenizer = RegexpTokenizer(r'\w+')
wnl = WordNetLemmatizer()

abstracts = []

for f in os.listdir(PATH):
    path = os.path.abspath(PATH+f)
    file = open(path, 'r')

    lines = file.readlines()

    i = 0
    sentences = []
    tokens = []
    text = ""

    for line in lines:

        if line.strip() == "\\\\":
            if i == 2:
                break
            i += 1

        if i == 2:
            line = line.split('.')

            for k in range(len(line)):
                sentence = line[k]
                sentence = sentence.strip()
                tokens.extend([wnl.lemmatize(token) for token in tokenizer.tokenize(sentence)])
                if k != (len(line) - 1):
                    sentences.append(tokens)
                    tokens = []

    abstracts.extend([x for x in sentences if len(x) > 0])

model = Word2Vec(abstracts, min_count=5)
word_vectors = model.wv
vectors = []

for word in word_vectors.vocab.items():
    vectors.append(word_vectors[word[0]])


for i in range(4,20):
    kmeans = KMeans(n_clusters=i).fit(vectors)
    print(silhouette_score(vectors, kmeans.labels_, sample_size=len(vectors)))




