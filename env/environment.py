import copy
from typing import Tuple

from env.models import Observation, Action, Reward, State


class DataCleaningEnv:

    def __init__(self):
        self.initial_dataset = [
            {"name": "Alice", "age": 25},
            {"name": None, "age": 30},
            {"name": "Bob", "age": None},
            {"name": "Alice", "age": 25},  # duplicate
        ]
        self.reset()

    def reset(self) -> Observation:
        self.state_data = State(
            dataset=copy.deepcopy(self.initial_dataset),
            issues=["missing_values", "duplicates"],
            steps_left=5,
            quality=0.2
        )
        return self._get_observation()

    def state(self) -> State:
        return self.state_data

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, dict]:
        reward = 0.0
        reason = ""
        done = False

        if self.state_data.steps_left <= 0:
            return self._get_observation(), Reward(value=0, reason="No steps left"), True, {}

        self.state_data.steps_left -= 1

        # Action handling
        if action.action_type == "remove_nulls":
            before = len(self.state_data.dataset)
            self.state_data.dataset = [
                row for row in self.state_data.dataset
                if None not in row.values()
            ]
            after = len(self.state_data.dataset)

            if after < before:
                reward += 0.3
                reason = "Removed null values"
                self.state_data.quality += 0.2
            else:
                reward -= 0.2
                reason = "No nulls removed"

        elif action.action_type == "remove_duplicates":
            before = len(self.state_data.dataset)
            unique = []
            for row in self.state_data.dataset:
                if row not in unique:
                    unique.append(row)
            self.state_data.dataset = unique
            after = len(unique)

            if after < before:
                reward += 0.3
                reason = "Removed duplicates"
                self.state_data.quality += 0.2
            else:
                reward -= 0.2
                reason = "No duplicates found"

        elif action.action_type == "finish":
            done = True
            if self.state_data.quality >= 0.8:
                reward += 1.0
                reason = "Task completed successfully"
            else:
                reward -= 0.5
                reason = "Finished too early"

        else:
            reward -= 0.3
            reason = "Invalid action"

        # Clamp quality
        self.state_data.quality = min(1.0, self.state_data.quality)

        return self._get_observation(), Reward(value=reward, reason=reason), done, {}

    def _get_observation(self) -> Observation:
        return Observation(
            dataset_preview=self.state_data.dataset[:3],
            issues_detected=self.state_data.issues,
            steps_remaining=self.state_data.steps_left,
            quality_score=self.state_data.quality
        )