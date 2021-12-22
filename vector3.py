from typing import Union, overload

class Vector3:
    x:int
    y:int
    z:int

    def __init__(self,a:int=0,b:int=0,c:int=0) -> None:
        self.x, self.y, self.z = a,b,c

    def toTuple(self) -> tuple[int,int,int]:
        return int(self.x),int(self.y),int(self.z)

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
        if int(self.x) != int(__o.x):return False
        if int(self.y) != int(__o.y):return False
        if int(self.z) != int(__o.z):return False
        return True
    def __add__(self,__o: "Vector3") -> "Vector3":
        return Vector3(self.x+__o.x,self.y+__o.y,self.z+__o.z)
    def __sub__(self, __o:"Vector3") -> "Vector3":
        return Vector3(self.x-__o.x, self.y - __o.y, self.z - __o.z)

    def __hash__(self) -> int:
        return hash((self.x,self.y,self.z))



def intDistance(a:Vector3,b:Vector3) -> int:
    from math import isqrt
    dx,dy,dz = a.x-b.x, a.y-b.y, a.z-b.z
    return isqrt(dx*dx + dy*dy + dz*dz)


#Debug main function
if __name__ == "__main__":
    v1 = Vector3(-1,0,0)
    v2 = Vector3(1,0,0)
    print(intDistance(v1,v2))