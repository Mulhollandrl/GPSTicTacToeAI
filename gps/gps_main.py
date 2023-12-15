from components.gps import GPS
import components.step
import enums.BOARDTILES as Tiles

class GPS_Player:
    def __init__(self) -> None:
        # TODO: Put in the code to read in the step list
        step_list = []

        self.gps = GPS(step_list=step_list)

    def get_current_step_name(self):
        # TODO: Get the current step from the GPS and return the name of that step
        pass

    def increment_step(self):
        # TODO: Change to the next step in the GPS path
        pass

    def choose_step_path(self):
        # TODO: Choose a step path to follow
        pass

if __name__ == "__main__":
    pass