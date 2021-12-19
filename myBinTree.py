from types import LambdaType


class BinNode:
    parent: "BinNode" = None
    value = None
    left:"BinNode" = None
    right:"BinNode" = None

    def __init__(self,val=None,_parent:"BinNode"=None) -> None:
        self.parent = _parent
        self.value = val
        self.left, self.right = None,None
    def addLeft(self,val) -> "BinNode":
        newNode = BinNode(val,self)
        self.left = newNode
        return newNode
    def addRight(self,val) -> "BinNode":
        newNode = BinNode(val,self)
        self.right = newNode
        return newNode
    
    def isRoot(self) -> bool:
        return self.parent is None
    def isLeaf(self) -> bool:
        return self.left is None and self.right is None
    def getRoot(self) -> "BinNode":
        if not self.isRoot(): return self.parent.getRoot()
        else: return self
    
    def inOrder(self,action,leafOnly:bool=False) -> None:
        if self.isLeaf(): action(self.value)
        else:
            self.right.inOrder(action,leafOnly)
            if not leafOnly: action(self.value)
            self.right.inOrder(action,leafOnly)

    def getLeaves(self) -> list["BinNode"]:
        if self.isLeaf(): return [self]
        lLeaves = self.left.getLeaves() if self.left is not None else []
        rLeaves = self.right.getLeaves() if self.right is not None else []
        return lLeaves + rLeaves
    def getAllLeaves(self) -> list["BinNode"]:
        return self.getRoot().getLeaves()
    def getLeftMost(self) -> "BinNode":
        return self.getLeaves()[0]
    def getRightMost(self) -> "BinNode":
        return self.getLeaves()[-1]

    def getNextLeft(self) -> "BinNode":
        adjacent = self.getLeftMost()
        leaves = self.getAllLeaves()
        adjIndex = leaves.index(adjacent)
        if adjIndex <= 0: return None
        else: return leaves[adjIndex-1]
    def getNextRight(self) -> "BinNode":
        adjacent = self.getRightMost()
        leaves = self.getAllLeaves()
        adjIndex = leaves.index(adjacent)
        if adjIndex >= len(leaves)-1: return None
        else: return leaves[adjIndex+1]

    def __str__(self) -> str:
        sVal,sLeft,sRight = str(self.value),str(self.left),str(self.right)
        if self.isLeaf(): return str(sVal)
        elif self.value is None: return f"[{sLeft},{sRight}]"
        else: return f"[{sVal}:{sLeft},{sRight}]"