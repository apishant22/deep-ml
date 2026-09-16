def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    count = {}
    for i in range(len(samples)):
        value = samples[i]
        count[value] = count.get(value, 0) + 1

    total = len(samples)

    return [(value, count[value] / total) for value in sorted(count)]