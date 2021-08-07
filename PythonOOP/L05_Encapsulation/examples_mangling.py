# class BankAccount:
#     def __init__(self, name):
#         self.name = name
#         self.card_numbr = 12343431432
#         self.exp_date = "2021-01-21"
#         self.cvv = 543
#
# my_account = BankAccount('Lazar')
#
#
# print(my_account.cvv)

##TODO DISPLAY HIDDEN ATTRIBUTES (NAME MANGLING)
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__card_nmbr = 12343431432
        self.__exp_date = "2021-01-21"
        self.__cvv = 543

class ExtendedBankAccount(BankAccount):
    def __init__(self, name, percentage_discount):
        super().__init__(name)
        self.discount = percentage_discount

my_account = BankAccount('Lazar')
#inherits protection
my_account1 = ExtendedBankAccount('Natalia', 20)
my_account.animal = "Lion"
#NAME MANGLING OF ATTRIBUTE
print(my_account._BankAccount__cvv)
#still visible i properly address despite mangling
print(my_account1._BankAccount__cvv)
print('')

