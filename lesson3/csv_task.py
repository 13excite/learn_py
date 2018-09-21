import argparse
import csv
import sys


def dict_writer(data, filename):
    try:
        with open(filename, 'w', newline='') as csv_f:
            fn = list(data[0].keys())
            w = csv.DictWriter(csv_f, fieldnames=fn, delimiter=';')
            w.writeheader()
            for d in example_data:
                w.writerow(d)
        print("Successful!")
    except csv.Error as err:
        sys.exit('file {}: {}'.format(filename, err))
    except IOError as err:
        print("I/O error: ", err)
        sys.exit(1)
    except Exception as err:
        print("Unexpected error ", err)
        sys.exit(1)


def main():
    example_data = [
            {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True, help='usage -f file.csv for writing data to file')
    args = parser.parse_args()

    dict_writer(example_data, args.filename)


if __name__ == '__main__':
    main()
