import random

class QuickUnion(object):
    def __init__(self, n):
# id is keyword is python use name data instead
        self.data = [i for i in range(n)]


    def root(self, i):
        while(i != self.data[i]):
            i = self.data[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)
        self.data[root_p] = root_q

if __name__ == "__main__":
    num = 10
    uf = QuickUnion(num)
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

