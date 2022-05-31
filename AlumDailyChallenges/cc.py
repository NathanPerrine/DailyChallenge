from functools import cache


class Transaction:
    def __init__(self, amount: int, day: int):
        self.amount = amount 
        self.day = day


class Payment(Transaction):
    pass

class Purchase(Transaction):
    pass 


class Credit_Card:
    def __init__(self, interest_rate: float):
        self.payments = []
        self.purchases = []
        self.interest_rate = interest_rate

    def add_purchase(self, amount: int, day: int):
        new_purchase = Purchase(amount, day)
        self.purchases.append(new_purchase)

    def add_payment(self, amount: int, day: int):
        new_payment = Payment(amount, day)
        self.payments.append(new_payment)

    @cache
    def get_balance_by_day_with_cache(self, day):
        daily_balance = 0
        payment_total = 0 
        purchase_total = 0

        for payment in self.payments:
            if payment.day <= day:
                payment_total += payment.amount 
        for purchase in self.purchases:
            if purchase.day <= day:
                purchase_total += purchase.amount 

        daily_balance = purchase_total - payment_total 
        return daily_balance 

    def get_interest_by_day_with_cache(self, day):
        interest = 0
        for num in range(1, day + 1):
            interest += self.get_balance_by_day_with_cache(num) * (self.interest_rate / 365)
        return interest

    def get_balance_by_day(self, day):
        daily_balance = 0
        payment_total = 0 
        purchase_total = 0

        for payment in self.payments:
            if payment.day <= day:
                payment_total += payment.amount 
        for purchase in self.purchases:
            if purchase.day <= day:
                purchase_total += purchase.amount 

        daily_balance = purchase_total - payment_total 
        return daily_balance 

    def get_interest_by_day(self, day):
        interest = 0
        for num in range(1, day + 1):
            interest += self.get_balance_by_day(num) * (self.interest_rate / 365)
        return interest

test_card = Credit_Card(0.1295)

test_card.add_purchase(100, 1)
# test_card.add_purchase(150, 2)
# test_card.add_purchase(50, 2)
# test_card.add_purchase(75, 3)

# test_card.add_payment(50, 1)
# test_card.add_payment(250, 3)
# test_card.add_payment(50, 4)

# print(test_card.get_balance_by_day(0))
# print(test_card.get_balance_by_day(1))
# print(test_card.get_balance_by_day(2))
# print(test_card.get_balance_by_day(3))
# print(test_card.get_balance_by_day(4))

# print(test_card.get_interest_by_day(5))

def interest_with_cache(day):
    return test_card.get_interest_by_day_with_cache(day)
def interest_no_cache(day):
    return test_card.get_interest_by_day(day)


import timeit
interest_time_cache = timeit.timeit(lambda: interest_with_cache(5), number=1_000_000)
interest_time_no_cache = timeit.timeit(lambda: interest_no_cache(5), number=1_000_000)
print(f"{interest_time_cache=}")
print(f"{interest_time_no_cache=}")