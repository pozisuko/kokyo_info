#!/usr/bin/env python3
# With this application, you can check the current information of the kokyo.

import argparse
import requests

parser = argparse.ArgumentParser(
    description='With this application, you can check the current information of the kokyo.')
parser.add_argument('-a', '--address', action='store_true',
                    help='display kokyo address')
parser.add_argument('-p', '--phone', action='store_true',
                    help='display kokyo phone number')
parser.add_argument('-w', '--weather', action='store_true',
                    help='display kokyo weather')
args = parser.parse_args()


def show_address():
    print('Address: 1-1 Kokyo-gaien, Chiyoda-ku, Tokyo 100-0002')


def show_phone_number():
    print('Phone: 03-(3213)-0095')


def show_weather():
    key = '3aeda3eb3478a482a96fda96e8cfbf65'
    lat = '35.685175'
    lon = '139.752'
    lang = 'jp'
    url = 'http://api.openweathermap.org/data/2.5/' + 'weather?lat=' + \
        lat + '&' + 'lon=' + lon + '&APPID=' + key + '&lang=' + lang

    data = requests.get(url).json()
    print(data['weather'][0]['main'])


if args.weather:
    show_weather()
elif args.address:
    show_address()
elif args.phone:
    show_phone_number()
else:
    parser.print_help()
