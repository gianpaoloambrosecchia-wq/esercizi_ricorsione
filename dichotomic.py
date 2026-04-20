def dichotomic(input_list, val):
    # Divio ogni lista a metà fino ad arrivare ad ottenere i singoli elementi a quel punto faccio il confronto
    # (es. 8 --> 4 --> 2 --> 1)
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        # Considero l'indice mediano (// dà divisione intera)
        index = len(input_list)//2

        # Invoco la stessa funzione sulle due sottoliste, la prima che è la prima metà della input_list
        # iniziale e la seconda è pari alla seconda metà della input_list iniziale
        return (dichotomic(input_list[:index], val) or dichotomic(input_list[index:], val))
        # Uso or così quando trova un True restituisce direttamente True


if __name__ == "__main__":
    sequenza = [x for x in range (1,10)]
    print(dichotomic(sequenza, 4))
    print(dichotomic(sequenza, 11))