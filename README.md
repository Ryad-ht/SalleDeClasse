# Gestionnaire de Planning Partagé

**Projet final - Master Data & AI**

---

## 👥 Membres du groupe

- **[Nom Prénom 1]** - [Email]
- **[Nom Prénom 2]** - [Email]
- **[Nom Prénom 3]** - [Email]
- **[Nom Prénom 4]** - [Email] *(optionnel)*

---

## 📋 Description du projet

Application console en Python permettant à une équipe de créer, gérer et optimiser un emploi du temps collectif.

### Fonctionnalités implémentées

✅ **Gestion des événements**
- Créer un événement (titre, date, horaires, salle optionnelle)
- Afficher tous les événements triés par date
- Supprimer un événement

✅ **Gestion des participants**
- Ajouter un participant à un événement
- Retirer un participant d'un événement
- Afficher l'agenda personnel d'un participant

✅ **Détection de conflits**
- Vérification automatique des conflits d'horaire pour les participants
- Vérification de la disponibilité des salles

✅ **Recherche de créneau commun**
- Trouver des plages horaires disponibles pour plusieurs participants
- Recherche entre 9h et 18h

✅ **Gestion des salles**
- Vérification de la capacité maximale
- Détection des doubles réservations

---

## 🚀 Installation et exécution

### Prérequis

- Python 3.7 ou supérieur
- Aucune bibliothèque externe requise (utilise uniquement les modules standards)

### Lancement du programme

```bash
# Cloner ou extraire le projet
cd projet_planning

# Lancer le programme
python3 planning.py
```

Ou sur Windows :
```bash
python planning.py
```

---

## 📖 Guide d'utilisation

### Menu principal

Au lancement, vous verrez le menu suivant :

```
📅 GESTIONNAIRE DE PLANNING PARTAGÉ
============================================================
1. Créer un nouvel événement
2. Afficher l'agenda d'un participant
3. Ajouter un participant à un événement
4. Supprimer un événement
5. Trouver un créneau commun
6. Retirer un participant d'un événement
7. Afficher tous les événements
0. Quitter
```

### Participants et salles

**Participants hardcodés** : Alice, Bob, Charlie, Diana, Eve

**Salles disponibles** :
- Salle A (capacité: 10 personnes)
- Salle B (capacité: 20 personnes)
- Salle C (capacité: 5 personnes)
- Salle D (capacité: 15 personnes)

### Formats requis

- **Date** : AAAA-MM-JJ (exemple: 2024-12-15)
- **Heure** : HH:mm (exemple: 14:30)
- **Plage horaire** : Les événements doivent être entre 09:00 et 18:00

### Exemples d'utilisation

#### Créer un événement
1. Choisir l'option 1
2. Entrer le titre : `Réunion projet`
3. Entrer la date : `2024-12-20`
4. Entrer l'heure de début : `14:00`
5. Entrer l'heure de fin : `15:30`
6. Choisir une salle (optionnel) : `Salle A`

#### Ajouter un participant
1. Choisir l'option 3
2. Sélectionner l'événement dans la liste
3. Entrer le nom du participant : `Alice`
4. Le système vérifie automatiquement :
   - Conflits d'horaire avec d'autres événements
   - Capacité maximale de la salle

#### Trouver un créneau commun
1. Choisir l'option 5
2. Entrer la date : `2024-12-20`
3. Entrer les participants séparés par des virgules : `Alice, Bob, Charlie`
4. Le système affiche tous les créneaux disponibles entre 9h et 18h

---

## 📁 Structure du projet

```
projet_planning/
├── planning.py              # Script principal (tout-en-un)
├── README.md               # Ce fichier
└── diagramme_flux.png     # Diagramme de flux du programme
```

---

## ⚙️ Détails techniques

### Fonctions principales implémentées

**Gestion des événements :**
- `ajouter_evenement()` - Création d'événements
- `afficher_evenements_par_date()` - Affichage trié
- `supprimer_evenement()` - Suppression avec confirmation

**Gestion des participants :**
- `ajouter_participant()` - Inscription avec vérifications
- `retirer_participant()` - Désinscription
- `afficher_agenda()` - Agenda personnel

**Détection de conflits :**
- `verifier_conflit_participant()` - Détection de chevauchements
- `verifier_conflit_salle()` - Vérification disponibilité salle
- `verifier_occupation_max_salle()` - Contrôle capacité

**Recherche de créneaux :**
- `trouver_creneau_commun()` - Algorithme de recherche de plages libres

### Validations implémentées

✅ Format de date (AAAA-MM-JJ)  
✅ Format d'heure (HH:mm)  
✅ Plage horaire 9h-18h  
✅ Heure début < heure fin  
✅ Conflits d'horaire participants  
✅ Conflits de réservation salles  
✅ Capacité maximale salles  
✅ Existence participants et salles  

---

## 🎨 Fonctionnalités bonus implémentées

- ✅ Validation complète des inputs utilisateurs
- ✅ Messages d'erreur détaillés et explicites
- ✅ Interface console claire avec séparateurs visuels
- ✅ Affichage des détails de conflits
- ✅ Confirmation avant suppression
- ✅ Code commenté et documenté
- ✅ Gestion robuste des erreurs

---

## 📊 Diagramme de flux

Le diagramme de flux complet du programme est disponible dans le fichier `diagramme_flux.png`.

Il représente :
- Le menu principal
- Les 6 fonctionnalités principales
- Les flux de validation
- Les détections de conflits
- Les retours au menu

---

## 🐛 Limitations connues

- Les données ne sont pas persistantes (perdues à la fermeture)
- Pas d'interface graphique
- Liste de participants fixe (hardcodée)

### Améliorations possibles

- Sauvegarde des données dans un fichier JSON
- CRUD complet sur les participants et salles
- Interface graphique (Tkinter, PyQt)
- Export des agendas en PDF
- Notifications par email

---

## 📝 Notes de développement

- **Langage** : Python 3
- **Modules utilisés** : `datetime`, `re` (bibliothèques standard uniquement)
- **Paradigme** : Programmation procédurale
- **Style de code** : PEP 8

---

## 📄 Licence

Projet réalisé dans le cadre du Master Data & AI - LiveCampus  
© 2024 - Tous droits réservés

---

## 📞 Contact

Pour toute question concernant ce projet, contactez les membres du groupe via leurs emails respectifs.
