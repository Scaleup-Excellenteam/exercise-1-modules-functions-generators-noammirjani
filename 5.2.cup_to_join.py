"""5.2 Cup to join by Noam Mir"""


def join(*lists, sep=None):
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


print(join([1, 2], [8], [9, 5, 6], sep='^'))
