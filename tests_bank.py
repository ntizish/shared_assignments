"""Tests for bank.py."""

import pytest
import datetime
from bank import Account, Person, Transaction, Bank, PersonError, TransactionError


def test_person_definition():
    """Test Person class."""
    p1 = Person('Jack', 'Jackson', 19)
    p3 = Person('Igor', 'Smirnov', 33)
    assert p3.age == 33
    assert p1.__repr__() == p1.full_name
    assert p1.bank_account is None
    with pytest.raises(PersonError):
        assert Person("aa", "BB", -4)


def test_bank_definition():
    """Test Bank class."""
    p1 = Person('Jack', 'Jackson', 19)
    p2 = Person('Anna', 'Dark', 194)
    p3 = Person('Igor', 'Smirnov', 33)
    b1 = Bank('NotSwedBank')
    b2 = Bank('CoolerThanLHV')
    assert b1.add_customer(p1) is True
    assert p1 in b1.customers
    assert b2.add_customer(p2) is True
    assert b2.add_customer(p3) is True
    assert p2 in b2.customers
    assert p3 in b2.customers
    assert b2.add_customer(p2) is False
    assert b2.remove_customer(Person('Jey', 'Winston', 57)) is False
    assert p1.bank_account.balance == 0
    assert len(b2.customers) == 2
    assert b2.customers == [p2, p3]
    assert b2.remove_customer(p3) is True
    assert p3 not in b2.customers
    assert len(b2.customers) == 1
    assert b1.__repr__() == b1.name


def test_account():
    """Test Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    p2 = Person('Anna', 'Dark', 194)
    b1 = Bank('NotSwedBank')
    b2 = Bank('CoolerThanLHV')
    p1_acc = Account(100, p1, b1)
    p2_acc = Account(25, p2, b2)
    assert len(p1_acc.number[2:]) == 18
    assert p1_acc.number[2]
    assert p1_acc.balance == 100
    assert p2_acc.balance == 25


def test_deposit():
    """Test deposit method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    p2 = Person('Anna', 'Dark', 194)
    b1 = Bank('NotSwedBank')
    b2 = Bank('CoolerThanLHV')
    p1_acc = Account(100, p1, b1)
    p2_acc = Account(25, p2, b2)
    with pytest.raises(TransactionError):
        assert p1_acc.deposit(-15)

    p1_acc.deposit(15)
    tr1 = Transaction(15, datetime.date.today(), p1_acc, p1_acc, True)
    assert str(p1_acc.transactions[0]) == str(tr1)

    p2_acc.deposit(20, is_from_atm=False)
    assert p2_acc.balance == 45


def test_withdraw():
    """Test withdraw method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    p2 = Person('Anna', 'Dark', 194)
    b1 = Bank('NotSwedBank')
    b2 = Bank('CoolerThanLHV')
    p1_acc = Account(100, p1, b1)
    p2_acc = Account(25, p2, b2)
    with pytest.raises(TransactionError):
        assert p1_acc.withdraw(p1_acc.balance + 5)
    with pytest.raises(TransactionError):
        assert p1_acc.withdraw(-225)

    p2_acc.withdraw(20)
    tr = Transaction(-20, datetime.date.today(), p2_acc, p2_acc, True)
    assert str(p2_acc.transactions[0]) == str(tr)

    p1_acc.withdraw(15, is_from_atm=False)
    assert p1_acc.balance == 100 - 15


def test_transfer():
    """Test transfer method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    p2 = Person('Anna', 'Dark', 194)
    p3 = Person('Igor', 'Smirnov', 33)
    p4 = Person('Nana', 'Banana', 44)
    b1 = Bank('NotSwedBank')
    b2 = Bank('CoolerThanLHV')
    b3 = Bank('NotYourSEB')
    p1_acc = Account(100, p1, b1)
    p2_acc = Account(25, p2, b2)
    p3_acc = Account(300, p3, b3)
    p4_acc = Account(0, p4, b3)
    with pytest.raises(TransactionError):
        assert p2_acc.transfer(100500, p1_acc)

    """transaction1 = Transaction(5, datetime.date.today(), p2_acc, p1_acc, False)
    transaction2 = Transaction(10, datetime.date.today(), p3_acc, p2_acc, False)"""

    # different banks transfer
    p2_acc.transfer(5, p1_acc)
    assert p2_acc.transactions == p1_acc.transactions == b1.transactions == b2.transactions
    # transaction repr tests for different bank operations
    expected = f'(5 €) {p2} -> {p1}'
    assert p2_acc.transactions[0].__repr__() == expected

    # same bank transfer
    p3_acc.transfer(10, p4_acc)
    assert p3_acc.transactions == p4_acc.transactions == b3.transactions


def test_acc_statement():
    """Test account_statement method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    b1 = Bank('NotSwedBank')
    p1_acc = Account(100, p1, b1)
    old_trans = Transaction(150, datetime.date.today() - datetime.timedelta(days=15), p1_acc, p1_acc, True)
    p1_acc.transactions.append(old_trans)
    new_trans = Transaction(50, datetime.date.today() - datetime.timedelta(days=5), p1_acc, p1_acc, True)
    p1_acc.transactions.append(new_trans)

    res_newer = p1_acc.account_statement(datetime.date.today() - datetime.timedelta(days=7),
                                         datetime.date.today())
    assert res_newer == [new_trans]

    res_old = p1_acc.account_statement(datetime.date.today() - datetime.timedelta(days=365),
                                       datetime.date.today() - datetime.timedelta(days=10))
    assert res_old == [old_trans]


def test_debit_turnover():
    """Test get_debit_turnover method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    b1 = Bank('NotSwedBank')
    p1_acc = Account(100, p1, b1)
    expected = 600
    p1_acc.deposit(500)
    p1_acc.deposit(100)
    p1_acc.withdraw(150)
    assert p1_acc.get_debit_turnover(datetime.date.today(), datetime.date.today()) == expected


def test_credit_turnover():
    """Test get_credit_turnover method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    b1 = Bank('NotSwedBank')
    p1_acc = Account(100, p1, b1)
    p1_acc = Account(100, p1, b1)
    expected = -150
    p1_acc.deposit(500)
    p1_acc.deposit(100)
    p1_acc.withdraw(50)
    p1_acc.withdraw(100)
    assert p1_acc.get_credit_turnover(datetime.date.today(), datetime.date.today()) == expected


def test_net_turnover():
    """Test get_net_turnover method in Account class."""
    p1 = Person('Jack', 'Jackson', 19)
    b1 = Bank('NotSwedBank')
    p1_acc = Account(100, p1, b1)
    p1_acc = Account(100, p1, b1)
    expected1 = 450
    p1_acc.deposit(500)
    p1_acc.withdraw(50)
    assert p1_acc.get_net_turnover(datetime.date.today(), datetime.date.today()) == expected1

    p2 = Person('Anna', 'Dark', 194)
    p2_acc = Account(200, p2, b1)
    expected2 = -50
    p2_acc.deposit(100)
    p2_acc.withdraw(150)
    assert p2_acc.get_net_turnover(datetime.date.today(), datetime.date.today()) == expected2
