from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction pour traiter chaque ligne de la matrice
def traiter_ligne(matrice):
    erreurs = []
    try:
        parcelle = matrice.get('Parcelle', '')
        commune = matrice.get('Commune', '')
        raison_sociale = matrice.get('Raison sociale', '')
        civilite = matrice.get('Civilité', '')
        nom = matrice.get('Nom', '')
        prenom = matrice.get('Prénom', '')
        adresse_principale = matrice.get('Adresse principale', '')
        adresse_complementaire = matrice.get('Adresse complémentaire', '')
        code_postal = matrice.get('Code postal', '')
        ville = matrice.get('Ville', '')
        droit = matrice.get('Droit', '')
        commentaire = matrice.get('Commentaire', '')

        # Vérification des erreurs
        if not parcelle or len(parcelle) > 6:
            erreurs.append(f"Erreur sur la parcelle : {parcelle}")
        
        if not code_postal or len(code_postal) != 5:
            erreurs.append(f"Erreur sur le code postal : {code_postal}")
        
        return [parcelle, commune, raison_sociale, civilite, nom, prenom, adresse_principale, adresse_complementaire, code_postal, ville, droit, commentaire], erreurs

@app.route('/process-matrices', methods=['POST'])
def process_matrices():
    data = request.json
    matrices = data.get('matrices', [])
    tableau = []
    erreurs_totales = []
    
    for matrice in matrices:
        ligne, erreurs = traiter_ligne(matrice)
        tableau.append(ligne)
        if erreurs:
            erreurs_totales.extend(erreurs)
    
    return jsonify({"tableau": tableau, "erreurs": erreurs_totales})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
