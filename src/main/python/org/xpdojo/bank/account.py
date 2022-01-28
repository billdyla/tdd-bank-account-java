'''bank account'''

from datetime import datetime 

class _Account:
    'a bank account'

    def __init__(self):
        self._balance = 0
        self._last_transaction_dt = None
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def transact(self, amount):

        self._last_transaction_dt = datetime.now()
        self._balance += amount
        self._transactions.append((self._last_transaction_dt, amount))
        return self

    @property
    def last_transaction_dt(self):
        return self._last_transaction_dt

    @property
    def transactions(self):
        return self._transactions


class AccountFactory:

    @staticmethod
    def getAccount():

        return _Account()
