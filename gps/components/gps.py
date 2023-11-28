class GPS:
    def __init__(self, end_goal="win", state_list=[], step_list=[]) -> None:
        self.current_step_index = 0
        self.forwards = True
        self.done = False
        
        self.end_goal = end_goal
        self.state_list = state_list
        self.step_list = step_list
        
        self.step_path = self.find_step_path(self.end_goal)
        
    def find_step_path(self, goal):
        pass
    
    def print_step_path(self):
        for i in range(len(self.step_path)):
            print("  " * i + self.step_path[i].name)
    
    def check_step_completion(self):
        if all(element in self.state_list for element in self.step_path[self.current_step_index].preconds):
            current_step = self.step_path[self.current_step_index]
            self.state_list = [element for element in self.state_list if element not in current_step.del_list]
            self.state_list = self.state_list + [element for element in current_step.add_list if element not in self.state_list]
            
            if self.forwards:
                self.current_step_index += 1
            else:
                self.current_step_index -= 1    
        
        if self.current_step_index == len(self.step_path):
            self.forwards = False
        
        if self.current_step_index < 0:
            self.done = True
    
    def get_preconds_for_step(self):
        return self.step_path[self.current_step_index].preconds