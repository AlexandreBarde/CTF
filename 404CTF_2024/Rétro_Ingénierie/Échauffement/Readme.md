<h1>Échauffement</h1>
<h3>Introduction - <b>100pts.</b></h3> 
<p>Un bon échauffement permet non seulement d'éviter des blessures, mais aussi de conditionner son corps et son esprit au combat qui va suivre. Ce crackme devrait constituer un exercice adéquat.

Auteurs : @<b>Izipak (_hdrien)</b></p>

<hr >


Fichier : 

<a href="./echauffement.bin">echauffement.bin</a>

<hr>

<h3>Solution</h3>

Plusieurs outils peuvent être utilisés pour ce challenge, personnellement j'ai utilisé <a href="https://github.com/fkie-cad/dewolf">dewolf</a>, qui va permettre de décompiler ce binaire et nous donner ceci (_j'ai uniquement affiché le code intéressant_) : 

```c
extern unsigned long secret_data = "\x68\x5f\x66\x83\xa4\x87\xf0\xd1\xb6\xc1\xbc\xc5\x5c\xdd\xbe\xbd\x56\xc9\x54\xc9\xd4\xa9\x50\xcf\xd0\xa5\xce\x4b\xc8\xbd\x44\xbd...";

unsigned long secret_func_dont_look_here(void * arg1) {
    int i;
    int var_4;
    unsigned long var_1;
    unsigned long var_2;
    var_1 = secret_data;
    var_4 = 0;
    for (i = 0; i < strlen(var_1); i++) {
        var_2 = secret_data;
        if (arg1[i] * 2 - (char)i != *(i + var_2)) {
            var_4 = 1;
        }
    }
    return (unsigned int)var_4;
}

int main(int argc, char ** argv, char ** envp) {
    void var_7;
    int var_8;
    unsigned long * var_9;
    puts(/* str */ "Vous ne devinerez jamais le mot de passe secret ! Mais allez-y, essayez..");
    var_9 = stdin;
    fgets(/* buf */ &var_7, /* n */ 64, /* fp */ var_9);
    var_8 = secret_func_dont_look_here(&var_7);
    if (var_8 == 0) {
        puts(/* str */ "Wow, impressionnant ! Vous avez r");
    }
    else {
        puts(/* str */ "C'est bien ce que je pensais, vous ne connaissez pas le mot de passe..");
    }
    return 0;
}

```

On remarque une variable `secret_data`, qui ressemble à de l'hexa, mais ne donne rien en ASCII..

Mais dans la fonction `secret_func_dont_look_here` on voit que cette variable est manipulée, donc il faut partir du mot de passe secret et inverser les choses qui sont faites dessus.

J'ai écrit un script en Python pour inverser ces méthodes, le voici :

```python
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
```

Le flag est donc : <b>404CTF{l_ech4uff3m3nt_3st_t3rm1ne}</b>