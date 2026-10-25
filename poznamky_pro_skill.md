# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- 2026-10-25: Skill nainstalovaný jako „synced“ (anthropic-skills:rodokmen v cloudu claude.ai) obsahoval jen SKILL.md – chyběly tools/, template/, reference/, VERZE. Vyřešeno instalací pluginu z marketplace (sarsonj/rodokmen-skill, verze 0.5.0). Do SKILL.md by se hodila poznámka, co dělat, když SKILL_DIR nemá tools/.
- Cloudové prostředí claude.ai: síťová politika ve výchozím stavu blokuje archivní portály (ARON: 403 od proxy) a chybí `magick` (je jen ImageMagick 6 `convert`). Kontejner je dočasný – projekt je třeba ukládat do repozitáře na GitHubu.
- Netlify z cloudu claude.ai: `npm run nasadit` padá na `getaddrinfo ENOTFOUND api.netlify.com` (Node fetch ignoruje HTTPS_PROXY) – pomohlo `NODE_USE_ENV_PROXY=1 npm run nasadit`. Nový účet: `sites:create` bez `--account-slug` hlásí „No teams available“ – slug zjistit `netlify api listAccountsForUser`. Nový web měl zapnutou Team protection (401 Login Redirect), jak popisuje web.md.
