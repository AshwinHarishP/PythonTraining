class Bank:
    def getROI(self):
        return 10

    
class SBI(Bank):
    def getROI(self):
        return 7

class ICIC(Bank):
    def getROI(self):
        return 5


bank = Bank()
sbi = SBI()
icic = ICIC()

print(bank.getROI())
print(sbi.getROI())
print(icic.getROI())