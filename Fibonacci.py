from functools import lru_cache
from time import time


class Fibonacci:
    def __init__(self):
        # Salviamo nel dizionario cache le soluzioni, con chiave il sottoproblema e valore la soluzione
        # a quel problema (per 0 e 1 so già che le soluzioni sono rispettivamente 0 e 1).
        # La cache serve per tener traccia della soluzione di un problema così se il problmea di ripresenta
        # abbiamo già la soluzione e aumentiamo l'efficienza
        self.cache = { 0: 0, 1: 1}
        self.ricorsioni = 0
        self.ricorsioni_cache = 0

    def calcola_elemento_cache(self, n):
        # Se ho già la soluzione per questo n (0 o 1) la prendo dalla cache, il get restituisce
        # il valore se la chiave esiste, sennò restituisce None
        if self.cache.get(n) is not None:
            return self.cache[n]
        # Altrimenti devo andare avanti con la ricorsione
        else:
            # Metto nella cache la soluzione per il problema corrente (n)
            self.ricorsioni_cache += 1
            self.cache[n] = self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2)
            return self.cache[n]


    def calcola_elemento(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            self.ricorsioni += 1
            return (self.calcola_elemento(n-1) + self.calcola_elemento(n-2))


    #Basta aggiungere questo decoratore per implementare automaticamente la cache e aumentare l'efficienza
    @lru_cache
    def calcola_elemento_lru(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.calcola_elemento(n-1) + self.calcola_elemento(n-2))



if __name__=="__main__":
    N=40
    fib = Fibonacci()
    start_time = time()
    print(fib.calcola_elemento(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")
    print(f"Numero ricorsioni: {fib.ricorsioni}")

    # Usando la cache il tempo diminuisce, quindi migliora l'efficienza
    start_time2 = time()
    print(fib.calcola_elemento_cache(N))
    end_time2 = time()
    print(f"Elapsed time2 - recursion: {end_time2 - start_time2}")
    print(f"Numero ricorsioni cache: {fib.ricorsioni_cache}")

    # Usando la cache il tempo diminuisce, quindi migliora l'efficienza
    start_time3 = time()
    print(fib.calcola_elemento_cache(N))
    end_time3 = time()
    print(f"Elapsed time3 - recursion: {end_time3 - start_time3}")