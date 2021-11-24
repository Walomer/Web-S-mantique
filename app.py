import os
from flask import Flask, render_template, request
import sys
from api import *
from word_similar import *

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route('/')
def home():
    # #* C'est ici qu'on fera le traitement des valeurs en python
    return render_template('home.html')#, data=res)

@app.route('/research', methods=['POST'])
def research():
    if request.form['data'] and request.form['choice']:
        data = request.form['data']
        print(data)
        choice = request.form['choice']
        mostSim = most_similar(data)
        res = search(data, choice)
        print(res)
        nlpTab = dictToNounsTab(res)
        res = cleanDict(res)
        return render_template('home.html', mostSim = mostSim, data=res, wordcloud=nlpTab)
    else:
        return render_template('home.html')        


@app.route('/test')
def test():
    return render_template('test.html')
if __name__=="__main__":
    app.run(debug=True, port=3000)