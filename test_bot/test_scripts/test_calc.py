import argparse
import re

# ([name for _0, _1, name in ephem._libastro.builtin_planets()])
ACTIONS = ('+', '-', '/', '*')


def parse_sring(calc):
    if calc.endswith('='):
        num_list = re.split("\+|\-|\/|\*", calc[:-1])
        if len(num_list) > 1:
            try:
                int(num_list[0])
                int(num_list[1])
                return eval(calc[:-1])
            except ZeroDivisionError:
                raise ZeroDivisionError
            except ValueError:
                raise ValueError
        else:
            print("Not okay")
            print(num_list)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--calc', type=str, help='usage -w some world', required=True)
    args = parser.parse_args()

    print(args.calc)
    print(parse_sring(args.calc))




if __name__ == '__main__':
    main()
