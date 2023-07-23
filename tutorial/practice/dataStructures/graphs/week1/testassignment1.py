#Uses python3
import os


def load(filePath):
    with open(filePath, 'r') as f:
        return f.read()

def dfs(visited, adj, node):
        if node not in visited:
            visited = (list(visited)).append(node)
        return visited

def reach(adj, x, y):
        #write your code here
        visited = []
        visited = dfs(visited, adj, x)
        return 1 if y in visited else 0


input1 = load(r'C:\Users\achyu\git\learnPython\tutorial\practice\dataStructures\graphs\week1\test1.txt')
input2 = load(r"C:\Users\achyu\git\learnPython\tutorial\practice\dataStructures\graphs\week1\test2.txt")
input3 = load(r"C:\Users\achyu\git\learnPython\tutorial\practice\dataStructures\graphs\week1\test3.txt")
input = input3
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
x, y = data[2 * m:]
adj = [[] for _ in range(n)]
x, y = x - 1, y - 1
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
print(reach(adj, x, y))
