def palyndrome(word):
    if len(word) <= 1:
        return True
    else:
        # In phyton l'indice -1 indica l'ultima lettera (leggendo al contrario)
        # Verifichiamo che la prima e l'ultima lettera della parola corrente siano uguali
        # e poi passiamo al metodo la parola dall'indice 1 all'indice -1 escluso (quindi considero dalla
        # seconda alla penultima lettera)
        return (word[0] == word[-1] and palyndrome(word[1:-1]))


def palyndrome_easier(word):
    # word[::-1] inverte la stringa
    return word[::-1] == word


if __name__ == '__main__':
    print(palyndrome('casa'))
    print(palyndrome('civic'))