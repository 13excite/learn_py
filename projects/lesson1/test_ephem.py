import ephem
from datetime import datetime
import argparse

# ([name for _0, _1, name in ephem._libastro.builtin_planets()])

PLANETS = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun', 'Moon', 'Phobos',
           'Deimos', 'Io', 'Europa', 'Ganymede', 'Callisto', 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan',
           'Hyperion', 'Iapetus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda']


def get_constellation(user_input):
    answer = user_input.capitalize()
    if answer in PLANETS:
        #print(datetime.today().strftime('%Y/%m/%d'))
        try:
            planet = getattr(ephem, answer)(datetime.today().strftime('%Y/%m/%d'))
            print(f"Today {answer} in {ephem.constellation(planet)[1]}")
        except:
            print("Ooops, Something went wrong")
    else:
        print("Not found plane {0}".format(answer))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--planet', type=str, help='usage -p planetName', required=True)
    args = parser.parse_args()
    get_constellation(args.planet)

if __name__ == '__main__':
    main()