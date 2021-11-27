import numpy as np
import spacy
import matplotlib.pyplot as plt

nlp = spacy.load("fr_core_news_lg")

def cleanDict(dict):
    dico = {}
    for key in dict:
        values = []
        tab = []
        i = 0
        score = "score"
        noms = "libelle"
        for libelle in dict[key]:
            if libelle[score]:
                values.append(libelle['score'])
                values.append(libelle['libelle'])
            i = i + 1
        tab.append(values)
        if not dict[key]:
            tab1 = [[0, "Aucune Donnée",0, "Aucune Donnée",0, "Aucune Donnée",0, "Aucune Donnée",0, "Aucune Donnée"]]
            dico[key]= tab1
        else:
            dico[key] = tab
    return dico

def dictToNounsTab(dico):
    text =""
    for key in dico:
        text = text + " " +  key
        for value in dico[key]:
            text = text + " " + value["libelle"]
    print(text)
    doc = nlp(text)
    tabNoms = []
    for token in doc:
        # print(token.text, token.pos_, token.dep_, token.head.text)
        if token.pos_ == 'NOUN' or token.pos_ =="ADJ":
            tabNoms.append(token.text)
    print(tabNoms)
    return (tabNoms)

def nounTabToDict(dico):
    dict = {}
    tab = []
    for item in dico:
        temp = item
        doc = nlp(item)
        token = doc[0]
        i = 0
        for items in dico :
            if temp == items :
                i = i + 1
        strtoaddtab = "{\"x\": " + item + ", \"value\":" + str(i) + ", category: " + token.pos_ + "}"
        tab.append(strtoaddtab)

    print(tab)

if __name__ == '__main__':
    dico = {'informatique': [{'libelle': 'Formateur / Formatrice bureautique', 'score': 0.92277384, 'reference': '38238','typeReference': 'metier'},{'libelle': 'Gestionnaire de ressources informatiques', 'score': 0.88337797, 'reference': '15350','typeReference': 'metier'},{'libelle': 'Technicien / Technicienne support en bureautique', 'score': 0.87524617,'reference': '20274', 'typeReference': 'metier'},{'libelle': 'Technicien / Technicienne en micro-informatique et bureautique', 'score': 0.81382895,'reference': '20096', 'typeReference': 'metier'},{'libelle': 'Technicien / Technicienne de maintenance en bureautique', 'score': 0.7996363,'reference': '19836', 'typeReference': 'metier'}], 'micro-informatique': [{'libelle': 'Analyste biologie/microbiologie en industrie', 'score': 1.560887, 'reference': '10931','typeReference': 'metier'},{'libelle': 'Ingénieur / Ingénieure en microbiologie en industrie', 'score': 1.5420476, 'reference': '15772','typeReference': 'metier'},{'libelle': 'Micromécanicien / Micromécanicienne', 'score': 1.4005253, 'reference': '16674','typeReference': 'metier'},{'libelle': 'Technicien / Technicienne en micro-informatique et bureautique', 'score': 1.24875,'reference': '20096', 'typeReference': 'metier'},{'libelle': 'Laborantin / Laborantine chimie environnement en industrie', 'score': 1.2110207,'reference': '16142', 'typeReference': 'metier'}], 'Bio-informatique': [{'libelle': 'Bioinformaticien / Bioinformaticienne en études, recherche et développement', 'score': 2.0,'reference': '11521', 'typeReference': 'metier'},{'libelle': "Directeur adjoint / Directrice adjointe de laboratoire d'analyses de biologie médicale", 'score': 1.7878175, 'reference': '14178', 'typeReference': 'metier'}, {'libelle': "Directeur / Directrice de laboratoire d'analyses de biologie médicale", 'score': 1.7878175, 'reference': '14278', 'typeReference': 'metier'},{'libelle': 'Analyste biologie/microbiologie en industrie', 'score': 1.7874135, 'reference': '10931', 'typeReference': 'metier'},{'libelle': 'Ingénieur / Ingénieure en microbiologie en industrie', 'score': 1.6861458, 'reference': '15772', 'typeReference': 'metier'}], 'bio-informatique': [ {'libelle': 'Bioinformaticien / Bioinformaticienne en études, recherche et développement', 'score': 2.0,'reference': '11521', 'typeReference': 'metier'},{'libelle': "Directeur adjoint / Directrice adjointe de laboratoire d'analyses de biologie médicale",'score': 1.7878175, 'reference': '14178', 'typeReference': 'metier'},{'libelle': "Directeur / Directrice de laboratoire d'analyses de biologie médicale", 'score': 1.7878175,'reference': '14278', 'typeReference': 'metier'},{'libelle': 'Analyste biologie/microbiologie en industrie', 'score': 1.7874135, 'reference': '10931','typeReference': 'metier'},{'libelle': 'Ingénieur / Ingénieure en microbiologie en industrie', 'score': 1.6861458, 'reference': '15772','typeReference': 'metier'}], 'Bioinformatique': []}
    nounTabToDict(dictToNounsTab(dico))

