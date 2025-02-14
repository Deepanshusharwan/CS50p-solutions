list = []
def main():
    list =[]
    while True:
        try:
            m = input()
            list.append(m)
        except EOFError:

            p = "Adieu, adieu, to "
            for a in list:
                if len(list) == 1:
                    p = p + a
                elif len(list) == 2:
                    if list.index(a) != len(list) - 1:
                        p = p + a
                    if list.index(a) == len(list) -1:
                        p = p + " and " + a
                else:
                    if list.index(a) != len(list) - 1:
                        p = p + a + ", "
                    if list.index(a) == len(list) -1:
                        p = p + "and " + a
            print(p)
            break

main()
