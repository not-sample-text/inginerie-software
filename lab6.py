import numpy as np

# exercitii de la http://cti.ubm.ro/is/#/IS/lab06

def ex1():
  # a
  fructe = ("mere", "pere", "prune", "banane", "cirese")
  print(", ".join(fructe[0:5]))
  
  # b
  preturi = (10, 20, 30, 40, 50)
  print(preturi[fructe.index("mere"):fructe.index("cirese")+1])
  
  # c
  desert = (fructe[-2:])
  print(", ".join(desert))
  
def ex2():
  # a
  note = {"Ionescu": 9, "Popescu": 8, "Georgescu": 10}
  
  # b
  nume_studenti = note.keys()
  print(*nume_studenti)
  
  # c
  for nume, nota in note.items():
    print(nume, "are nota", nota)

def ex3():
  # a
  set1 = {1, 2, 3, 4, 5}
  set2 = {4, 5, 6, 7, 8}
  print("Set1: ", set1)
  print("Set2: ", set2)
  
  # b
  print("Reuniunea: ", set1.union(set2))
  
  # c
  print("Intersectia: ", set1.intersection(set2))
  
  # d
  print("Diferenta: ", set1.difference(set2))

def ex4():
  # a
  arr1 = np.array([range(1, 11)])
  
  # b
  arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  
  # c
  print(arr2.shape)
  
  # d
  arr1_reshape = arr1.reshape(2, 5)
  print(arr1_reshape)
  
  # e
  arr3 = np.random.rand(4, 4)
  
  # f
  arr_3x3_1 = np.random.randint(10, size=(3, 3))
  arr_3x3_2 = np.random.randint(10, size=(3, 3))
  produs = np.dot(arr_3x3_1, arr_3x3_2)
  print(produs)
  
  # g
  arr_5x5 = np.random.randint(-10, 11, size=(5, 5))
  print("Val. max = ", np.max(arr_5x5))
  print("Val. min = ", np.min(arr_5x5))
  
  # h
  arr_det = arr2
  print(arr_det)
  print("Det. matricii = ", np.linalg.det(arr_det))
def run_exercise():
    choice = input("Alege un exercitiu (1-4): ")
    func_name = "ex" + choice
    try:
      globals()[func_name]()
    except KeyError:
      print("Exercitiul nu exista!")

if __name__ == "__main__":
    run_exercise()
