def tupleSum(a,b) -> tuple:
    z = zip(a,b)
    return tuple(sum(x) for x in z)

def getAdventData(dirPath:str,filePath:str) -> list[str]:
    from os import path
    if path.exists(dirPath): completePath = dirPath + "/" + filePath
    else: completePath = filePath
    with open(completePath) as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    return data
