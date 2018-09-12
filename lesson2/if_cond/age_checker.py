import sys


def type_checker(number):
    try:
        return int(number)
    except:
        print("Failed convert value to integer")
        sys.exit(1)


def check_place_by_age(age):
    if age < 0:
        return "You were not born"
    elif age in range(0, 7):
        return "You in infant school"
    elif age in range(7, 18):
        return "Your in school"
    elif age in range(18, 24):
        return "You in university"
    else:
        return "You are work"


def main():
    answer_age = type_checker(input("How old are your? "))
    result = check_place_by_age(answer_age)
    print(result)


if __name__ == '__main__':
    main()
