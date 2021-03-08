problemInput = input("Digite o array de preços:")

    ###Manipulações das strings de input para adequar às estruturas de dados desejadas.
priceArray = [int(x) for x in problemInput.split(",")[1:-1]]
priceArray.append(int(problemInput[-2]))
priceArray.insert(0, int(problemInput[1]))


    ###Função para calcular o lucro máximo, dado um array de preços com cada elemento representando um dia.
    ###A idéia da função é percorrer o array de preços, salvando as possíveis transações lucrativas (valor de compra e venda) em um array (transactionsArray)
    ###E por fim, fazer o cálculo do maior lucro possível obtido, respeitando-se a condição da compra antes da venda.
    ###Cada elemento do array transactionsArray representa uma possível transação, sendo o formato: [valor mínimo, valor máximo].

def findMaxProfit(array):
    transactionsArray = []
    for i in range(len(array)):
        if len(transactionsArray)==0: transactionsArray.append([array[i]])

        for k in range(len(transactionsArray)):
            
            if array[i] <= min(transactionsArray[k]):
                transactionsArray.append([array[i]])

            if array[i] > max(transactionsArray[k]):
                if len(transactionsArray[k]) == 1:
                    transactionsArray[k].append(array[i])
                else:
                    transactionsArray[k][1] = array[i]

    profitArray = []
    for i in range(len(transactionsArray)):
        if len(transactionsArray[i]) > 1:
            profitArray.append(transactionsArray[i][1] - transactionsArray[i][0])

    try: return max(profitArray)
    except: return 0


print(findMaxProfit(priceArray))