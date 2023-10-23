class UF:
    def __init__(self,n):
        
        self.rank = [1]*n
        self.parent = [i for i in range(n)]

    def find(self,x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,a,b):
        
        aset=self.find(a)
        bset=self.find(b)

        if aset == bset:
            return
        
        if self.rank[aset] < self.rank[bset]:
            self.parent[aset] = bset

        elif self.rank[aset] > self.rank[bset]:
            self.parent[bset] = aset

        else:
            self.parent[bset] = aset
            self.rank[aset] = self.rank[aset] + 1

nodes = int(input("Enter the number of nodes  "))
obj = UF(nodes)
no_of_connections = int(input("Enter the number of connections  "))

for i in range(no_of_connections):
    x = int(input("Enter the first vertex  "))
    y = int(input("Enter the second vertex  "))
    obj.union(x,y)

while(1):
    n = int(input("Enter\n1. for finding a connection\n2. for exit\n"))
    if n == 2:
        break
    elif n==1:
        x = int(input("Enter the first vertex  "))
        y = int(input("Enter the second vertex  "))
        if obj.find(x) == obj.find(y):
            print("Yes")
        else:
            print("No")