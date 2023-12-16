import json
from gps.components.gps import GPS
from gps.components.step import Step

if __name__ == "__main__":
    with open('gps/tictactoe_steps/3by3_steps.json', 'r') as step_file:
        # Load the JSON data into a Python dictionary
        steps = json.load(step_file)
        steps = steps["steps"]
        step_list = []
        
        print("Steps:\n")
        for step in steps:
            print(step)
            step_list.append(Step(step.get("name"),step.get("preconds"), step.get("add_list"), step.get("del_list")))
            
    gps = GPS(step_list=steps)
    
    print(gps.all_step_paths)