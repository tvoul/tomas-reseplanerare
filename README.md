# Tomas Reseplanerare

## Innehåll
* app - innehåller appen (backend + frontend + html + css)
* examples innehåller script.py - kod för att skriva ut svar från api-anrop i terminal eller spara ner till fil
* requirements.txt - beroenden för app
* Dockerfile - bygg en container
* .gitignore - ignorerar filer som inte ska sparas i Git

## Hint
### Kör igång applikationen
* pip install -r requirements.txt
* py app/frontend.py (obs, kan variera beroende på hur python anropas - t ex: py, python3, py3)

### Bygg och starta en container
* docker build -t tomas-reseplanerare . 
* docker run -p 5001:5001 tomas-reseplanerare
