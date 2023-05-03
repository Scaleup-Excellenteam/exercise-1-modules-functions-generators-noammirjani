"""5.2 Cup to join by Noam Mir"""


def join(*lists, sep="-"):
    """
    Join a list of lists with a separator
    :param lists:  list of lists
    :param sep: separator
    :return: list of joined lists
    """
    if not lists:
        return None

    list_str = list(lists[0])
    for li in lists[1:]:
        list_str.extend([sep])
        list_str.extend(li)
    return list_str


if __name__ == '__main__':
    print(join())
    print(join([1]))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1, 2], [8], [9, 5, 6], sep='@'))

# output:
# None
# [1]
# [1, '-', 2, '-', 8, '-', 9, '-', 5, '-', 6]
# [1, '@', 2, '@', 8, '@', 9, '@', 5, '@', 6]


