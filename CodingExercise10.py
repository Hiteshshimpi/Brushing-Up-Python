class BasicCalculator:
    def __init__(self,a,b):
        self.first=a
        self.second=b

    def add(self):
        return self.first+self.second

    def sub(self):
        return self.first-self.second

    def multiply(self):
        return self.first*self.second

    def divide(self):
        return self.first/self.second


obj = BasicCalculator(10,5)
print(obj.add())
print(obj.sub())
print(obj.multiply())
print(obj.divide())