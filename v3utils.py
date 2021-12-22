from vector3 import Vector3, intDistance
from typing import Union


def getDistances(points:list[Vector3])-> list[list[int]]:
    "returns list of all reciprocal distances of points in list"
    dists = []
    for p in points:
        dists.append([intDistance(p,pp) for pp in points if pp is not p])
    return dists

def getRotations(vec:Vector3) -> list[Vector3]:
    "get list of all 24 possible 90 degree rotations of input vector"
    ans = []
    v = vec.copy()
    for _ in range(4):
        v.rotateY()
        ans.append(v.copy())
    v.rotateZ()
    for _ in range(4):
        v.rotateX()
        ans.append(v.copy())
    v.rotateZ()
    for _ in range(4):
        v.rotateY()
        ans.append(v.copy())
    v.rotateZ()
    for _ in range(4):
        v.rotateX()
        ans.append(v.copy())
    v.rotateY()
    for _ in range(4):
        v.rotateZ()
        ans.append(v.copy())
    v.rotateY()
    v.rotateY()
    for _ in range(4):
        v.rotateZ()
        ans.append(v.copy())
    return ans

def getListRotations(vecs:list[Vector3]) -> list[list[Vector3]]:
    "get all 24 90 degree rotations of list of vectors"
    ans = [[] for _ in range(24)]
    for v in vecs:
        for i,x in enumerate(getRotations(v)):
            ans[i].append(x)
    return ans

def getTranslations(points:list[Vector3],move:Vector3) -> list[Vector3]:
    "returns list of points, translated by move vector"
    ans = []
    for p in points:
        ans.append(p.copy()+move)
    return ans

def getAdjustments(points:list[Vector3],ref:Vector3) -> list[list[Vector3]]:
    "copies list for every translation which puts a point over ref"
    ans = []
    for p in points:
        motion = ref - p
        ans.append(getTranslations(points,motion))
    #print(len(points)==len(ans))
    return ans

def getOverlap(p1:list[Vector3],p2:list[Vector3]) -> int:
    "returns number of points that overlap"
    #print("_-_")
    count = 0
    hasPrinted = False
    for p in p1:
        if p in p2: 
            hasPrinted = True
            #print(p)
            count+=1
        else:
            #print(f"{p} not in control list")
            pass
    if hasPrinted:
        #print("---")
        #print(*p1)
        #print(*p2)
        pass
    #print("-_-")
    return count
        

# Return points adjusted for maximum overlap, plus the relative vector
def getSufficientOverlap(ref:list[Vector3],points:list[Vector3],threshold:int=12) -> Union[tuple[list[Vector3],Vector3],None]:
    """returns rotation and translation of list of points that has >= threshold of overlap with ref\n
    almost impossible to debug, probably doesn't work"""
    refPoint = ref[0]

    for p in points:
        motion = p - refPoint
        newPointList = getTranslations(points,motion)
        overlap = getOverlap(ref,newPointList)
        #print(overlap)
        if overlap>=threshold: return newPointList,motion
    
    return None