< button onclick = 'wordcloud("[&#39;{&#34;x&#34;: informatique, &#34;value&#34;:1, category: ADJ}&#39;, &#39;{&#34;x&#34;: Formateur, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: Formatrice, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: bureautique, &#34;value&#34;:5, category: ADJ}&#39;, &#39;{&#34;x&#34;: Gestionnaire, &#34;value&#34;:1, category: ADJ}&#39;, &#39;{&#34;x&#34;: ressources, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: informatiques, &#34;value&#34;:1, category: ADJ}&#39;, &#39;{&#34;x&#34;: Technicien, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: Technicienne, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: support, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: bureautique, &#34;value&#34;:5, category: ADJ}&#39;, &#39;{&#34;x&#34;: Technicien, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: Technicienne, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: micro-informatique, &#34;value&#34;:3, category: ADJ}&#39;, &#39;{&#34;x&#34;: bureautique, &#34;value&#34;:5, category: ADJ}&#39;, &#39;{&#34;x&#34;: Technicien, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: Technicienne, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: maintenance, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: bureautique, &#34;value&#34;:5, category: ADJ}&#39;, &#39;{&#34;x&#34;: micro-informatique, &#34;value&#34;:3, category: ADJ}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: microbiologie, &#34;value&#34;:6, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: Ingénieur, &#34;value&#34;:3, category: NOUN}&#39;, &#39;{&#34;x&#34;: Ingénieure, &#34;value&#34;:3, category: ADJ}&#39;, &#39;{&#34;x&#34;: microbiologie, &#34;value&#34;:6, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: Micromécanicien, &#34;value&#34;:1, category: PROPN}&#39;, &#39;{&#34;x&#34;: Micromécanicienne, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: Technicien, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: Technicienne, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: micro-informatique, &#34;value&#34;:3, category: ADJ}&#39;, &#39;{&#34;x&#34;: bureautique, &#34;value&#34;:5, category: ADJ}&#39;, &#39;{&#34;x&#34;: Laborantin, &#34;value&#34;:1, category: PROPN}&#39;, &#39;{&#34;x&#34;: chimie, &#34;value&#34;:1, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: Bio-informatique, &#34;value&#34;:1, category: ADJ}&#39;, &#39;{&#34;x&#34;: Bioinformaticien, &#34;value&#34;:2, category: ADJ}&#39;, &#39;{&#34;x&#34;: études, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: recherche, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: développement, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: Directeur, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: adjoint, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: Directrice, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: adjointe, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: laboratoire, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: analyses, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: médicale, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: Directeur, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: Directrice, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: laboratoire, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: analyses, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: médicale, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: Analyste, &#34;value&#34;:2, category: PROPN}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: microbiologie, &#34;value&#34;:6, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: Ingénieur, &#34;value&#34;:3, category: NOUN}&#39;, &#39;{&#34;x&#34;: Ingénieure, &#34;value&#34;:3, category: ADJ}&#39;, &#39;{&#34;x&#34;: microbiologie, &#34;value&#34;:6, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: bio-informatique, &#34;value&#34;:1, category: ADJ}&#39;, &#39;{&#34;x&#34;: Bioinformaticien, &#34;value&#34;:2, category: ADJ}&#39;, &#39;{&#34;x&#34;: études, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: recherche, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: développement, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: Directeur, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: adjoint, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: Directrice, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: adjointe, &#34;value&#34;:2, category: NOUN}&#39;, &#39;{&#34;x&#34;: laboratoire, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: analyses, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: médicale, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: Directeur, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: Directrice, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: laboratoire, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: analyses, &#34;value&#34;:4, category: NOUN}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: médicale, &#34;value&#34;:4, category: ADJ}&#39;, &#39;{&#34;x&#34;: Analyste, &#34;value&#34;:2, category: PROPN}&#39;, &#39;{&#34;x&#34;: biologie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: microbiologie, &#34;value&#34;:6, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: Ingénieur, &#34;value&#34;:3, category: NOUN}&#39;, &#39;{&#34;x&#34;: Ingénieure, &#34;value&#34;:3, category: ADJ}&#39;, &#39;{&#34;x&#34;: microbiologie, &#34;value&#34;:6, category: NOUN}&#39;, &#39;{&#34;x&#34;: industrie, &#34;value&#34;:7, category: NOUN}&#39;, &#39;{&#34;x&#34;: Bioinformatique, &#34;value&#34;:1, category: ADJ}&#39;]")' > nuage < / button >
