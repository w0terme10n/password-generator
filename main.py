import argparse
import random
import string


def get_letters(special_chars: bool) -> list[str]:
    punctuation = '!#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    letters = string.ascii_letters + string.digits
    if special_chars: letters += punctuation
    lst_letters = list(letters)
    random.shuffle(lst_letters)
    return lst_letters


def generate_password(length: int = 8, special_chars: bool = True) -> str:
    letters = get_letters(special_chars)
    passwd = random.choices(letters, k=length)
    return ''.join(passwd)


def main():
    parser = argparse.ArgumentParser(description='Password generator')
    parser.add_argument('--length', '-l', type=int, help='Password length', default=12)
    parser.add_argument('--special', '-s', action='store_true', help='Include special characters')
    
    args = parser.parse_args()
    passwd = generate_password(args.length, args.special)
    print(passwd)


if __name__ == '__main__':
    main()