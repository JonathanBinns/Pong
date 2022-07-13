from .jsonloading import loadjson as lj, writejson as wj
import pygame as pg

# windowClass handles the window for the program as well as all the key/mouse inputs
# this input information is stored in attributes as dictionaries, making accessing the values very simple in higher levels of the code
# it essentially takes some functionality from pygame that I need and puts it into an object that I can use easily
class windowClass:
    # in initialization, all the important attributes are created and assigned default values
    # filename determines where the dictionary for the keys are taken from
    # the dictionaries are given indexes by iterating through lists with literal values in for loops
    def __init__(self, filename = "keys"):
        self.screenMode = [(1920, 1080), pg.FULLSCREEN]
        self.screen = pg.display.set_mode(*self.screenMode)
        self.input = {}
        self.mouse = {}
        self.clock = pg.time.Clock()
        self.tick = 0

        self.keyData = lj(filename)
        for num in self.keyData:
            key = self.keyData[num]
            self.input[key] = 0
            self.input[key + "T"] = 0

        for item in ["m1", "m2", "m3", "m1T", "m2T", "m3T", "m1V", "m2V", "m3V", "mx", "my"]: # T for Toggle, V for Previous
            self.mouse[item] = 0
        self.mouse['list'] = []

    # processing refreshes the screen window and packages all the event input so it can be accessed easily through the object
    # this function needs to run every frame in a while loop so that the screen refreshes and all the inputs are accurate
    def processing(self):
        self.tick = self.clock.tick(120)
        for key in self.input:
            if key[-1] == "T":
                self.input[key] = 0
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and str(event.key) in self.keyData:
                key = self.keyData[str(event.key)]
                self.input[key] = 1
                self.input[key + "T"] = 1
            if event.type == pg.KEYUP and str(event.key) in self.keyData:
                key = self.keyData[str(event.key)]
                self.input[key] = 0
            if event.type == pg.VIDEORESIZE and not self.screenMode[1] == pg.FULLSCREEN:
                self.screenMode = [(event.w, event.h), pg.RESIZABLE]
                pg.display.set_mode(*self.screenMode)

        self.mouse['list'] = []
        self.mouse["mx"], self.mouse["my"] = pg.mouse.get_pos()
        self.mouse["m1"], self.mouse["m3"], self.mouse["m2"] = pg.mouse.get_pressed()
        for item in ["m1T", "m2T", "m3T"]:
            self.mouse[item] = 0
        for item in ["m1", "m2", "m3"]:
            if self.mouse[item] != self.mouse[item + "V"]:
                if self.mouse[item]:
                    self.mouse[item + "T"] = 1
                self.mouse[item + "V"] = self.mouse[item]

        if self.input["F11T"]:
            if self.screenMode[0] == (1920, 1080):
                self.screenMode = [(900, 600), pg.RESIZABLE]
            else:
                self.screenMode = [(1920, 1080), pg.FULLSCREEN]
            pg.display.set_mode(*self.screenMode)

        pg.display.flip()

    # this just makes the function .display.set_caption() more accessible
    def rename(self, name):
        pg.display.set_caption(name)

    # its a bit cheeky, but I use this if statement as the condition for the while loop of the program
    # the purpose is so that I can close it by holding shift and pressing escape
    def isRunning(self):
        return not (self.input["shift"] and self.input["escapeT"])
