# Repozitoriu Inginerie Software

Acest repo conține exerciții de programare preluate de pe site-ul [CTI - IS](http://cti.ubm.ro/is/) pentru diverse laboratoare.

## Structura Repo-ului

- **[.gitignore](.gitignore)** – Listează fișierele și folderele ce trebuie ignorate de Git.
- **[lab2.py](lab2.py)** – Exerciții de laborator 02 (exerciții de bază: input, condiții, bucle, etc.) preluate de la [CTI - IS lab02](http://cti.ubm.ro/is/#/IS/lab02).
- **[lab4.py](lab4.py)** – Exerciții de laborator 04 (liste, șiruri de caractere, manipulare de fișiere) de la [CTI - IS lab04](http://cti.ubm.ro/is/#/IS/lab04).
- **[lab6.py](lab6.py)** – Exerciții de laborator 06, folosind biblioteca NumPy (operații pe array-uri, matrice) conform cerințelor de la [CTI - IS lab06](http://cti.ubm.ro/is/#/IS/lab06).
- **[lab7.py](lab7.py)** – Exerciții de laborator 07 care acoperă programarea orientată pe obiect (clase, moștenire, metode) preluate de la [CTI - IS lab07](http://cti.ubm.ro/is/#/IS/lab07).
- **lab8/**
  - **[lab8.py](lab8/lab8.py)** – Conține exerciții de laborator 08 legate de prelucrarea fișierelor (CSV, JSON) și manipularea datelor privind studenții și profesorii.
  - **[materie.txt](lab8/materie.txt)** – Specifică materia de interes pentru filtrarea profesoarelor.
  - **[medie.txt](lab8/medie.txt)** – Conține valoarea medie de referință pentru studenți.
  - **[medii.json](lab8/medii.json)** – Fișierul de ieșire ce stochează mediile calculate ale studenților.
  - **[profesori.json](lab8/profesori.json)** – Stochează date despre profesori în format JSON.
  - **[studenti.csv](lab8/studenti.csv)** – Conține lista studenților și notele lor în format CSV.
- **[random-words.txt](random-words.txt)** – Fișier text ce conține o listă de cuvinte, folosit în exercițiile de laborator 04.
- **[requirements.txt](requirements.txt)** – Specifică dependențele proiectului (ex.: NumPy).

## Utilizare

Pentru a rula un laborator, de exemplu laboratorul 2, folosiți comanda:

```sh
python lab2.py
```
