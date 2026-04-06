def grade_easy(state):
    dataset = state.dataset

    total = len(dataset)
    clean = sum(1 for row in dataset if None not in row.values())

    return clean / total if total > 0 else 0.0


def grade_medium(state):
    dataset = state.dataset

    total = len(dataset)
    clean = sum(1 for row in dataset if None not in row.values())

    unique = len([dict(t) for t in {tuple(d.items()) for d in dataset}])
    duplicate_score = unique / total if total > 0 else 0

    return 0.5 * (clean / total) + 0.5 * duplicate_score


def grade_hard(state):
    dataset = state.dataset

    total = len(dataset)

    # Missing values
    clean = sum(1 for row in dataset if None not in row.values())
    clean_score = clean / total if total > 0 else 0

    # Duplicates
    unique = len([dict(t) for t in {tuple(d.items()) for d in dataset}])
    duplicate_score = unique / total if total > 0 else 0

    # Formatting (NEW)
    properly_formatted = sum(
        1 for row in dataset
        if isinstance(row.get("name"), str) and row["name"].istitle()
    )
    format_score = properly_formatted / total if total > 0 else 0

    return (
        0.4 * clean_score +
        0.3 * duplicate_score +
        0.3 * format_score
    )