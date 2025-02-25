import math

def ex1():
    num = float(input("Introdu un numar: "))
    if num >= 0:
        print("Pozitiv")
    else:
        print("Negativ")

def ex2():
    print(sum(range(10)))

def ex3():
    num = float(input("Introdu un numar: "))
    is_prime = num >= 2 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
    if is_prime:
        print("Numarul este prim")
    else:
        print("Numarul nu este prim")

def ex4():
    result = [str(i) for i in range(1, 21) if i % 2 == 0]
    print(" ".join(result))

def ex5():
    result = [str(i) for i in range(10, 31) if i % 2 != 0]
    print(" ".join(result))

def ex6():
    count = int(float(input("Introdu numarul de elemente: ")))
    numbers = [float(input(f"Introdu elementul {i+1}: ")) for i in range(count)]
    print(sum(numbers) / count)

def ex7():
    litera = input("Introdu litera: ")
    sir = input("Introdu sirul: ")
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
    result = [str(i) for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]
    print(" ".join(result))

def ex10():
    num = int(input("Introdu numarul: "))
    print(math.factorial(num))

def ex11():
    count = int(float(input("Introdu numarul: ")))
    for i in range(1, count + 1):
        print("*" * i)

def ex12():
    num = float(input("Introdu numarul: "))
    result = [f"{num} * {i} = {num * i}" for i in range(1, 11)]
    print(" | ".join(result))

def ex13():
    a, b = 0, 1
    fib = []
    for _ in range(10):
        fib.append(a)
        a, b = b, a + b
    print(" ".join(str(x) for x in fib))

def ex14():
    a = float(input("Introdu primul numar: "))
    b = float(input("Introdu al doilea numar: "))
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    print(gcd(a, b))

def ex15():
    num = float(input("Introdu numarul: "))
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")

def ex16():
    temp_c = float(input("Introdu temperatura: "))
    fahrenheit = temp_c * 9 / 5 + 32
    print(f"Temperatura in Fahrenheit: {fahrenheit}")

def ex17():
    num = float(input("Introdu numarul: "))
    print(math.sqrt(num))

def ex18():
    num = float(input("Introdu numarul: "))
    print(math.pi * num ** 2)

def ex19():
    propozitie = input("Introdu propozitia: ")
    count = len(propozitie.split())
    print(f"{count} cuvinte")

def ex20():
    sir = input("Introdu sirul: ")
    print(sir[::-1])

def ex21():
    num1 = float(input("Introdu primul numar: "))
    num2 = float(input("Introdu al doilea numar: "))
    print(max(num1, num2))

def ex22():
    num = float(input("Introdu numarul: "))
    if num % 5 == 0:
        print("Da")
    else:
        print("Nu")

def ex23():
    text = input("Introdu un șir de caractere: ")
    print(text.encode())

def ex24():
    byte_str = input("Introdu bytes: ")
    print(bytes(byte_str, 'utf-8').decode())

def ex25():
    num1 = int(input("Primul număr: "))
    num2 = int(input("Al doilea număr: "))
    print(num1 + num2)

def ex26():
    num1 = float(input("Primul număr: "))
    num2 = float(input("Al doilea număr: "))
    print(num1 * num2)

def ex27():
    num = int(input("Introdu un număr întreg: "))
    if num > 0:
        print("Pozitiv")
    else:
        print("Negativ")

def ex28():
    num = float(input("Introdu un număr real: "))
    if num != 0:
        print("Nenul")
    else:
        print("Nul")

def ex29():
    sir = input("Introdu un șir de caractere: ")
    if sir == sir[::-1]:
        print("Este palindrom")
    else:
        print("Nu este palindrom")

def ex30():
    sir = input("Introdu un șir: ")
    print(f"Primul: {sir[0]}, Ultimul: {sir[-1]}")

def ex31():
    n = int(input("Introdu n: "))
    result = ''.join([chr(ord('a') + i) for i in range(n)])
    print(result)

def ex32():
    sir = input("Introdu un șir: ")
    if sir.isalpha():
        print("Conține doar litere")
    else:
        print("Nu conține doar litere")

def ex33():
    sir = input("Introdu un șir: ")
    print(''.join(sir.split()))

def ex34():
    sir = input("Introdu un șir: ")
    print(sir[::-1])

def ex35():
    n = int(input("Introdu un număr: "))
    if n % 3 == 0 or n % 5 == 0:
        print("Divizibil")
    else:
        print("Nu este divizibil")

def ex36():
    subsir = input("Introdu subșirul: ")
    sir = input("Introdu șirul: ")
    if subsir in sir:
        print("Conține subșirul")
    else:
        print("Nu conține subșirul")

def ex37():
    sir = input("Introdu un șir: ")
    result = [sir[i] for i in range(len(sir)) if i % 2 == 0]
    print(''.join(result))

def ex38():
    count = int(input("Câte numere? "))
    numbers = [int(input(f"Numărul {i+1}: ")) for i in range(count)]
    repeat_count = int(input("Repetă, câte numere? "))
    print(sum(numbers) / repeat_count)

def ex39():
    num1 = int(input("Primul număr: "))
    num2 = int(input("Al doilea număr: "))
    num3 = int(input("Al treilea număr: "))
    print(max(num1, num2, num3))

def ex40():
    n = int(input("Introdu n: "))
    result = [str(i) for i in range(1, n + 1)]
    print(','.join(result))

def run_exercise():
    choice = input("Alege un exercitiu (1-40): ")
    func_name = "ex" + choice
    try:
        globals()[func_name]()
    except KeyError:
        print("Exercitiul nu exista!")

if __name__ == "__main__":
    run_exercise()
