menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.00
    while True:
        try:
            a = input('Item: ')
            a = a.title()
            total += menu[a]
          #  total = '{2:.2f}'.format(total)
            print(f'Total: ${total:.2f}')
        except KeyError:
            pass
        except EOFError:
            break
main()
