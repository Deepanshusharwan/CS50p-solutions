months = {
      "January": '01',
    "February": '02',
    "March": '03',
    "April": '04',
    "May":'05',
    "June": '06',
    "July": '07',
    "August": '08',
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12'
}

def main():
    while True:
        try:
            m = input('Date: ').strip()
            if '/' in m:
                a,b,c = m.split('/')
                if int(a) > 12 or int(b) > 31:
                    break
                if int(a) < 10:
                    a = '0' + a
                if int(b) < 10:
                    b = "0" + b
                print(c,a,b,sep ='-')
                break

            elif ',' in m:
                a,c = m.split(',')
                a, b = a.split()
                a = a.lower().title()
                if int(b) < 10:
                    b = "0" + b

                if a in months:
                    a = months[a]
                    print(c,a,b,sep = '-')
                    break
        except ValueError:
            pass

main()
