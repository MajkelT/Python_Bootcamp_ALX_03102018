import pytest


class NotEnoughMoney(ValueError):  # dziedziczy po value error
    pass


class AmountNotDividedBy10(ValueError):
    pass


class ErrorError(ValueError):
    pass


class CashMachine:
    def __init__(self):
        self._money = []  # to podkreślenie oznacza, że zmienna jest prywatna

    @property
    def is_available(self):
        if self._money:
            return True
        return False

    def put_money(self, money):
        if len(money) + len(self._money) > 10:
            raise ValueError("Za duzo banknotow")
        else:
            self._money.extend(money)  # dodaje kasę

    def withdraw_money(self, to_withdraw):

        if to_withdraw % 10 != 0:
            raise AmountNotDividedBy10("BLAD: Kwota powinna byc wielokrotnoscia 10")

        bills_to_withdraw = []
        for bill in sorted(self._money, reverse=True):
            if sum(bills_to_withdraw) + bill <= to_withdraw:
                bills_to_withdraw.append(bill)

        if sum(bills_to_withdraw) != to_withdraw:  # jak nie ma wystarczających środków
            raise NotEnoughMoney("Blad: Brak wystarczajcej liczby banknotow dla kwoty 150!")

        for bill in bills_to_withdraw:  # usuwamy banknot, który jest wypłacany
            self._money.remove(bill)

        return bills_to_withdraw


def main():
    bankomat = CashMachine()
    while True:
        # 1. Zapytać co chcę zrobić
        operacja = input("Podaj typ operacji: w - wpłata, y - wypłata, k - zakoncz")
        if operacja == 'k':
            # break ,a alternatywnie to co nizej
            print("Dziekujemy za skorzystanie z naszych uslug")
            return None
        # wpłata
        if operacja == 'w':
            banknoty = input("Podaj jakie banknoty wpłacasz - wpisz je rozdzielając spacją")
            banknoty = banknoty.split()  # dzielimy tekst
            banknoty = [int(x) for x in banknoty]  # wyrażenie listowe i zamiana tekstu na banktnowy
            # np [i**2 for i in range(10]
            # nb = []   - to wyrazenie listowe zastepuje te 4 linie kodu
            # for x in banknoty
            # nb.append int(x)
            try:
                bankomat.put_money(banknoty)
                print(banknoty)
            except ValueError as e:
                print(e)

        # wypłata
        if operacja == 'y':
            kwota_do_wyplaty = int(input("Jaka kwote chcesz wyplacic?"))
            try:
                wyplacone = bankomat.withdraw_money(kwota_do_wyplaty)
            except ValueError as e:
                wyplacone = False
                print(e)
            if wyplacone:
                print(wyplacone)


main()


def test_cash_machine_not_avaiable():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50])
    cash_machine.put_money([50])
    assert cash_machine.is_available


def test_cash_machine_whithdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]
    with pytest.raises(NotEnoughMoney):
        cash_machine.withdraw_money(150)


def test_cash_machine_whithdraw_money_sort_is_important():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 20, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]


def test_cash_machine_whithdraw_money_value_is_not_divided_by_ten():
    cash_machine = CashMachine()
    with pytest.raises(AmountNotDividedBy10) as e:
        cash_machine.withdraw_money(123)


def test_za_duzo_banknotow():
    cash_machine = CashMachine()
    with pytest.raises(ErrorError) as e:
        cash_machine.put_money([10, 10, 20, 50, 50, 20, 100, 100, 200, 500, 50, 20])

