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
            tab = [[0, "Aucune Donnée",0, "Aucune Donnée",0, "Aucune Donnée",0, "Aucune Donnée",0, "Aucune Donnée"]]
        dico[key] = tab
    print(dico)

if __name__ == '__main__':
    dico = {'mathématique': [{'libelle': 'Pratiquer une rééducation orthophonique du raisonnement logico-mathématique (dyscalculie, ...)','score': 0.7788358, 'reference': '107543', 'typeReference': 'competence'}, {'libelle': 'Développer la démarche pédagogique et enseigner les savoirs fondamentaux (français, mathématiques, sciences, ...)','score': 0.7785947, 'reference': '108475', 'typeReference': 'competence'},{'libelle': 'Modélisation mathématique', 'score': 0.4637821, 'reference': '101332','typeReference': 'competence'},{'libelle': 'Education physique et sportive (EPS)', 'score': 0.41906714, 'reference': '118219','typeReference': 'competence'},{'libelle': 'Réaliser des modèles mathématiques financiers pour des opérateurs de marchés', 'score': 0.3980957,'reference': '124135', 'typeReference': 'competence'}], 'Mathématique': [{'libelle': 'Professeur / Professeure de mathématiques', 'score': 1.1606647, 'reference': '38344','typeReference': 'metier'},{'libelle': "Professeur / Professeure d'éducation physique et sportive -EPS-", 'score': 0.52861255,'reference': '18150', 'typeReference': 'metier'},{'libelle': "Professeur / Professeure d'histoire géographie", 'score': 0.4630537, 'reference': '38347','typeReference': 'metier'},{'libelle': 'Chercheur / Chercheuse en géographie', 'score': 0.3741603, 'reference': '12609','typeReference': 'metier'},{'libelle': 'Chercheur / Chercheuse en sciences humaines et sociales', 'score': 0.31309664,'reference': '12614', 'typeReference': 'metier'}], 'mathématisation': [], 'arithmétique': [], 'théorique': [{'libelle': "Pharmacien / Pharmacienne responsable BPDO - bonnes pratiques de dispensation de l'oxygène",'score': 0.2955705, 'reference': '140907', 'typeReference': 'metier'},{'libelle': "Professeur / Professeure d'enseignement technique et pratique", 'score': 0.26814485,'reference': '18159', 'typeReference': 'metier'},{'libelle': "Chargé / Chargée d'affaires bancaires professionnelles", 'score': 0.21708167, 'reference': '11750','typeReference': 'metier'},{'libelle': 'Responsable de communication interne', 'score': 0.21016213, 'reference': '18693','typeReference': 'metier'},{'libelle': 'Consultant / Consultante interne en formation', 'score': 0.21016213, 'reference': '13547','typeReference': 'metier'}]}
    cleanDict(dico)

