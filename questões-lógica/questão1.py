arrayInput = input("Digite o array de números inteiros (no formato [x,y,z,w...])")
objective = int(input("Digite o número alvo:"))

    ###Manipulações das strings de input para adequar às estruturas de dados desejadas.
intArray = [int(x) for x in arrayInput.split(",")[1:-1]]
intArray.append(int(arrayInput[-2]))
intArray.insert(0, int(arrayInput[1]))

    ###A resolução assume que o array de números fornecido está ordenado, assim como demonstrado no documento do desafio.
    ###No caso de ser um array não-ordenado, visando menor complexidade algoritmíca, bastaria realizar um 'merge-sort' para ordenar o array antes da execução da função abaixo.
    ###

def findObjectiveSumIndex(array, obj):
    arrayCopy = array[0:]
    array.sort()
    for i in range(len(array)):
        numberToSearch = abs(array[i] - obj)
        for k in range(len(array[i:])):
            if array[k] > numberToSearch:
                break
            if array[k] == numberToSearch:
                return [i,k]


print(findObjectiveSumIndex(intArray, objective))