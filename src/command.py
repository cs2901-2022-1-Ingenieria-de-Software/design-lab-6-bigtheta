from lights import Light


class LightCommand():
    
    #def __init__(self):
    #    self.queue = []

    @staticmethod
    def turn_on(light):
        light.estado = True
        
    @staticmethod
    def turn_off(light): 
        light.estado = False

    @staticmethod
    def lightnescommand(light,val):
        if light.estado:
            light.intensidad(val)
        else:
            return -1        


        
