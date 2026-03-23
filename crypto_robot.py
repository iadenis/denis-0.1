import random, os, sys, string

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("pip install colorama"); sys.exit()

R=Fore.RED+Style.BRIGHT; G=Fore.GREEN+Style.BRIGHT; Y=Fore.YELLOW+Style.BRIGHT
B=Fore.BLUE+Style.BRIGHT; M=Fore.MAGENTA+Style.BRIGHT; C=Fore.CYAN+Style.BRIGHT
W=Fore.WHITE+Style.BRIGHT; DIM=Style.DIM; RST=Style.RESET_ALL
BGBL=Back.BLUE+Fore.WHITE+Style.BRIGHT; BGGR=Back.GREEN+Fore.BLACK+Style.BRIGHT
BGRD=Back.RED+Fore.WHITE+Style.BRIGHT; BGYL=Back.YELLOW+Fore.BLACK+Style.BRIGHT
BGMG=Back.MAGENTA+Fore.WHITE+Style.BRIGHT; BGCY=Back.CYAN+Fore.BLACK+Style.BRIGHT
BGWH=Back.WHITE+Fore.BLACK+Style.BRIGHT

def effacer(): os.system('cls' if os.name=='nt' else 'clear')
def pause(): input(f"\n  {DIM}Appuie sur Entrée pour continuer...{RST}")

def titre(t, col=M):
    print(); b="═"*(len(t)+4)
    print(col+f"  ╔{b}╗\n  ║  {W}{t}{col}  ║\n  ╚{b}╝{RST}"); print()

def encadre(txt, col=C):
    ls=txt.strip().split("\n"); w=max(len(l) for l in ls)+4
    print(col+"  ┌"+"─"*w+"┐")
    for l in ls: print(col+f"  │  {W}{l}{' '*(w-len(l)-2)}{col}  │")
    print(col+"  └"+"─"*w+"┘"+RST); print()

def afficher_regle(t): print(f"  {BGYL}  RÈGLE  {RST} {Y}{t}{RST}\n")
def succes(m="✓ Correct !"): print(f"\n  {BGGR} {m} {RST}\n")
def erreur(m="✗ Pas tout à fait..."): print(f"\n  {BGRD} {m} {RST}\n")
def indice(m): print(f"\n  {BGYL}  💡 INDICE  {RST} {Y}{m}{RST}\n")

def afficher_alphabet():
    print(f"\n  {C}Alphabet :{RST}")
    l1=l2="  "
    for i,c in enumerate(string.ascii_uppercase):
        l1+=f"{C}{c}{RST} "; l2+=f"{Y}{i:2}{RST}"
        if (i+1)%13==0: print(l1); print(l2); l1=l2="  "
    if l1.strip(): print(l1); print(l2)
    print()

def visualiser_decalage(lettre, dec, res):
    alph=string.ascii_uppercase; pd=alph.index(lettre.upper()); pa=alph.index(res.upper())
    print(f"\n  {C}Visualisation :{RST}")
    print(f"  {W}Départ : {Y}{lettre.upper()}{RST} (pos {Y}{pd}{RST}) + {G}{dec}{RST} = {M}{pd+dec}{RST} mod 26 = {M}{pa}{RST} → {Y}{res.upper()}{RST}\n")

def afficher_grille(robot, but, taille=6, traces=None):
    if traces is None: traces=set()
    sep=C+"  +"+"────+"*taille; print()
    print(sep)
    for y in range(taille):
        lg=C+"  |"
        for x in range(taille):
            p=(x,y)
            if p==robot: case=BGBL+" R  "+RST+C+"|"
            elif p==but: case=BGGR+" G  "+RST+C+"|"
            elif p in traces: case=BGYL+" ·  "+RST+C+"|"
            else: case="    |"
            lg+=case
        print(lg); print(sep)
    print()
    print(f"  {BGBL} R {RST}=Robot  {BGGR} G {RST}=Goal  {BGYL} · {RST}=Chemin")
    print(f"  Pos:{Y}({robot[0]},{robot[1]}){RST}  But:{G}({but[0]},{but[1]}){RST}\n")

def dep(robot, delta, t=6):
    return (max(0,min(t-1,robot[0]+delta[0])), max(0,min(t-1,robot[1]+delta[1])))

def dir_input(q="  → Direction : "):
    d={"droite":(1,0),"d":(1,0),"gauche":(-1,0),"g":(-1,0),"haut":(0,-1),"h":(0,-1),"bas":(0,1),"b":(0,1)}
    print(f"  {DIM}(droite/gauche/haut/bas  ou  d/g/h/b){RST}")
    while True:
        r=input(q).strip().lower()
        if r in d: return r,d[r]
        print(f"  {R}✗ Essaie : droite, haut, gauche, bas{RST}")

def ask(q): return input(f"  {Y}→ {q} {RST}").strip()
def ask_int(q, mi=None, ma=None):
    while True:
        try:
            v=int(input(f"  {Y}→ {q} {RST}").strip())
            if mi is not None and v<mi: print(f"  {R}Min:{mi}{RST}"); continue
            if ma is not None and v>ma: print(f"  {R}Max:{ma}{RST}"); continue
            return v
        except: print(f"  {R}Nombre entier requis{RST}")

def lettre_dir(l):
    l=l.upper()
    if l in "ABCDEF": return "droite",(1,0)
    if l in "GHIJKLM": return "haut",(0,-1)
    if l in "NOPQRST": return "gauche",(-1,0)
    return "bas",(0,1)

# ── Fonctions crypto ──────────────────────────────────────
def cesar(txt, d): return ''.join(chr((ord(c)-65+d)%26+65) if c.isalpha() else c for c in txt.upper())
def vigenere_c(txt, cle):
    r=""; j=0; cle=cle.upper()
    for c in txt.upper():
        if c.isalpha(): r+=chr((ord(c)-65+ord(cle[j%len(cle)])-65)%26+65); j+=1
        else: r+=c
    return r
def vigenere_d(txt, cle):
    r=""; j=0; cle=cle.upper()
    for c in txt.upper():
        if c.isalpha(): r+=chr((ord(c)-65-(ord(cle[j%len(cle)])-65))%26+65); j+=1
        else: r+=c
    return r
def pgcd(a,b):
    while b: a,b=b,a%b
    return a
