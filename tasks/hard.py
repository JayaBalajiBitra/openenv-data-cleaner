from env.environment import DataCleaningEnv
from env.models import Action


def run_hard_task():
    env = DataCleaningEnv()
    obs = env.reset()

    # Inject extra complexity
    env.state_data.dataset.append({"name": "alice", "age": 25})  # inconsistent format
    env.state_data.issues.append("formatting")

    done = False

    actions = [
        Action(action_type="remove_nulls"),
        Action(action_type="remove_duplicates"),
        Action(action_type="finish")
    ]

    for action in actions:
        obs, reward, done, _ = env.step(action)
        if done:
            break

    return env.state()