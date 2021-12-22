from vector3 import Vector3
from typing import Union

def getRotations(vec:Vector3) -> list[Vector3]:
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
    ans = [[] for _ in range(24)]
    for v in vecs:
        for i,x in enumerate(getRotations(v)):
            ans[i].append(x)
    return ans

def getTranslations(points:list[Vector3],move:Vector3) -> list[Vector3]:
    ans = []
    for p in points:
        ans.append(p.copy()+move)
    return ans

def getAdjustments(points:list[Vector3],ref:Vector3) -> list[list[Vector3]]:
    ans = []
    for p in points:
        motion = ref - p
        ans.append(getTranslations(points,motion))
    #print(len(points)==len(ans))
    return ans

def getOverlap(p1:list[Vector3],p2:list[Vector3]) -> int:
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
    refPoint = ref[0]

    for p in points:
        motion = p - refPoint
        newPointList = getTranslations(points,motion)
        overlap = getOverlap(ref,newPointList)
        #print(overlap)
        if overlap>=threshold: return newPointList,motion
    
    return None