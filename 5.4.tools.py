"""5.4 Tools by Noam Mir"""""


def interleave(*iterables):
    """Interleave the elements of multiple iterables."""
    iterators = [iter(it) for it in iterables]
    return list(lter_func(iterators))


def lter_func(iterators):
    """Iterate over the iterators.
    :param iterators: list of iterators
    :return: iterator to next element
    """
    while iterators:
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)


print(list(interleave('abc', [1, 2, 3], ('!', '@'))))
