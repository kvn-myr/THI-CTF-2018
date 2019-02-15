def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def num_to_str(num):
    res = ""
    while num > 0:
        res = chr(num % 256) + res
        num = num / 256
    return res

def main():

    p = 287707519340024534819672541734682755279
    q = 328652642654856331261136192361290324249
    e = 65537
    ct = 53880535074945013230435758976480263950284747331505425222992943706506535017211

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    #print( "pt: " + str(pt) )

    print(num_to_str(pt))

if __name__ == "__main__":
    main()
