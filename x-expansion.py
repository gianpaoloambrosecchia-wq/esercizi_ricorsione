import copy


class XExpansion:

    def __init__(self):
        # Lista in cui aggiungere tutte le soluzioni
        self.soluzioni = []
        self.soluzioni_list = []


    # Implementiamo il parziale come una lista
    def calcola_list(self, input):
        self.soluzioni_list = []
        self._ricorsione_list([], input)

    def _ricorsione_list(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            #print(parziale)

            # Mi serve fare una copia profonda, perchè quando aggiungo il parziale
            # nella soluzione aggiungo la lista stessa e non una copia come avviene per le stringhe
            self.soluzioni_list.append(copy.deepcopy(parziale))
        else:
            # Se il primo carattere dei rimanenti è X, faccio la ricorsione ai restanti
            # mentre alla soluzione parziale aggiungo 0 ed 1, e i rimanenti diminuiscono di 1
            # quindi per i rimanenti considero a partire dal secondo elemento
            if rimanenti[0] == 'X':
                # Ciclare sugli step possibili
                for c in ["0","1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()

            else:
            # Se il primo carattere dei rimanenti è uno 0 o un 1 allora semplicemente lo
            # aggiungo alla soluzione parziale.
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])


    #Uso questo metodo calcola pubblico per leggibilità (non necessario)
    def calcola(self, input):
        # Mettiamo a 0 le soluzioni, altrimenti ogni volta che chiamiamo la funzion
        # aggiunge le nuove soluzioni a quelle vecchie
        self.soluzioni = []
        self._ricorsione("", input)

    # parziale è la soluzione parziale, rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            #print(parziale)
            self.soluzioni.append(parziale)
        else:
            # Se il primo carattere dei rimanenti è X, faccio la ricorsione ai restanti
            # mentre alla soluzione parziale aggiungo 0 ed 1, e i rimanenti diminuiscono di 1
            # quindi per i rimanenti considero a partire dal secondo elemento
            if rimanenti[0] == 'X':
                # Parallelamente fa ricorsione su due sequenze ogni volta che c'è una X
                self._ricorsione(parziale + '0', rimanenti[1:])
                self._ricorsione(parziale + '1', rimanenti[1:])
            else:
            # Se il primo carattere dei rimanenti è uno 0 o un 1 allora semplicemente lo
            # aggiungo alla soluzione parziale.
                self._ricorsione(parziale + rimanenti[0], rimanenti[1:])


# ========================================================================================================
# ========================================================================================================

# Utilizzo un metodo dentro un altro metodo


def x_expansion2(input):
    soluzioni = []
    # parziale è la soluzione parziale, rimanenti sono il resto dei caratteri da esaminare
    def ricorsione(parziale, rimanenti):
        if len(rimanenti) == 0:
            #print(parziale)
            soluzioni.append(parziale)
        else:
            # Se il primo carattere dei rimanenti è X, faccio la ricorsione ai restanti
            # mentre alla soluzione parziale aggiungo 0 ed 1, e i rimanenti diminuiscono di 1
            # quindi per i rimanenti considero a partire dal secondo elemento
            if rimanenti[0] == 'X':
                # Parallelamente fa ricorsione su due sequenze ogni volta che c'è una X
                ricorsione(parziale + '0', rimanenti[1:])
                ricorsione(parziale + '1', rimanenti[1:])
            else:
            # Se il primo carattere dei rimanenti è uno 0 o un 1 allora semplicemente lo
            # aggiungo alla soluzione parziale.
                ricorsione(parziale + rimanenti[0], rimanenti[1:])

    ricorsione("", input)
    return soluzioni


if __name__ == '__main__':
    sequenza = "01X0X"
    xexp = XExpansion()

    #Metodo con soluzioni parziali rappresentate come stringhe
    xexp.calcola(sequenza)
    print(xexp.soluzioni)

    #Metodo con soluzioni parziali rappresentate come liste
    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)



