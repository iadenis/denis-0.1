import os, sys

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("pip install colorama"); sys.exit()

# ── palette ──────────────────────────────────────────────────
GR  = Fore.GREEN  + Style.BRIGHT   # sage
RD  = Fore.RED    + Style.BRIGHT   # blush
YL  = Fore.YELLOW + Style.BRIGHT   # sand
CY  = Fore.CYAN   + Style.BRIGHT   # sky
W   = Fore.WHITE  + Style.BRIGHT   # ink
DIM = Style.DIM
RST = Style.RESET_ALL
OK  = Back.GREEN  + Fore.BLACK + Style.BRIGHT
NO  = Back.RED    + Fore.WHITE + Style.BRIGHT
HL  = Back.YELLOW + Fore.BLACK + Style.BRIGHT

# ── robot ─────────────────────────────────────────────────────
ROBOT_OK = f"""
  {GR}  ╔═══╗
  {GR}  ║ ◉◉║
  {GR}  ║ ▀ ║
  {GR}  ╚═╤═╝
  {GR}  ╱   ╲{RST}"""

ROBOT_NO = f"""
  {RD}  ╔═══╗
  {RD}  ║ ×× ║
  {RD}  ║    ║
  {RD}  ╚═╤═╝
  {RD}  ╱   ╲{RST}"""

ROBOT_IDLE = f"""
  {CY}  ╔═══╗
  {CY}  ║ ·· ║
  {CY}  ║ ── ║
  {CY}  ╚═╤═╝
  {CY}  ╱   ╲{RST}"""

ROBOT_WIN = f"""
  {YL}  ╔═══╗
  {YL}  ║ ★★ ║
  {YL}  ║ ◡  ║
  {YL}  ╚═╤═╝
  {YL}  ╱   ╲{RST}"""

