'''test the account abstraction'''

from unittest import TestCase

from org.xpdojo.bank.account import AccountFactory


class Account_Test(TestCase):

    def test(self):
        self.assertEqual(AccountFactory.getAccount().balance, 0)

    def test_transact(self):

        transaction = 5
        self.assertEqual(AccountFactory.getAccount().transact(transaction).balance, transaction)

    def test_last_transaction_date(self):

        self.assertEqual(AccountFactory.getAccount().last_transaction_dt, None)
    
    def test_last_transaction_date_with_transaction(self):

        acct = AccountFactory.getAccount().transact(10)
        self.assertTrue(acct.last_transaction_dt is not None)

    def test_statement(self):

        acct = AccountFactory.getAccount().transact(10).transact(-5)
        self.assertEqual(len(acct.transactions), 2)

    def test_deposits(self):

        acct = AccountFactory.getAccount().transact(10).transact(-5)
        self.assertEqual(len(list(filter(lambda x: x[1] > 0, acct.transactions))), 1)
