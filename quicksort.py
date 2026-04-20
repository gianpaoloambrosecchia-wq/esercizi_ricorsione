def quicksort(sequenza):
    if len(sequenza) <= 1:
        return sequenza
    # Poichè mi aspetto che ogni chiamata ritorni il suo vettore ordinato, se il vettore è lungo 1 o 0 non serve
    # ordinarlo
    else:
        # 1. Scelta pivot (arbitraria)
        pivot = sequenza[0]
        # 2. Dividere sequenza in base al pivot (più piccoli, uguali e più grandi) e riempio le liste
        #    con un ciclo for
        sequenza_smaller  = []
        sequenza_pivot = []
        sequenza_larger = []

        for i in sequenza:
            # il numero è minore del pivot, lo aggiungo alla lista dei minori
            if i < pivot:
                sequenza_smaller.append(i)
            # il numero è maggiore del pivot, lo aggiungo alla lista dei maggiori
            elif i > pivot:
                sequenza_larger.append(i)
            # il numero è uguale al pivot, lo aggiungo alla lista degli uguali
            else:
                sequenza_pivot.append(i)

        # Modo breve:
        # sequenza_smaller = [n for n in sequenza if n < pivot]
        # sequenza_larger = [n for n in sequenza if n > pivot]
        # sequenza_pivot = [n for n in sequenza if n = pivot]

        # 3. La soluzione è data da: ordinare il vettore smaller + ordinare il vettore uguale al pivot + ordinare
        #    il vettore larger
        # Ritorno le sottoliste che ordino ogni volta sapendo che a sinistra ho i minori, al centro quelli uguali
        # e a destra quelli maggiori del pivot (e così via)
        return (quicksort(sequenza_smaller) + sequenza_pivot + quicksort(sequenza_larger))





if __name__ == "__main__":
    sequenza = [9, 3 , 2 , 6, 8, 5, 199]
    print(quicksort(sequenza))