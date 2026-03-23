# Denis

**Apprendre n'importe quoi, progressivement.**

Denis est une plateforme d'apprentissage interactif basée sur des mini-jeux pédagogiques où un robot se déplace sur une grille à chaque bonne réponse. Chaque domaine a ses propres jeux, outils cliniques, et bibliothèques.

---

## Structure des fichiers

```
index.html                        ← page d'accueil principale
sciences.html                     ← hub sciences (animation + physique/chimie/maths)
bibliotheque.html                 ← ma bibliothèque perso (créer, entraîner, paramètres)
bibliotheques_expertisees.html    ← bibliothèques testées par des experts

denis_physique.html               ← jeu physique
denis_maths.html                  ← jeu mathématiques
denis_chimie_generale.html        ← jeu chimie générale (18 chapitres)
denis_chimie_organique.html       ← jeu chimie organique
denis_biochimie.html              ← jeu biochimie
denis_espagnol.html               ← jeu espagnol
denis_cbip.html                   ← médecine · CBIP pharmacologie
denis_neurochirurgie.html         ← neurochirurgie · cas cliniques
pico_medical.html                 ← outil PICO · aide au traitement EBM
diagnostic_medical.html           ← aide au diagnostic différentiel
quantum_robot.html                ← quantum computing · Qiskit
sources.html                      ← sources et références
```

---

## Nouvelles fonctionnalités (v0.3)

### 🔬 Sciences
Hub dédié avec animation orbitale animée. Choix direct entre physique, chimie et maths. Accès aussi à biochimie, chimie organique, et quantum.

### 📚 Ma bibliothèque perso
- **Profil étudiant ou professionnel**
- **Ajout de contenu** : colle tes cours, notes, résumés
- **URL & QR code** : ajoute des ressources en ligne (DynaMed, UpToDate, Cochrane, PubMed, sites avec abonnement…)
- **Clé API** : configure ton accès Claude pour générer des questions
- **Paramètres de l'assistant** :
  - Vitesse de progression (lent → rapide)
  - Questions supplémentaires sur les notions difficiles
  - Mode examen (sans indice)
  - Types de questions : QCM · vrai/faux · questions ouvertes · cas pratiques
  - Feedback et explications après chaque question

### ⭐ Bibliothèques expertisées
Bibliothèques construites et validées par des experts avec protocole documenté :
- **PICO · aide au traitement** (médecins, pharmaciens)
- **Aide au diagnostic** (internistes, urgentistes)
- **CBIP pharmacologie** (pharmaciens, prescripteurs)
- **Neurochirurgie** (neurochirurgiens, résidents)

Chaque fiche affiche : testeurs · méthode · critères · résultat · avis.

---

## Déploiement GitHub Pages

1. Mets tous les fichiers `.html` dans un repo GitHub
2. Active GitHub Pages (`Settings → Pages → main branch / root`)
3. Ton URL sera : `https://[username].github.io/[repo]/`

Aucune dépendance, aucun serveur — tout fonctionne en HTML statique.  
La clé API est stockée uniquement dans le `localStorage` du navigateur de l'utilisateur.

---

## Contribuer une bibliothèque expertisée

Vous êtes expert dans un domaine ? Voir la page `bibliotheques_expertisees.html` pour le protocole de contribution.

---

*Denis · v0.3 · 2025*
