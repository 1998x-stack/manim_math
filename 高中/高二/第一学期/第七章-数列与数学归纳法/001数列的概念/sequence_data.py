"""Pure, testable data for the sequence-concept animation."""


def arithmetic_terms(count: int, first: int = 2, difference: int = 2) -> tuple[int, ...]:
    """Return a finite prefix of a_n = first + (n - 1) * difference."""
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ValueError("count must be a positive integer")
    return tuple(first + index * difference for index in range(count))


def prefix_sums(terms: tuple[int, ...]) -> tuple[int, ...]:
    total = 0
    result = []
    for term in terms:
        total += term
        result.append(total)
    return tuple(result)


def classification_samples(count: int = 8) -> dict[str, tuple[int, ...]]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ValueError("count must be a positive integer")
    return {
        "递增数列": arithmetic_terms(count),
        "递减数列": arithmetic_terms(count, first=2 * count, difference=-2),
        "常数列": (8,) * count,
        "周期数列": tuple((4, 8, 12)[index % 3] for index in range(count)),
    }