# ── questions ─────────────────────────────────────────────────
QUESTIONS = [
    {
        "concept": 1,
        "concept_code": [
            "// trois types d'affirmations",
            "type Opinion        = préférence personnelle",
            "type Croyance       = non vérifiée rigoureusement",
            "type Science        = testée · mesurée · reproductible",
        ],
        "q": '"Le chocolat est meilleur que la vanille." C\'est quoi ?',
        "ch": ["a) une opinion", "b) une croyance", "c) une connaissance scientifique"],
        "ok": "a",
        "fb_ok": "// correct — les préférences de goût ne se mesurent pas.",
        "fb_no": "// c'est une opinion. personne n'a tort ici.",
        "hint": "peut-on mesurer si c'est vrai pour tout le monde ?",
        "mv": (1, 0)
    },
    {
        "concept": 1,
        "concept_code": [
            "// reconnaitre une croyance",
            "ex = 'Mon voisin a pris ce médicament et est guéri.'",
            "problème = un seul cas ≠ une preuve",
            "solution = tester sur beaucoup de personnes",
            "          + groupe de comparaison",
        ],
        "q": '"Je suis sûr que les vaccins rendent malade, mon voisin me l\'a dit." C\'est quoi ?',
        "ch": ["a) une opinion", "b) une croyance non vérifiée", "c) une connaissance scientifique"],
        "ok": "b",
        "fb_ok": "// correct — un témoignage isolé n'est pas une preuve.",
        "fb_no": "// c'est une croyance. le témoignage d'un voisin ≠ des études sur des milliers de personnes.",
        "hint": "est-ce que le voisin représente tout le monde ?",
        "mv": (1, 0)
    },
    {
        "concept": 1,
        "concept_code": [
            "// qu'est-ce qui rend une affirmation scientifique ?",
            "if (testée AND mesurée AND reproductible) {",
            "    → connaissance scientifique",
            "}",
            "// le sucre ne rend PAS les enfants hyperactifs",
            "// c'est un mythe — 15 études indépendantes le confirment",
        ],
        "q": "Laquelle est la plus scientifique ?",
        "ch": [
            'a) "Mon médecin dit que ça marche."',
            'b) "Tout le monde sait que le sucre rend fou."',
            'c) "15 études indépendantes → aucun lien sucre/hyperactivité."'
        ],
        "ok": "c",
        "fb_ok": "// correct — plusieurs études, indépendantes, avec résultat mesuré.",
        "fb_no": "// la c) est juste. elle cite des études multiples avec des chiffres précis.",
        "hint": "cherche la réponse avec des chiffres et plusieurs études.",
        "mv": (0, -1)
    },
    {
        "concept": 2,
        "concept_code": [
            "// pourquoi une expérience seule ne suffit pas",
            "ex = 'J\\'ai pris du sirop. 7 jours après : guéri.'",
            "mais un rhume dure naturellement 5-10 jours",
            "sans groupe de comparaison → impossible de conclure",
            "// notre cerveau cherche des causes même sans preuves",
        ],
        "q": "Tu prends du sirop. Tu guéris en 7 jours. Quelle conclusion est correcte ?",
        "ch": [
            "a) le sirop a guéri mon rhume.",
            "b) peut-être — un rhume guérit souvent seul en 7 jours.",
            "c) le sirop ne sert à rien."
        ],
        "ok": "b",
        "fb_ok": "// correct — guérir après ≠ guérir grâce à.",
        "fb_no": "// la b) est juste. sans comparaison, impossible de conclure.",
        "hint": "combien de temps dure un rhume sans traitement ?",
        "mv": (1, 0)
    },
    {
        "concept": 2,
        "concept_code": [
            "// corrélation ≠ causalité",
            "ex = 'ventes de glaces ↑  ET  noyades ↑'",
            "   → les glaces causent des noyades ?",
            "non — les deux augmentent en été (cause commune)",
            "// deux choses qui varient ensemble",
            "// ne sont pas forcément liées par une cause",
        ],
        "q": "Les enfants avec plus de livres réussissent mieux. Quelle conclusion est prudente ?",
        "ch": [
            "a) les livres rendent les enfants plus intelligents.",
            "b) il y a un lien, mais le niveau des parents explique probablement les deux.",
            "c) c'est prouvé : les livres causent la réussite."
        ],
        "ok": "b",
        "fb_ok": "// correct — corrélation ≠ causalité.",
        "fb_no": "// la b) est juste. le niveau des parents est probablement la cause commune.",
        "hint": "quelles autres différences y a-t-il entre ces familles ?",
        "mv": (0, -1)
    },
    {
        "concept": 2,
        "concept_code": [
            "// l'effet placebo",
            "ex = '30-40% des patients prennent du sucre'",
            "   '→ ressentent quand même une amélioration réelle'",
            "solution = essai en double aveugle",
            "  // ni patient, ni médecin ne sait qui reçoit quoi",
            "  // élimine les biais des deux côtés",
        ],
        "q": "Pourquoi personne ne sait qui prend le vrai médicament dans une étude sérieuse ?",
        "ch": [
            "a) pour que les médecins ne trichent pas.",
            "b) pour éliminer l'effet placebo et les biais d'évaluation.",
            "c) c'est une règle administrative."
        ],
        "ok": "b",
        "fb_ok": "// correct — le double aveugle élimine les biais des deux côtés.",
        "fb_no": "// la b) est juste. sans ça, le médecin évalue inconsciemment différemment.",
        "hint": "que se passe-t-il dans la tête du médecin s'il sait qui prend quoi ?",
        "mv": (1, 0)
    },
    {
        "concept": 3,
        "concept_code": [
            "// la question magique",
            "function evaluer(information) {",
            "    return 'comment on le sait ?'",
            "    // pas : 'qui l\\'a dit ?'",
            "    // pas : 'est-ce que ça semble logique ?'",
            "    // pas : 'beaucoup de gens le croient ?'",
            "}",
        ],
        "q": '"Le wifi cause le cancer." Quelle est la meilleure réaction ?',
        "ch": [
            "a) éteindre le wifi.",
            "b) lui dire qu'il a tort.",
            'c) demander : "c\'est quelle étude ? sur combien de personnes ?"'
        ],
        "ok": "c",
        "fb_ok": "// correct — demander la source, toujours. (aucun lien wifi/cancer trouvé à ce jour)",
        "fb_no": '// la c) est juste. la question magique : "comment on le sait ?"',
        "hint": "qu'est-ce qui distingue une rumeur d'une preuve ?",
        "mv": (0, -1)
    },
    {
        "concept": 3,
        "concept_code": [
            "// hiérarchie des preuves",
            "const preuves = [",
            '    "témoignage isolé",      // peu fiable',
            '    "avis d\\'un expert",     // mieux',
            '    "une étude",             // début de preuve',
            '    "plusieurs études",      // plus solide',
            '    "méta-analyse",          // très solide',
            '    "consensus mondial",     // le plus fiable',
            "]",
        ],
        "q": "Un médecin célèbre contredit 10 000 études. Que penser ?",
        "ch": [
            "a) le médecin célèbre a forcément raison.",
            "b) les 10 000 études sont toutes fausses.",
            "c) un expert isolé pèse moins que des milliers d'études indépendantes."
        ],
        "ok": "c",
        "fb_ok": "// correct — la notoriété ne remplace pas les preuves.",
        "fb_no": "// la c) est juste. nombre + indépendance des études > avis d'un seul expert.",
        "hint": "qu'est-ce qui est plus difficile à falsifier ?",
        "mv": (1, 0)
    },
    {
        "concept": 3,
        "concept_code": [
            "// la science se corrige elle-même",
            "ex = 'Pendant des siècles : la Terre est au centre.'",
            "   = 'En 1984 : ulcères → bactérie H. pylori. Nobel 2005.'",
            "croyance  → résiste aux preuves contraires",
            "science   → intègre les nouvelles preuves et évolue",
            "// changer d'avis = signe de santé, pas de faiblesse",
        ],
        "q": "La science change parfois d'avis. Est-ce un problème ?",
        "ch": [
            "a) oui — si elle change d'avis, elle ne sait rien.",
            "b) non — changer d'avis face aux preuves, c'est ça la science.",
            "c) oui — mieux vaut s'en tenir aux traditions."
        ],
        "ok": "b",
        "fb_ok": "// correct — se corriger est la plus grande force de la science.",
        "fb_no": "// la b) est juste. une idéologie qui ne change jamais n'apprend jamais.",
        "hint": "qu'est-ce qu'on préfère : quelqu'un qui admet ses erreurs ou pas ?",
        "mv": (0, -1)
    },
]

