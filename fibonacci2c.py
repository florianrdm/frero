# Ecrire un script demandant à l’utilisateur combien de nombres de Fibonacci il doit générer et ensuite générer ces
# nombres de Fibonacci sur une sortie écran (écrire sous la forme d’une fonction ce générateur).

def fibonacci(nterms):
    n1 = 0
    n2 = 1
    count = 0
    # Tant que 0 est inférieur à la valeur entrer par l'utilisateur (nterms)
    while(count < nterms):
        print(n1)
        nth = n1 + n2
        # update des valeurs
        n1 = n2
        n2 = nth
        count += 1
    
fibo_entry = int(input("Entre un nombre, pour que je génère ta fibonacci : "))
fibonacci(fibo_entry)
