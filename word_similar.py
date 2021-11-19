import numpy as np
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nlp = spacy.load("fr_core_news_lg")

def word_vector(word):
    return np.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]])

def most_similar(word, n=1):
    most_similar = nlp.vocab.vectors.most_similar(word_vector(word), n=5)
    return [nlp.vocab.strings[w] for w in most_similar[0][0]]

def wordCloud():
    wc = WordCloud(max_font_size=40, background_color = 'white').generate("je ne sais pas ce que je suis en traine de dire, je ne sais pas je dire que le temps")
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    

if __name__ == "__main__":
    #print(most_similar("informatique"))
    wordCloud()