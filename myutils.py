def tupleSum(a,b) -> tuple:
    """
    Element-wise addition of tuples
    """
    z = zip(a,b)
    return tuple(sum(x) for x in z)

def getAdventData(dirPath:str,filePath:str) -> list[str]:
    """
    Get a list of all strings in advent of code file input
    The lines are already trimmed

    dirPath: the name of the folder the file is in
    filePath: the name of the file
    """
    from os import path
    if path.exists(dirPath): completePath = dirPath + "/" + filePath
    else: completePath = filePath
    with open(completePath) as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    return data
