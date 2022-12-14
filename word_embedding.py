# %%
from itertools import combinations

import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "funny comedy music laugh humor song songs jokes musical hilarious"
)
doc = nlp(text)

for token1, token2 in combinations(doc, 2):
    print(
        f"similarity between {token1} and {token2} is {token1.similarity(token2)}"
    )


# %%
import pandas as pd
from gensim.models import Word2Vec
from tqdm import tqdm


data = pd.read_csv("train.csv")

# train a Word2vec model
sentences=[]
data = data.sample(200)
for review in data["review"]:
    doc = nlp(review)
    for sent in doc.sents:
        sentences.append(
            [token.text.lower() for token in sent]
        )

model = Word2Vec(sentences)


# %%
for token1, token2 in combinations(text.split(), 2):
    print(
        f"similarity between {token1} and {token2} is {model.wv.similarity(token1, token2)}"
    )

# %%
