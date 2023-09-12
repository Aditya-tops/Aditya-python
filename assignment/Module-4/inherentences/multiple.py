class A:
    def __init__(self, p, q):
        self.n1 = p
        self.n2 = q

    def add(self):
        return self.n1 + self.n2


class B:
    def __init__(self, p, q):
        self.n1 = p
        self.n2 = q

    def sub(self):
        return self.n1 - self.n2


class C(A, B):
    def mul(self):
        return self.n1 * self.n2


obj = C(12, 12)

print(obj.add())  # Output: 24
print(obj.sub())  # Output: 0
print(obj.mul())  # Output: 144
