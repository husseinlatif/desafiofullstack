problemInput = input("Digite o mapa de elevação:")

    ###Manipulações das strings de input para adequar às estruturas de dados desejadas.
elevationMap = [int(x) for x in problemInput.split(",")[1:-1]]
elevationMap.append(int(problemInput[-2]))
elevationMap.insert(0, int(problemInput[1]))


    ###Função para cálculo do volume retido de água, percorrendo o mapa de elevação fornecido horizontalmente e mapeando as extremidades
    ###Verticais de retenção (alturas máximas), fazendo o cálculo do volume por meio das diferenças entre os máximos encontrados e os valores de altura menores, que serão preenchidos com água.
def calculateWaterVolume(eMap):
    waterVolume = 0
    maxLeftHeight = 0
    maxRightHeight = 0
    leftIndex = 0
    rightIndex = len(eMap)-1
    while (leftIndex < rightIndex):
        if (eMap[leftIndex] < eMap[rightIndex]):
            if (eMap[leftIndex] >= maxLeftHeight):
                maxLeftHeight = eMap[leftIndex]
            else:
                waterVolume += maxLeftHeight - eMap[leftIndex]
            leftIndex += 1 

        else:
            if (eMap[rightIndex] >= maxRightHeight):
                maxRightHeight = eMap[rightIndex]
            else:
                waterVolume += maxRightHeight - eMap[rightIndex]
            rightIndex -= 1
    
    return waterVolume
    
print(calculateWaterVolume(elevationMap))
        