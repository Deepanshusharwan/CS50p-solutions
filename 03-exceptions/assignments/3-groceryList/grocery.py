def main():
    grocery_list = []
    while True:
        try:
            m = input().upper()
            grocery_list.append(m)
            grocery_list.sort()
        except EOFError:
            ls = []
            for k in grocery_list:
                if not k in ls:
                    ls.append(k)
            for m in ls:
                print(grocery_list.count(m), m)
            break


main()

'''

the old working method...


ls = []
            final_list = []
            for k in grocery_list:
                a = grocery_list.count(k)
                lst = str(a) + ' ' + k
                ls.append(lst)
                for a in ls:                     #this is  how to rmeove duplicates from a list

                    if not a in final_list:
                        final_list.append(a)
            for i in final_list:
                print(i)
            break
'''
