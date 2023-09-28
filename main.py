class A:
    def __init__(a1, a2):
        self.a1 = a1
        self.a2 = a2

    def getA1():
        return a1

    def setA1(x):
        a1 = x

    def getA2():
        return a2

    def setA2(x):
        a2 = x

    def ma1():
        print("ma1")

    def ma2():
        print("ma1")

    def ma3():
        print("Alteração a classe A partir do clone")


class B:
    def __init__(b1, b2):
        self.b1 = b1
        self.b2 = b2

    def getB1():
        return b1

    def setB1(x):
        b1 = x

    def getB2():
        return b2

    def setB2(x):
        b2 = x

    def mb1():
        print("mb1")
    
    def mb2():
        print("mb2")
 
class C:
    def __init__(c1, c2):
        self.c1 = c1
        self.c2 = c2

    def mc1():
        print("mc1")

    def mc2():
        print("mc1")

 
