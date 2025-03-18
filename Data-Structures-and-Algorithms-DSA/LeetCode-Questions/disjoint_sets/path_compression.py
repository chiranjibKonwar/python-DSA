# Given a graph, we have to find whether 2 vertices are connected
# Can be done using disjoint set
# Path Compression (optimization of Quick Union implementation): 

# Time Complexity: 
# find(x) --> O(log n) and union(x, y) --> O(log n)
# Space Complexity = O(n)


class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])    # recursive call
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.root[node1]
        root2 = self.root[node2]
        if root1 != root2:
            self.root[root2] = root1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true