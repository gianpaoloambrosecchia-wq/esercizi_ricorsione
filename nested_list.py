def count_leaf_nodes(input_list):

    if len(input_list) == 0:
        return 0

    else:
        counter = 0
        for element in input_list:
            #controllo che l'elemento della lista iniziale sia a sua volyta una lista
            if type(element) == list:
                #Aggiungo al counter il conteggio sulla lista annidata
                counter += count_leaf_nodes(element)
            #Se l'elemento non è una lista aggiungo 1 al counter
            else:
                counter += 1
        return counter

if __name__=='__main__':
    #Liste annidate
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names))  #ci aspettiamo 10