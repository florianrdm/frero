# Reprendre la question 2.3, et au lieu d’afficher le résultat à l’écran le stocker dans un fichier texte en demandant
# à l’utilisateur de rentrer le nom du fichier texte.


def fibonacci(nterms, nameFile):
    n1 = 0
    n2 = 1
    count = 0
    # Tant que 0 est inférieur à la valeur entrer par l'utilisateur (nterms)
    while(count < nterms):
        f = open(nameFile,'w')
        f.write(str(n1))
        f.close()
        #print(n1)
        nth = n1 + n2
        # update des valeurs
        n1 = n2
        n2 = nth
        count += 1
        
        with open(nameFile, "r") as fichier:
	        print(fichier.read())
    
fibo_entry = int(input("Entre un nombre, pour que je génère ta fibonacci : "))
name_file = input("Donne un nom de fichier : ")


