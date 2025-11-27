# Elevguide: Hvordan bruke Markdown i README-filer

## Hva er Markdown?
Markdown er et **enkelt språk for å formatere tekst** — akkurat som i Word, men med **kode** i stedet for knapper.  
Det brukes til å lage dokumentasjon, spesielt i `README.md`-filer på GitHub og i programmeringsprosjekter.

Eksempel:
```markdown
# Mitt prosjekt
Dette er et prosjekt laget i Flask med MariaDB.
```

Vises som:

# Mitt prosjekt
Dette er et prosjekt laget i Flask med MariaDB.

---

## Grunnleggende oppsett
En `README.md`-fil ligger vanligvis i rotmappen til prosjektet ditt.  
Den bør forklare:
- Hva prosjektet handler om  
- Hvordan man installerer og kjører det  
- Hvem som har laget det  
- Eventuelle krav eller lisensinformasjon  

---

## De mest brukte Markdown-kodene

### 1. Overskrifter
Bruk `#` for overskrifter — jo flere `#`, jo mindre tittel.

```markdown
# Tittel 1
## Tittel 2
### Tittel 3
#### Tittel 4
```

### 2. Fet og kursiv tekst
```markdown
**Fet tekst**
*Kursiv tekst*
***Fet og kursiv***
```

Vises som:  
**Fet tekst**  
*Kursiv tekst*  
***Fet og kursiv***

---

### 3. Punktlister
```markdown
- Punkt 1
- Punkt 2
  - Underpunkt
```

Vises som:
- Punkt 1  
- Punkt 2  
  - Underpunkt  

### 4. Nummererte lister
```markdown
1. Første punkt
2. Andre punkt
3. Tredje punkt
```

Vises som:
1. Første punkt  
2. Andre punkt  
3. Tredje punkt  

---

### 5. Lenker og bilder
**Lenke:**
```markdown
[OpenAI](https://www.openai.com)
```

Vises som: [OpenAI](https://www.openai.com)

**Bilde:**
```markdown
![Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
```

Vises som:  
![Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

---

### 6. Kode og kodeblokker
**Kort kode (inline):**
```markdown
`print("Hei")`
```
Vises som: `print("Hei")`

**Kodeblokk:**
```markdown
```python
print("Hei verden")
```
```

Vises som:
```python
print("Hei verden")
```

---

### 7. Sitater
```markdown
> Dette er et sitat.
```

Vises som:
> Dette er et sitat.

---

### 8. Tabeller
```markdown
| Navn | Rolle | Poeng |
|------|--------|--------|
| Anders | Utvikler | 10 |
| Sara | Designer | 9 |
```

Vises som:

| Navn | Rolle | Poeng |
|------|--------|--------|
| Anders | Utvikler | 10 |
| Sara | Designer | 9 |

---

### 9. Skillelinje
```markdown
---
```

Vises som:

---

### 10. Avkrysningsbokser (to-do-lister)
```markdown
- [x] Laget database
- [ ] Ferdig med frontend
- [ ] Testet alt
```

Vises som:
- [x] Laget database  
- [ ] Ferdig med frontend  
- [ ] Testet alt  

---

## Tips til god README
Bruk **overskrifter** for struktur  
Bruk **kodeblokker** til kommandoer og kode  
Forklar kort hva prosjektet gjør  
Legg til **installasjonssteg**  
Bruk **bilder eller GIF-er** for å vise hvordan prosjektet ser ut  

---
!!!

## Draft README

```markdown
# Drone Database

### Denne databasen er basert på en scene fra en "indie" animasjonsserie (uavhengig animasjon) på youtube som heter MURDER DRONES. Jeg har tatt litt kreativ frihet ved å adaptere en database som kan vise kompetansen min med databaser.

Databasen holder 2 forskjellige tabeller. En tabell for "worker drones" som inneholder navn og status og en tabell for "disassembly drones". "Disassembly drones" har i tilegg også et tilfeldig serienummer hver. (Blir også gitt til nye "disassembly drones" som blir lagt til.)

Det er mulig å slette droner, legge til droner og redigere de via "view profile" knappen.
De får også en automatisk ID som ikke endrer seg. 

## Installasjon
1. Klon prosjektet:
   ```bash
   git clone https://github.com/SD-Shar/Prosjekt_uke.git
   ```
2. Installer krav:
   ```bash
   pip install flask

   ```

## Kjør prosjektet
```bash
python -m flask run
```
## (Se brukerveiledning med i mappen)


## Laget av
- Rebecca
```
#!!!

En `README.md`-fil ligger vanligvis i rotmappen til prosjektet ditt.  
Den bør forklare:
- Hva prosjektet handler om  
- Hvordan man installerer og kjører det  
- Hvem som har laget det  
- Eventuelle krav eller lisensinformasjon  



```markdown
# Sykkelverkstedet

Et webprosjekt laget i Flask og MariaDB som lar deg registrere og vise sykkelreparasjoner.

## Installasjon
1. Klon prosjektet:
   ```bash
   git clone https://github.com/brukernavn/sykkelverksted.git
   ```
2. Installer krav:
   ```bash
   pip install -r requirements.txt
   ```

## Kjør prosjektet
```bash
flask run
```


## Laget av
- Anders Ljung
- Sara Hansen
```