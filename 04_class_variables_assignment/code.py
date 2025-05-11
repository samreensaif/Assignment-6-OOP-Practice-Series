class Bank:
  bank_name = "ICICI"

  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name

bank1 = Bank()
bank2 = Bank()

print(bank1.bank_name)
print(bank2.bank_name)

Bank.change_bank_name("SBI")

print(bank1.bank_name)
print(bank2.bank_name)
