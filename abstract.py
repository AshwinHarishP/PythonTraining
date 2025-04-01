from abc import *
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass


class sbi(Bank):
    def interest(self):
        roi = 10
        print("SBI Interest: ",roi)

class indian_bank(Bank):
    def interest(self):
        roi = 7.5
        print("Indian Bank Interest: ", roi)
    

sbiObj = sbi()
indian_bankObj = indian_bank()

sbiObj.interest()
indian_bankObj.interest()