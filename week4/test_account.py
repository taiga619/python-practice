from account import Account

def test_deposit_increase_balance():
    acct = Account(1000)
    acct.deposit(500)
    assert acct.get_balance() == 1500

def test_withdraw_decrease_balance():
    acct = Account(1000)
    acct.withdraw(500)
    assert acct.get_balance() == 500

def test_withdraw_notchange_balance():
    acct = Account(1000)
    acct.withdraw(-500)
    assert acct.get_balance() == 1000

def test_deposit_notchange_balance():
    acct = Account(1000)
    acct.deposit(-500)
    assert acct.get_balance() == 1000

def test_withdraw_overdraw_balance():
    acct = Account(1000)
    acct.withdraw(1500)
    assert acct.get_balance() == 1000
