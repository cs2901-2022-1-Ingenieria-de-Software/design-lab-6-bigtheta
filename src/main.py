from lights import Green, Light, Orange, Red, Stop
from siscontrol import SisControl
from command import LightCommand

def main():

    sistemaControl = SisControl()
    sistemaControl.add_light("orange",Orange("orange",0))
    sistemaControl.add_light("red",Red("red",0))
    sistemaControl.add_light("green",Green("green",0))
    sistemaControl.add_light("stop",Stop("stop",0))



    LightCommand.turn_on(sistemaControl.get_light("orange"))
    LightCommand.lightnescommand(sistemaControl.get_light("green"))


    