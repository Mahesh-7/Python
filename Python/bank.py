class bank:
    total=0
    def deposit(self,deposit=0):
        self.total=self.total+deposit
        print('deposit amount\n',deposit)
    def withdraw(self,withdraw=0):
        self.total=self.total-withdraw
        print('withdraw amount\n',withdraw)
    def balance(self):
        print('total amount\n',self.total)

obj=bank()
obj.deposit(10000)
obj.withdraw(300)
obj.deposit(500)
obj.balance()
