problemInput = input("Digite o mapa de elevação:")
elevationMap = [int(x) for x in problemInput.split(",")[1:-1]]
elevationMap.append(int(problemInput[-2]))
elevationMap.insert(0, int(problemInput[1]))

def calculateWaterVolume(eMap):
    print(eMap)
    if len(eMap)==2: return max(eMap)-min(eMap)
    
    leftHeight = max(eMap[ 0:round(len(eMap)/2) ])
    rightHeight = max(eMap[ round(len(eMap)/2)+1: ])
    
    if leftHeight < rightHeight:
        if leftHeight > eMap[1]: return (leftHeight-eMap[1]) + calculateWaterVolume(eMap[1:-1])
        else: return calculateWaterVolume(eMap[1:-1])
    
    else:
        if rightHeight > eMap[-2]: return  (rightHeight-eMap[-1]) + calculateWaterVolume(eMap[1:-1])
        else: return calculateWaterVolume(eMap[1:-1])
    
    
print(calculateWaterVolume(elevationMap))
        