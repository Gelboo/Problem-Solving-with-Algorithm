class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+" -->> "))
        else:
            return self.pinA.getFrom.getOutput()
    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+" -->> "))
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error:No Empty Pins")

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
    def getPin(self):
        return int(input("Enter Pin input for gate "+self.getLabel()+" --> "))

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self,fgate,tgate):#fromgate , togate
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate



g1 = AndGate('G1')
print(g1.getOutput())

g2 = OrGate('G2')
print(g2.getOutput())

g3 = NotGate('G3')
print(g3.getOutput())