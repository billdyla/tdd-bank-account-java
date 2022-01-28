package org.xpdojo.bank;

import static java.lang.Math.abs;

public class Account {
    private int _balance;
    public static Account newAccount() {
        return new Account();
    }

    private Account() {
        _balance = 0;
    }

    public int transact(int transaction) {
        _balance += transaction;
        return _balance;
    }

    public void transfer(Account source, Account target, int transaction) {
        source.transact(-1 * abs(transaction) );
        target.transact(abs(transaction));
    }

    public int balance() {
        return _balance;
    }
}
