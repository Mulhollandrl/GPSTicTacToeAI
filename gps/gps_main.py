from gps.components.gps import GPS
from gps.components.step import Step
import json

class GPS_Player:
    def __init__(self) -> None:
        self.invalid_steps = []

        with open('gps/tictactoe_steps/3by3_steps.json', 'r') as step_file:
            steps = json.load(step_file)
            steps = steps["steps"]
            step_list = []
            
            print("Steps:\n")
            for step in steps:
                print(step)
                step_list.append(Step(step.get("name"),step.get("preconds"), step.get("add_list"), step.get("del_list")))
 
        self.gps = GPS(step_list=step_list)
        self.check_step_paths_valid()

    def get_current_step_name(self):
        self.check_step_paths_valid()
        self.choose_step_path()
        return self.gps.get_current_step_name()

    def increment_step(self):
        self.check_step_paths_valid()
        self.choose_step_path()

        incremented = self.gps.increment_step()

        if not incremented:
            self.choose_step_path()
            self.gps.current_step_index = 0

    def choose_step_path(self, strategy="greedy"):
        self.check_step_paths_valid()

        if strategy == "greedy":
            best_length = 500
            best_step_path = []

            for step_path in self.gps.all_step_paths:
                if len(step_path) < best_length:
                    best_length = len(step_path)
                    best_step_path = step_path

            self.gps.step_path = best_step_path

    def check_step_paths_valid(self):
        invalid_step_paths = []

        for step_path in self.gps.all_step_paths:
            for step in step_path:
                if step.name in self.invalid_steps:
                    invalid_step_paths.append(step_path)

        self.gps.all_step_paths = [step_path for step_path in self.gps.all_step_paths if step_path not in invalid_step_paths]


if __name__ == "__main__":
    pass