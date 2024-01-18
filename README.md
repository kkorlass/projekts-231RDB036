
# projekts-231RDB036
Python skripts, lai nolasītu jaunākos rakstus ziņu portālā Phoronix un izvadītu terminālī, lai varētu tos izmantot cmd, PowerShell, bash vai zsh skriptos.

## Instalācija

### Parastā instalācija
1. Klonē git repozitoriju: `git clone https://github.com/kkorlass/projekts-231RDB036.git`
2. Atver mapi project-231RDB036: `cd project-231RDB036`
3. Instalē nepieciešamās pakotnes: `pip install requests beautifulsoup4 pytz`

### Python venv instalācija
Šis instalācijas veids ir ieteicams sistēmām, kas neatbalsta globālo `pip`, piemēram, Arch Linux.
1. Klonē git repozitoriju: `git clone https://github.com/kkorlass/projekts-231RDB036.git`
2. Atver mapi project-231RDB036: `cd project-231RDB036`
3. Izveido venv: `python -m venv venv`
4. Aktivizē venv: `source venv/bin/activate`
5. Instalē nepieciešamās pakotnes: `pip install requests beautifulsoup4 pytz`

## Izmantošana
### Parastā instalācija
Sāc `scrape.py` skriptu ar noklusējuma ziņu vecumu (48h): `python scrape.py`.
Lai nomainītu ziņu vecumu pievieno stundu skaitu, kā argumentu, piemēram: `python scrape.py 16`.

Tipiska izvade:
```
Python 3.13 Alpha 3 Released - Work Continues On Dropping The GIL, Improving Performance  
https://phoronix.com/news/Python-3.13-Alpha-3  
  
RISC-V With Linux 6.8 Restores XIP Kernel Support  
https://phoronix.com/news/RISC-V-Linux-6.8  
  
Mesa 24.0-rc2 Released With This Quarter's Release Looking Good  
https://phoronix.com/news/Mesa-24.0-rc2-Released
```

Izvadi var izmantot skriptos, piemēram, uz Linux `python scrape.py | grep "Mesa"` izvadīs šo:
```
Mesa 24.0-rc2 Released With This Quarter's Release Looking Good  
https://phoronix.com/news/Mesa-24.0-rc2-Released
```

### Python venv instalācija
Aktivizē venv: `source venv/bin/activate`
Tālāk visi soļi ir identiski parastajai instalācijai.
