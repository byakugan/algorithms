import random

class QuickUnionWeighted(object):
    def __init__(self, n):
# id is keyword is python use name data instead
        self.data = [i for i in range(n)]
        self.sz = [1] * n

    def root(self, i):
        while(i != self.data[i]):
            self.data[i] = self.data[self.data[i]] # Optimization
            i = self.data[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            self.sz[i] += self.sz[j]
            self.data[j] = i
        else:
            self.sz[j] += self.sz[i]
            self.data[i] = j

if __name__ == "__main__":
    num = 10
    uf = QuickUnionWeighted(num)
    print "Before start: {}".format(uf.data)
    for i in range(num):
        p = random.randint(0, num-1)
        q = random.randint(0, num-1)
        uf.union(p, q)
        print "union({}, {}) => {}".format(p, q, uf.data)

    print "After union: data  {}".format(uf.data)
    print "After union: index {}".format([i for i in range(num)])
    for i in range(num):
        p = random.randint(0, num-1)
        q = random.randint(0, num-1)
        print "connected({}, {}) => {}".format(p, q, uf.connected(p, q))