def est_premier(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
def euclide_ext(a,b):
    if a==0: return b,0,1
    g,x,y=euclide_ext(b%a,a); return g,y-(b//a)*x,x
def inv_mod(e,phi):
    g,x,_=euclide_ext(e,phi); return x%phi if g==1 else None


# ════════════════════════════════════════════════════════
#  MODULE 1 — CÉSAR
# ════════════════════════════════════════════════════════
def module_cesar():
    titre("MODULE 1 — Le Chiffre de César", M)
    encadre(
        "Jules César décalait chaque lettre dans l'alphabet.\n"
        "Décalage de 3 : A→D, B→E, C→F... X→A, Y→B, Z→C\n"
        "\n"
        "Formule : chiffré = (position + décalage) mod 26\n"
        "\n"
        "Dans ce jeu, la lettre déchiffrée donne une direction :\n"
        "  A-F → droite    G-M → haut\n"
        "  N-T → gauche    U-Z → bas"
    )
    afficher_regle("A-F=droite  G-M=haut  N-T=gauche  U-Z=bas")
    pause(); score=0

    # Ex 1.1
    effacer(); titre("MODULE 1 — Ex 1/5 : Comprendre le décalage", C)
    robot=(0,3); but=(5,0); afficher_grille(robot,but)
    afficher_alphabet()
    encadre("Décalage=3. Message chiffré : D\nD est en position 3. 3-3=0 → A → droite")
    visualiser_decalage('D',-3,'A')
    rep,d=dir_input("→ A → direction : ")
    if d==(1,0): succes("✓ A→droite !"); score+=10
    else: erreur("A est dans A-F → droite !")
    robot=dep(robot,(1,0)); afficher_grille(robot,but); pause()

    # Ex 1.2
    effacer(); titre("MODULE 1 — Ex 2/5 : Déchiffre toi-même !", C)
    robot=(0,3); traces=set(); afficher_grille(robot,but,traces=traces)
    dec=4; chif="LMTV"; clair=cesar(chif,-dec)
    print(f"  {BGCY}  Chiffré : {chif}  Décalage : {dec}  {RST}\n")
    afficher_alphabet()
    encadre(f"Déchiffre : (position - {dec}) mod 26\nL(11)-4=7→H  M(12)-4=8→I  T(19)-4=15→P  V(21)-4=17→R")
    print(f"  {W}Message déchiffré : {G}{clair}{RST}\n")
    sc=0
    for i,c in enumerate(clair):
        nom,d=lettre_dir(c)
        print(f"\n  {M}Lettre {i+1} '{c}' → direction ?{RST}")
        rep,dr=dir_input()
        traces.add(robot)
        if dr==d: succes(f"✓ {c}→{nom}!"); sc+=1
        else: erreur(f"'{c}'→{nom}!")
        robot=dep(robot,d); afficher_grille(robot,but,traces=traces)
    score+=sc*5; pause()

    # Ex 1.3
    effacer(); titre("MODULE 1 — Ex 3/5 : Chiffre un message !", C)
    mot="BONJOUR"; dec=7; att=cesar(mot,dec)
    print(f"  {BGCY}  Mot : {mot}   Décalage : {dec}  {RST}\n")
    afficher_alphabet()
    encadre(f"(position + {dec}) mod 26\nB(1)+7=8→I  O(14)+7=21→V  Calcule les autres !")
    rep=ask(f"Résultat chiffré ({len(att)} lettres) : ").upper().replace(" ","")
    if rep==att: succes(f"✓ {mot}→{att}"); score+=15
    else: erreur(f"La réponse est {att}"); indice(f"Chaque lettre : (position+{dec}) mod 26")
    pause()

    # Ex 1.4 force brute
    effacer(); titre("MODULE 1 — Ex 4/5 : Attaque force brute !", C)
    secret="KHOOR"
    print(f"  {BGRD}  Intercepté : {secret}  {RST}\n")
    encadre("César n'a que 26 décalages possibles.\nOn peut tous les essayer : force brute !")
    for d in range(1,27):
        t=cesar(secret,-d)
        if d==3: print(f"  {G}  Décalage {d:2} → {t}  ← vrai mot !{RST}")
        else: print(f"  {DIM}  Décalage {d:2} → {t}{RST}")
    print()
    rep=ask("Quel décalage donne un vrai mot ? ")
    if rep.strip()=="3": succes(f"✓ Décalage 3 ! {secret}→{cesar(secret,-3)}"); score+=10
    else: erreur(f"C'est 3 ! {secret}→{cesar(secret,-3)}")
    pause()

    # Ex 1.5 mission
    effacer(); titre("MODULE 1 — Ex 5/5 : Mission secrète !", C)
    robot=(0,5); but=(5,0); traces=set()
    chif="HFGBV"; dec=6; clair=cesar(chif,-dec)
    afficher_grille(robot,but,traces=traces)
    print(f"  {BGRD}  Chiffré : {chif}  Décalage : {dec}  {RST}\n")
    encadre("Déchiffre et guide le robot !")
    sc=0
    for i,cc in enumerate(chif):
        cl=cesar(cc,-dec); nom,d=lettre_dir(cl)
        print(f"\n  {M}Lettre {i+1} '{cc}' → déchiffrée = ?{RST}")
        rep=ask("Lettre : ").upper()
        if rep and rep[0]==cl: succes(f"✓ {cc}→{cl}→{nom}!"); sc+=1
        else: erreur(f"'{cc}' décalage -{dec} = '{cl}' → {nom}")
        traces.add(robot); robot=dep(robot,d); afficher_grille(robot,but,traces=traces)
    if robot==but: print(f"\n  {BGGR}  🎯 But atteint !  {RST}\n")
    score+=sc*8
    print(f"\n  {BGMG}  Score module 1 : {score}  {RST}\n"); pause()
    return score


# ════════════════════════════════════════════════════════
#  MODULE 2 — VIGENÈRE
# ════════════════════════════════════════════════════════
def module_vigenere():
    titre("MODULE 2 — Le Chiffre de Vigenère", M)
    encadre(
        "Vigenère = César avec une CLÉ qui change le décalage.\n"
        "\n"
        "Clé 'CLE' (C=2, L=11, E=4) :\n"
        "  Message :  B  O  N  J  O  U  R\n"
        "  Clé     :  C  L  E  C  L  E  C\n"
        "  Décalage:  2  11  4  2  11  4  2\n"
        "\n"
        "La clé se RÉPÈTE. Chaque lettre a un décalage différent.\n"
        "Beaucoup plus difficile à casser que César !"
    )
    afficher_regle("A-F=droite  G-M=haut  N-T=gauche  U-Z=bas")
    pause(); score=0

    # Ex 2.1
    effacer(); titre("MODULE 2 — Ex 1/5 : La clé de Vigenère", C)
    afficher_alphabet()
    cle="SOL"; msg="CAT"; chif=vigenere_c(msg,cle)
    print(f"  {BGCY}  Message : {msg}   Clé : {cle}  {RST}\n")
    encadre(f"C(2)+S(18)=20→U  A(0)+O(14)=14→O  T(19)+L(11)=4→E\nRésultat : {chif}")
    rep=ask(f"'{msg}' chiffré avec '{cle}' = ").upper().replace(" ","")
    if rep==chif: succes(f"✓ {msg}→{chif}"); score+=10
    else: erreur(f"Réponse : {chif}")
    pause()

    # Ex 2.2
    effacer(); titre("MODULE 2 — Ex 2/5 : Déchiffre !", C)
    afficher_alphabet()
    cle="CHAT"; chif="JJEF"; clair=vigenere_d(chif,cle)
    print(f"  {BGRD}  Chiffré : {chif}   Clé : {cle}  {RST}\n")
    encadre(f"J(9)-C(2)=7→H  J(9)-H(7)=2→C  E(4)-A(0)=4→E  F(5)-T(19)=12→M\nRésultat : {clair}")
    rep=ask("Message déchiffré : ").upper().replace(" ","")
    if rep==clair: succes(f"✓ {chif}→{clair}"); score+=10
    else: erreur(f"Réponse : {clair}")
    pause()

    # Ex 2.3 robot
    effacer(); titre("MODULE 2 — Ex 3/5 : Robot Vigenère !", C)
    robot=(0,5); but=(5,0); traces=set()
    cle="BD"; chif="CGBF"; clair=vigenere_d(chif,cle)
    afficher_grille(robot,but,traces=traces)
    print(f"  {BGRD}  Chiffré : {chif}   Clé : {cle}  {RST}")
    print(f"  {DIM}  Clé se répète : B D B D ...{RST}\n")
    afficher_alphabet()
    sc=0
    for i,cc in enumerate(chif):
        lk=cle[i%len(cle)]; cl=vigenere_d(cc,lk); nom,d=lettre_dir(cl)
        print(f"\n  {M}Lettre {i+1} : '{cc}' - clé '{lk}' = ?{RST}")
        rep=ask("Lettre déchiffrée : ").upper()
        if rep and rep[0]==cl: succes(f"✓ {cc}-{lk}={cl}→{nom}!"); sc+=1
        else: erreur(f"'{cc}'({ord(cc)-65}) - '{lk}'({ord(lk)-65}) = {cl} → {nom}")
        traces.add(robot); robot=dep(robot,d); afficher_grille(robot,but,traces=traces)
    score+=sc*8; pause()

    # Ex 2.4 comparaison
    effacer(); titre("MODULE 2 — Ex 4/5 : César vs Vigenère", C)
    msg="ATTAQUE"; cc=cesar(msg,3); cv=vigenere_c(msg,"CLE")
    print(f"  {W}Original : {Y}{msg}{RST}\n")
    print(f"  {C}César   (décalage=3) : {G}{cc}{RST}")
    print(f"  {M}Vigenère (clé='CLE') : {G}{cv}{RST}\n")
    encadre(f"'ATTAQUE' contient 3 T.\nCésar : tous les T→{cesar('T',3)} (pareil)\nVigenère : les T donnent des lettres DIFFÉRENTES !")
    rep=ask("Avec lequel les T répétés donnent des lettres différentes ? ").lower()
    if "vig" in rep or rep=="v":
        succes("✓ Vigenère ! Les décalages variables masquent les répétitions."); score+=10
    else: erreur("Vigenère ! Décalages variables.")
    pause()

    # Ex 2.5 libre
    effacer(); titre("MODULE 2 — Ex 5/5 : Chiffre TON message !", C)
    while True:
        tm=ask("Ton mot (lettres, sans accents) : ").upper()
        if tm.isalpha() and len(tm)>=2: break
        print(f"  {R}✗ Au moins 2 lettres, sans accents.{RST}")
    tk=ask("Ta clé (1-5 lettres) : ").upper()
    if not tk.isalpha(): tk="KEY"
    res=vigenere_c(tm,tk)
    print(f"\n  {BGMG}  Résultat  {RST}")
    print(f"  {W}Original : {Y}{tm}{RST}\n  {W}Clé : {Y}{tk}{RST}\n  {W}Chiffré : {G}{res}{RST}")
    print(f"  {DIM}Vérif : {res} → {vigenere_d(res,tk)}{RST}")
    rep=ask("On retrouve ton mot original ? (oui/non) ").lower()
    if "oui" in rep or rep=="o": succes("✓ La crypto fonctionne !"); score+=15
    else: print(f"  {Y}Résultat : {vigenere_d(res,tk)}{RST}")
    print(f"\n  {BGMG}  Score module 2 : {score}  {RST}\n"); pause()
    return score


# ════════════════════════════════════════════════════════
#  MODULE 3 — ENIGMA
# ════════════════════════════════════════════════════════
def module_enigma():
    titre("MODULE 3 — Enigma et les Clés Secrètes", M)
    encadre(
        "La machine Enigma = Vigenère ULTRA-complexe.\n"
        "\n"
        "  • 3 rotors qui tournent à chaque lettre\n"
        "  • La clé change à CHAQUE frappe\n"
        "  • Propriété magique : chiffrer = déchiffrer !\n"
        "    (mêmes réglages → même opération)\n"
        "\n"
        "Mais aussi sa FAIBLESSE :\n"
        "  Une lettre ne peut JAMAIS se chiffrer en elle-même.\n"
        "  A ne donne jamais A. C'est ce qu'a exploité Turing !"
    )
    pause(); score=0

    class Enigma:
        def __init__(self, start=0, plug=None):
            self.r=start; self.w="EKMFLGDQVZNTOWYHXUSPAIBRCJ"; self.ref="YRUHQSLDPXNGOKMIEBFZCWVJAT"; self.p=plug or {}
        def ps(self,c): return self.p.get(c,c)
        def enc(self,c):
            c=c.upper()
            if not c.isalpha(): return c
            c=self.ps(c); pos=(ord(c)-65+self.r)%26; c=self.w[pos]
            c=self.ref[ord(c)-65]; pos=self.w.index(c); c=chr((pos-self.r)%26+65)
            c=self.ps(c); self.r=(self.r+1)%26; return c
        def chiffrer(self,t): return ''.join(self.enc(c) for c in t)

    # Ex 3.1
    effacer(); titre("MODULE 3 — Ex 1/5 : Symétrie Enigma", C)
    e1=Enigma(5); msg="BONJOUR"; chif=e1.chiffrer(msg)
    e2=Enigma(5); dec=e2.chiffrer(chif)
    print(f"  {BGCY}  Démonstration  {RST}\n")
    print(f"  {W}Original   : {Y}{msg}{RST}")
    print(f"  {W}Chiffré    : {G}{chif}{RST}")
    print(f"  {W}Déchiffré  : {G}{dec}{RST}\n")
    encadre("Chiffrer = Déchiffrer avec les mêmes réglages.\nMais : une lettre ne peut jamais se chiffrer en elle-même !")
    rep=ask("Enigma peut-elle chiffrer A en A ? (oui/non) ").lower()
    if "non" in rep or rep=="n": succes("✓ Non ! Faille exploitée par Turing !"); score+=10
    else: erreur("Non ! Jamais une lettre en elle-même.")
    pause()

    # Ex 3.2 clé secrète
    effacer(); titre("MODULE 3 — Ex 2/5 : Qu'est-ce qu'une clé ?", C)
    encadre(
        "Une CLÉ SECRÈTE = information partagée entre émetteur et récepteur.\n"
        "\n"
        "  César    → clé = un nombre\n"
        "  Vigenère → clé = un mot\n"
        "  Enigma   → clé = réglage rotors + plugboard\n"
        "\n"
        "Problème fondamental : comment partager la clé\n"
        "sans que l'ennemi l'intercepte ?\n"
        "→ C'est le PROBLÈME DE L'ÉCHANGE DE CLÉS."
    )
    qs=[("Avec César, la clé est...",["nombre","chiffre","un nombre"],"Un nombre (le décalage) !"),
        ("Avec Vigenère, la clé est...",["mot","un mot","chaine"],"Un mot !"),
        ("Le problème de l'échange : comment...",["partager","transmettre"],"Comment partager sans se faire intercepter !")]
    for q,b,e in qs:
        print(f"  {C}▶ {q}{RST}"); rep=ask("→ ").lower()
        if any(x in rep for x in b): succes(f"✓ {e}"); score+=5
        else: erreur(f"✗ {e}")
        print()
    pause()

    # Ex 3.3 robot Enigma
    effacer(); titre("MODULE 3 — Ex 3/5 : Robot Enigma !", C)
    robot=(0,5); but=(5,0); traces=set()
    e=Enigma(3); chif="XKQP"; ed=Enigma(3); clair=ed.chiffrer(chif)
    afficher_grille(robot,but,traces=traces)
    print(f"  {BGRD}  Intercepté : {chif}   Rotor départ : 3  {RST}")
    print(f"  {BGCY}  Déchiffré  : {clair}  {RST}\n")
    encadre("Chiffrer = Déchiffrer ! Tu as déjà le résultat. Guide le robot !")
    sc=0
    for i,c in enumerate(clair):
        nom,d=lettre_dir(c)
        print(f"\n  {M}Lettre {i+1} : '{c}' → direction ?{RST}")
        rep,dr=dir_input()
        traces.add(robot)
        if dr==d: succes(f"✓ {c}→{nom}!"); sc+=1
        else: erreur(f"'{c}'→{nom}!")
        robot=dep(robot,d); afficher_grille(robot,but,traces=traces)
    score+=sc*8; pause()

    # Ex 3.4 Turing
    effacer(); titre("MODULE 3 — Ex 4/5 : Alan Turing et la Bombe", C)
    encadre(
        "Turing a cassé Enigma en 1940.\n"
        "\n"
        "  1. Les météorologues envoyaient toujours 'WETTER'\n"
        "     → Ces mots connus = CRIBS\n"
        "  2. A ne peut jamais donner A → exclusion\n"
        "  3. Sa machine 'Bombe' testait des milliers\n"
        "     de configurations par seconde\n"
        "\n"
        "Les Alliés déchiffraient les messages en temps réel !"
    )
    qs=[("Comment appelle-t-on un mot connu dans le message ?",["crib","cribs"],"Un CRIB !"),
        ("Quelle faille a aidé Turing ?",["elle-meme","jamais","lettre"],"Une lettre ne se chiffre jamais en elle-même !"),
        ("La machine de Turing s'appelle ?",["bombe","bomb"],"La Bombe !")]
    for q,b,e in qs:
        print(f"  {C}▶ {q}{RST}"); rep=ask("→ ").lower()
        if any(x in rep for x in b): succes(f"✓ {e}"); score+=5
        else: erreur(f"✗ {e}")
        print()
    pause()

    # Ex 3.5 plugboard
    effacer(); titre("MODULE 3 — Ex 5/5 : Le Plugboard", C)
    encadre(
        "Le plugboard connecte des paires de lettres AVANT les rotors.\n"
        "\n"
        "  Plugboard {A↔Z, B↔Y} :\n"
        "    Frappe A → A remplacé par Z → entre dans les rotors\n"
        "    Frappe Z → Z remplacé par A → entre dans les rotors\n"
        "\n"
        "Avec 10 paires sur 26 lettres :\n"
        "  150 000 000 000 000 000 000 combinaisons !"
    )
    plug={'A':'Z','Z':'A','B':'Y','Y':'B'}
    ep=Enigma(0,plug)
    print(f"  {W}Plugboard : A↔Z, B↔Y{RST}")
    print(f"  {C}▶ A est d'abord remplacé par ? (via plugboard){RST}")
    rep=ask("A → ").upper()
    if rep and rep[0]=='Z': succes("✓ A→Z via plugboard, puis rotors !"); score+=10
    else: erreur("A est câblé à Z dans le plugboard !")
    print(f"\n  {BGMG}  Score module 3 : {score}  {RST}\n"); pause()
    return score


# ════════════════════════════════════════════════════════
#  MODULE 4 — CLÉ PUBLIQUE
# ════════════════════════════════════════════════════════
def module_cle_publique():
    titre("MODULE 4 — Cryptographie à Clé Publique", M)
    encadre(
        "Jusqu'ici : chiffrement SYMÉTRIQUE\n"
        "  → même clé pour chiffrer ET déchiffrer\n"
        "  → problème : comment partager la clé ?\n"
        "\n"
        "1976 : Diffie & Hellman inventent l'ASYMÉTRIQUE !\n"
        "\n"
        "  CLÉ PUBLIQUE → tout le monde la connaît\n"
        "  CLÉ PRIVÉE   → toi seul la connais\n"
        "\n"
        "  Chiffrer avec clé PUBLIQUE de Bob\n"
        "  Seul Bob peut déchiffrer avec sa clé PRIVÉE\n"
        "\n"
        "C'est ce qui sécurise HTTPS sur internet !"
    )
    pause(); score=0

    # Ex 4.1 cadenas
    effacer(); titre("MODULE 4 — Ex 1/5 : L'analogie du Cadenas", C)
    encadre(
        "Imagine un cadenas ouvert :\n"
        "\n"
        "  Bob envoie son CADENAS OUVERT à Alice\n"
        "  (clé publique = cadenas ouvert)\n"
        "\n"
        "  Alice met son message dans une boîte\n"
        "  et ferme avec le cadenas de Bob\n"
        "\n"
        "  Seul Bob a la CLÉ pour ouvrir\n"
        "  (clé privée = clé du cadenas)\n"
        "\n"
        "Eve intercepte la boîte fermée mais ne peut pas l'ouvrir !"
    )
    qs=[("La clé publique ressemble à...",["cadenas","ouvert","cadenas ouvert"],"Le cadenas ouvert !"),
        ("La clé privée ressemble à...",["cle","clé","cle du cadenas"],"La clé du cadenas !"),
        ("Peut-on déchiffrer avec la clé publique ?",["non"],"Non ! Elle chiffre seulement.")]
    for q,b,e in qs:
        print(f"  {C}▶ {q}{RST}"); rep=ask("→ ").lower()
        if any(x in rep for x in b): succes(f"✓ {e}"); score+=5
        else: erreur(f"✗ {e}")
        print()
    pause()

    # Ex 4.2 factorisation
    effacer(); titre("MODULE 4 — Ex 2/5 : La Fonction à Sens Unique", C)
    encadre(
        "Fonctions à sens unique :\n"
        "  17 × 19 = 323  → FACILE (1 seconde)\n"
        "  323 = ? × ?    → DIFFICILE\n"
        "\n"
        "Avec des nombres de 300 chiffres :\n"
        "  Multiplier : 1 milliseconde\n"
        "  Factoriser : plus long que l'âge de l'univers !\n"
        "\n"
        "C'est la base de RSA."
    )
    for n,f1,f2 in [(15,3,5),(21,3,7),(35,5,7)]:
        print(f"  {Y}{n} = ? × ?{RST}"); rep=ask(f"Facteurs de {n} (ex: 3 5) : ")
        nums=[int(x) for x in rep.split() if x.isdigit()]
        if len(nums)>=2 and set([nums[0],nums[1]])=={f1,f2}:
            succes(f"✓ {n}={f1}×{f2}!"); score+=5
        else: erreur(f"{n}={f1}×{f2}")
    pause()

    # Ex 4.3 Diffie-Hellman couleurs
    effacer(); titre("MODULE 4 — Ex 3/5 : Diffie-Hellman en couleurs !", C)
    encadre(
        "Échange de clés avec des peintures :\n"
        "\n"
        "  1. Couleur commune publique : JAUNE\n"
        "  2. Secrets : Alice=ROUGE, Bob=BLEU\n"
        "  3. Échange : Alice→ORANGE(jaune+rouge), Bob→VERT(jaune+bleu)\n"
        "  4. Mélange final :\n"
        "     Alice : VERT  + ROUGE = MARRON\n"
        "     Bob   : ORANGE+ BLEU  = MARRON\n"
        "\n"
        "→ Même couleur finale sans révéler le secret !\n"
        "   Eve voit jaune+orange+vert mais pas rouge ni bleu."
    )
    print(f"  {C}▶ Qu'est-ce qu'Eve voit sur le réseau ?{RST}")
    rep=ask("→ ").lower()
    if any(x in rep for x in ["orange","vert","jaune","couleur","melange"]):
        succes("✓ Jaune, orange et vert — mais pas rouge ni bleu !"); score+=10
    else: erreur("Elle voit jaune, orange, vert — mais pas les secrets rouge/bleu !")
    print(f"\n  {C}▶ Pourquoi Eve ne peut pas trouver la couleur finale ?{RST}")
    rep=ask("→ ").lower()
    if any(x in rep for x in ["secret","rouge","bleu","pas les","sans"]):
        succes("✓ Elle n'a jamais vu rouge ni bleu !"); score+=10
    else: erreur("Elle n'a pas les couleurs secrètes (rouge et bleu) !")
    pause()

    # Ex 4.4 signatures
    effacer(); titre("MODULE 4 — Ex 4/5 : La Signature Numérique", C)
    encadre(
        "La clé privée sert aussi à SIGNER !\n"
        "\n"
        "  Chiffrement  : clé publique  → clé privée\n"
        "  Signature    : clé privée    → clé publique\n"
        "\n"
        "Usages :\n"
        "  → Logiciels (vérifier l'auteur)\n"
        "  → Emails signés\n"
        "  → Certificats HTTPS\n"
        "  → Bitcoin et cryptomonnaies !"
    )
    qs=[("Pour chiffrer à Bob, on utilise sa clé...",["publique","public"],"Clé PUBLIQUE de Bob !"),
        ("Pour signer, on utilise sa clé...",["privee","privée","prive","privé"],"Clé PRIVÉE !"),
        ("HTTPS utilise...",["publique","rsa","tls","ssl","asymet"],"La cryptographie à clé publique !")]
    for q,b,e in qs:
        print(f"  {C}▶ {q}{RST}"); rep=ask("→ ").lower()
        if any(x in rep for x in b): succes(f"✓ {e}"); score+=5
        else: erreur(f"✗ {e}")
        print()
    pause()

    # Ex 4.5 récap
    effacer(); titre("MODULE 4 — Ex 5/5 : Récapitulatif", C)
    print(f"  {BGWH}  Symétrique vs Asymétrique  {RST}\n")
    rows=[("Nb de clés","1 clé partagée","2 clés pub/priv"),
          ("Exemples","César,Vigenère,AES","RSA,ECC"),
          ("Vitesse","Très rapide","Plus lent"),
          ("Usage","Chiffrer données","Échange de clé")]
    print(f"  {C}{'Critère':<20} {'Symétrique':<20} {'Asymétrique'}{RST}")
    print(f"  {'─'*60}")
    for c,s,a in rows: print(f"  {W}{c:<20}{RST} {Y}{s:<20}{RST} {G}{a}{RST}")
    print()
    rep=ask("Lequel est le plus rapide ? (symetrique/asymetrique) ").lower()
    if "sym" in rep: succes("✓ Symétrique ! C'est pourquoi HTTPS utilise les deux."); score+=10
    else: erreur("Symétrique ! L'asymétrique est puissant mais lent.")
    print(f"\n  {BGMG}  Score module 4 : {score}  {RST}\n"); pause()
    return score


# ════════════════════════════════════════════════════════
#  MODULE 5 — ARITHMÉTIQUE RSA
# ════════════════════════════════════════════════════════
def module_arithmetique_rsa():
    titre("MODULE 5 — Arithmétique pour RSA", M)
    encadre(
        "RSA repose sur 3 outils mathématiques :\n"
        "\n"
        "  1. NOMBRES PREMIERS\n"
        "     Divisibles seulement par 1 et eux-mêmes\n"
        "     Ex : 2, 3, 5, 7, 11, 13, 17...\n"
        "\n"
        "  2. MODULO (reste de la division)\n"
        "     17 mod 5 = 2  (17 = 3×5 + 2)\n"
        "     C'est ce qu'on utilise dans César !\n"
        "\n"
        "  3. INDICATRICE D'EULER φ(n)\n"
        "     Pour n = p×q (p,q premiers) :\n"
        "     φ(n) = (p-1)×(q-1)"
    )
    pause(); score=0

    # Ex 5.1 premiers
    effacer(); titre("MODULE 5 — Ex 1/5 : Nombres Premiers", C)
    premiers=[n for n in range(2,31) if est_premier(n)]
    print(f"  {C}Grille d'Ératosthène (2 à 30) :{RST}\n  ", end="")
    for n in range(2,31):
        if est_premier(n): print(f"{G}{n:3}{RST}",end="")
        else: print(f"{DIM}{n:3}{RST}",end="")
    print(f"\n\n  {G}Vert{RST}=premier  {DIM}Gris{RST}=non premier\n")
    for n in [17,15,23,9,29]:
        print(f"  {C}▶ {n} est-il premier ? (oui/non){RST}"); rep=ask("→ ").lower()
        att=est_premier(n); ok=("oui" in rep or rep=="o")==att
        if ok: succes(f"✓ {n} {'EST' if att else 'N EST PAS'} premier !"); score+=4
        else:
            erreur(f"{n} {'EST' if att else 'N EST PAS'} premier !")
            if not att:
                for i in range(2,n):
                    if n%i==0: indice(f"{n}={i}×{n//i}"); break
    pause()

    # Ex 5.2 modulo
    effacer(); titre("MODULE 5 — Ex 2/5 : Le Modulo", C)
    encadre(
        "Modulo = reste de la division entière\n"
        "  17 mod 5 = 2   (17 = 3×5 + 2)\n"
        "  Comme une horloge : 14h mod 12 = 2h\n"
        "  César : Z+3 = C  (25+3=28, 28 mod 26 = 2 = C)"
    )
    print(f"  {C}Horloge mod 12 :{RST}")
    for h in [0,6,12,14,25]: print(f"  {Y}  {h:2}h mod 12 = {h%12:2}h{RST}")
    print()
    for a,m,res in [(17,5,2),(25,7,4),(100,13,9),(30,4,2)]:
        print(f"  {C}▶ {a} mod {m} = ?{RST}"); rep=ask("→ ")
        try:
            if int(rep)==res: succes(f"✓ {a} mod {m} = {res}  ({a}={a//m}×{m}+{res})"); score+=5
            else: erreur(f"{a} mod {m} = {res}  ({a}={a//m}×{m}+{res})")
        except: erreur(f"{a} mod {m} = {res}")
    pause()

    # Ex 5.3 PGCD
    effacer(); titre("MODULE 5 — Ex 3/5 : PGCD et Copremierse", C)
    encadre(
        "PGCD = Plus Grand Commun Diviseur\n"
        "  PGCD(12,8)=4   PGCD(7,9)=1\n"
        "\n"
        "Copremierse (premiers entre eux) = PGCD = 1\n"
        "\n"
        "Algorithme d'Euclide pour PGCD(48,18) :\n"
        "  48=2×18+12 → PGCD(18,12)\n"
        "  18=1×12+6  → PGCD(12,6)\n"
        "  12=2×6+0   → PGCD=6"
    )
    for a,b,res in [(12,8,4),(15,25,5),(7,13,1),(36,24,12)]:
        print(f"  {C}▶ PGCD({a},{b}) = ?{RST}"); rep=ask("→ ")
        try:
            if int(rep)==res: succes(f"✓ PGCD({a},{b})={res} {'→ copremierse !' if res==1 else ''}"); score+=5
            else: erreur(f"PGCD({a},{b})={res}")
        except: erreur(f"PGCD({a},{b})={res}")
    pause()

    # Ex 5.4 phi
    effacer(); titre("MODULE 5 — Ex 4/5 : φ(n) — Indicatrice d'Euler", C)
    encadre(
        "φ(n) = nombre d'entiers < n copremierse avec n\n"
        "Si n=p×q (p,q premiers) : φ(n)=(p-1)×(q-1)\n"
        "\n"
        "n=15=3×5 → φ(15)=(3-1)×(5-1)=2×4=8\n"
        "Si on connaît p et q → φ facile à calculer\n"
        "Si on ne les connaît pas → très difficile !"
    )
    for n,p,q,phi in [(15,3,5,8),(21,3,7,12),(35,5,7,24)]:
        print(f"  {C}▶ n={p}×{q}={n}. φ({n})=(p-1)×(q-1) = ?{RST}"); rep=ask(f"φ({n}) = ")
        try:
            if int(rep)==phi: succes(f"✓ φ({n})=({p}-1)×({q}-1)={p-1}×{q-1}={phi}"); score+=8
            else: erreur(f"φ({n})={p-1}×{q-1}={phi}")
        except: erreur(f"φ({n})={phi}")
    pause()

    # Ex 5.5 inverse modulaire
    effacer(); titre("MODULE 5 — Ex 5/5 : Inverse Modulaire", C)
    encadre(
        "Inverse modulaire de e mod φ(n) :\n"
        "  d tel que e×d ≡ 1 (mod φ(n))\n"
        "\n"
        "Exemple : e=3, φ=8\n"
        "  3×1=3 mod 8=3 ✗\n"
        "  3×2=6 mod 8=6 ✗\n"
        "  3×3=9 mod 8=1 ✓ → d=3\n"
        "\n"
        "d = clé PRIVÉE   e = clé PUBLIQUE dans RSA"
    )
    for e,phi,d in [(3,8,3),(5,12,5),(7,20,3)]:
        print(f"  {C}▶ {e}×d ≡ 1 (mod {phi}) → d = ?{RST}")
        for t in range(1,phi+1):
            if (e*t)%phi==1: print(f"  {DIM}  Vérif : {e}×{t}={e*t}, mod {phi}={(e*t)%phi}{RST}"); break
        rep=ask("d = ")
        try:
            if int(rep)==d: succes(f"✓ d={d}! {e}×{d}={e*d} mod {phi}={(e*d)%phi}"); score+=8
            else: erreur(f"d={d}")
        except: erreur(f"d={d}")
    print(f"\n  {BGMG}  Score module 5 : {score}  {RST}\n"); pause()
    return score


# ════════════════════════════════════════════════════════
#  MODULE 6 — RSA COMPLET
# ════════════════════════════════════════════════════════
def module_rsa():
    titre("MODULE 6 — Le Chiffrement RSA", M)
    encadre(
        "RSA = Rivest, Shamir, Adleman (1977)\n"
        "\n"
        "GÉNÉRATION DES CLÉS :\n"
        "  1. Choisir p, q premiers\n"
        "  2. n = p×q\n"
        "  3. φ(n) = (p-1)×(q-1)\n"
        "  4. Choisir e : PGCD(e,φ(n))=1\n"
        "  5. d = inverse de e mod φ(n)\n"
        "\n"
        "  Clé publique : (n, e)\n"
        "  Clé privée   : (n, d)\n"
        "\n"
        "CHIFFRER  : c = m^e mod n\n"
        "DÉCHIFFRER: m = c^d mod n"
    )
    pause(); score=0

    # Ex 6.1 générer clés
    effacer(); titre("MODULE 6 — Ex 1/5 : Générer des clés RSA !", C)
    p,q=5,11; n=p*q; phi=(p-1)*(q-1); e=3; d=inv_mod(e,phi)
    print(f"  {BGCY}  p={p}, q={q}  {RST}\n")
    print(f"  {C}Étape 1 : n = {p}×{q}{RST}")
    rep=ask(f"n = ")
    try:
        if int(rep)==n: succes(f"✓ n={n}"); score+=8
        else: erreur(f"n={n}")
    except: erreur(f"n={n}")
    print(f"\n  {C}Étape 2 : φ({n}) = ({p}-1)×({q}-1){RST}")
    rep=ask("φ(n) = ")
    try:
        if int(rep)==phi: succes(f"✓ φ({n})={phi}"); score+=8
        else: erreur(f"φ({n})={phi}")
    except: erreur(f"φ({n})={phi}")
    print(f"\n  {C}Étape 3 : e={e}, trouve d tel que {e}×d≡1 (mod {phi}){RST}")
    rep=ask("d = ")
    try:
        if int(rep)==d: succes(f"✓ d={d}!"); score+=8
        else: erreur(f"d={d}")
    except: erreur(f"d={d}")
    print(f"\n  {BGMG}  Clé publique : (n={n}, e={e})  {RST}")
    print(f"  {BGMG}  Clé privée   : (n={n}, d={d})  {RST}\n"); pause()

    # Ex 6.2 chiffrer
    effacer(); titre("MODULE 6 — Ex 2/5 : Chiffrer avec RSA !", C)
    p,q=5,11; n=p*q; phi=(p-1)*(q-1); e=3; d=inv_mod(e,phi); m=7
    print(f"  {BGCY}  Clé publique : (n={n}, e={e})   Message : m={m}  {RST}\n")
    encadre(f"c = m^e mod n = {m}^{e} mod {n}\n{m}^{e} = {m**e}\n{m**e} mod {n} = ?")
    c=pow(m,e,n)
    print(f"  {DIM}  {m}^{e}={m**e}   mod {n}=?{RST}")
    rep=ask(f"c = ")
    try:
        if int(rep)==c: succes(f"✓ c={c} ! {m} chiffré en {c}."); score+=12
        else: erreur(f"c={m**e} mod {n}={c}")
    except: erreur(f"c={c}")
    pause()

    # Ex 6.3 déchiffrer
    effacer(); titre("MODULE 6 — Ex 3/5 : Déchiffrer avec RSA !", C)
    p,q=5,11; n=p*q; phi=(p-1)*(q-1); e=3; d=inv_mod(e,phi)
    c=pow(7,e,n); m_att=7
    print(f"  {BGRD}  Chiffré : c={c}  {RST}")
    print(f"  {BGCY}  Clé privée : (n={n}, d={d})  {RST}\n")
    encadre(f"m = c^d mod n = {c}^{d} mod {n}\n{c}^{d} = {c**d}\n{c**d} mod {n} = ?")
    m=pow(c,d,n)
    rep=ask(f"m = ")
    try:
        if int(rep)==m: succes(f"✓ m={m} ! On retrouve le message original !"); score+=12
        else: erreur(f"m={c**d} mod {n}={m}")
    except: erreur(f"m={m}")
    pause()

    # Ex 6.4 robot RSA
    effacer(); titre("MODULE 6 — Ex 4/5 : Robot RSA !", C)
    robot=(0,5); but=(5,0); traces=set()
    p,q=3,7; n=p*q; phi=(p-1)*(q-1); e=5; d=inv_mod(e,phi)
    msgs=[2,5,8,1]
    cs=[pow(m,e,n) for m in msgs]
    ms=[pow(c,d,n) for c in cs]
    dirs=[lettre_dir(chr(m+65)) for m in ms]
    afficher_grille(robot,but,traces=traces)
    print(f"  {BGCY}  Clé publique (n={n},e={e}) · Clé privée (n={n},d={d})  {RST}")
    print(f"  {W}Messages chiffrés : {G}{cs}{RST}")
    print(f"  {DIM}Formule : m = c^d mod n{RST}\n")
    sc=0
    for i,(cv,mv,(nom,dd)) in enumerate(zip(cs,ms,dirs)):
        lettre=chr(mv+65)
        print(f"\n  {M}c={cv} → {cv}^{d} mod {n}={mv} → '{lettre}' → direction ?{RST}")
        rep,dr=dir_input()
        traces.add(robot)
        if dr==dd: succes(f"✓ {lettre}→{nom}!"); sc+=1
        else: erreur(f"c={cv}→m={mv}→'{lettre}'→{nom}!")
        robot=dep(robot,dd); afficher_grille(robot,but,traces=traces)
    score+=sc*10; pause()

    # Ex 6.5 bout en bout
    effacer(); titre("MODULE 6 — Ex 5/5 : RSA de bout en bout !", C)
    p,q=7,11; n=p*q; phi=(p-1)*(q-1); e=13; d=inv_mod(e,phi)
    print(f"  {BGCY}  BOB : p={p}, q={q} → n={n}, φ={phi}, e={e}, d={d}  {RST}")
    print(f"  {BGMG}  Clé publique de Bob : (n={n}, e={e})  {RST}")
    print(f"  {BGRD}  Clé privée de Bob   : (n={n}, d={d})  {RST}\n")
    m_alice=4
    print(f"  {BGCY}  ALICE envoie m={m_alice}  {RST}")
    print(f"  {C}ALICE chiffre : c = {m_alice}^{e} mod {n}{RST}")
    c_alice=pow(m_alice,e,n)
    rep=ask(f"c = {m_alice}^{e} mod {n} = ")
    try:
        if int(rep)==c_alice: succes(f"✓ c={c_alice} ! Alice envoie {c_alice} à Bob."); score+=10
        else: erreur(f"c={c_alice}")
    except: pass
    print(f"\n  {BGRD}  BOB reçoit c={c_alice} et déchiffre  {RST}")
    print(f"  {M}BOB : m = {c_alice}^{d} mod {n}{RST}")
    m_bob=pow(c_alice,d,n)
    rep=ask(f"m = {c_alice}^{d} mod {n} = ")
    try:
        if int(rep)==m_bob: succes(f"✓ m={m_bob} ! Bob a reçu {m_alice} !"); score+=10
        else: erreur(f"m={m_bob}")
    except: pass
    print(f"\n  {BGGR}  🎉 m={m_alice}→chiffré={c_alice}→déchiffré={m_bob}  {RST}\n")
    print(f"\n  {BGMG}  Score module 6 : {score}  {RST}\n"); pause()
    return score


# ════════════════════════════════════════════════════════
#  ÉCRAN TITRE
# ════════════════════════════════════════════════════════
def ecran_titre():
    effacer(); print()
    print(M+"  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ")
    print(C+"  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗")
    print(B+"  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║")
    print(Y+"  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║")
    print(G+"  ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝")
    print(R+"   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ "+RST)
    print()
    print(f"  {W}Apprends la Cryptographie de César à RSA en jouant !{RST}")
    print(f"  {DIM}Du chiffre antique aux secrets d'internet{RST}\n")
    infos=[("MODULE 1","César","Décalage — Jules César"),
           ("MODULE 2","Vigenère","Clé répétée — La chiffre indéchiffrable"),
           ("MODULE 3","Enigma","Machine de guerre — Alan Turing"),
           ("MODULE 4","Clé publique","Révolution 1976 — Diffie & Hellman"),
           ("MODULE 5","Arithmétique RSA","Premiers, modulo, φ(n)"),
           ("MODULE 6","RSA complet","Le chiffrement d'internet")]
    for c,n,d in infos: print(f"  {C}{c}{RST} {W}{n:<18}{RST} {DIM}{d}{RST}")
    print(); pause()


# ════════════════════════════════════════════════════════
#  MENU
# ════════════════════════════════════════════════════════
def menu():
    modules=[
        ("Module 1","Chiffre de César",module_cesar),
        ("Module 2","Chiffre de Vigenère",module_vigenere),
        ("Module 3","Enigma et clés secrètes",module_enigma),
        ("Module 4","Cryptographie à clé publique",module_cle_publique),
        ("Module 5","Arithmétique pour RSA",module_arithmetique_rsa),
        ("Module 6","Chiffrement RSA",module_rsa),
    ]
    scores={}
    for label,tm,fn in modules:
        effacer()
        print(f"\n  {BGMG}  {label} : {tm}  {RST}\n")
        print(f"  {DIM}Entrée pour commencer, 'passer' pour sauter.{RST}")
        if input("  → ").strip().lower()=="passer": continue
        scores[label]=fn()

    effacer(); titre("BILAN FINAL — De César à RSA !", G)
    parcours=[
        ("César (−50 av. J.-C.)","Décalage simple, 26 possibilités"),
        ("Vigenère (1553)","Clé répétée, plus difficile"),
        ("Enigma (1918-1945)","Machine, espace de clés énorme"),
        ("Diffie-Hellman (1976)","Échange de clés sans rencontre"),
        ("RSA (1977)","Clé publique/privée, sécurise internet"),
    ]
    print(f"  {W}Le chemin parcouru :{RST}\n")
    for ep,d in parcours: print(f"  {Y}{ep:<28}{RST} {C}{d}{RST}")
    print()
    total=0
    for l,s in scores.items(): print(f"  {Y}{l}{RST} : {G}{s} pts{RST}"); total+=s
    print(f"\n  {BGMG}  Total : {total} points  {RST}")
    print(f"\n  {W}Prochaines étapes :{RST}")
    print(f"  {C}  → AES — chiffrement symétrique moderne{RST}")
    print(f"  {C}  → Courbes elliptiques (ECC){RST}")
    print(f"  {C}  → Cryptographie quantique !{RST}\n")

if __name__=="__main__":
    ecran_titre()
    menu()
