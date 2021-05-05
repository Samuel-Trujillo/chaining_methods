class User:
    def __init__(self, name):
        self.name = name
        self.cash = 0
    def deposit(self, deposit):
        self.cash += deposit
        return self
    def withdraw(self, withdraw):
        self.cash -= withdraw
        return self
    def balance(self):
        print(f"{self.name}, Balance of: {self.cash}")
        return self



samuel = User("Samuel")
jack = User("Jack")
alice = User("Alice")

samuel.deposit(100).deposit(100).deposit(100).withdraw(100).balance()
jack.deposit(1000).deposit(1000).withdraw(500).withdraw(500).balance()
alice.deposit(10000).withdraw(1000).withdraw(1000).withdraw(1000).balance()