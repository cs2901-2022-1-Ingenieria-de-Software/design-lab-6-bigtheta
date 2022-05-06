from lights import Light

class SisControl():

    lights = {}

    def add_light(name,light):
        lights [name] = light

    def get_light(name):
        return lights[name]



