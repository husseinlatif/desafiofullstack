arrayInput = input("Digite o array de números inteiros (no formato [x,y,z,w...])")
objective = int(input("Digite o número alvo:"))

    ###Manipulações das strings de input para adequar às estruturas de dados desejadas.
intArray = [int(x) for x in arrayInput.split(",")[1:-1]]
intArray.append(int(arrayInput[-2]))
intArray.insert(0, int(arrayInput[1]))

    ###Visando menor complexidade algorítmica, a função abaixo primeiramente faz uma 'deep-copy' do array fornecido (para preservar os índices), e ordena o array fornecido como argumento.
    ###Tendo em vista que agora temos um array ordenado, o número de iterações sob tal array é considerávelmente reduzido, já que a idéia da função é
    ###Obter o retorno esperado por meio da subtração de um elemento do array ordenado pelo valor do objetivo. O resultado é buscado na lista ordenada.

def findObjectiveSumIndex(array, obj):
    arrayCopy = array[0:]
    array.sort()
    for i in range(len(array)):
        numberToSearch = abs(array[i] - obj)
        for k in range(len(array[i:])):
            if array[k] > numberToSearch:
                break
            if array[k] == numberToSearch:
                return [arrayCopy.index(array[i]),arrayCopy.index(array[k])]


print(findObjectiveSumIndex(intArray, objective))