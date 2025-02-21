
def main():
    time = int(input("What time is it?").split(":")[0])
    meal_time(time)


def convert(time):
    time = time.split(":")
    current_time = float(time[0]) + float(time[1])/60
    return current_time


def meal_time(time):
    if time == 7:
        print("breakfast time")

    elif time == 13:
        print("lunch time")
    elif time == 18:
        print("dinner time")


if __name__ == "__main__":
    main()