"""5.3 Spelling by Noam Mir"""
import re


def FindSecretMessage(filename):
    """
    :param filename: str, The path to the file.
    :return: strings that contain at least 5 consecutive letters and end with an exclamation mark.
    """
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            matches = re.findall(b'[a-z]{5,}!', chunk)
            if matches:
                for match in matches:
                    yield match.decode('utf-8')


print(list(FindSecretMessage('logo.jpg')))
