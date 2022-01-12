from vector3 import Vector3, intDistance, vecDistance
from typing import Union


def fusePointLists(points1:list[Vector3],points2:list[Vector3]) -> list[Vector3]:
    """
    returns union of unique points in both lists
    """
    ans = points1[:]
    ans2 = [p for p in points2 if p not in ans]
    return ans+ans2

def getDistances(points:list[Vector3])-> list[list[int]]:
    "returns list of all reciprocal distances of points in list"
    dists = []
    for p in points:
        dists.append([intDistance(p,pp) for pp in points if pp is not p])
    return dists
def getVecDistances(points:list[Vector3]) -> list[list[tuple[int,int,int]]]:
    """
    returns list of reciprocal distances in tuples
    """
    dists = []
    for p in points:
        dists.append([vecDistance(p,pp) for pp in points if pp is not p])
    return dists



def areDistancesCompatible(points1:list[Vector3],points2:list[Vector3], threshold:int) -> bool:
    """
    Where n = threshold\n
    Returns True if at least n points in points1 and points2 have n distances in common\n
    (similar to h-index)

    points1: first list of Vector3
    points2: second list of Vector3
    threshold: barrier to surpass for both number of points and distances in common
    """
    dists1 = getDistances(points1)
    dists2 = getDistances(points2)
    count = 0
    usedpoints = [] #points that have already satisfied the property
    for dist1 in dists1:
        shouldLoop = True
        for dist2 in dists2:
            if not shouldLoop: break
            if dist2 in usedpoints: continue
            else:
                distcount = 0
                for d in dist1:
                    if d in dist2: distcount += 1
                if distcount >= threshold-1:
                    count += 1
                    if count >= threshold: return True
                    usedpoints.append(dist2)
                    shouldLoop = False
    return False

def areDistancesVecCompatible(points1:list[Vector3],points2:list[Vector3],threshold:int) -> bool:
    """
    Like areDistancesCompatible, but for vectors\n
    The result will depend on the correct orientation
    """
    dists1 = getVecDistances(points1)
    dists2 = getVecDistances(points2)
    count = 0
    usedpoints = [] #points that have already satisfied the property
    for dist1 in dists1:
        shouldLoop = True
        for dist2 in dists2:
            if not shouldLoop: break
            if dist2 in usedpoints: continue
            else:
                distcount = 0
                for d in dist1:
                    if d in dist2: distcount += 1
                if distcount >= threshold-1:
                    count += 1
                    if count >= threshold: return True
                    usedpoints.append(dist2)
                    shouldLoop = False
    return False

def extractDistCompatible(candidates:list[list[Vector3]], refPoints:list[Vector3], threshold:int) \
    -> Union[list[Vector3],None]:
    """
    returns first match for areDistancesCompatible with refPoints with
    given threshold
    """
    for c in candidates:
        if areDistancesCompatible(c,refPoints,threshold): return c
    return None

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

def extractCompatibleRotation(points:list[Vector3],refPoints:list[Vector3],threshold:int) ->\
    Union[list[Vector3],None]:
    """
    rotate points such that the vec distance with refPoints matches >= threshold\n
    or None if no rotation satisfies the criteria
    """
    rots = getListRotations(points)
    for r in rots:
        if areDistancesVecCompatible(r,refPoints,threshold): return r
    return None

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

def extractSufficientAdjustment(points:list[Vector3],refPoints:list[Vector3],threshold:int)->\
    Union[list[Vector3],None]:
    """
    Return translation of points that overlap with >= threshold elements of refPoints
    """
    for ref in refPoints:
        trs = getAdjustments(points,ref)
        for t in trs:
            if getOverlap(t,refPoints) >= threshold: return t
    return None