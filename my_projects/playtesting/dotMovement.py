from manimlib.imports import *

class DotMovement(Scene):

    def construct(self):
        dotlist = []
        nDots = 3
        colorlist  = [BLUE, RED, GREEN]
        positionlist = [ORIGIN, UP, DOWN]
        for i in range(nDots):
            dotlist.append(Dot(positionlist[i], color=colorlist[i]))
        self.add(*dotlist)
        self.play(
            Indicate(dotlist[1])
        )
        self.wait()

        dotlist[1].target = Dot(LEFT, color=PURPLE)
        self.play(
            MoveToTarget(dotlist[1])
        )
        self.wait(5)