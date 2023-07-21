# Principal : 원금 / rate : 이율 / 기간 : time / 
# Interest : 이자 / Amount : 원리금
# I = Prt / A = P(1 + rt)

def simple_interest(principal, rate, time):
    return principal * rate * time


def simple_interest_amount(principal, rate, time):
    return principal * (1 + (rate * time))