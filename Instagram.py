import random
import string
import threading
from concurrent.futures import ThreadPoolExecutor

import requests
from cfonts import render
from colorama import Fore, Style, init
from user_agent import generate_user_agent

init(autoreset=True)

MIN_LENGTH = 5
ALLOWED_CHARS = '1234567890qwertyuiopasdfghjklzxcvbnm._'

COLOR_COMBOS = [
    ['cyan', 'blue'],
    ['magenta', 'white'],
    ['yellow', 'red'],
    ['green', 'black'],
    ['blue', 'white'],
    ['red', 'black'],
    ['magenta', 'cyan'],
    ['yellow', 'blue'],
    ['white', 'magenta'],
    ['cyan', 'black'],
]

print_lock = threading.Lock()


def print_banner():
    stein_colors, qe_colors = random.sample(COLOR_COMBOS, 2)
    stein = render('STEIN', colors=stein_colors, align='center', font='block', background='black')
    qe = render(
        'Telegram: @rejerk | Join @keped\nV7.2 ',
        colors=qe_colors,
        align='right',
        font='console',
        background='black',
    )
    print(stein)
    print(qe)


def normalize_username(username):
    username = username.strip()
    if username.startswith('@'):
        username = username[1:]
    return username


def get_instagram_cookies():
    try:
        session = requests.Session()
        session.get('https://www.instagram.com/')
        csrftoken = session.cookies.get('csrftoken', 'missing')

        headers = {
            'user-agent': generate_user_agent(),
            'x-csrftoken': csrftoken,
            'x-requested-with': 'XMLHttpRequest',
            'referer': 'https://www.instagram.com/accounts/login/',
            'content-type': 'application/x-www-form-urlencoded',
        }

        data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:0:maybe-jay-z',
            'optIntoOneTap': 'false',
            'queryParams': '{}',
            'trustedDeviceRecords': '{}',
            'username': 'maybe_jay_z',
        }

        session.post(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
            headers=headers,
            data=data,
        )

        cookies = {
            'csrftoken': session.cookies.get('csrftoken', '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'),
            'mid': session.cookies.get('mid', 'ZVfGvgABAAGoQqa7AY3mgoYBV1nP'),
            'ig_did': session.cookies.get('ig_did', ''),
            'ig_nrcb': session.cookies.get('ig_nrcb', ''),
        }
    except Exception:
        cookies = {
            'csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'mid': 'ZVfGvgABAAGoQqa7AY3mgoYBV1nP',
            'ig_did': '',
            'ig_nrcb': '1',
        }

    try:
        with open('instagram.txt', 'w') as f:
            for key, value in cookies.items():
                f.write(f'{key}={value}\n')
    except Exception:
        pass


