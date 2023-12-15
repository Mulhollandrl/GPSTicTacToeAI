class GPS:
    def __init__(self, end_goal="win", state_list=[], step_list=[]) -> None:
        self.current_step_index = 0
        self.forwards = True
        self.done = False
        self.step_path = None
        
        self.end_goal = end_goal
        self.state_list = state_list
        self.step_list = step_list

        self.all_step_paths = self.find_all_step_paths(self.end_goal)
        
    def find_all_step_paths(self, goal):
        all_end_steps = []

        for step in self.step_list:
            if goal in step["add_list"]:
                all_end_steps.append(step)

        for step in all_end_steps:
            step_path = self.find_all_preconds_steps(step, [step])

            if step_path:
                self.all_step_paths.append(step_path)

    def find_all_preconds_steps(self, step, step_path):
        evil = [steps for steps in step_path]
        all_deletions = [deleted_state for steps in step_path for deleted_state in steps.get("del_list")]
        current_state_list = [state for state in self.state_list if state not in all_deletions] + \
            [added_state for steps in step_path for added_state in steps["add_list"] if added_state not in all_deletions]

        all_preconds_not_met = [precond for precond in step["preconds"] if precond not in current_state_list]
        steps_for_preconds = [step for precond in all_preconds_not_met for step in self.step_list if step.get("name") == precond]

        if not all_preconds_not_met:
            return step_path
        
        all_preconds = [precond for step in self.step_list for precond in step["preconds"]]
        not_met_preconds = [precond for precond in all_preconds if precond not in current_state_list]

        if [precond for precond in all_preconds_not_met if precond not in not_met_preconds and precond not in current_state_list]:
            return []

        # Find the rest of the steps needed for the step_path to be complete
        results = list(set([self.find_all_preconds_steps(current_step, step_path + [current_step]) for current_step in steps_for_preconds]))

        # Return the completed step_path
        return list(set([current_step for current_step_path in results for current_step in current_step_path]))
    
    def print_step_path(self):
        for i in range(len(self.step_path)):
            print("  " * i + self.step_path[i]["name"])
    
    def get_preconds_for_step(self):
        return self.step_path[self.current_step_index]["preconds"]