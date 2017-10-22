def testaVogal(letra):
    if letra in "aeiou":
        return True
    else:
        return False

def calculaMaior(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def testaMultiplo4(num):
    if num % 4 == 0:
        return True
    else:
        return False

def testaDivisor(x,y):
    if x%y == 0:
        return True
    else:
        return False
