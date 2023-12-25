from src.kifli import *

def test_chiffrement_dechiffrement(message, n):
    # Chiffre et déchiffre un message et vérifie que le message déchiffré est bien égal au message initial
    cle_privee = gen_cle_privee(n)
    cle_publique = gen_cle_publique(cle_privee)
    print("cle privée : " + str(cle_privee[0]))
    print("")
    print("cle publique : " + str(cle_publique))
    print("")
    print("message à encoder : " + message)
    message_chiffre = chiffre(message, cle_publique)
    print("message encodé :    " + str(message_chiffre))
    message_dechiffre = dechiffre(message_chiffre, cle_privee)
    print("message décodé :    " + message_dechiffre)
    assert(message == message_dechiffre)

def exemple():
    # Compare les résultats des fonctions aux résultats de l'exemple
    P = [2, 5, 11, 23, 55]
    M = 113
    W = 27
    SIGMA = [1, 4, 2, 0, 3]
    A = [22, 16, 71, 54, 56]
    message = "10101"
    C = 149
    D = 39
    assert(A == gen_cle_publique((P, M, W, SIGMA)))
    assert(C == chiffre(message, A)) 
    assert [23, 11, 5] == solve_pochon(P, D)
    assert (message == dechiffre(C, (P, M, W, SIGMA)))
    
if __name__ == "__main__":
    exemple()
    test_chiffrement_dechiffrement("10100000000000000000000000000000000000000000000000", 50)