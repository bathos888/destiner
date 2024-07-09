lettre1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}
lettre2 = {"j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9}
lettre3 = {"s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6, "y": 7, "z": 8}

numerology_meanings = {
    1: {
        "Signification": "Leadership, indépendance, innovation, ambition.",
        "Caractéristiques": "Créatif, déterminé, sûr de soi, individualiste.",
        "Défis": "Éviter l'égoïsme et la solitude."
    },
    2: {
        "Signification": "Coopération, équilibre, sensibilité, diplomatie.",
        "Caractéristiques": "Empathique, adaptable, diplomatique, patient.",
        "Défis": "Éviter la dépendance et l'indécision."
    },
    3: {
        "Signification": "Créativité, communication, expression, sociabilité.",
        "Caractéristiques": "Expressif, optimiste, sociable, artistique.",
        "Défis": "Éviter la dispersion et l'imprévoyance."
    },
    4: {
        "Signification": "Stabilité, travail, structure, fiabilité.",
        "Caractéristiques": "Pratique, organisé, discipliné, méthodique.",
        "Défis": "Éviter la rigidité et l'entêtement."
    },
    5: {
        "Signification": "Liberté, aventure, changement, adaptabilité.",
        "Caractéristiques": "Curieux, adaptable, énergique, dynamique.",
        "Défis": "Éviter l'impatience et l'instabilité."
    },
    6: {
        "Signification": "Responsabilité, service, amour, harmonie.",
        "Caractéristiques": "Protecteur, attentionné, loyal, équilibré.",
        "Défis": "Éviter l'ingérence et le sacrifice excessif."
    },
    7: {
        "Signification": "Introspection, sagesse, spiritualité, analyse.",
        "Caractéristiques": "Réfléchi, intuitif, introspectif, intellectuel.",
        "Défis": "Éviter l'isolement et le scepticisme excessif."
    },
    8: {
        "Signification": "Pouvoir, matérialisme, réussite, autorité.",
        "Caractéristiques": "Ambitieux, discipliné, efficient, leader.",
        "Défis": "Éviter l'avidité et l'abus de pouvoir."
    },
    9: {
        "Signification": "Humanitarisme, altruisme, compassion, universalisme.",
        "Caractéristiques": "Généreux, compatissant, idéaliste, tolérant.",
        "Défis": "Éviter la désillusion et le sentiment de martyr."
    }
}

# Demander le nom de l'utilisateur
entreNom = input("Entrer votre nom s'il vous plaît: ").lower()

# Initialiser la somme des valeurs des lettres du nom
valeur_totale = 0

# Initialiser le dictionnaire pour stocker les valeurs des caractères avec leurs occurrences
nom = {}

# Calculer la somme des valeurs des lettres en prenant en compte les occurrences
for char in entreNom:
    if char in lettre1:
        valeur_totale += lettre1[char]
    elif char in lettre2:
        valeur_totale += lettre2[char]
    elif char in lettre3:
        valeur_totale += lettre3[char]
    
    # Enregistrer l'occurrence du caractère et sa valeur
    if char in nom:
        nom[char].append(lettre1.get(char) or lettre2.get(char) or lettre3.get(char))
    else:
        nom[char] = [lettre1.get(char) or lettre2.get(char) or lettre3.get(char)]

# Calculer la somme des chiffres si la valeur totale est composée de plusieurs chiffres
somme_chiffres = valeur_totale
if valeur_totale > 9:
    somme_chiffres = sum(int(chiffre) for chiffre in str(valeur_totale))

# Afficher les résultats pour chaque caractère
for char, valeurs in nom.items():
    if valeurs[0] is not None:
        occurrences = len(valeurs)
        total_par_lettre = sum(valeurs)
        print(f"Le caractère '{char}' apparaît {occurrences} fois avec une valeur totale de {total_par_lettre}")
    else:
        print(f"Le caractère '{char}' n'est trouvé dans aucun dictionnaire")

print(f"La valeur totale des lettres dans le nom '{entreNom}' est: {valeur_totale}")
print(f"La somme des chiffres de la valeur totale est: {somme_chiffres}")

# Afficher les significations en numérologie
if somme_chiffres in numerology_meanings:
    print(f"Signification du chiffre {somme_chiffres} :")
    print(f"Signification : {numerology_meanings[somme_chiffres]['Signification']}")
    print(f"Caractéristiques : {numerology_meanings[somme_chiffres]['Caractéristiques']}")
    print(f"Défis : {numerology_meanings[somme_chiffres]['Défis']}")
else:
    print(f"Aucune signification trouvée pour le chiffre {somme_chiffres}.")
