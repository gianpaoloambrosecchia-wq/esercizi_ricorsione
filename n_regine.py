import copy
from time import time
class NRegine():

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []

    #===========================================================================
    # CASO 2 : rappresentiamo la soluzione come un vettore di N regine
    #          ognuna rappresentante una regina come riga e colonna in cui si trova
    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self._ricorsione2([], N)

    # parziale è un vettore di coppie (riga,colonna)
    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1
        # caso terminale : ho messo N regine
        if len(parziale) == N:
            #if self._is_soluzione(parziale):
                #self.n_soluzioni += 1
                #print(parziale)
            # Verificare che la soluzione sia nuova (non ce ne siano altre uguali)
            if self._is_nuova_soluzione(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))


        else:
        # Devo verificare tutte le possibili soluzioni, quindi
        # devo partire da ogni casella della scacchiera
            for riga in range(N):
                for col in range(N):
                    nuovaRegina = [riga, col]

                    # Verifico se la nuova regina sia ammissibile passo per passo, ottimizzazione
                    if self._step_is_valid(nuovaRegina, parziale):

                        # Aggiungi questo pezzetto di soluzione in parziale
                        parziale.append(nuovaRegina)
                        # Andare avanti con la ricorsione
                        self._ricorsione2(parziale, N)
                        # backtracking
                        parziale.pop()

    # Confrontiamo la soluzione potenziale con quelle già trovate, per verificare
    # che sia diversa dalle altre
    def _is_nuova_soluzione(self, soluzione_potenziale):
        N = len(soluzione_potenziale)
        # Considero tutte le soluzioni nella lista delle soluzioni
        for soluzione in self.soluzioni:
            counter = 0
            # Considero le regine nella mia soluzione possibile
            for regina in soluzione_potenziale:
                # Se la mia regina è nella soluzione considerata incremeneto il contatore
                if regina in soluzione:
                    counter += 1
            # Se il contatore è pari al numero tottale di regine N
            # cioè ho N regine uguali tra soluzione possibile e soluzione
            # allora return False
            if counter == N:
                return False
        return True




    # Funzione che controlla se la nuova regina da inserire sia ammissibile
    # rispetto alla soluzione parziale costruita fino ad ora
    def _step_is_valid(self, nuovaRegina, parziale):
        for regina in parziale:
            if not self._is_pair_admissible(nuovaRegina,regina):
                return False
        return True


    #Verifico se la regina2 che voglio aggiungere è ammissibile rispetto
    # alla regina1 che già ho (verifico il rispetto dei vincoli)
    def _is_pair_admissible(self, regina1, regina2):

        # 1) Verifico la riga, se non va bene return False
        # Se hanno stessa riga, cioè primo elemento della tupla, non va bene
        if regina1[0] == regina2[0]:
            return False

        # 2) Verifico la colonna, se non va bene return False
        # Se hanno stessa colonna, cioè secondo elemento della tupla, non va bene
        if regina1[1] == regina2[1]:
            return False

        # 3) Verifico la diagonale 1, se non va bene return False
        # Per fare questa verifica devo controllare che:
        # colonna di regina1 - riga di regina 1 sia uguale a colonna di regina2 - riga di regina2
        # poichè la stessa diagonale implica una stessa differenza tra indice riga meno indice colonna
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:
            return False

        # 4) Verifico la diagonale 2, se non va bene return False
        # Per fare questa verifica devo controllare che:
        # colonna di regina1 + riga di regina 1 sia uguale a colonna di regina 2 + riga di regina 2
        # poichè stessa diagonale secondaria implica una stessa somma tra indice riga e colonna
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:
            return False

        # 5) Ho passato tutti i controlli, return True
        return True

    #Metodo che consente di vedere se una possibile soluzione è effettivamente
    # una soluzione reale (rispetto dei vincoli)
    def _is_soluzione(self, soluzione_possibile):
        # Considero la soluzione_possibile (quella parziale) e per ogni coppia di regine
        # verifico se rispettino i vincoli
        for i in range(len(soluzione_possibile)-1):
            # Poichè se ho già fatto il primo controllo è inutile rifarlo, ottimizzazione
            for j in range(i+1, len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    return False

        return True


if __name__ == '__main__':
    nreg = NRegine()
    start_time = time()
    nreg.solve2(4)
    end_time = time()

    print("Elapsed time: ", end_time - start_time)
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")
    print(nreg.soluzioni)