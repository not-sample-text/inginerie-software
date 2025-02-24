def ex1():
  num = int(input("Introdu un numar: "))
  if num >= 0:
    print("Pozitiv")
  else:
    print("Negativ")

def ex2():
  suma = 0
  for i in range(1, 11):
    suma += i
  print(suma)

def ex3():
  num = int(input("Introdu un numar: "))
  if num < 2:
    print("Numarul nu este prim")
  else:
    for i in range(2, num):
      if num % i == 0:
        print("Numarul nu este prim")
        return
    print("Numarul este prim")

def ex4():
  for i in range(1, 21):
    if i % 2 == 0:
      print(i)

def ex5():
  for i in range(10, 31):
    if i % 2 != 0:
      print(i)

def ex6():
  n = int(input("Introdu numarul de elemente: "))
  suma = 0
  for i in range(n):
    suma += int(input("Introdu elementul: "))
  print(suma / n)

def ex7():
  sir = input("Introdu sirul: ")
  litera = input("Introdu litera: ")
  if litera in sir:
    print("Litera se afla in sir")
  else:
    print("Litera nu se afla in sir")

def ex8():
  sir = input("Introdu sirul: ")
  if sir == sir[::-1]:
    print("Sirul este palindrom")
  else:
    print("Sirul nu este palindrom")

def ex9():
  for i in range (1, 5100000):
    if i % 3 == 0 and i % 5 == 0:
      print(i)

if __name__ == "__main__":
  # print("call a function dumbass")
  ex9()

