class Army:
    def __init__(self, army_list):
        self.army_list = army_list
        self.phase = "command"
    def change_phase(self, phase):
        print(phase)
        self.phase = phase


