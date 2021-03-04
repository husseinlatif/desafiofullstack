problemInput = input("Digite o mapa de elevação:")
elevationMap = [int(x) for x in problemInput.split(",")[1:-1]]
elevationMap.append(int(problemInput[-2]))
elevationMap.insert(0, int(problemInput[1]))

def calculateWaterVolume(eMap):
    waterVolume=0
    i=0
    for squareHeight in eMap[1:-1]:
        deep=min(eMap)
        i+=1
        if (squareHeight<=0 and (eMap[i+1]>=0 and eMap[i-1]>=0) or (eMap[i+1]>=0 and eMap[i-1]>=0)):
            waterVolume+=1
        eMap[i]-=1
    print(waterVolume)
    print(eMap)
    if waterVolume==0:
        return waterVolume
    else:
        return waterVolume+calculateWaterVolume(eMap)

print(calculateWaterVolume(elevationMap))
        