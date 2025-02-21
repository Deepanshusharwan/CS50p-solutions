

def main():
    plate = input('plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('invalid')

def is_valid(s):
    rule_4(s)
    if rule_1(s) and rule_2(s) and rule_3(s) and rule_5(s):
        return True

def rule_1(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def rule_2(s):
    if len(s) > 1 and len(s) < 7:
        return True
    else:
        return False

def rule_3(m):
    for s in range(len(m)):
        if m.index(m[s]) == len(m) - 1:
            break
        elif m[s].isnumeric():
            if m[s+1].isnumeric():
                if m[s+1] == m[-1]:
                    return True
                else:
                    pass
            else:
                return False
        else:
            pass
    if m.isalpha():
        return True
def rule_4(m):
    m = m.strip()

def rule_5(m):
    numbers = ''
    for k in m:
        if k.isnumeric():
            numbers += k
    if m.isalpha():
        return True
    elif numbers.isnumeric():
        if numbers[0] == '0':
            return False
        else:
            return True
    else:
        return True

main()
