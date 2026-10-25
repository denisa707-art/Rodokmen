# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Prostředí (cloud claude.ai)
- Kontejner je dočasný: po každém kroku uložit a odeslat `git add -A && git commit -m "…" && git push` (repozitář denisa707-art/rodokmen).
- Není `magick`, jen ImageMagick 6 (`convert`) – nástroje si ho najdou samy.
