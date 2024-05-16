# secret_data
secret_data_hex = "685f6683a487f0d1b6c1bcc55cddbebd56c954c9d4a950cfd0a5ce4bc8bd44bd"

# Fonction pour inverser la transformation du caractère
# La fonction ord(char) renvoie le code ASCII du caractère char,
# puis ord(char) + index ajoute l'index au code ASCII. 
# Ensuite, (ord(char) + index) // 2 divise cette somme par 2, 
# arrondissant le résultat à l'entier inférieur, et chr() convertit ce nombre en un caractère ASCII.
def reverse_transform(char, index):
    return chr((ord(char) + index) // 2)

# Fonction pour reconstruire le mot de passe
# 
def reconstruct_password():
    
    reconstructed_password = ""
    
    for i in range(len(secret_data_hex) // 2):
        # Convertir le caractère hexadécimal en caractère ASCII
        hex_char = secret_data_hex[i * 2: (i + 1) * 2]
        char = chr(int(hex_char, 16))
        
        original_char = reverse_transform(char, i)
        
        reconstructed_password += original_char
        
    return reconstructed_password

password = reconstruct_password()

print("Mot de passe trouvé:", password)

# 404CTF{l_ech4uff3m3nt_3st_t3rm1ne}
