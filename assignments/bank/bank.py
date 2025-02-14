greetings = input('Greeting: ')

'''for k in greetings.split():
    if k == 'hello':
        print('$0')
        break
    else:
        break

for m in greetings.split(''):
    if m == 'h':
        print('$20')
        break
    else:
        break'''

greetings = str(greetings.lower())
if greetings.split('o')[0] == 'hell' or greetings.split()[0] == 'hello':
    print("$0")
elif greetings.split('h')[0] == '':
    print("$20")
else:
    print("$100")
