from time import sleep

#Soluzione iterativa (non ricorsiva)
def countdown(n):
    while n >= 0:
        print(n)
        sleep(1)  #Aspetta 1 secondo
        n -= 1


#Soluzione ricorsiva
def countdown_recursive(n):
    #Condizione terminale (if)
    if n == 0:
        #Se n=0 è finito il metodo, stampo Stop e basta
        print("Stop")
    #Condizione non terminale (else)
    else:
        print(n)
        sleep(1)
        #Chiamo il metodo stesso con argomento n-1
        countdown_recursive(n-1)



if __name__ == '__main__':
    N=10
    countdown(N)
    countdown_recursive(N)