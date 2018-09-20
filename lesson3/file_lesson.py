import sys
import argparse
import re
import os


def exit_with_error(text, err):
    print(text, err)
    sys.exit(1)


def file_reader(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError as err:
        exit_with_error("I/O error", err)
    except FileNotFoundError as err:
        exit_with_error("File not found", err)
    except Exception as err:
        exit_with_error("Some error", err)


def len_file_read(filename):
    return f"Length file as string = {len(file_reader(filename))}"


def word_count_file(filename):
    return "Text has {} words".format(len(re.findall('\w+', file_reader(filename))))


def replace_dots(filename):
    return "Splited dots on exclamation: \n {}".format(file_reader(filename).replace('.', '!'))


def write_file(filename):
    data = file_reader(filename)
    try:
        with open('referat2.txt', 'w') as f:
            f.write(data)
    except IOError as err:
        exit_with_error("I/O error reading file", err)
    except Exception as err:
        exit_with_error("Some error", err)

    if os.path.isfile('referat2.txt'):
        print("Successful writing file")
    else:
        print("Write file not found")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='usage -f file.txt for reading file')
    args = parser.parse_args()

    print(len_file_read(args.file))
    print(word_count_file(args.file))
    write_file(args.file)


if __name__ == '__main__':
    main()