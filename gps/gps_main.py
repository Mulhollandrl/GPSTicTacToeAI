import json
from gps.components.gps import GPS
from gps.components.step import Step

class GPS_Player:
    def __init__(self) -> None:
        with open('gps/tictactoe_steps/3by3_steps.json', 'r') as step_file:
            step_list = json.load(step_file)
            step_list = step_list["steps"]
            step_list = []
            
            print("Steps:\n")
            for step in step_list:
                print(step)
                step_list.append(Step(step.get("name"),step.get("preconds"), step.get("add_list"), step.get("del_list")))

        self.gps = GPS(step_list=step_list)

    def get_current_step_name(self):
        return self.gps.get_current_step_name()

    def increment_step(self):
        not_choose_new_path = self.gps.increment_step()
        
        if not not_choose_new_path:
            self.choose_step_path()

    def choose_step_path(self, method="greedy"):
        if method == "greedy":
            best_length = 500
            best_step_path = []
            
            for step_path in self.gps.all_step_paths:
                if len(step_path) < best_length:
                    best_length = len(step_path)
                    best_step_path = step_path
                    
            self.gps.step_path = best_step_path
            
if __name__ == "__main__":
    pass