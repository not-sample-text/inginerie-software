import csv
import json

# 1
class Student:
    def __init__(self, nume, prenume, note):
        self.nume = nume
        self.prenume = prenume
        self.note = note

    # 2
    @staticmethod
    def citeste_din_csv():
        studenti = []
        with open('studenti.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                studenti.append(Student(row[0], row[1], row[2]))
        return studenti

    # 3
    @staticmethod
    def scrie_in_csv(studenti):
        with open('studenti.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for student in studenti:
                writer.writerow([student.nume, student.prenume, student.note])

    # 4
    @staticmethod
    def medie_in_json(studenti):
        medii = []
        for student in studenti:
            note_list = list(map(float, student.note.split()))
            media = sum(note_list) / len(note_list)
            medii.append({f"{student.nume} {student.prenume}": media})
        # Write averages to a JSON file
        with open('medii.json', 'w') as file:
            json.dump(medii, file)
        return medii

    # 5
    @staticmethod
    def studenti_peste_medie():
        with open('medie.txt', 'r') as f:
            threshold = float(f.read().strip())
        studenti = Student.citeste_din_csv()
        for student in studenti:
            note_list = list(map(float, student.note.split()))
            media = sum(note_list) / len(note_list)
            if media > threshold:
                print(f"{student.nume} {student.prenume}: {media}")


# 6
class Profesor:
    def __init__(self, nume, prenume, materie):
        self.nume = nume
        self.prenume = prenume
        self.materie = materie

    @staticmethod
    def salveaza_profesori_in_json(profesori):
        with open('profesori.json', 'w') as file:
            json.dump(profesori, file)

    # 7
    @staticmethod
    def citeste_profesori_din_json():
        with open('profesori.json', 'r') as file:
            return json.load(file)

    # 8
    @staticmethod
    def adauga_profesor_in_json(profesor):
        profesori = Profesor.citeste_profesori_din_json()
        profesori.append(profesor)
        Profesor.salveaza_profesori_in_json(profesori)

    # 9
    @staticmethod
    def profesori_din_materie():
        with open('materie.txt', 'r') as f:
            materie_cautata = f.read().strip().lower()
        profesori = Profesor.citeste_profesori_din_json()
        for profesor in profesori:
            if profesor.get('materie', '') == materie_cautata:
                print(f"{profesor.get('nume', '')} {profesor.get('prenume', '')} - {profesor.get('materie', '')}")


# 10
class Catalog:
    def __init__(self, studenti, profesori):
        self.studenti = studenti
        self.profesori = profesori

    def salveaza_in_csv(self):
        Student.scrie_in_csv(self.studenti)
        Profesor.salveaza_profesori_in_json(self.profesori)

    def incarca_din_csv(self):
        self.studenti = Student.citeste_din_csv()
        self.profesori = Profesor.citeste_profesori_din_json()

if __name__ == '__main__':
    studenti = [Student('Popescu', 'Ion', '10 9 8 7 6'), Student('Ionescu', 'Maria', '9 8 7 6 5')]
    profesori = [{'nume': 'Popescu', 'prenume': 'Ion', 'materie': 'Matematica'},
                 {'nume': 'Ionescu', 'prenume': 'Maria', 'materie': 'Informatica'}]
    catalog = Catalog(studenti, profesori)
    catalog.salveaza_in_csv()
    catalog.incarca_din_csv()
    Student.medie_in_json(catalog.studenti)
    Student.studenti_peste_medie()
    Profesor.profesori_din_materie()
    Profesor.adauga_profesor_in_json({'nume': 'Georgescu', 'prenume': 'Andrei', 'materie': 'Fizica'})
    Profesor.profesori_din_materie()
