class BankAccount:
    def __init__(self, account_id, name, balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "name": self.name,
            "balance": self.balance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["account_id"], data["name"], data["balance"])