# ── grille ────────────────────────────────────────────────────
TAILLE = 6

def afficher_grille(robot, but, traces):
    sep = DIM + "  +" + ("────+" * TAILLE) + RST
    print()
    print(sep)
    for y in range(TAILLE):
        ligne = DIM + "  |" + RST
        for x in range(TAILLE):
            p = (x, y)
            if p == robot:
                case = CY + " R  " + RST + DIM + "|" + RST
            elif p == but:
                case = GR + " G  " + RST + DIM + "|" + RST
            elif p in traces:
                case = DIM + " ·  |" + RST
            else:
                case = DIM + "    |" + RST
            ligne += case
        print(ligne)
        print(sep)
    print()
    print(f"  {CY}R{RST} = robot   {GR}G{RST} = goal   {DIM}·{RST} = chemin")
    print()

def dep(robot, delta):
    return (
        max(0, min(TAILLE-1, robot[0] + delta[0])),
        max(0, min(TAILLE-1, robot[1] + delta[1]))
    )

# ── affichage code ────────────────────────────────────────────
def afficher_code(lignes):
    print()
    print(DIM + "  ┌" + "─" * 46 + "┐" + RST)
    for l in lignes:
        if l.startswith("//"):
            print(DIM + f"  │  {l:<44}│" + RST)
        elif "=" in l and not l.startswith("if") and not l.startswith("const") and not l.startswith("function"):
            parts = l.split("=", 1)
            print(f"  {DIM}│{RST}  {CY}{parts[0]}{RST}={W}{parts[1]:<{43-len(parts[0])}}{DIM}│{RST}")
        elif l.startswith("    //"):
            print(DIM + f"  │      {l.strip():<40}│" + RST)
        elif l.startswith("    "):
            print(f"  {DIM}│{RST}    {YL}{l.strip():<42}{DIM}│{RST}")
        else:
            print(f"  {DIM}│{RST}  {W}{l:<44}{DIM}│{RST}")
    print(DIM + "  └" + "─" * 46 + "┘" + RST)
    print()

