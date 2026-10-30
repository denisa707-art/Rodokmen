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
    2: dict(n="Josef Zubaj", y="* 1961", st="fam", f=[], note="Žijící – údaje jen základní. Pochází ze Slovenska."),
    3: dict(n="Ivana Pinkavová", y="* 1965", st="fam", f=[], note="Žijící – údaje jen základní."),
    4: dict(n="Július Zubaj", y="1929–2008", st="mh", f=["* 27. 3. 1929", "× Helena Pačajová", "† 16. 7. 2008 Lučivná"],
            note="Z Denisina stromu na MyHeritage; údaje tam převzaté přes Smart Match z cizího stromu (Čonka Web Site) – ověřit u tatínka a v matrice. Ve stromu psán „Jůlius“."),
    5: dict(n="Helena Pačajová", y="1936–2021", st="mh", f=["* 30. 3. 1936", "× Július Zubaj", "† 26. 10. 2021 Kolín", "pohřbena 30. 10. 2021 Lučivná"],
            note="Z Denisina stromu na MyHeritage (přidáno přes Person Discovery) – ověřit u tatínka."),
    6: dict(n="Oldřich Pinkava", y="* 1942", st="fam", f=[],
            note="Žijící – údaje jen základní."),
    7: dict(n="Ludmila Švecová", y="1942–2017", st="fam", f=["* 12. 12. 1942 Praha", "× Oldřich Pinkava", "† 17. 7. 2017"],
            note="Údaje od rodiny."),
    8: dict(n="Koloman Gaži", y="† 1978", st="mh", f=["† 1978"],
            note="Jen z cizího stromu (Čonka Web Site, Smart Match na MyHeritage). Otec a syn mají v cizím stromu různá příjmení (Gaži × Zubaj) – spojení ověřit."),
    9: dict(n="Rozária Gažiová", y="", st="mh", f=[],
            note="Jen z cizího stromu (Čonka Web Site, Smart Match). Rodné příjmení neznámé."),
    10: dict(n="Ján Pačaj", y="", st="mh", f=[], note="Z MyHeritage (Person Discovery) – neověřeno."),
    11: dict(n="Mária (rodné příjmení neznámé)", y="", st="mh", f=["× Ján Pačaj"], note="Z MyHeritage (Person Discovery) – neověřeno."),
    12: dict(n="Oldřich Pinkava", y="1909–1987", st="fam", f=["* 9. 6. 1909 Dobrošov", "† 8. 8. 1987 Praha"],
             note="Údaje od rodiny (Dobrošov u Náchoda – upřesnila Denisa 25. 10. 2026). Místo úmrtí zatím neznámé. V Dobrošově žili Pinkavové už v 80. letech 19. stol. (chalupa č. 15)."),
    24: dict(n="Stanislav Pinkava", y="1882–1953", st="doc",
             f=["* 7. 10. 1882 Dolní Radechová čp. 10", "× 9. 11. 1908 Náchod Anna Nyčová (?)", "† 13. 2. 1953 Chcebuz"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"],
             note="Narození čteno v matrice. Sňatek a úmrtí z pozdějších poznámek na okraji křestního zápisu. "
                  "Ztotožnění s otcem Oldřicha (* 1909 Dobrošov): rodina zná jména rodičů Standa a Anna, poznámka uvádí sňatek se Annou "
                  "v Náchodě 1908 a je to jediný Stanislav Pinkava ve farnosti 1867–1899. Zápis o narození Oldřicha (matrika Náchod) to potvrdí."),
    25: dict(n="Anna Nyčová (?)", y="", st="prob", f=["× 9. 11. 1908 Náchod Stanislav Pinkava"],
             note="Jméno Anna od rodiny; příjmení z okrajové poznámky u křtu Stanislava – čtení nejisté (Nyčová / Myčová?). Ověřit v oddací matrice Náchod 1907–1916."),
    48: dict(n="Arnošt Pinkava", y="", st="doc", f=["nájemník v Dolní Radechové čp. 10 (1882)", "× Vincencie Žídková (?)"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"], note="Z křestního zápisu syna Stanislava (1882)."),
    49: dict(n="Vincencie Žídková (?)", y="", st="doc", f=["× Arnošt Pinkava"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"], note="Z křestního zápisu syna Stanislava (1882); příjmení otce čteno „Žídka“ – nejisté."),
    96: dict(n="František Pinkava", y="", st="doc", f=["chalupník v Dolní Radechové čp. 37 (1882)", "× Josefa Pinkavová"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"], note="Z křestního zápisu vnuka Stanislava (1882)."),
    97: dict(n="Josefa Pinkavová", y="", st="doc", f=["z Dolní Radechové čp. 27", "× František Pinkava"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"], note="Rozená Pinkavová (z čp. 27) – ve vsi bylo víc rodin Pinkavů. Z křestního zápisu vnuka Stanislava (1882)."),
    98: dict(n="Jan Žídek (?)", y="", st="doc", f=["chalupník a kovář v Dolní Radechové čp. 54 (1882)", "× Veronika Benešová"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"], note="Z křestního zápisu vnuka Stanislava (1882); příjmení čteno nejistě."),
    99: dict(n="Veronika Benešová", y="", st="doc", f=["ze Lhoty u Machova čp. 18", "× Jan Žídek (?)"],
             r=["dolni_radechova_krest_stanislav_pinkava_1882"], note="Dcera Václava Beneše, kováře ze Lhoty u Machova (okr. Broumov). Z křestního zápisu vnuka Stanislava (1882)."),
    13: dict(n="Růžena Krausová", y="1919–1993", st="fam", f=["* 19. 8. 1919 Krupka", "× Oldřich Pinkava", "† 19. 4. 1993 Praha"],
             note="Údaje od rodiny; rodné příjmení Krausová dohledala Denisa (25. 10. 2026). Místo narození zatím neznámé."),
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
