class A:
    def my01(self):
        print('A my01')


class B(A):
    def my01(self):
        print('B my01')

    def my03(self):
        print('B my03')


class C(A):
    def my01(self):
        print('C my01')


class D(C, B):
    def my02(self):
        self.my01()
        self.my03()


d01 = D()
d01.my02()

print(D.mro())
