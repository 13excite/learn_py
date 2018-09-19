import argparse
import re

# ([name for _0, _1, name in ephem._libastro.builtin_planets()])

def parse_sring(words):
    pattern = re.compile('(^".+"$)|(^\'.+\'$)')
    if pattern.match(words):
        print(words)
        print(f"words count = {len(words.split(' '))}")



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word', type=str, help='usage -w some world', required=True)
    args = parser.parse_args()

    print(args.word)

    parse_sring(args.word)


if __name__ == '__main__':
    main()
