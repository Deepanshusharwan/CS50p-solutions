def main():
    get_xy()

def get_xy():
    while True:
        m = input('Fraction: ')
        try:
            x,y = m.split('/')
            x = int(x)
            y = int(y)
            c = (100*x) / y
            c = round(c)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except UnboundLocalError:
            pass
        else:
            if y >= x:
                if c > 98:
                    print('F')
                elif c < 2:
                    print('E')
                else:
                    print(c,'%',sep='')
                break

main()
