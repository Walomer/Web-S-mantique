import requests
import urllib3
import time
import json
from word_similar import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"

client_id = 'PAR_websemantique_6b9a9a83f0946fdf26704cad34bc48f61a3d56c980c4a7b608fcafee09096a29'
client_secret = '23fe9002964208cf8f72199219d06f5772672fb4354ea816a96f3de7b4e36b65'

scope = 'application_PAR_websemantique_6b9a9a83f0946fdf26704cad34bc48f61a3d56c980c4a7b608fcafee09096a29 api_explorateurmetiersv1 explojob'

payload = {
 'client_id': client_id,
 'client_secret': client_secret,
 'grant_type': "client_credentials",
 'scope': scope
}

print("Requesting Token...")
response = requests.post(auth_url, data=payload, verify=False)

print("Response: " + str(response.status_code))
if response.status_code == 200:
 print('Status: Success!\n')
elif response.status_code == 404:
 print('Status: Not Found.\n')

access_token = response.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}

# url = "https://api.emploi-store.fr/partenaire/offresdemploi/v2/referentiel/naturesContrats"
# result = requests.get(url, headers=header, params=param).json()
# print(result)

def search(word, choice):
    answer = {}
    print(most_similar(word))
    url = "https://api.emploi-store.fr/partenaire/explorateurmetiers/v1/explorateurmetiers?libelle="+word+"&nombre=5&type="+choice
    result = requests.get(url, headers=header, params=param).json()
    answer[word] = result
    #* Acces API selon compétences
    #* url_competence = "https://api.emploi-store.fr/partenaire/explorateurmetiers/v1/explorateurmetiers?libelle="+word+"&nombre=5&type=competence"
    #* result_comp = requests.get(url_competence, headers=header, params=param).json()
    #* print(result_comp)
    
    #? faire la double séléction métier/compétence, trier par score et retourner les meilleurs avec les word similar ?
    
    i=0
    while i < len(most_similar(word))-1:
        i+=1
        url = "https://api.emploi-store.fr/partenaire/explorateurmetiers/v1/explorateurmetiers?libelle="+most_similar(word)[i]+"&nombre=5&type=metier"
        result = requests.get(url, headers=header, params=param).json()
        if not result:
            print("Profession pas trouvée dans l'API")
        answer[most_similar(word)[i]]=result
    return answer

def cleanDict(dict):
    dico = {}
    for key in dict:
        values = []
        tab = []
        i = 0
        score = "score"
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
        print(dico)
    return dico