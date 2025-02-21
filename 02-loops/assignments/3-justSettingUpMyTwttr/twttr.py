
def main():
    txt = input('Input: ')
    print('Output:',end='')
    remove_vowel(txt)

def remove_vowel(txt):
    for a in txt:
        b = a.lower()
        if b == 'a' or b == 'e' or b == 'i' or b == 'o' or b == 'u':
            print('',end='')
        else:
            print(a,end='')
    print()


main()
