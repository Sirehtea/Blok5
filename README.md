# Plagiaatdetectie

Een tool voor het detecteren van plagiaat tussen Python-bestanden door middel van syntactische analyse en tekstvergelijking.

## Functies

- Vergelijkt bestanden op basis van inhoud, opmerkingen en spelfouten.
- Verwijdert opmerkingen uit de code en vergelijkt de syntactische bomen.
- Genereert een matrix van plagiaatresultaten per auteur.
- Maakt een HTML-rapport met de resultaten.

## Installatie

1. **Clone deze repository**  
```bash
git clone https://github.com/Sirehtea/Plagiaatdetectie.git
cd plagiaatdetectie
```

2. **Installeer requirements**

```bash
pip install -r requirements.txt
```

3. **Start applicatie**

```bash
python.exe .\main.py
```

4. **Open je HTML pagina met de liver server**

## MapStructuur

```bash
plagiaatdetectie/
├───analysis_directory
│   ├───X
│      ├───...
│   ├───X2
│      ├───...
│── static/
│   ├── style.css
│── outputtemplate.html
│── plagiaatdetectie.py
│── requirements.txt
│── README.md
```
