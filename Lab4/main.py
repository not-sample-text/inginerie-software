import random
import math

# exercitii de la http://cti.ubm.ro/is/#/IS/lab04

with open("../random-words.txt", "r") as file:
  cuvinte = file.read().split("\n")

lista_cuvinte = random.sample(cuvinte, 10)

lista_numere = random.sample(range(100), 11)

def afiseaza_lista(lista):
  print("Lista:", ", ".join(map(str, lista)))

def ex1():
  # copy numbers list
  lista = lista_numere.copy()
  # print the list
  afiseaza_lista(lista)
  # sort the list
  list.sort(lista)
  # print the sorted list
  afiseaza_lista(lista)

def ex2():
  # copy word list
  lista = lista_cuvinte.copy()
  # reverse the list
  list.reverse(lista)
  # print the reversed list
  afiseaza_lista(lista)

def ex3():
  # copy numbers list and make it into a tuple
  tuplu = tuple(lista_numere.copy())
  # print the sum of the tuple
  print(sum(tuplu))

def ex4():
  # copy numbers list
  lista = lista_numere.copy()
  # take every element from the list
  for i in range(len(lista)):
    # if the element is even
    if lista[i] % 2 == 0:
      # multiply it by 2
      lista[i] = lista[i] * 2
  # print the modified list
  afiseaza_lista(lista)

def ex5():
  # copy word list
  lista = lista_cuvinte.copy()
  # ask the user for word
  cuvant = input("Introduceti un cuvant: ")
  # if the word is in the list
  if cuvant in lista:
    # print word is in list
    print("Cuvantul se gaseste in lista")
  else:
    # print word is not in list
    print("Cuvantul nu se gaseste in lista")

def ex6():
  # copy word list
  lista = lista_cuvinte.copy()
  # shuffle the list
  random.shuffle(lista)
  # sort the list in descending order
  lista.sort(reverse=True)
  # print the sorted list
  afiseaza_lista(lista)

def ex7():
  # copy numbers list
  lista = lista_numere.copy()
  # make the list only 5 elements long
  lista = lista[:5]
  # show max number
  print("Cel mai mare numar din lista este:", max(lista))
  # show min number
  print("Cel mai mic numar din lista este:", min(lista))

def ex8():
  # copy numbers list
  lista = lista_numere.copy()
  # make the list only numbers greater than 5
  lista = [i for i in lista if i >= 5]
  # print the modified list
  afiseaza_lista(lista)

def ex9():
  #copy numbers list
  lista = lista_numere.copy()
  # print the list
  afiseaza_lista(lista)
  #check if the list has duplicate elements
  if len(set(lista)) == len(lista):
    print("Lista nu contine elemente duplicate")
  else:
    print("Lista contine elemente duplicate")

def ex10():
  # copy numbers list and make it into a tuple
  tuplu = tuple(lista_numere.copy())
  # from tuple to list
  lista = list(tuplu)
  # print the list
  afiseaza_lista(lista)

def ex11():
  # copy words list
  lista = lista_cuvinte.copy()
  # concatenate the list so its one string
  sir = "".join(lista)
  # print the string
  print(sir)

def ex12():
  # copy numbers list
  lista = lista_numere.copy()
  # check if every element is prime
  if all(i >= 2 and all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)) for i in lista):
    print("Toate numerele sunt prime")
  else:
    print("Nu toate numerele sunt prime")

def ex13():
  # copy numbers list
  lista = lista_numere.copy()
  # square every number less than 10
  for i in range(len(lista)):
    if lista[i] < 10:
      lista[i] = lista[i] ** 2
  # print the modified list
  afiseaza_lista(lista)

def ex14():
  # copy numbers list and make into tuple
  tuplu = tuple(lista_numere.copy())
  # check if any two numbers have the same value
  if len(set(tuplu)) == len(tuplu):
    print("Nu exista doua numere cu aceeasi valoare")
  else:
    print("Exista doua numere cu aceeasi valoare")

def ex15():
  # copy numbers list
  lista = lista_numere.copy()
  # find second smallest number
  lista.remove(min(lista))
  print("Al doilea cel mai mic numar din lista este:", min(lista))

def ex16():
  # copy numbers list
  lista = lista_numere.copy()
  # check if list is palindrome
  if lista == lista[::-1]:
    print("Lista este palindrom")
  else:
    print("Lista nu este palindrom")

def ex17():
  # copy words list
  lista = lista_cuvinte.copy()
  # replace small letter words with big letter
  for i in range(len(lista)):
    lista[i] = lista[i].upper()
  # print the modified list
  afiseaza_lista(lista)

def ex18():
  # copy numbers list and make it into a tuple
  tuplu = tuple(lista_numere.copy())
  #check if already sorted
  if tuplu == tuple(sorted(tuplu)):
    print("Lista este in ordine crescatoare")
  else:
    print("Lista nu este in ordine crescatoare")

def ex19():
  # copy numbers list
  lista = lista_numere.copy()
  # find duplicate numbers
  duplicate = set([i for i in lista if lista.count(i) > 1])
  # print the duplicate numbers
  afiseaza_lista(duplicate)

def ex20():
  # copy words list
  lista = lista_cuvinte.copy()
  # find words longer than 5 characters
  lista = [i for i in lista if len(i) > 5]
  # print the modified list
  afiseaza_lista(lista)

def run_exercise():
    choice = input("Alege un exercitiu (1-20): ")
    func_name = "ex" + choice
    try:
        globals()[func_name]()
    except KeyError:
        print("Exercitiul nu exista!")

if __name__ == "__main__":
    run_exercise()
