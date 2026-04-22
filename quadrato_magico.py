import copy
from time import time


class QuadratoMagico():

    def __init__(self, N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []

    # Soluzione del quadrato magico rappresentata da un vettore di N^2 elementi,
    # ogni elemento rappresenta una cella del quadrato
    # ed il suo valore è il numero che mettiamo nella cella
    def risolvi_quadrato(self):
        self.n_chiamate = 0
        self.n_soluzioni = 0
        # Nel quadrato magico devo mettere tutti i numeri da 1 a N*N
        # ma ogni numero compare 1 volta
        rimanenti = set(range(1, self.N*self.N + 1))
        parziale = []
        self.soluzioni = []
        self._ricorsione([], rimanenti)

    def _ricorsione(self, parziale, rimanenti):
        self.n_chiamate += 1
        if len(parziale) == self.N * self.N:
            if self._is_parziale_valid(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
        else:
            # Considero tutti i numeri da 1 a N^" (scrivo + 1 per includere N^2)
            for numero in rimanenti:

                # 1) Aggiungo il numero alla soluzione parziale e tolgo il numero da rimanenti
                parziale.append(numero)
                # Controllo ad ogni passo se parziale è valida
                if self._is_valid(parziale):
                    # Faccio una copia di rimanenti perchè cosi non devo rimettere il numero nel backtracking
                    nuoviRimanenti = copy.deepcopy(rimanenti)
                    nuoviRimanenti.remove(numero)

                    # 2) Andare avanti nella ricorsione
                    self._ricorsione(parziale, nuoviRimanenti)

                #3) Backtracking
                parziale.pop()


    # Controllo sulla soluzione potenziale
    def _is_parziale_valid(self, potenziale_soluzione):
        numero_magico = self.N*(self.N*self.N+1)/2   # Formula data del numero magico
        # 1) Controllare le righe
        for indice_riga in range(self.N):
            # Considero ogni riga della potenziale soluzione
            riga = potenziale_soluzione[indice_riga*self.N : (indice_riga+1)*self.N]
            # Verifico che la somma della riga sia uguale al numero magico
            if sum(riga) != numero_magico:
                return False

        # 2) Controllare le colonne
        for indice_colonna in range(self.N):
            # Consider ogni colonna della potenziale soluzione
            colonna = potenziale_soluzione[indice_colonna: (self.N-1)*self.N + indice_colonna + 1: self.N]
            # Verifico che la somma della colonna sia uguale al numero magico
            if sum(colonna) != numero_magico:
                return False

        # 3) Controllare diagonale 1
        diagonale1 = potenziale_soluzione[0 : self.N*self.N + 1 : self.N + 1]
        if sum(diagonale1) != numero_magico:
            return False

        # 4) Controllare diagonale 2
        somma = 0
        # Per ogni riga (indice) trovo la cella che fa parte della diagonale 2 per quella riga
        for indice in range(self.N):
            somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        if somma != numero_magico:
            return False

        # 5) Se tutti i controlli sono passati con successo, return True
        return True


    # Controllo sul parziale (ad ogni passo)
    def _is_valid(self, parziale):
        numero_magico = self.N*(self.N*self.N+1)/2 # Formula data del numero magico
        # Calcolo quante righe ho completato della mia soluzione parziale
        n_righe_completate = len(parziale)//self.N

        # 1) Controllare le righe
        for indice_riga in range(n_righe_completate):
            # Considero ogni riga della potenziale soluzione
            riga = parziale[indice_riga*self.N : (indice_riga+1)*self.N]
            # Verifico che la somma della riga sia uguale al numero magico
            if sum(riga) != numero_magico:
                return False

        # 2) Controllare le colonne
        # Calcolo quante colonne ho completato
        n_col_completate = max((len(parziale) - self.N*(self.N - 1)),0)
        for indice_colonna in range(n_col_completate):
            # Consider ogni colonna della potenziale soluzione
            colonna = parziale[indice_colonna: (self.N-1)*self.N + indice_colonna + 1: self.N]
            # Verifico che la somma della colonna sia uguale al numero magico
            if sum(colonna) != numero_magico:
                return False

        # 3) Controllare diagonale 1
        diagonale1 = parziale[0 : self.N*self.N + 1 : self.N + 1]
        if sum(diagonale1) != numero_magico:
            return False

        # 4) Controllare diagonale 2
        somma = 0
        # Per ogni riga (indice) trovo la cella che fa parte della diagonale 2 per quella riga
        for indice in range(self.N):
            somma += parziale[indice*self.N + (self.N-1 - indice)]
        if somma != numero_magico:
            return False

        # 5) Se tutti i controlli sono passati con successo, return True
        return True




    def stampa_quadrato(self, soluzione):
        print("--------------------")
        # Considero i numeri da 0 a N-1, cioè N numeri (le righe)
        for riga in range(self.N):
            # Per ogni riga stampo la riga corrispondente della lista soluzione e poi va a capo
            print(soluzione[riga * self.N : (riga + 1) *self.N])
        print("--------------------")





if __name__ == '__main__':
    qm = QuadratoMagico(3)
    start_time = time()
    qm.risolvi_quadrato()
    end_time = time()

    print(f"Chiamate effettuate: {qm.n_chiamate}")
    print(f"Soluzioni trovate: {qm.n_soluzioni}")
    print(f"Tempo impiegato: {end_time - start_time}")

    for soluzione in qm.soluzioni:
        qm.stampa_quadrato(soluzione)




# Rappresentiamo la matrice N*N come una lista lunga N^2 in cui ogni elemento corrisponde ad una cella della matrice,
# in particolare disponiamo le righe una dopo l'altra.

# Di conseguenza considerando la RIGA i, nella lista gli elementi della riga i saranno:
#                  [ i * N : (i + 1) * N ]

# Considerando la COLONNA i, nella lista gli elementi della colonna i saranno:
#                  [ i : (N-1)*N + i +1: N ]
#                                      N finale è il passo

# Gli elementi della DIAGONALE !, nella lista, saranno:
#                  [ 0 : (N*N) - 1: N+1]

# Gli elementi della diagonale 2, nella lista, saranno:
#                  [