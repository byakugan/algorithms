import random

class QuickFind(object):
    def __init__(self, n):
# id is keyword is python use name data instead
        self.data = [i for i in range(n)]

    def connected(self, p, q):
        return self.data[p] == self.data[q]

    def union(self, p, q):
        pid = self.data[p]
        qid = self.data[q]
        for i, d in enumerate(self.data):
            if d == pid:
                self.data[i] = qid

if __name__ == "__main__":
    num = 10
    uf = QuickFind(num)
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
