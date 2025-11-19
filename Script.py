#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de Planning Partagé
Projet Python - Gestion d'événements et participants
"""

from datetime import datetime

# Données de base
PARTICIPANTS = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
SALLES = {"Salle A": 10, "Salle B": 20, "Salle C": 5, "Salle D": 15}
evenements = []


def valider_date(date_str):
    """Vérifie si le format de date est correct"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False


def valider_heure(heure_str):
    """Vérifie si le format d'heure est correct"""
    try:
        datetime.strptime(heure_str, "%H:%M")
        return True
    except:
        return False


def ajouter_evenement():
    """Créer un nouvel événement"""
    print("\n=== CRÉER UN ÉVÉNEMENT ===")
    
    titre = input("Titre: ")
    if not titre:
        print("Erreur: titre vide")
        return
    
    date = input("Date (AAAA-MM-JJ): ")
    if not valider_date(date):
        print("Erreur: format de date invalide")
        return
    
    heure_debut = input("Heure début (HH:mm): ")
    if not valider_heure(heure_debut):
        print("Erreur: format d'heure invalide")
        return
    
    heure_fin = input("Heure fin (HH:mm): ")
    if not valider_heure(heure_fin):
        print("Erreur: format d'heure invalide")
        return
    
    # Vérifier que l'heure est entre 9h et 18h
    h_debut = datetime.strptime(heure_debut, "%H:%M").time()
    h_fin = datetime.strptime(heure_fin, "%H:%M").time()
    limite_min = datetime.strptime("09:00", "%H:%M").time()
    limite_max = datetime.strptime("18:00", "%H:%M").time()
    
    if not (limite_min <= h_debut <= limite_max and limite_min <= h_fin <= limite_max):
        print("Erreur: les heures doivent être entre 9h et 18h")
        return
    
    if h_debut >= h_fin:
        print("Erreur: l'heure de début doit être avant l'heure de fin")
        return
    
    print(f"Salles: {', '.join(SALLES.keys())}")
    salle = input("Salle (optionnel): ")
    
    if salle and salle not in SALLES:
        print("Erreur: cette salle n'existe pas")
        return
    
    # Vérifier si la salle est libre
    if salle:
        for evt in evenements:
            if evt['salle'] == salle and evt['date'] == date:
                debut1 = datetime.strptime(evt['heure_debut'], "%H:%M")
                fin1 = datetime.strptime(evt['heure_fin'], "%H:%M")
                debut2 = datetime.strptime(heure_debut, "%H:%M")
                fin2 = datetime.strptime(heure_fin, "%H:%M")
                
                if not (fin1 <= debut2 or fin2 <= debut1):
                    print("Erreur: salle déjà occupée à cet horaire")
                    return
    
    evenements.append({
        "titre": titre,
        "date": date,
        "heure_debut": heure_debut,
        "heure_fin": heure_fin,
        "salle": salle if salle else None,
        "participants": []
    })
    
    print(f"Événement '{titre}' créé!")


def afficher_evenements_par_date():
    """Afficher tous les événements"""
    print("\n=== LISTE DES ÉVÉNEMENTS ===")
    
    if not evenements:
        print("Aucun événement")
        return
    
    # Trier par date et heure
    evt_tries = sorted(evenements, key=lambda e: (e["date"], e["heure_debut"]))
    
    for i, evt in enumerate(evt_tries, 1):
        salle_info = f" - Salle: {evt['salle']}" if evt['salle'] else ""
        print(f"\n{i}. {evt['titre']}")
        print(f"   {evt['date']} | {evt['heure_debut']}-{evt['heure_fin']}{salle_info}")
        print(f"   Participants: {len(evt['participants'])}")


def supprimer_evenement():
    """Supprimer un événement"""
    print("\n=== SUPPRIMER UN ÉVÉNEMENT ===")
    
    if not evenements:
        print("Aucun événement")
        return
    
    for i, evt in enumerate(evenements, 1):
        print(f"{i}. {evt['titre']} - {evt['date']}")
    
    try:
        choix = int(input("\nNuméro (0 pour annuler): "))
        if choix == 0:
            return
        
        if 1 <= choix <= len(evenements):
            evt = evenements[choix - 1]
            confirm = input(f"Supprimer '{evt['titre']}' ? (oui/non): ")
            
            if confirm.lower() == "oui":
                evenements.pop(choix - 1)
                print("Événement supprimé")
        else:
            print("Numéro invalide")
    except:
        print("Erreur de saisie")


