from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

def dfs(root, prefix=""):
    if root.isEnd:
        print(prefix)
    
    for char, child in root.children.items():   # Accessing char and the corresponding node of child
        dfs(child, prefix + char)

def bfs(root):
    queue = deque( [(root, "")] )

    while queue:
        node, prefix = queue.popleft()  # Got node and prefix of top queue
        if node.isEnd:
            print(prefix)
        
        for char, child in node.children.items():
            queue.append((child, prefix + char))    # Add node and its prefix
        

def main():
    root = TrieNode()
    root.children['c'] = TrieNode()
    root.children['b'] = TrieNode()
    root.children['c'].children['a'] = TrieNode()
    root.children['c'].children['a'].children['t'] = TrieNode()
    root.children['c'].children['a'].children['t'].isEnd = True
    root.children['c'].children['a'].children['t'].children['n'] = TrieNode()
    print("DFS result: ")
    dfs(root)
    print("BFS result: ")
    bfs(root)

if __name__ == "__main__":
    main()