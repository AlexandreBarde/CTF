encrypted_flag = "-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_"

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def f(a, b, n, x):
    return (a * x + b) % n

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def decrypt(encrypted, a, b, n):
    decrypted = ""
    a_inv = modinv(a, n)
    for char in encrypted:
        x = charset.index(char)
        x = (a_inv * (x - b)) % n
        decrypted += charset[x]
    return decrypted

# Essayez de toutes les combinaisons possibles de a et b pour obtenir le bon déchiffrement
for a_guess in range(2, len(charset)):
    for b_guess in range(1, len(charset)):
        decrypted_flag = decrypt(encrypted_flag, a_guess, b_guess, len(charset))
        if "CTF" in decrypted_flag:  # Vérifiez si le mot 'CTF' est dans le message déchiffré
            print("Found potential decryption with a = {}, b = {}: {}".format(a_guess, b_guess, decrypted_flag))
