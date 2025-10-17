from collections import deque

class Node: 
    def __init__(self, val): 
        self.val = val 
        self.children = [] 

    def BFS(self): 
        visited = set() 
        queue = deque([self])  
        while queue: 
            node = queue.popleft()  
            if node not in visited: 
                print(node.val, end=" ") 
                visited.add(node) 
                for child in node.children: 
                    queue.append(child) 

    def DFS_Rec(self, visited=None): 
        if visited is None: 
            visited = set()
        if self not in visited:
            print(self.val, end=" ")  
            visited.add(self)  
            for child in self.children: 
                child.DFS_Rec(visited)
