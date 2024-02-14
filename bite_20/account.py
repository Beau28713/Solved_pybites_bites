
class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    def __enter__(self):
        self._copy = self._transactions.copy()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value is not None or self.balance < 0:
            self._transactions = self._copy
            print('Rollback')
        self._copy = None
    