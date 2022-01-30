'''bank account'''

import calendar
from collections import namedtuple
from datetime import datetime

def nextmonth(date):

    if date.month == 12:
        return date(date.year + 1, 1, 1)

    return datetime(date.year, date.month + 1, 1)

class _Account:
    'a bank account'

    _Transaction = namedtuple('Transaction', ['transaction_dt', 'amount'])

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
        self._transactions.append(self._Transaction(self._last_transaction_dt, amount))
        return self

    def transaction_filter_funct(self, start_dt=None, end_dt=None):
        first_day = datetime.today().replace(day=1)
        last_day = nextmonth(first_day)

        return lambda x: x.transaction_dt >= first_day and x.transaction_dt < last_day

    def current_statement(self):
        
        return filter(self.transaction_filter_funct(), self._transactions)

    @property
    def last_transaction_dt(self):
        return self._transactions[-1].transaction_dt if self._transactions else None

    @property
    def transactions(self):
        return self._transactions


class AccountFactory:

    @staticmethod
    def getAccount():

        return _Account()
