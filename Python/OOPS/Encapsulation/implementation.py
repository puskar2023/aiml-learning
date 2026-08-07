class BankAccount:
    def __init__(self, name, balance, acNo):
        self.name = name  #public
        self._balance = balance  #protected
        self.__acNo = acNo  #private
        
    def get_acNo(self):  #getter
        return self.__acNo
    
    def set_acNo(self, newacNo):  #setter
        self.__acNo = newacNo
        
acc1 = BankAccount("Sarthak Sharma", 100_000, 369)

print(acc1._balance)
print(f"Before change of the account number: {acc1.get_acNo()}")
acc1.set_acNo(666)
print(f"After change of the account number: {acc1.get_acNo()}")