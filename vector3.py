from typing import Union, overload

class Vector3:
    x:float
    y:float
    z:float

    def __init__(self,a:float,b:float,c:float) -> None:
        self.x, self.y, self.z = a,b,c

    def toTuple(self) -> tuple[float,float,float]:
        return self.x,self.y,self.z

    def rotateX(self) -> None:
        self.z, self.y = self.y, -self.z
    def rotateY(self) -> None:
        self.x, self.z = self.z, -self.x
    def rotateZ(self) -> None:
        self.y, self.x = self.x, -self.y
    
    def copy(self) -> "Vector3":
        return Vector3(self.x,self.y,self.z)

    def __str__(self) -> str:
        return str(self.toTuple())

    def __eq__(self, __o: "Vector3") -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z
    def __add__(self,__o: "Vector3") -> "Vector3":
        return Vector3(self.x+__o.x,self.y+__o.y,self.z+__o.z)
    def __sub__(self, __o:"Vector3") -> "Vector3":
        return Vector3(self.x-__o.x, self.y - __o.y, self.z - __o.z)

    def __hash__(self) -> int:
        return hash((self.x,self.y,self.z))

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
        ans.append(p+move)
    return ans

def getOverlap(p1:list[Vector3],p2:list[Vector3]) -> int:
    count = 0
    #print(*p1)
    #print(*p2)
    for i in range(min(len(p2),len(p1))): 
        #print(i)
        if p1[i] in p2: count+=1
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

if __name__=="__main__":
    l1 = [Vector3(4,5,6),Vector3(3,2,1)]
    l2 = [Vector3(3,2,1),Vector3(4,5,6)]
    print(getOverlap(l1,l2))