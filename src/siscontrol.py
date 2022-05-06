from lights import Light


class SisControl():

    instance = None

    global lights
        

    @staticmethod
    def get_instance():
        if instance == None:
            instance = SisControl()
        return instance

    @staticmethod
    def add_light(name,light):
        lights [name] = light

    @staticmethod
    def get_light(name):
        return lights[name]



