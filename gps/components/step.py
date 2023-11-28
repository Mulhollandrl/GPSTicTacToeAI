class Step:
    def __init__(self, name, preconds, add_list, del_list) -> None:
        self.name = name
        self.preconds = preconds
        self.add_list = add_list
        self.del_list = del_list
        
    def set_name(self, name):
        self.name = name
        
    def set_preconds(self, preconds):
        self.preconds = preconds
        
    def set_add_list(self, add_list):
        self.add_list = add_list
        
    def set_del_list(self, del_list):
        self.del_list = del_list