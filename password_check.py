import requests
import hashlib
import sys


def get_response_from_API(hashedPassword):
    url = 'https://api.pwnedpasswords.com/range/' + hashedPassword
    resp = requests.get(url)
    return resp


def hash_password(password):
    hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    first_five, tail = hashed_password[:5], hashed_password[5:]
    return first_five, tail


def send_check_request(password):
    hashed_password = hash_password(password)

    resp = get_response_from_API(hashed_password[0])
    if resp.status_code == 200:
        records = (line.split(':') for line in resp.text.splitlines())
        for psw, numbers in records:
            if psw == hashed_password[1]:
                print(
                    f'OH NOO! your password has been leaked and has been seen {numbers} times before')
                return
        print('Your password is safe')
    else:
        print(f'API request failed with error code {resp.status_code}')


def main():
    passwords = sys.argv[1:]

    for password in passwords:
        send_check_request(password)


if __name__ == '__main__':
    sys.exit(main())
