#Ecrire un générateur de mot de passe aléatoire. Le mot de passe sera composé de 8 caractères comprenant un
#mixe de lettres minuscules, majuscules, de chiffres et de caractères spéciaux. Un nouveau mot de passe sera généré à
#chaque fois que l’utilisateur le demandera.

import random
import string

def randomString(stringLength=8):
    generatePassword = string.ascii_letters + string.punctuation  + string.digits
    return ''.join(random.choice(generatePassword) for i in range(stringLength))
    
    
responseUser = input("Voulez-vous un password ? : y or n : ")

if responseUser == "y":
    realPassword = randomString()
    print(realPassword)
else:
    print("bye !")