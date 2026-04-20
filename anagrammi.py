import copy

from anyio.functools import lru_cache


def anagrammi(parola):
    soluzioni = []

    # Alla funzione ricorsione passiamo un parziale (lista vuota), la parola e le soluzioni
    ricorsione([], parola, soluzioni)
    return soluzioni

def ricorsione(parziale: list, rimanenti: str, soluzioni: list) -> list:
    # caso terminale
    if (len(rimanenti) == 0):
        soluzioni.append(copy.deepcopy(parziale))
    else:
        for i in range(len(rimanenti)):
            # Aggiungo una nuova lettera tra le rimanenti alla soluzione parziale
            parziale.append(rimanenti[i])
            # Considero i nuovi rimanenti come i precedenti rimanenti meno
            # l'elemento con indice i
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            # Devo togleire l'ultimo elemento in parziale, cioè alla prima iterazione
            # considera la prima lettera e ci fa la ricorsione fino ad avere tutte le soluzioni
            # che inizino con la prima lettera, quindi la elimino da parziale e considero la seconda lettera
            # e così via
            parziale.pop()




#===================================================================================================
# Considero parziale come una stringa e soluzioni come un set per evitare
# di avere soluzioni uguali quando una parola ha delle lettere che si ripetono
# Per usare il set devo avere delle stringhe, non posso inserire delle liste
# perchè le liste non sono oggetti hashable (potrei creare una classe hashable apposita)

def anagrammi_str(parola):
    soluzioni_set = set()

    # Alla funzione ricorsione passiamo un parziale (lista vuota), la parola e le soluzioni
    ricorsione_str("", parola, soluzioni_set)
    return soluzioni_set


def ricorsione_str(parziale: str, rimanenti: str, soluzioni_set: set):
    # caso terminale
    if (len(rimanenti) == 0):
        soluzioni_set.add(copy.deepcopy(parziale))
    else:
        for i in range(len(rimanenti)):
            # Aggiungo una nuova lettera tra le rimanenti alla soluzione parziale

            # Considero i nuovi rimanenti come i precedenti rimanenti meno
            # l'elemento con indice i
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str(parziale + rimanenti[i], nuovi_rimanenti, soluzioni_set)
            # Devo togleire l'ultimo elemento in parziale, cioè alla prima iterazione
            # considera la prima lettera e ci fa la ricorsione fino ad avere tutte le soluzioni
            # che inizino con la prima lettera, quindi la elimino da parziale e considero la seconda lettera
            # e così via


#===============================================================================================================
# Se voglio usare la cache non posso usare le soluzioni poichè posso creare dei dizionari
# su parziale e rimanenti che sono hashable, mentre soluzioni non lo è.
# Ho lo stesso effetto del caso precedente, non considero parole uguali poichè la cache non
# considera input uguali

def anagrammi_str2(parola):
    ricorsione_str2("", parola)

@lru_cache(maxsize=None)
def ricorsione_str2(parziale: str, rimanenti: str):
    # caso terminale
    if (len(rimanenti) == 0):
        print(parziale)
    else:
        for i in range(len(rimanenti)):
            # Aggiungo una nuova lettera tra le rimanenti alla soluzione parziale

            # Considero i nuovi rimanenti come i precedenti rimanenti meno
            # l'elemento con indice i
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str2(parziale + rimanenti[i], nuovi_rimanenti)
            # Devo togleire l'ultimo elemento in parziale, cioè alla prima iterazione
            # considera la prima lettera e ci fa la ricorsione fino ad avere tutte le soluzioni
            # che inizino con la prima lettera, quindi la elimino da parziale e considero la seconda lettera
            # e così via





if __name__ == '__main__':
    print(anagrammi('casa'))

    print(anagrammi_str('casa'))

    anagrammi_str2('casa')

