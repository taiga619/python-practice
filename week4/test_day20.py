from day20 import SavingsAccount

def test_add_interest_increase_balance():
    acct = SavingsAccount(1000)
    acct.add_interest(0.1)
    assert acct.get_balance() == 1100.0
def test_add_interest_zero_rate_keeps_balance():
    acct = SavingsAccount(1000)
    acct.add_interest(0)
    assert acct.get_balance() == 1000.0
def test_withdraw_at_limit_succeeds():
    acct = SavingsAccount(100000)
    acct.withdraw(50000)
    assert acct.get_balance() == 50000
def test_withdraw_over_limit_keeps_balance():
    acct = SavingsAccount(100000)
    acct.withdraw(50001)
    assert acct.get_balance() == 100000
def test_deposit_inherited_increases_balance():
    acct = SavingsAccount(1000)
    acct.deposit(500)
    assert acct.get_balance() == 1500