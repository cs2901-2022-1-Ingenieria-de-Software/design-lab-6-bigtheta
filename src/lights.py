
from matplotlib.colors import LightSource


class Light():
    def __init__(self,color,intensidad):
        self.color = color
        self.intens = intensidad
        self.estado = False

    def intensidad(self,val):
        self.intens = val
        print("intensidad: ",self.intens)
        


class Orange(Light):
    def __init__(self,*args):
        super().__init__(*args)
        

class Red(Light):
    def __init__(self,*args):
        super().__init__(*args)
    


class Green(Light):
    def __init__(self,*args):
        super().__init__(*args)
    


class Stop(Light):

    def __init__(self,*args):
        super().__init__(*args)
    