import random
from abc import ABC, abstractmethod
import cmath
# exercitii de la http://cti.ubm.ro/is/#/IS/lab07

def ex1():
  # define bank account class
  class ContBancar:
    # constructor with account number and balance
    def __init__(self, numar_cont, sold):
      # private account number
      self.__numar_cont = numar_cont
      # private balance
      self.__sold = sold

    # string representation method
    def __str__(self):
      # return formatted account info
      return f"Cont {self.__numar_cont} are soldul {self.__sold}"

    # deposit method
    def depune(self, suma):
      # add amount to balance
      self.__sold += suma

    # withdraw method
    def retrage(self, suma):
      # check if enough funds
      if suma > self.__sold:
        # show error message
        print("Fonduri insuficiente!")
        # exit function
        return
      # subtract amount from balance
      self.__sold -= suma

  # generate random account number
  numar_cont = random.randint(10000, 99999)
  # generate random initial balance
  sold = random.randint(0, 1000)
  # create account object
  cont1 = ContBancar(numar_cont, sold)
  # display created account
  print("Cont creat:", cont1)
  # get user input for account number
  user_input = input("Introdu numarul de cont: ")
  # try to convert input to integer
  try:
    # convert to integer
    user_num = int(user_input)
  # handle conversion error
  except ValueError:
    # show error message
    print("Numar invalid!")
    # exit program
    return
  # check if account number matches
  if user_num == numar_cont:
    # get operation type
    optiune = input("Alege: depune sau retrage : ").strip().lower()
    # handle deposit option
    if optiune == "depune":
      # get deposit amount
      suma_input = input("Introdu suma de depus: ")
      # try to convert input to float
      try:
        # convert to float
        suma = float(suma_input)
      # handle conversion error
      except ValueError:
        # show error message
        print("Suma invalida!")
        # exit program
        return
      # call deposit method
      cont1.depune(suma)
      # show updated account
      print("Dupa depunere, contul este:", cont1)
    # handle withdraw option
    elif optiune == "retrage":
      # get withdrawal amount
      suma_input = input("Introdu suma de retras: ")
      # try to convert input to float
      try:
        # convert to float
        suma = float(suma_input)
      # handle conversion error
      except ValueError:
        # show error message
        print("Suma invalida!")
        # exit program
        return
      # call withdraw method
      cont1.retrage(suma)
      # show updated account
      print("Dupa retragere, contul este:", cont1)
      # handle invalid option
    else:
      # show error message
      print("Optiune invalida!")
  # handle incorrect account number
  else:
    # show error message
    print("Numar de cont incorect!")

def ex2():
  class Aeronava(ABC):
    def __init__(self, tip_incarcatura, capacitate):
      self.tip_incarcatura = tip_incarcatura
      self.capacitate = capacitate

  class AeronavaPasageri(Aeronava):
    def __init__(self, tip_incarcatura, capacitate):
      super().__init__(tip_incarcatura, capacitate)

    def descrie(self):
      return (f"Aeronava de pasageri cu incarcatura {self.tip_incarcatura}, "
              f"capacitate {self.capacitate} locuri, ")

  class AeronavaMarfa(Aeronava):
    def __init__(self, tip_incarcatura, capacitate):
      super().__init__(tip_incarcatura, capacitate)

    def descrie(self):
      return (f"Aeronava de marfa cu incarcatura {self.tip_incarcatura}, "
              f"capacitate ce poate fi de {self.capacitate} unitati")
      
def ex3():
  class Vehicul:
    def viteza_maxima(self):
      print("Viteza maximă generică pentru vehicul.")

  class Masina(Vehicul):
    def viteza_maxima(self):
      print("Masina poate atinge 240 km/h.")

  class Bicicleta(Vehicul):
    def viteza_maxima(self):
      print("Bicicleta poate atinge 35 km/h.")

  # Creare listă de obiecte de tip Vehicul
  vehicule = [Masina(), Bicicleta(), Vehicul()]

  # Iterare prin listă și apelarea metodei viteza_maxima
  for vehicul in vehicule:
    vehicul.viteza_maxima()

def ex4():
  class Persoana:
    def __init__(self, nume, varsta):
      self.nume = nume
      self.varsta = varsta

    def saluta(self):
      print(f"Salut, ma numesc {self.nume}!")

    def spune_varsta(self):
      print(f"Am {self.varsta} ani.")

  # Creăm câteva instanțe și apelăm metodele
  persoana1 = Persoana("Ana", 30)
  persoana2 = Persoana("Mihai", 25)

  persoana1.saluta()
  persoana1.spune_varsta()

  persoana2.saluta()
  persoana2.spune_varsta()

