# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Denisa Zubajová", y="* 1986", st="fam", f=[], sex="F", note="Žijící – údaje jen základní."),
    3: dict(n="Ivana Pinkavová", y="* 1965", st="fam", f=[], note="Žijící – údaje jen základní."),
    6: dict(n="Oldřich Pinkava", y="* 1942", st="fam", f=["* 5. 12. 1942 Praha"],
            note="Údaj od rodiny. Zda žije, zatím nevíme – do té doby jen základní údaje."),
    7: dict(n="Ludmila Švecová", y="1942–2017", st="fam", f=["* 12. 12. 1942 Praha", "× Oldřich Pinkava", "† 17. 7. 2017"],
            note="Údaje od rodiny."),
    14: dict(n="František Švec", y="1912–1996", st="fam",
             f=["* 14. 9. 1912", "řidič lokomotivy", "× 1940 Marie Bendová", "† 5. 9. 1996 Praha"],
             note="Údaje od rodiny. Místo narození neznámé; „Praha“ je nejspíš místo úmrtí. S manželkou žili v Salačově Lhotě (okr. Pelhřimov)."),
    15: dict(n="Marie Bendová", y="1921–2007", st="fam",
             f=["* 23. 11. 1921", "× 1940 František Švec", "† 17. 7. 2007 Praha"],
             note="Údaje od rodiny. Rodina nejdřív uvedla rok narození 1912, pak přesné datum 23. 11. 1921 – platí zatím 1921 (viz Co hledáme). Místo narození neznámé, „jižní Čechy“."),
    31: dict(n="Marie Bendová", y="1889–1964", st="prob",
             f=["* 15. 8. 1889 jižní Čechy", "† 25. 4. 1964"],
             note="Údaj od rodiny: „nejspíš maminka“ Marie (1921) – zatím nedoloženo. Není jasné, zda je Bendová její rodné příjmení, nebo po manželovi."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdy se narodila Marie Švecová, roz. Bendová?", "Otevřené: rodina uvedla nejdřív rok 1912, pak datum 23. 11. 1921 (rok 1912 je rok narození jejího manžela Františka)."),
    ("Kde se narodila Marie Bendová (1921) a kde se v roce 1940 brala s Františkem Švecem?", "Otevřené: žili v Salačově Lhotě (fara Lukavec, okr. Pelhřimov); sňatky odtud po roce 1911 nejsou online."),
    ("Je Marie Bendová (1889) maminkou Marie (1921)? Je Bendová její rodné příjmení, nebo po manželovi?", "Otevřené: rozhodne křestní zápis Marie z roku 1921."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
