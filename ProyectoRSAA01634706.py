#Hehco por Amilcar Ibarra Barreda
#A01634706
#Algoritmo de Euclid basado de https://scipython.com/book/chapter-2-the-core-python-language-i/examples/euclids-algorithm-for-finding-the-gcd-of-a-number/

import math

print("Programa RSA")
print("Introduce los valores de p y q")
p = int(input("Inserta valor de p (Tiene que ser primo)\n"))
q = int(input("Inserta valor de q (Tiene que ser primo)\n"))

def verificarPrimo(num, n=2):
    if n >= num:
        print("El valor primo")
        return True
    elif num % n != 0:
        return verificarPrimo(num, n + 1)
    else:
        print("El valor no es primo", n, "es divisor")
        return False


primop = verificarPrimo(p)
primoq = verificarPrimo(q)
while (((primop != True) or (primoq != True))):

    p = int(input("Inserta valor de p (Tiene que ser primo)\n"))
    q = int(input("Inserta valor de q (Tiene que ser primo)\n"))
    primop = verificarPrimo(p)
    primoq = verificarPrimo(q)
n = p * q
print("Valor de N", n)
r = (p - 1) * (q - 1)
print("Valor de Euler es  ", r) #Valor de Euler

#Calcular GCD
def calcularGCD(a, b):
    while b:
        a, b = b, a % b
    return a
#Ecuentra el mayor valor posible de 'e' entre 1 y 1000
for i in range(1, 1000):
    if (calcularGCD(i, r) == 1):
        a = i
print("El valor de a es de: ", a)

# Euclidiano Extendido
def euclidianoExtendido(a, b):
    if a == 0:
        return b, 0, 1

    euc, x1, y1 = euclidianoExtendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return euc, x, y

#multiplo inverso para conseguir d
def multiploin(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

d = multiploin(a, r)

#imprimir d, llaves publicas y privadas

def encryptar(llavep,texton ):
    e, n = llavep
    x = []
    m = 0
    for i in texton:
        if (i.isupper()):
            m = ord(i) - 65
            c = (m ** e) % n
            x.append(c)
        elif (i.islower()):
            m = ord(i) - 97
            c = (m ** e) % n
            x.append(c)
        elif (i.isspace()):
            spc = 400
            x.append(400)
    return x
def descryptar(llavep, textoc):
    d, n = llavep
    txt = textoc.split(' ') #Separar por espacios
    x = ''
    m = 0
    for i in txt:
        if (i == '400'):
            x += ' '
        else:
            m = (int(i) ** d) % n
            m += 65
            c = chr(m)
            x += c
    return x
print("El valor de d es:", d)
public = (a, n)
private = (d, n)
print("La llave privada es: ", private)
print("La llave publica es: ", public)
texto = input("Escribe el texto a encryptar o descryptar (Si es numero. Separa por espacios): \n")
escoge = input("Escribe 'e' para encryptar y 'd' para descryptar\n")
if (escoge == 'e'):
    enc_msg = encryptar(public, texto)
    print("Tu texto encryptado es: ", enc_msg)
elif (escoge == 'd'):
    print("Tu texto desencryptado es: ", descryptar(private, texto))
