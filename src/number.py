"""
Source: https://github.com/Bl4omArchie/Pubcrypt/blob/main/pubcrypt/number/util.py
"""

def invmod(z, a):
    """Théorème de bezout"""
    if not z < a:
        z, a = a, z

    i, j = a, z
    y1, y2 = 1, 0

    while j > 0:
        q = i // j
        r = i - (j * q)
        y = y2 - (y1 * q)
        i, j = j, r
        y2, y1 = y1, y

    return y2 % a


def PGCD(x, y):
    """Plus grand diviseur commun version binaire"""
    if x == 0:
        return y
    if y == 0:
        return x

    x_z = (x & -x).bit_length()-1
    y_z = (y & -y).bit_length()-1
    shift = min(x_z, y_z)
    y_z >>= y_z

    while x != 0:
        x >>= x_z
        diff = y-x
        x_z = (diff & -diff).bit_length()-1
        y = min(x, y)
        x = abs(diff)

    return y << shift
    

def fast_exp(b, e, m=None):
    """Exponentiation rapide: a**b et a**b%m version binaire. Le modulo n'est pas obligatoire"""
    result = 1
    while e > 0:
        if e & 1:
            result *= b
            if m:
                result %= m
        b *= b
        if m:
            b %= m
        e >>= 1

        if b == 0 and m:
            b = 1  
        if m == 0:
            m = 1 
    if m:
        result %= m
    return result


def int_to_bin(n, iter="big"):
    """Conversion entier en binaire"""
    result = ""
    
    while n > 0:
        bit = n & 1  # Obtient le bit le plus à droite de n
        result += str(bit)
        n = n >> 1   # Décalage de n vers la droite d'une position (équivalent à n // 2)

        bit = n & 1  # Obtient le bit le plus à droite de n
        result += str(bit)
        n = n >> 1   # Décalage de n vers la droite d'une position (équivalent à n // 2)

    if iter == "little":
        return result[::-1][::-1]
    else:
        return result[::-1]