def main():
    coke_machine(50)

def coke_machine(amount_due):
    while amount_due > 0:
        print('Amount Due:',amount_due)
        a = int(input('Insert Coin: '))
        if a == 25 or a == 10 or a == 5:
            amount_due = amount_due - a
    if amount_due <= 0:
        print('Change Owed:',-amount_due)

main()