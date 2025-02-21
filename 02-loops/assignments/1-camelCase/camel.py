def main():
    a = input('CamelCase:')
    snake_case(a)

def snake_case(abc):
    for i in abc:
        if i.isupper():
            print('_',i.lower(),end='',sep='')
        else:
            print(i,end='')
    print()
main()