def ex5():
  class Angajat:
    def __init__(self, nume, salariu, data_angajarii):
      self.nume = nume
      self.__salariu = salariu
      self.data_angajarii = data_angajarii

    def calculare_bonus(self):
      # Calculăm bonusul ca 10% din salariu
      return self.__salariu * 0.10

  # Exemplu de utilizare:
  angajat = Angajat("Ion Popescu", 3000, "2020-01-01")
  print("Bonusul angajatului este:", angajat.calculare_bonus())

def ex6():
  class Tranzistor:
    def __init__(self, tip, configuratie, coeficient_amplificare):
      self.__tip = tip
      self.__configuratie = configuratie
      self.__coeficient_amplificare = coeficient_amplificare

    def set_tip(self, tip):
      self.__tip = tip

    def set_configuratie(self, configuratie):
      self.__configuratie = configuratie

    def set_coeficient_amplificare(self, coeficient):
      self.__coeficient_amplificare = coeficient

    def get_tip(self):
      return self.__tip

    def get_configuratie(self):
      return self.__configuratie

    def get_coeficient_amplificare(self):
      return self.__coeficient_amplificare

    def afiseaza(self):
      print("Tranzistor:")
      print("  Tip:", self.__tip)
      print("  Configuratie:", self.__configuratie)
      print("  Coeficient amplificare:", self.__coeficient_amplificare)


  class ProiectCircuit:
    def __init__(self):
      self.__componente = []

    def adauga_componenta(self, componenta):
      self.__componente.append(componenta)

    def afiseaza_componente(self):
      if not self.__componente:
        print("Nu sunt componente adaugate in circuit.")
      else:
        print("Componenta in circuit:")
        for idx, comp in enumerate(self.__componente, 1):
          print(f"Componenta {idx}:")
          comp.afiseaza()


  # Exemplu de utilizare:
  tranzistor1 = Tranzistor("NPN", "comun", 100)
  tranzistor2 = Tranzistor("PNP", "alta configuratie", 150)

  circuit = ProiectCircuit()
  circuit.adauga_componenta(tranzistor1)
  circuit.adauga_componenta(tranzistor2)

  print("Detalii componente circuit:")
  circuit.afiseaza_componente()

def ex7():
  class ComponentaElectronica(ABC):
    @abstractmethod
    def calcul_valoare(self):
      pass

  class Rezistor(ComponentaElectronica):
    def __init__(self, rezistenta):
      self.rezistenta = rezistenta
      
    def calcul_valoare(self):
      # Impedanta unui rezistor este pur si simplu rezistenta (valoare reala)
      return self.rezistenta

  class Condensator(ComponentaElectronica):
    def __init__(self, capacitate, frecventa):
      self.capacitate = capacitate  # in Farazi
      self.frecventa = frecventa    # in Hertz
      
    def calcul_valoare(self):
      # Impedanta condensatorului: Z = -j/(ωC)
      omega = 2 * 3.141592653589793 * self.frecventa
      if omega * self.capacitate == 0:
        return float('inf')
      return -1j / (omega * self.capacitate)

  class Bobina(ComponentaElectronica):
    def __init__(self, inductanta, frecventa):
      self.inductanta = inductanta  # in Henry
      self.frecventa = frecventa    # in Hertz
      
    def calcul_valoare(self):
      # Impedanta bobinei: Z = jωL
      omega = 2 * 3.141592653589793 * self.frecventa
      return 1j * omega * self.inductanta

  class CircuitRLCSerie:
    def __init__(self):
      self.componente = []
      
    def adauga_componenta(self, componenta: ComponentaElectronica):
      self.componente.append(componenta)
      
    def elimina_componenta(self, componenta: ComponentaElectronica):
      if componenta in self.componente:
        self.componente.remove(componenta)
    
    def calcul_impedanta_totala(self):
      impedanta_totala = 0 + 0j
      for comp in self.componente:
        impedanta_totala += comp.calcul_valoare()
      return impedanta_totala

  # Exemplu de utilizare:
  rezistor = Rezistor(100)                     # 100 Ohmi
  condensator = Condensator(10e-6, 50)          # 10 microfarazi la 50 Hz
  bobina = Bobina(0.1, 50)                      # 0.1 Henry la 50 Hz

  circuit = CircuitRLCSerie()
  circuit.adauga_componenta(rezistor)
  circuit.adauga_componenta(condensator)
  circuit.adauga_componenta(bobina)

  print("Impedanta totala a circuitului:", circuit.calcul_impedanta_totala())

def run_exercise():
  choice = input("Alege un exercitiu (1-4): ")
  func_name = "ex" + choice
  try:
    globals()[func_name]()
  except KeyError:
    print("Exercitiul nu exista!")

if __name__ == "__main__":
  run_exercise()
