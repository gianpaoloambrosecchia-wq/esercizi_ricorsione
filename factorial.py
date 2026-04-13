def factorial(n):
    #Condizione terminale
    if n == 1 or n == 0:
        return 1
    #Condizione non terminale
    else:
        #moltiplica il valore corrente di n per il valore di ritorno della chiamata alla funzione factorial(n-1)
        return n * factorial(n-1)


if __name__=='__main__':
    N=5
    print(factorial(N))