def ajouter_participant():
    """Ajouter un participant à un événement"""
    print("\n=== AJOUTER UN PARTICIPANT ===")
    
    if not evenements:
        print("Aucun événement")
        return
    
    for i, evt in enumerate(evenements, 1):
        print(f"{i}. {evt['titre']} - {evt['date']}")
    
    try:
        choix = int(input("\nNuméro événement: "))
        if not (1 <= choix <= len(evenements)):
            print("Numéro invalide")
            return
        
        evt = evenements[choix - 1]
        
        print(f"Participants: {', '.join(PARTICIPANTS)}")
        participant = input("Nom: ")
        
        if participant not in PARTICIPANTS:
            print("Ce participant n'existe pas")
            return
        
        if participant in evt['participants']:
            print("Déjà inscrit")
            return
        
        # Vérifier les conflits d'horaire
        for e in evenements:
            if participant in e['participants'] and e['date'] == evt['date']:
                d1 = datetime.strptime(e['heure_debut'], "%H:%M")
                f1 = datetime.strptime(e['heure_fin'], "%H:%M")
                d2 = datetime.strptime(evt['heure_debut'], "%H:%M")
                f2 = datetime.strptime(evt['heure_fin'], "%H:%M")
                
                if not (f1 <= d2 or f2 <= d1):
                    print(f"Conflit: {participant} a déjà '{e['titre']}' à cet horaire")
                    return
        
        # Vérifier la capacité de la salle
        if evt['salle']:
            if len(evt['participants']) + 1 > SALLES[evt['salle']]:
                print(f"Erreur: capacité max de {SALLES[evt['salle']]} atteinte")
                return
        
        evt['participants'].append(participant)
        print(f"{participant} ajouté à l'événement")
    except:
        print("Erreur de saisie")


def retirer_participant():
    """Retirer un participant d'un événement"""
    print("\n=== RETIRER UN PARTICIPANT ===")
    
    if not evenements:
        print("Aucun événement")
        return
    
    for i, evt in enumerate(evenements, 1):
        print(f"{i}. {evt['titre']} ({len(evt['participants'])} participants)")
    
    try:
        choix = int(input("\nNuméro événement: "))
        if not (1 <= choix <= len(evenements)):
            print("Numéro invalide")
            return
        
        evt = evenements[choix - 1]
        
        if not evt['participants']:
            print("Aucun participant inscrit")
            return
        
        print(f"Participants: {', '.join(evt['participants'])}")
        participant = input("Nom à retirer: ")
        
        if participant not in evt['participants']:
            print("Ce participant n'est pas inscrit")
            return
        
        evt['participants'].remove(participant)
        print(f"{participant} retiré")
    except:
        print("Erreur de saisie")


def afficher_agenda():
    """Afficher l'agenda d'un participant"""
    print("\n=== AGENDA D'UN PARTICIPANT ===")
    
    print(f"Participants: {', '.join(PARTICIPANTS)}")
    participant = input("Nom: ")
    
    if participant not in PARTICIPANTS:
        print("Ce participant n'existe pas")
        return
    
    evt_participant = [e for e in evenements if participant in e['participants']]
    
    if not evt_participant:
        print(f"{participant} n'a aucun événement")
        return
    
    evt_participant.sort(key=lambda e: (e['date'], e['heure_debut']))
    
    print(f"\n=== AGENDA DE {participant.upper()} ===")
    for evt in evt_participant:
        salle = f" - {evt['salle']}" if evt['salle'] else ""
        print(f"• {evt['titre']}")
        print(f"  {evt['date']} | {evt['heure_debut']}-{evt['heure_fin']}{salle}")


