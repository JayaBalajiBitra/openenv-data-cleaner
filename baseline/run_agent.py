from tasks.easy import run_easy_task
from tasks.medium import run_medium_task
from tasks.hard import run_hard_task

from tasks.grader import grade_easy, grade_medium, grade_hard


def run_baseline():
    results = {}

    # Easy
    easy_state = run_easy_task()
    results["easy"] = grade_easy(easy_state)

    # Medium
    medium_state = run_medium_task()
    results["medium"] = grade_medium(medium_state)

    # Hard
    hard_state = run_hard_task()
    results["hard"] = grade_hard(hard_state)

    return results


if __name__ == "__main__":
    scores = run_baseline()
    print("Baseline Scores:")
    for k, v in scores.items():
        print(f"{k}: {v}")