# ── dots de progression ───────────────────────────────────────
def afficher_dots(cur, total):
    dots = ""
    for i in range(total):
        if i < cur:
            dots += GR + "● " + RST
        elif i == cur:
            dots += W + "● " + RST
        else:
            dots += DIM + "○ " + RST
    print(f"  {dots}")
    print()

# ── main ──────────────────────────────────────────────────────
def jouer():
    robot = (0, 5)
    but   = (5, 0)
    traces = set()
    score = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    # écran titre
    print()
    print(ROBOT_IDLE)
    print()
    print(f"  {W}denis{RST} {DIM}·{RST} {CY}module_0{RST} {DIM}·{RST} {YL}niveau_1{RST}")
    print(f"  {DIM}qu'est-ce qu'on sait vraiment ?{RST}")
    print()
    input(f"  {DIM}→ entrée pour commencer{RST}")

    for i, q in enumerate(QUESTIONS):
        os.system('cls' if os.name == 'nt' else 'clear')

        # header
        print()
        print(f"  {DIM}concept_{q['concept']}/3{RST}   ", end="")
        afficher_dots(i, len(QUESTIONS))

        # code
        afficher_code(q["concept_code"])

        # grille
        afficher_grille(robot, but, traces)

        # question
        print(f"  {W}{q['q']}{RST}")
        print()
        for c in q["ch"]:
            print(f"  {DIM}{c}{RST}")
        print()
        print(f"  {DIM}(tape a, b ou c — ou 'indice'){RST}")

        # réponse
        while True:
            rep = input(f"  {CY}→ {RST}").strip().lower()
            if rep == "indice":
                print(f"\n  {YL}// {q['hint']}{RST}\n")
                continue
            if rep in ["a", "b", "c"]:
                break
            print(f"  {DIM}tape a, b ou c{RST}")

        # feedback
        ok = rep == q["ok"]
        print()
        if ok:
            print(f"  {OK}  ✓ correct  {RST}")
            print(f"  {GR}{q['fb_ok']}{RST}")
            score += 10
            print(ROBOT_OK)
        else:
            print(f"  {NO}  ✗  {RST}")
            print(f"  {RD}{q['fb_no']}{RST}")
            print(ROBOT_NO)

        # déplacement
        traces.add(robot)
        robot = dep(robot, q["mv"])
        dir_nom = {(1,0):"droite",(-1,0):"gauche",(0,-1):"haut",(0,1):"bas"}[q["mv"]]
        print()
        print(f"  {DIM}→ robot : {dir_nom}   score : {score}/{len(QUESTIONS)*10}{RST}")
        print()
        input(f"  {DIM}entrée pour continuer{RST}")

    # fin
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(ROBOT_WIN)
    print()
    print(f"  {W}denis{RST} {DIM}·{RST} {YL}// niveau_1 complété{RST}")
    print()
    print(f"  {DIM}take_home_messages[] = [{RST}")
    msgs = [
        "opinion ≠ croyance ≠ connaissance scientifique",
        "une expérience personnelle ne prouve rien seule",
        "corrélation ≠ causalité",
        "'comment on le sait ?' — toujours la bonne question",
        "la science change d'avis. c'est sa force.",
    ]
    for m in msgs:
        print(f"  {GR}  → {RST}{DIM}{m}{RST}")
    print(f"  {DIM}]{RST}")
    print()
    print(f"  {YL}score final : {score}/{len(QUESTIONS)*10}{RST}")
    print()
    rep = input(f"  {DIM}recommencer ? (o/n) → {RST}").strip().lower()
    if rep == "o":
        jouer()

if __name__ == "__main__":
    jouer()
