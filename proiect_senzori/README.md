# Proiect Senzori

Acest proiect reprezintă o aplicație web dezvoltată folosind Flask, destinată afișării și analizării datelor de la senzori.

## Structura Proiectului

- **app.py** – Fișierul principal ce inițializează aplicația Flask și definește rutele.
- **requirements.txt** – Listă de dependențe necesare pentru rularea aplicației.
- **static/** – Directorul ce conține:
  - **css/** – Fișiere de stil (ex.: `index.css`, `graph.css`) pentru styling-ul paginilor.
  - **img/** – Imagini folosite în interfață.
  - **js/** – Scripturi JavaScript (dacă este cazul) pentru funcționalități suplimentare.
- **templates/** – Directorul cu șabloane HTML:
  - **index.html** – Pagina principală a aplicației.
  - **graph.html** – Șablonul pentru afișarea graficelor și statisticilor.

## Utilizare

1. Instalați dependențele specificate în `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```
2. Rulați aplicația utilizând:
   ```sh
   python app.py
   ```
3. Accesați aplicația prin browser la adresa indicată în consola de output (de obicei: [http://127.0.0.1:5000](http://127.0.0.1:5000)).

## Notă

Acest proiect este structurat pentru a facilita ulterior integrarea unor API-uri și generarea de grafice pe baza datelor senzoriale. Fișierele din directorul `static/` și `templates/` sunt organizate pentru a asigura o experiență vizuală clară și responsivă.

Bucurați-vă de dezvoltarea și testarea aplicației!
