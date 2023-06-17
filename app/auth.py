from datetime import datetime
import random


def get_js():
    temp = ''
    with open('app/main.js', 'r') as file:
        temp = file.read()
        file.close()
    return temp

def get_key(length):
    chars = (
        "ABCDEFGH-IJKLMNOPQRSTUV-WXYZabcdefghi-jklmnopqrstuvwxyz-1234567890#@!$%&*()-_=+"
    )
    temp = random.choice(chars)
    for x in range(1, length):
        temp += random.choice(chars)
    return temp


def get_time():
    return datetime.now().strftime("%d-%b-%y %H:%M")
