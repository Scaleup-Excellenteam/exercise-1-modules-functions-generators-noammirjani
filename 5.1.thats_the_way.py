""" 5.1 That's the way by Noam Mir"""

import os


def get_files_starts_with(word, path):
    """
    :param word: str, The starting word to filter the file names.
    :param path: str, The path to the directory.
    :return: list of strings, contains all the file names in the directory that start with the given word.
    """
    try:
        return [file.startswith(word) and os.path.isfile(os.path.join(path, file)) for file in os.listdir(path)]
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    dir_path = "images"
    print(get_files_starts_with("deep", dir_path))
