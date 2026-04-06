from tasks.easy import run_easy_task
from tasks.medium import run_medium_task
from tasks.hard import run_hard_task
from tasks.grader import grade_easy, grade_medium, grade_hard


easy_state = run_easy_task()
print("Easy Score:", grade_easy(easy_state))

medium_state = run_medium_task()
print("Medium Score:", grade_medium(medium_state))

hard_state = run_hard_task()
print("Hard Score:", grade_hard(hard_state))