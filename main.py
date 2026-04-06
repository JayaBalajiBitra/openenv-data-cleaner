from fastapi import FastAPI
from baseline.run_agent import run_baseline
from tasks.grader import grade_easy, grade_medium, grade_hard
from tasks.easy import run_easy_task
from tasks.medium import run_medium_task
from tasks.hard import run_hard_task

app = FastAPI()


@app.get("/")
def home():
    return {"message": "OpenEnv Data Cleaning Environment Running"}


@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {"name": "easy", "description": "Remove missing values"},
            {"name": "medium", "description": "Remove missing values + duplicates"},
            {"name": "hard", "description": "Full cleaning + formatting"}
        ]
    }


@app.get("/baseline")
def baseline():
    return run_baseline()


@app.get("/grader")
def grader():
    easy_state = run_easy_task()
    medium_state = run_medium_task()
    hard_state = run_hard_task()

    return {
        "easy_score": grade_easy(easy_state),
        "medium_score": grade_medium(medium_state),
        "hard_score": grade_hard(hard_state),
    }