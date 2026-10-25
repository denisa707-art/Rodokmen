# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Denisa Zubajová, * 1986 (žijící – na webu jen jméno a rok). Linie k Švecům/Bendovým vede přes maminku Ivanu, roz. Pinkavovou.
- Kdo s Claudem pracuje a jak chce komunikovat: Denisa sama; česky, stručně, bez žargonu. Píše krátce, bez diakritiky.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Web: https://rodokmen-pinkavovych-a-svecovych.netlify.app (přihlášení otázkou na psa). Aktualizace: `cd web && NODE_USE_ENV_PROXY=1 npm run nasadit` (v cloudu; v novém kontejneru nejdřív `npm install` a znovu přihlásit Netlify přes `login --request`).
- Švecovi/Bendovi: matriky Salačovy Lhoty (fara Lukavec) po 1876 nejsou online → čekáme na rodinu (místo narození Marie 1921, doklady, hrob) nebo žádost na matriční úřad (`archivni_dotazy.md`).
- Pinkavovi: pradědeček Oldřich * 1909 Dobrošov u Náchoda; Pinkavové hlavně v sousední Dol. Radechové (index N Náchod 1867–1899 prošlý). Čeká se na výpis z matriky Náchod (jména rodičů). Krausovi: Růžena * 19. 8. 1919 Krupka u Teplic (potvrzeno) – SOA Litoměřice byl 25. 10. mimo provoz.
- Rod otce (Zubajovi, Lučivná, okr. Poprad) – zatím nic nevíme.
