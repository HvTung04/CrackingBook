from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def dfs(root):
    if not root:
        return
    print(root.data, end=' ')    # Print the current node data
    for child in root.children:
        dfs(child)  # Recursively visit each child

def bfs(root):
    if not root:
        return

    queue = deque() # Create a queue for bfs
    queue.append(root) # add current node to queue

    while queue:
        node = queue.popleft()
        print(node.data, end=' ')
        queue.extend(node.children) # add all children of current node
        

def main():
    root = TreeNode('A')
    root.children.append(TreeNode('B'))
    root.children.append(TreeNode('C'))
    root.children[0].children.append(TreeNode('D'))
    root.children[0].children.append(TreeNode('E'))

    print("DFS result:")
    dfs(root)
    print("\nBFS result:")
    bfs(root)

if __name__ == '__main__':
    main()