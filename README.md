# Denis — Assistant IA Personnel

Application web statique multi-modules basée sur l'API Claude (Anthropic). Aucun backend requis — tout fonctionne côté client.

## Structure du projet

```
index.html                        ← Point d'entrée principal
sources.html                      ← Gestion des sources EBM (bibliothèque)
│
├── Sciences
│   ├── denis_maths.html          ← Tutor mathématiques
│   ├── denis_physique.html       ← Tutor physique
│   ├── denis_chimie_generale.html← Tutor chimie générale
│   ├── denis_chimie_organique.html← Tutor chimie organique
│   └── denis_biochimie.html      ← Tutor biochimie
│
├── Médecine
│   ├── denis_neurochirurgie.html ← Tutor neurochirurgie
│   ├── denis_cbip.html           ← CBIP / pharmacologie
│   ├── pico_medical.html         ← Aide à la décision EBM (PICO)
│   └── diagnostic_medical.html   ← Aide au diagnostic différentiel
│
├── Langues
│   ├── denis_francais.html       ← Tutor français
│   └── denis_espagnol.html       ← Tutor español
│
└── Informatique / Robots
    ├── python_learn.html          ← Robot Python interactif
    ├── crypto_robot_web.html      ← Robot crypto / trading
    ├── quantum_robot_avec_correctifs_.html ← Robot quantique (Qiskit)
    └── quantum_robot_qsharp.html  ← Robot quantique (Q#)
```

## Déploiement

### GitHub Pages (recommandé)
1. Crée un repository GitHub (ex: `denis`)
2. Upload tous les fichiers `.html` et ce `README.md`
3. Dans **Settings → Pages**, sélectionne la branche `main` et le dossier `/root`
4. L'app sera disponible sur `https://<ton-pseudo>.github.io/denis/`

### Local
Ouvre simplement `index.html` dans un navigateur. Aucun serveur nécessaire.

## Configuration de l'API

Chaque page demande une clé API Anthropic au premier lancement. La clé est stockée localement dans le navigateur (`localStorage`) — elle n'est jamais envoyée ailleurs qu'à `api.anthropic.com`.

Pour obtenir une clé : [console.anthropic.com](https://console.anthropic.com)

## Technologies

- HTML / CSS / JS vanilla — aucun framework, aucune dépendance npm
- API Anthropic Claude (modèle `claude-sonnet-4-20250514`)
- Web Search tool (pour PICO et diagnostic)
- `localStorage` pour persistance des préférences et clé API

## Notes

- Les modules médicaux (PICO, diagnostic, CBIP) sont des outils d'aide à la décision — ils ne remplacent pas un avis médical.
- Les robots quantiques nécessitent une connexion internet pour appeler l'API Claude.
