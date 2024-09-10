import argparse
import secrets
import string


def get_letters(rnd_object: secrets.SystemRandom, special_chars: bool) -> list[str]:
    punctuation = '!#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    letters = string.ascii_letters + string.digits
    if special_chars: letters += punctuation
    lst_letters = list(letters)
    rnd_object.shuffle(lst_letters)
    return lst_letters


def generate_password(rnd_object: secrets.SystemRandom, length: int = 8, special_chars: bool = True) -> str:
    letters = get_letters(rnd_object, special_chars)
    passwd = rnd_object.choices(letters, k=length)
    return ''.join(passwd)


def main():
    parser = argparse.ArgumentParser(description='Password generator')
    parser.add_argument('--length', '-l', type=int, help='Password length', default=12)
    parser.add_argument('--special', '-s', action='store_true', help='Include special characters')
    
    args = parser.parse_args()
    rnd = secrets.SystemRandom()
    passwd = generate_password(rnd, args.length, args.special)
    print(passwd)


if __name__ == '__main__':
    main()