def verifier_conflit_participant(participant, date, h_debut, h_fin):
    """Vérifie si un participant a un conflit"""
    for evt in evenements:
        if participant in evt['participants'] and evt['date'] == date:
            d1 = datetime.strptime(evt['heure_debut'], "%H:%M")
            f1 = datetime.strptime(evt['heure_fin'], "%H:%M")
            d2 = datetime.strptime(h_debut, "%H:%M")
            f2 = datetime.strptime(h_fin, "%H:%M")
            
            if not (f1 <= d2 or f2 <= d1):
                return False
    return True


def verifier_conflit_salle(date, h_debut, h_fin, salle):
    """Vérifie si une salle est disponible"""
    for evt in evenements:
        if evt['salle'] == salle and evt['date'] == date:
            d1 = datetime.strptime(evt['heure_debut'], "%H:%M")
            f1 = datetime.strptime(evt['heure_fin'], "%H:%M")
            d2 = datetime.strptime(h_debut, "%H:%M")
            f2 = datetime.strptime(h_fin, "%H:%M")
            
            if not (f1 <= d2 or f2 <= d1):
                return False
    return True


def verifier_occupation_max_salle(salle, nb_participants):
    """Vérifie la capacité de la salle"""
    if salle not in SALLES:
        return True
    return nb_participants <= SALLES[salle]


def trouver_creneau_commun():
    """Trouve un créneau disponible pour plusieurs participants"""
    print("\n=== TROUVER UN CRÉNEAU COMMUN ===")
    
    date = input("Date (AAAA-MM-JJ): ")
    if not valider_date(date):
        print("Format de date invalide")
        return
    
    print(f"Participants: {', '.join(PARTICIPANTS)}")
    participants_str = input("Liste (séparés par virgules): ")
    
    participants_list = [p.strip() for p in participants_str.split(",")]
    
    for p in participants_list:
        if p not in PARTICIPANTS:
            print(f"'{p}' n'existe pas")
            return
    
    print(f"\nRecherche pour: {', '.join(participants_list)}")
    
    # Trouver les créneaux occupés
    occupes = []
    for evt in evenements:
        if evt['date'] == date:
            if any(p in evt['participants'] for p in participants_list):
                occupes.append({
                    'debut': evt['heure_debut'],
                    'fin': evt['heure_fin']
                })
    
    occupes.sort(key=lambda c: c['debut'])
    
    # Calculer les créneaux libres
    libres = []
    heure_actuelle = "09:00"
    
    for creneau in occupes:
        if heure_actuelle < creneau['debut']:
            libres.append({'debut': heure_actuelle, 'fin': creneau['debut']})
        if creneau['fin'] > heure_actuelle:
            heure_actuelle = creneau['fin']
    
    if heure_actuelle < "18:00":
        libres.append({'debut': heure_actuelle, 'fin': "18:00"})
    
    if libres:
        print("\nCréneaux disponibles:")
        for i, c in enumerate(libres, 1):
            print(f"  {i}. {c['debut']} - {c['fin']}")
    else:
        print("Aucun créneau disponible")


def menu():
    """Menu principal"""
    while True:
        print("\n" + "="*50)
        print("GESTIONNAIRE DE PLANNING")
        print("="*50)
        print("1. Créer un événement")
        print("2. Afficher l'agenda d'un participant")
        print("3. Ajouter un participant")
        print("4. Supprimer un événement")
        print("5. Trouver un créneau commun")
        print("6. Retirer un participant")
        print("7. Afficher tous les événements")
        print("0. Quitter")
        print("="*50)
        
        choix = input("Choix: ")
        
        if choix == "1":
            ajouter_evenement()
        elif choix == "2":
            afficher_agenda()
        elif choix == "3":
            ajouter_participant()
        elif choix == "4":
            supprimer_evenement()
        elif choix == "5":
            trouver_creneau_commun()
        elif choix == "6":
            retirer_participant()
        elif choix == "7":
            afficher_evenements_par_date()
        elif choix == "0":
            print("\nAu revoir!")
            break
        else:
            print("Choix invalide")


if __name__ == "__main__":
    print("\nBienvenue dans le gestionnaire de planning!")
    print(f"Participants: {', '.join(PARTICIPANTS)}")
    print(f"Salles: {', '.join(SALLES.keys())}")
    input("\nAppuyez sur Entrée pour continuer...")
    menu()