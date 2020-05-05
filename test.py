def fibonacci(nterms):
    n1 = 0
    n2 = 1
    count = 0
    # Tant que 0 est inférieur à la valeur entrer par l'utilisateur (nterms)
    while(count < nterms):
        '''
        f = open('helloworld.txt','wb')
        f.write(n1.encode('utf-8'))
        f.close()
        '''
       # print(n1)
        f = open('helloworld.txt','wb')
        f.write(str(n1))
        f.close()
        nth = n1 + n2
        # update des valeurs
        n1 = n2
        n2 = nth
        count += 1
    
fibo_entry = int(input("Entre un nombre, pour que je génère ta fibonacci : "))
fibonacci(int((fibo_entry)))