class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def BFS(root):
    visited = set()         
    queue = [root]          

    while queue:
        node = queue.pop(0) 
        if node not in visited:
            print(node.val, end=" ")
            visited.add(node)

            for child in node.children:
                queue.append(child)

def DFS_Rec(node, visited=None):
    if visited is None:
        visited = set()

    if node is None or node in visited:
        return

    print(node.val, end=" ")
    visited.add(node)

    for child in node.children:
        DFS_Rec(child, visited)

def DFS(root):
    visited = set()
    stack = [root]          

    while stack:
        current = stack.pop()  
        if current not in visited:
            print(current.val, end=' ')
            visited.add(current)

            for child in reversed(current.children):
                stack.append(child)

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

A.children = [B, C, D]
B.children = [A, E]
C.children = [A, E]
D.children = [A, E]
E.children = [B, C, D]

BFS(A)

print("\n\nDFS Iterative:")
DFS(A)

print("\n\nDFS Recursive:")
DFS_Rec(A)
