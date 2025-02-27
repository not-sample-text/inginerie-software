import csv
import json

class Student:
  def __init__(self, nume, prenume, note):
    self.nume = nume
    self.prenume = prenume
    self.note = note  # a list of note (float)

  def average(self):
    if self.note:
      return sum(self.note) / len(self.note)
    return 0

  @staticmethod
  def save_students_to_csv(students, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow(["nume", "prenume", "note"])
      for stud in students:
        # convert list of notes to semicolon-separated string
        notes_str = ";".join(str(n) for n in stud.note)
        writer.writerow([stud.nume, stud.prenume, notes_str])

  @staticmethod
  def read_students_from_csv(filename):
    students = []
    with open(filename, mode='r', newline='', encoding='utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
        # notes are stored as semicolon-separated string, convert them to float list
        notes = [float(n) for n in row["note"].split(";") if n]
        students.append(Student(row["nume"], row["prenume"], notes))
    return students

  @staticmethod
  def add_student_to_csv(student, filename):
    # If the file does not exist, write header first.
    try:
      with open(filename, mode='r', newline='', encoding='utf-8') as f:
        pass
    except FileNotFoundError:
      with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["nume", "prenume", "note"])
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
      writer = csv.writer(f)
      notes_str = ";".join(str(n) for n in student.note)
      writer.writerow([student.nume, student.prenume, notes_str])

  @staticmethod
  def calculate_and_save_averages_to_json(students, json_filename):
    averages = []
    for stud in students:
      averages.append({
        "nume": stud.nume,
        "prenume": stud.prenume,
        "media": stud.average()
      })
    with open(json_filename, mode='w', encoding='utf-8') as f:
      json.dump(averages, f, ensure_ascii=False, indent=4)

  @staticmethod
  def display_students_above_average(threshold_filename, students):
    # Se asteapta ca fisierul sa contina o singura valoare numerica (pragul)
    try:
      with open(threshold_filename, mode='r', encoding='utf-8') as f:
        threshold_str = f.read().strip()
        threshold = float(threshold_str)
    except Exception as e:
      print("Eroare la citirea pragului:", e)
      return

    print(f"Studenti cu media notelor peste {threshold}:")
    for stud in students:
      if stud.average() > threshold:
        print(f"{stud.nume} {stud.prenume} - Media: {stud.average():.2f}")


class Profesor:
  def __init__(self, nume, prenume, materie):
    self.nume = nume
    self.prenume = prenume
    self.materie = materie

  @staticmethod
  def save_profesori_to_json(profesori, filename):
    data = []
    for prof in profesori:
      data.append({
        "nume": prof.nume,
        "prenume": prof.prenume,
        "materie": prof.materie
      })
    with open(filename, mode='w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

  @staticmethod
  def read_profesori_from_json(filename):
    profesori = []
    try:
      with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
          profesori.append(Profesor(item["nume"], item["prenume"], item["materie"]))
    except FileNotFoundError:
      pass
    return profesori

  @staticmethod
  def add_profesor_to_json(profesor, filename):
    profesori = Profesor.read_profesori_from_json(filename)
    profesori.append(profesor)
    Profesor.save_profesori_to_json(profesori, filename)

  @staticmethod
  def display_profesori_by_materie(threshold_filename, profesori):
    # Citim materia dintr-un fisier text (se presupune o singura linie cu materia)
    try:
      with open(threshold_filename, mode='r', encoding='utf-8') as f:
        materie_cautata = f.read().strip()
    except Exception as e:
      print("Eroare la citirea materiei:", e)
      return

    print(f"Profesori care predau {materie_cautata}:")
    for prof in profesori:
      if prof.materie.lower() == materie_cautata.lower():
        print(f"{prof.nume} {prof.prenume}")


  @staticmethod
  def save_profesori_to_csv(profesori, filename):
    # Opțional: salvare în format CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow(["nume", "prenume", "materie"])
      for prof in profesori:
        writer.writerow([prof.nume, prof.prenume, prof.materie])

  @staticmethod
  def read_profesori_from_csv(filename):
    profesori = []
    with open(filename, mode='r', newline='', encoding='utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
        profesori.append(Profesor(row["nume"], row["prenume"], row["materie"]))
    return profesori


class Catalog:
  def __init__(self):
    self.students = []
    self.profesori = []

  def save_to_csv(self, student_csv, profesor_csv):
    Student.save_students_to_csv(self.students, student_csv)
    Profesor.save_profesori_to_csv(self.profesori, profesor_csv)

  def load_from_csv(self, student_csv, profesor_csv):
    try:
      self.students = Student.read_students_from_csv(student_csv)
    except FileNotFoundError:
      self.students = []
    try:
      self.profesori = Profesor.read_profesori_from_csv(profesor_csv)
    except FileNotFoundError:
      self.profesori = []

  def save_to_json(self, json_filename):
    data = {
      "students": [
        {
          "nume": stud.nume,
          "prenume": stud.prenume,
          "note": stud.note
        }
        for stud in self.students
      ],
      "profesori": [
        {
          "nume": prof.nume,
          "prenume": prof.prenume,
          "materie": prof.materie
        }
        for prof in self.profesori
      ]
    }
    with open(json_filename, mode='w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

  def load_from_json(self, json_filename):
    try:
      with open(json_filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        self.students = [Student(item["nume"], item["prenume"], item["note"]) for item in data.get("students", [])]
        self.profesori = [Profesor(item["nume"], item["prenume"], item["materie"]) for item in data.get("profesori", [])]
    except FileNotFoundError:
      self.students = []
      self.profesori = []


# Exemplu de utilizare:
if __name__ == "__main__":
  # Studenți exemplu
  s1 = Student("Popescu", "Ion", [8, 9, 10])
  s2 = Student("Ionescu", "Ana", [7, 6, 8])
  students = [s1, s2]
  Student.save_students_to_csv(students, "studenti.csv")
  # Adăugare student
  s3 = Student("Georgescu", "Elena", [10, 9, 9])
  Student.add_student_to_csv(s3, "studenti.csv")
  # Calcul și salvare medii
  all_students = Student.read_students_from_csv("studenti.csv")
  Student.calculate_and_save_averages_to_json(all_students, "medii.json")
  # Afișare studenți peste o anumită medie (valoare citită din fisier text "prag.txt")
  Student.display_students_above_average("prag.txt", all_students)

  # Profesori exemplu
  p1 = Profesor("Marinescu", "Vasile", "Matematică")
  p2 = Profesor("Dumitrescu", "Maria", "Informatică")
  profesori = [p1, p2]
  Profesor.save_profesori_to_json(profesori, "profesori.json")
  # Adăugare profesor
  p3 = Profesor("Stanciu", "Mircea", "Informatică")
  Profesor.add_profesor_to_json(p3, "profesori.json")
  all_profesori = Profesor.read_profesori_from_json("profesori.json")
  Profesor.display_profesori_by_materie("materie.txt", all_profesori)

  # Utilizarea Catalogului
  catalog = Catalog()
  catalog.students = all_students
  catalog.profesori = all_profesori
  catalog.save_to_csv("catalog_studenti.csv", "catalog_profesori.csv")
  catalog.save_to_json("catalog.json")
  # Pentru a încărca din fișiere:
  new_catalog = Catalog()
  new_catalog.load_from_csv("catalog_studenti.csv", "catalog_profesori.csv")
  print("Catalogul încărcat din CSV:")
  for stud in new_catalog.students:
    print(f"{stud.nume} {stud.prenume}")
  new_catalog.load_from_json("catalog.json")
  print("Catalogul încărcat din JSON:")
  for prof in new_catalog.profesori:
    print(f"{prof.nume} {prof.prenume}")
