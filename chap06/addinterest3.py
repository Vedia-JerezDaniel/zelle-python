def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)

test()

    """ Instead what has happened is that new values
were created, and the assignments into the list caused it to refer to the new values. The old values
will actually get cleaned up when Python does garbage collection.
    """