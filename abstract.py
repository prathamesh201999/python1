from abc import ABC,abstractmethod


class computer:
    @abstractmethod
    def show(self):
        pass
    
    
class laptop(computer):
    def show(self):
        print("It is running")
    
    
    
l1 = laptop()
l1.show()
