import numpy as np
import spacy
import matplotlib.pyplot as plt

nlp = spacy.load("fr_core_news_lg")

def word_vector(word):
    return np.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]])

def most_similar(word, n=1):
    most_similar = nlp.vocab.vectors.most_similar(word_vector(word), n=5)
    return [nlp.vocab.strings[w] for w in most_similar[0][0]]

#Retourne un tableau de nom
def dictToNounsTab(dico):
    text =""
    for key in dico:
        text = text + " " +  key
        for value in dico[key]:
            text = text + " " + value["libelle"]

    doc = nlp(text)
    tabNoms = []
    for token in doc:
        # print(token.text, token.pos_, token.dep_, token.head.text)
        if token.pos_ == 'NOUN' or token.pos_ =="ADJ":
            tabNoms.append(token.text)
    return (tabNoms)
