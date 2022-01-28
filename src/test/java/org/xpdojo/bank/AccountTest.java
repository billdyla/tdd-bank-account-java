package org.xpdojo.bank;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.xpdojo.bank.Account.newAccount;

public class AccountTest {

    @Test
    public void check_new_account() {
        assertThat(newAccount().balance() == 0);
    }

    @Test
    public void check_transation() {
        int transaction = 10;
        assertThat(newAccount().transact(transaction) == transaction);
    }

    @Test
    public void check_transfer() {
        Account source = newAccount();
        source.transact(10);
        Account target = newAccount();
        assertThat(source.balance() == 5);
        assertThat(target.balance() == 5);
    }
}
