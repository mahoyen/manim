from manimlib.imports import *
from my_projects.playtesting.moveToPoint import *

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

        poslist = [DR, DL, UR]
        
        tri = Triangle()
        self.add(tri)
        #dotlist[1].apply_function(lambda x: apply_rotTransMatrix(*x, rotTransMatrix))
        self.play(
            MoveToPoint(UR, dotlist[0]),
            MoveToPoint(3*UL, dotlist[2]),
            MoveToPointAndRotate(2*DR,30, tri),
        )
        self.wait()
        self.play(
            *[MoveToPoint(pos, dotitem) for pos, dotitem in zip(poslist, dotlist)],
        )
        self.wait(5)