def pos_neg():
  num = int(input("Introdu un numar: "))
  if num >= 0:
    print("Pozitiv")
  else:
    print("Negativ")

def suma_1_10():
  suma = 0
  for i in range(1, 11):
    suma += i
  print(suma)

def prim():
  num = int(input("Introdu un numar: "))
  if num < 2:
    print("Numarul nu este prim")
  else:
    for i in range(2, num):
      if num % i == 0:
        print("Numarul nu este prim")
        return
    print("Numarul este prim")

def par_1_20():
  for i in range(1, 21):
    if i % 2 == 0:
      print(i)

def impar_10_30():
  for i in range(10, 31):
    if i % 2 != 0:
      print(i)

if __name__ == "__main__":
  print("call a function dumbass")