def instagram(username):
    try:
        cookies = {}
        with open('instagram.txt', 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    cookies[key] = value

        cookie_header = '; '.join([f'{k}={v}' for k, v in cookies.items()])
        csrf_token = cookies.get('csrftoken', '')

        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        headers = {
            'Host': 'www.instagram.com',
            'content-length': '85',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'sec-ch-ua-mobile': '?0',
            'x-instagram-ajax': '81f3a3c9dfe2',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '/',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '198387',
            'user-agent': generate_user_agent(),
            'x-csrftoken': csrf_token,
            'sec-ch-ua-platform': '"Linux"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IQ,en;q=0.9',
            'cookie': cookie_header,
        }

        data = f'email=l7ntopython%40gmail.com&username={username}&first_name=&opt_into_one_tap=false'
        response = requests.post(url=url, headers=headers, data=data)

        if '{"message":"feedback_required","spam":true,' in response.text:
            return False
        if '"errors": {"username":' in response.text or '"code": "username_is_taken"' in response.text:
            return False
        if response.status_code == 200:
            return True
    except Exception:
        return False

    return False


def send_hit(bot_token, chat_id, username):
    try:
        message = (
            f'`{username}` is Available on Instagram\n\n'
            f'Developer: @rejerk\n'
            f'Channel: @keped'
        )
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        requests.post(
            url,
            json={
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'Markdown',
            },
            timeout=10,
        )
    except Exception:
        pass


def check_username(username, bot_token, chat_id):
    username = normalize_username(username)
    if len(username) < MIN_LENGTH:
        return False

    available = instagram(username)

    with print_lock:
        if available:
            print(f'{Fore.GREEN}{username} | Available{Style.RESET_ALL}')
            send_hit(bot_token, chat_id, username)
        else:
            print(f'{Fore.RED}{username} | Unavailable{Style.RESET_ALL}')

    return available


def random_worker_auto(length, bot_token, chat_id):
    letters = string.ascii_lowercase
    while True:
        username = ''.join(random.choice(letters) for _ in range(length))
        check_username(username, bot_token, chat_id)


def random_worker_custom(char_sets, bot_token, chat_id):
    while True:
        username = ''.join(random.choice(char_sets[i]) for i in range(len(char_sets)))
        check_username(username, bot_token, chat_id)


def prompt_char_sets(length):
    char_sets = []
    for i in range(length):
        prompt = (
            f'{Fore.CYAN}Position {i + 1} characters '
            f'(Enter for all): {Style.RESET_ALL}'
        )
        chars = input(prompt).strip().lower()
        if not chars:
            chars = ALLOWED_CHARS
        else:
            chars = ''.join(c for c in chars if c in ALLOWED_CHARS)
            if not chars:
                chars = ALLOWED_CHARS
        char_sets.append(chars)
    return char_sets


def load_usernames(path):
    usernames = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            username = normalize_username(line)
            if username:
                usernames.append(username)
    return usernames


def start_threads(target, args):
    threads = []
    for _ in range(20):
        thread = threading.Thread(target=target, args=args, daemon=True)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def run_random_auto(length, bot_token, chat_id):
    start_threads(random_worker_auto, (length, bot_token, chat_id))


def run_random_custom(char_sets, bot_token, chat_id):
    start_threads(random_worker_custom, (char_sets, bot_token, chat_id))


def run_list(path, bot_token, chat_id):
    usernames = load_usernames(path)
    if not usernames:
        return

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [
            executor.submit(check_username, username, bot_token, chat_id)
            for username in usernames
        ]
        for future in futures:
            future.result()


def main():
    print_banner()

    bot_token = input(f'{Fore.CYAN}Enter Telegram bot token: {Style.RESET_ALL}').strip()
    chat_id = input(f'{Fore.CYAN}Enter chat ID: {Style.RESET_ALL}').strip()

    print(f'\n{Fore.YELLOW}Choose an option:{Style.RESET_ALL}')
    print(f'{Fore.WHITE}1. Check random{Style.RESET_ALL}')
    print(f'{Fore.WHITE}2. Check from list{Style.RESET_ALL}')

    choice = input(f'{Fore.CYAN}Enter choice (1/2): {Style.RESET_ALL}').strip()
    get_instagram_cookies()

    if choice == '1':
        print(f'\n{Fore.YELLOW}Random format:{Style.RESET_ALL}')
        print(f'{Fore.WHITE}1. Auto{Style.RESET_ALL}')
        print(f'{Fore.WHITE}2. Choose specific randomness{Style.RESET_ALL}')
        random_choice = input(f'{Fore.CYAN}Enter choice (1/2): {Style.RESET_ALL}').strip()

        length = int(input(f'{Fore.CYAN}Enter username length: {Style.RESET_ALL}').strip())
        if length < MIN_LENGTH:
            return False

        if random_choice == '1':
            run_random_auto(length, bot_token, chat_id)
        elif random_choice == '2':
            char_sets = prompt_char_sets(length)
            run_random_custom(char_sets, bot_token, chat_id)
        else:
            print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
            return False

    elif choice == '2':
        path = input(f'{Fore.CYAN}Enter path to username list: {Style.RESET_ALL}').strip().strip('"')
        run_list(path, bot_token, chat_id)
    else:
        print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
        return False

    return True


if __name__ == '__main__':
    main()
