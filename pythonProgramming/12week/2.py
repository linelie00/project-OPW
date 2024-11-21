class Calculator:
    def __init__(self):
        self.count = 0
        self.value = 0

    def init(self):
        self.value = 0
        self.count = 0

    def add(self, val):
        self.value += val
        self.count += 1
        print('add :', self.value)
    
    def sub(self, val):
        self.value -= val
        self.count += 1
        print('subtract :', self.value)
    
    def mul(self, val):
        self.value *= val
        self.count += 1
        print('multiply :', self.value)
    
    def div(self, val):
        self.value /= val
        self.count += 1
        print('divide :', self.value)
    
    def pow(self, val):
        self.value **= val
        self.count += 1
        print('power :', self.value)

a = Calculator()
a.add(8)
a.mul(1)
a.sub(2)
a.div(2)
print('operation count :', a.count)