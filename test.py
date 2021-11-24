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

if __name__ == '__main__':
    dico = {'informatique': [{'libelle': 'Formateur / Formatrice bureautique', 'score': 0.92277384, 'reference': '38238','typeReference': 'metier'},{'libelle': 'Gestionnaire de ressources informatiques', 'score': 0.88337797, 'reference': '15350','typeReference': 'metier'},{'libelle': 'Technicien / Technicienne support en bureautique', 'score': 0.87524617,'reference': '20274', 'typeReference': 'metier'},{'libelle': 'Technicien / Technicienne en micro-informatique et bureautique', 'score': 0.81382895,'reference': '20096', 'typeReference': 'metier'},{'libelle': 'Technicien / Technicienne de maintenance en bureautique', 'score': 0.7996363,'reference': '19836', 'typeReference': 'metier'}], 'micro-informatique': [{'libelle': 'Analyste biologie/microbiologie en industrie', 'score': 1.560887, 'reference': '10931','typeReference': 'metier'},{'libelle': 'Ingénieur / Ingénieure en microbiologie en industrie', 'score': 1.5420476, 'reference': '15772','typeReference': 'metier'},{'libelle': 'Micromécanicien / Micromécanicienne', 'score': 1.4005253, 'reference': '16674','typeReference': 'metier'},{'libelle': 'Technicien / Technicienne en micro-informatique et bureautique', 'score': 1.24875,'reference': '20096', 'typeReference': 'metier'},{'libelle': 'Laborantin / Laborantine chimie environnement en industrie', 'score': 1.2110207,'reference': '16142', 'typeReference': 'metier'}], 'Bio-informatique': [{'libelle': 'Bioinformaticien / Bioinformaticienne en études, recherche et développement', 'score': 2.0,'reference': '11521', 'typeReference': 'metier'},{'libelle': "Directeur adjoint / Directrice adjointe de laboratoire d'analyses de biologie médicale", 'score': 1.7878175, 'reference': '14178', 'typeReference': 'metier'}, {'libelle': "Directeur / Directrice de laboratoire d'analyses de biologie médicale", 'score': 1.7878175, 'reference': '14278', 'typeReference': 'metier'},{'libelle': 'Analyste biologie/microbiologie en industrie', 'score': 1.7874135, 'reference': '10931', 'typeReference': 'metier'},{'libelle': 'Ingénieur / Ingénieure en microbiologie en industrie', 'score': 1.6861458, 'reference': '15772', 'typeReference': 'metier'}], 'bio-informatique': [ {'libelle': 'Bioinformaticien / Bioinformaticienne en études, recherche et développement', 'score': 2.0,'reference': '11521', 'typeReference': 'metier'},{'libelle': "Directeur adjoint / Directrice adjointe de laboratoire d'analyses de biologie médicale",'score': 1.7878175, 'reference': '14178', 'typeReference': 'metier'},{'libelle': "Directeur / Directrice de laboratoire d'analyses de biologie médicale", 'score': 1.7878175,'reference': '14278', 'typeReference': 'metier'},{'libelle': 'Analyste biologie/microbiologie en industrie', 'score': 1.7874135, 'reference': '10931','typeReference': 'metier'},{'libelle': 'Ingénieur / Ingénieure en microbiologie en industrie', 'score': 1.6861458, 'reference': '15772','typeReference': 'metier'}], 'Bioinformatique': []}
    dictToNounsTab(dico)

