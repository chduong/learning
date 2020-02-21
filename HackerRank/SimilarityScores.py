# ###### Not using Sklearn
import math

corpus = """I'd like an apple.
          An apple a day keeps the doctor away.
          Never compare an apple to an orange.
          I prefer scikit-learn to orange."""

count = lambda word, doc: sum(w == word for w in doc.split())
inner = lambda a, b: [aa * bb for aa, bb in zip(a, b)]
dot = lambda a, b: sum(inner(a,b))

words = list(set(corpus.split()))
tf = [[count(word, doc) for word in words] for doc in corpus.split('\n')]
idf = [math.log(1. / (1 + sum(word in doc.split() for doc in corpus.split('\n')))) for word in words]

# Term Frequency-Inverse Document Frequency
# https://en.wikipedia.org/wiki/Tf%E2%80%93idf
tfidf = [inner(t, idf) for t in tf]

# Cosine similarity to compare documents
# https://en.wikipedia.org/wiki/Cosine_similarity
cosine_similarity = [dot(tfidf[0], t) /
                     math.sqrt(dot(tfidf[0], tfidf[0])) /
                     math.sqrt(dot(t, t)) for t in tfidf[1: ]]

print(cosine_similarity.index(max(cosine_similarity)) + 2) # starting with the second document

# ###### Using Sklearn
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
#
# # Document list
# corpus = [
#     "I'd like an apple.",
#     "An apple a day keeps the doctor away.",
#     "Never compare an apple to an orange.",
#     "I prefer scikit-learn to orange.",
# ]
#
# # Tokenize and Transform to Sparse Matrix
# vectorizer = TfidfVectorizer()
# sparse = vectorizer.fit_transform(corpus)
#
# # Dot product similiarities
# similarities_matrix = sparse * sparse.T
#
# # Returns the maximum element of similarity matrix, sheet-0, rows 1 onwards, all columns.
# # Adds 2 to the answer since the documents are 1-indexed and we're starting with the second document.
# print("{0}".format(np.argmax(similarities_matrix[0, 1:].toarray()) + 2))
#
# # Scores closer to 1 indicate high similarity
