
from datetime import date
import sys
import inflect


def main():
    try:
        year,month,day = input("Date Of Birth: ").split("-")
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        sys.exit("Invalid date of birth")
    print(age_in_word(age_count(year,month,day)))

def age_count(year,month,day):
    current_time = date.today()
    birth_date = date(year,month,day)
    age = current_time - birth_date
    age_in_minutes = int(age.total_seconds()//60)

    return age_in_minutes

def age_in_word(age):
    i = inflect.engine()
    return f"{i.number_to_words(age).capitalize().replace("and ",'')} minutes"


if __name__ == "__main__":
    main()
