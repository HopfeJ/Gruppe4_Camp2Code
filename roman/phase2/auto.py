class Auto():

    def fahren(self):
        print("Das Auto fährt.")

class RennAuto(Auto):

    def __init__(self) -> None:
        super().__init__()

    def fahren(self):
        print("Das Rennauto fährt")

auto = RennAuto()
auto.fahren()