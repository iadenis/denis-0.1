# Denis — Assistant IA Personnel

Application web statique multi-modules. Aucun backend requis — tout fonctionne côté client dans le navigateur.

## Structure du projet

```
index.html                          ← Point d'entrée principal
sources.html                        ← Bibliothèque EBM & préférences IA
│
├── Sciences
│   ├── denis_maths.html            ← Tutor mathématiques
│   ├── denis_physique.html         ← Tutor physique
│   ├── denis_chimie_generale.html  ← Tutor chimie générale (18 chapitres)
│   ├── denis_chimie_organique.html ← Tutor chimie organique
│   └── denis_biochimie.html        ← Tutor biochimie
│
├── Médecine
│   ├── denis_neurochirurgie.html   ← Tutor neurochirurgie (14 chapitres)
│   ├── denis_cbip.html             ← CBIP · pharmacologie (10 chapitres)
│   ├── pico_medical.html           ← Aide à la décision EBM (PICO)
│   └── diagnostic_medical.html     ← Aide au diagnostic différentiel
│
├── Langues
│   ├── denis_francais.html         ← Tutor français
│   └── denis_espagnol.html         ← Tutor español
│
└── Informatique / Robots
    ├── python_learn.html            ← Robot Python interactif
    ├── crypto_robot_web.html        ← Robot crypto / chiffrement
    ├── quantum_robot_qiskit.html    ← Robot quantique · Qiskit (redesigné)
    └── quantum_robot_qsharp.html    ← Robot quantique · Q# (redesigné)
```

## Déploiement sur GitHub Pages

1. Crée un repository GitHub (ex: `denis`)
2. Upload **tous les fichiers `.html`** et ce `README.md` à la racine
3. Dans **Settings → Pages**, sélectionne la branche `main` et le dossier `/ (root)`
4. L'app sera disponible sur `https://<ton-pseudo>.github.io/denis/`

> Pas de build, pas de npm, pas de configuration — un simple upload suffit.

## Fonctionnement hors ligne / sans API

Les modules de jeu (maths, physique, chimie, langues, neurochirurgie, CBIP, quantum, python, crypto) sont **entièrement statiques** — ils fonctionnent sans connexion et sans clé API.

Les outils médicaux (PICO et diagnostic) fonctionnent en deux modes automatiques :

| Mode | Condition | Comportement |
|------|-----------|--------------|
| **IA complète** | Clé API configurée (voir ci-dessous) | Analyse IA personnalisée via Claude |
| **Base locale** | Pas de clé / CORS GitHub Pages | Base EBM intégrée (HTA, IC, ITU, douleur thoracique, dyspnée…) |

Dans tous les cas, un bouton **"copier prompt → Claude"** permet d'envoyer la question à claude.ai.

## Configuration de la clé API (optionnel)

Pour activer l'IA complète dans PICO et le diagnostic, une clé API Anthropic est nécessaire.

**Obtenir une clé :** [console.anthropic.com](https://console.anthropic.com) — gratuit pour commencer.

**Configurer :** la clé se renseigne directement dans les fichiers `pico_medical.html` et `diagnostic_medical.html`, dans l'en-tête `Authorization` du `fetch`. Elle peut aussi être stockée dans le `localStorage` du navigateur sous la clé `denis_api_key`.

La clé n'est **jamais envoyée ailleurs qu'à `api.anthropic.com`** — aucun serveur intermédiaire.

> **Note GitHub Pages :** l'appel API direct depuis GitHub Pages est bloqué par CORS (restriction Anthropic). La base locale prend le relais automatiquement. Pour l'IA complète depuis GitHub Pages, utilisez le bouton "copier prompt → claude.ai".

## Technologies

- HTML / CSS / JS vanilla — aucun framework, aucune dépendance
- Police : [DM Mono + DM Sans](https://fonts.google.com/) (Google Fonts)
- API Anthropic Claude `claude-sonnet-4-6` (optionnel, pour PICO et diagnostic)
- `localStorage` pour persistance des préférences (sources EBM, mode IA)

## Modules en détail

### Robots interactifs (statiques)
Chaque robot suit la même mécanique : **concept → question → réponse → feedback + déplacement du robot sur une grille 6×6**.

- **Quantum Qiskit** — 5 modules : qubits, porte X, porte H, CNOT, circuits complets
- **Quantum Q#** — 5 modules : syntaxe, portes, types, boucles, algorithmes (avec panneau dual Qiskit↔Q#)
- **Python** — variables, conditions, boucles, fonctions
- **Crypto** — César, Vigenère, RSA, chiffrement moderne

### Tuteurs (statiques)
Questionnaires à choix multiples avec concepts intégrés, feedback immédiat, score.

### PICO · aide au traitement
Formulaire P-I-C-O → recommandations EBM hiérarchisées par grade (1A, 1B, 2A, 2B).
Base locale couvre : HTA, insuffisance cardiaque, FA, ITU, angine, pneumonie, douleur, dépression, diabète T2, asthme.

### Aide au diagnostic
Présentation clinique → différentiel structuré avec probabilités, arguments pour/contre, examens à réaliser (urgent / rapide / utile).
Base locale couvre : douleur thoracique, dyspnée, douleur abdominale, fièvre, céphalées.

## Notes

- Les modules médicaux sont des **outils d'aide à la décision** — ils ne remplacent pas un avis médical.
- Sources EBM intégrées : Cochrane, NICE, ESC/ACC, OMS, CBIP — version mars 2025.
