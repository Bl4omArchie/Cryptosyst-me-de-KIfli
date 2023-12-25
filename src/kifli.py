from src.number import *
import random

def gen_pochon(n): 
    # Génère un pochon de taille n
    # Initialisation des variables
    P = []
    sommeP = 0

    # Premiere itération
    p1 = random.randint(0, 1000)
    sommeP += p1
    P.append(p1)

    # Autres itérations
    for _ in range(n-1):
        pX = random.randint(sommeP, sommeP*10)
        sommeP += pX
        P.append(pX)

    # On return le pochon et la somme de ses valeurs
    return P, sommeP

def gen_cle_privee(n):
    # On prend notre pochon
    P, sommeP = gen_pochon(n)
    M = random.randint(sommeP+1, sommeP*10)
    W = random.randint(1, M-1)
    while (PGCD(W, M) != 1):
        W = random.randint(1, M-1)
    SIGMA = [i for i in range(n)]
    random.shuffle(SIGMA)
    return (P, M, W, SIGMA)

def gen_cle_publique(cle_privee):
    # Génère la clé publique à partir de la clé privée
    a = []
    P = cle_privee[0]
    M = cle_privee[1]
    W = cle_privee[2]
    SIGMA = cle_privee[3]
    for i in range(len(P)):
        a.append((P[SIGMA[i]]*W)%M)
    return a

def solve_pochon(pochon, c):
    # Résout un problème de pochon
    e = []
    index = len(pochon) - 1

    while c > 0 and index >= 0:
        if pochon[index] <= c:
            c -= pochon[index]
            e.append(pochon[index])
        index -= 1
    
    assert(c == 0)
    return e

def chiffre(message, cle_publique):
    # Chiffre un message
    assert(len(message) == len(cle_publique))
    c = 0
    for i in range(len(message)):
        c += int(message[i]) * cle_publique[i]
    return c

def dechiffre(message_chiffre, cle_privee):
    # Déchiffre un message
    message = ""
    P = cle_privee[0]
    M = cle_privee[1]
    W = cle_privee[2]
    SIGMA = cle_privee[3]
    D = (invmod(W, M) * message_chiffre) % M
    e = solve_pochon(P, D)
    for i in range(len(P)):
        if P[SIGMA[i]] in e:
            message = message + "1"
        else:
            message = message + "0"
    return message
