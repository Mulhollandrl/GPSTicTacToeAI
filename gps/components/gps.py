class GPS:
    def __init__(self, end_goal="win", state_list=[], step_list=[]) -> None:
        self.current_step_index = 0
        self.forwards = True
        self.done = False
        self.step_path = None
        
        self.end_goal = end_goal
        self.state_list = state_list
        self.step_list = step_list

        self.all_step_paths = []
        self.find_all_step_paths(self.end_goal)
        
    def find_all_step_paths(self, goal):
        all_end_steps = []

        for step in self.step_list:
            if goal in step.add_list:
                all_end_steps.append(step)

        for step in all_end_steps:
            other_precond_steps = []
            step_path = self.find_all_preconds_steps(step, [step], other_precond_steps)

            if step_path:
                for steps in step_path:
                    if steps.name.split("_")[0] == "win":
                        step_path.remove(steps)

                self.all_step_paths.append(step_path)

    def find_all_preconds_steps(self, step, step_path, other_precond_steps):
        step_path = list(step_path)
        all_deletions = [deleted_state for steps in step_path + other_precond_steps for deleted_state in steps.del_list]
        current_state_list = [state for state in self.state_list if state not in all_deletions] + \
            [added_state for steps in step_path + other_precond_steps for added_state in steps.add_list if added_state not in all_deletions]

        all_preconds_not_met = [precond for precond in step.preconds if precond not in current_state_list]
        steps_for_preconds = [steps for steps in self.step_list for precond in all_preconds_not_met if precond in steps.add_list]

        if not all_preconds_not_met:
            return step_path
        
        all_preconds = [precond for steps in self.step_list for precond in steps.preconds]
        not_met_preconds = [precond for precond in all_preconds if precond not in current_state_list]

        if [precond for precond in all_preconds_not_met if precond not in not_met_preconds and precond not in current_state_list]:
            return []

        # Find the rest of the steps needed for the step_path to be complete
        results = list(set(tuple(self.find_all_preconds_steps(current_step, tuple(step_path + [current_step]), [steps for steps in steps_for_preconds if steps != current_step])) for current_step in steps_for_preconds))

        # Return the completed step_path
        return list(set([current_step for current_step_path in results for current_step in current_step_path]))
    
    def print_step_path(self):
        for i in range(len(self.step_path)):
            print("  " * i + self.step_path[i].name)
    
    def get_preconds_for_step(self):
        return self.step_path[self.current_step_index].preconds
    
    def get_current_step_name(self):
        return self.step_path[self.current_step_index].name
    
    def increment_step(self):
        if not self.current_step_index == len(self.step_path) - 1:
            if not self.step_path:
                return True
                
            self.step_path.remove(self.step_path[0])
            # self.current_step_index += 1
            return True
        
        return False