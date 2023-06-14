#Uses python3
import os


def load(filePath):
        with open(filePath, 'r') as f:
            return f.read()

def reach(adj, x, y):
    #write your code here
    return 0

if __name__ == '__main__':
    input = load(r'C:\Users\achyu\git\learnPython\tutorial\practice\dataStructures\graphs\test1.txt')
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
