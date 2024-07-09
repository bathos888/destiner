 # Dictionnaire pour les valeurs numériques des lettres
lettre_valeurs = {
    'a': 1, 'j': 1, 's': 1,
    'b': 2, 'k': 2, 't': 2,
    'c': 3, 'l': 3, 'u': 3,
    'd': 4, 'm': 4, 'v': 4,
    'e': 5, 'n': 5, 'w': 5,
    'f': 6, 'o': 6, 'x': 6,
    'g': 7, 'p': 7, 'y': 7,
    'h': 8, 'q': 8, 'z': 8,
    'i': 9, 'r': 9
}

# Dictionnaire des significations de numérologie
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

# Dictionnaire des significations des Nombres de Personnalité
personality_meanings = {
    1: {
        "Impression": "Fort, indépendant, confiant, leader.",
        "Traits visibles": "Dynamisme, charisme, capacité à prendre des initiatives."
    },
    2: {
        "Impression": "Aimable, diplomate, coopératif, calme.",
        "Traits visibles": "Sensibilité, adaptabilité, facilité à travailler en équipe."
    },
    3: {
        "Impression": "Charismatique, communicatif, joyeux, créatif.",
        "Traits visibles": "Enthousiasme, optimisme, capacité à inspirer les autres."
    },
    4: {
        "Impression": "Fiable, pratique, méthodique, sérieux.",
        "Traits visibles": "Sens de l'organisation, discipline, constance."
    },
    5: {
        "Impression": "Aventurier, flexible, sociable, énergique.",
        "Traits visibles": "Curiosité, besoin de liberté, adaptabilité aux changements."
    },
    6: {
        "Impression": "Attentionné, responsable, protecteur, harmonieux.",
        "Traits visibles": "Sens du devoir, compassion, engagement envers les autres."
    },
    7: {
        "Impression": "Introspectif, sage, réservé, analytique.",
        "Traits visibles": "Profondeur intellectuelle, intuition, intérêt pour les questions spirituelles."
    },
    8: {
        "Impression": "Ambitieux, puissant, autoritaire, efficace.",
        "Traits visibles": "Leadership, capacité à gérer des projets, orientation vers le succès matériel."
    },
    9: {
        "Impression": "Humanitaire, généreux, idéaliste, compatissant.",
        "Traits visibles": "Sens de la justice, désir de contribuer au bien-être général, tolérance."
    }
}

# Fonction pour réduire un nombre à un seul chiffre, sauf pour les nombres maîtres 11, 22 et 33
def reduire_nombre(n):
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(chiffre) for chiffre in str(n))
    return n

# Calcul du Nombre de Chemin de Vie
def calculer_nombre_chemin_vie(jour, mois, annee):
    jour_reduit = reduire_nombre(jour)
    mois_reduit = reduire_nombre(mois)
    annee_reduite = reduire_nombre(annee)
    chemin_vie = jour_reduit + mois_reduit + annee_reduite
    return reduire_nombre(chemin_vie)

# Calcul du Nombre d’Expression
def calculer_nombre_expression(nom_complet):
    valeur_totale = sum(lettre_valeurs[char] for char in nom_complet if char in lettre_valeurs)
    return reduire_nombre(valeur_totale)

# Calcul du Nombre d’Âme
def calculer_nombre_ame(nom_complet):
    voyelles = 'aeiou'
    valeur_totale = sum(lettre_valeurs[char] for char in nom_complet if char in voyelles)
    return reduire_nombre(valeur_totale)

# Calcul du Nombre de Personnalité
def calculer_nombre_personnalite(nom_complet):
    voyelles = 'aeiou'
    valeur_totale = sum(lettre_valeurs[char] for char in nom_complet if char not in voyelles and char in lettre_valeurs)
    return reduire_nombre(valeur_totale)

# Fonction pour demander et vérifier l'entrée de la date de naissance
def demander_date_naissance():
    while True:
        date_naissance = input("Entrez votre date de naissance (JJ/MM/AAAA) : ")
        try:
            jour, mois, annee = map(int, date_naissance.split('/'))
            return jour, mois, annee
        except ValueError:
            print("Format de date invalide. Veuillez entrer une date au format JJ/MM/AAAA.")

# Fonction pour demander et vérifier l'entrée du nom complet
def demander_nom_complet():
    while True:
        nom_complet = input("Entrez votre nom complet : ").lower().replace(' ', '')
        if all(char.isalpha() for char in nom_complet):
            return nom_complet
        else:
            print("Le nom ne doit contenir que des lettres.")

# Exemple d'utilisation
jour, mois, annee = demander_date_naissance()
nom_complet = demander_nom_complet()

# Calcul des différents nombres
chemin_vie = calculer_nombre_chemin_vie(jour, mois, annee)
expression = calculer_nombre_expression(nom_complet)
ame = calculer_nombre_ame(nom_complet)
personnalite = calculer_nombre_personnalite(nom_complet)

# Affichage des résultats
print(" "f"\nNombre de Chemin de Vie : {chemin_vie}")
if chemin_vie in numerology_meanings:
    print("     "f"Signification : {numerology_meanings[chemin_vie]['Signification']}")
    print("     "f"Caractéristiques : {numerology_meanings[chemin_vie]['Caractéristiques']}")
    print("     "f"Défis : {numerology_meanings[chemin_vie]['Défis']}")

print(" "f"\nNombre d’Expression : {expression}")
if expression in numerology_meanings:
    print("     "f"Signification : {numerology_meanings[expression]['Signification']}")
    print("     "f"Caractéristiques : {numerology_meanings[expression]['Caractéristiques']}")
    print("     "f"Défis : {numerology_meanings[expression]['Défis']}")

print(" "f"\nNombre d’Âme : {ame}")
if ame in numerology_meanings:
    print("     "f"Signification : {numerology_meanings[ame]['Signification']}")
    print("     "f"Caractéristiques : {numerology_meanings[ame]['Caractéristiques']}")
    print("     "f"Défis : {numerology_meanings[ame]['Défis']}")

print(" "f"\nNombre de Personnalité : {personnalite}")
if personnalite in personality_meanings:
    print("     "f"Impression : {personality_meanings[personnalite]['Impression']}")
    print("     "f"Traits visibles : {personality_meanings[personnalite]['Traits visibles']}")
